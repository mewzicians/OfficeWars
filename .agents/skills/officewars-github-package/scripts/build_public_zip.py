#!/usr/bin/env python3
"""Build and byte-verify a deterministic GitHub-ready ZIP."""

import argparse
import hashlib
import json
import os
import zipfile
from pathlib import Path


EXCLUDED_PARTS = {".git", "__pycache__"}
EXCLUDED_NAMES = {".DS_Store", "Thumbs.db"}
EXCLUDED_SUFFIXES = {".pyc", ".zip"}
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def sha256(data):
    return hashlib.sha256(data).hexdigest().upper()


def public_files(source):
    files = []
    for path in source.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(source)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        if path.name in EXCLUDED_NAMES or path.suffix.lower() in EXCLUDED_SUFFIXES:
            continue
        files.append((relative.as_posix(), path))
    files.sort(key=lambda item: item[0])
    return files


def validate_names(files):
    lowered = {}
    for name, _ in files:
        if name.startswith("/") or ".." in Path(name).parts:
            raise ValueError(f"Unsafe archive path: {name}")
        folded = name.casefold()
        if folded in lowered:
            raise ValueError(f"Case-insensitive duplicate: {lowered[folded]} and {name}")
        lowered[folded] = name


def build(source, output):
    source = source.resolve()
    output = output.resolve()
    if not source.is_dir():
        raise ValueError(f"Public mirror does not exist: {source}")
    if output.suffix.lower() != ".zip":
        raise ValueError("Output must use the .zip extension.")
    try:
        output.relative_to(source)
    except ValueError:
        pass
    else:
        raise ValueError("Output ZIP must be outside the public mirror.")

    files = public_files(source)
    if not files:
        raise ValueError("Public mirror contains no packageable files.")
    validate_names(files)

    temporary = output.with_suffix(output.suffix + ".tmp")
    if temporary.exists():
        temporary.unlink()
    try:
        with zipfile.ZipFile(
            temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
        ) as archive:
            for name, path in files:
                info = zipfile.ZipInfo(name, ZIP_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = (0o100644 & 0xFFFF) << 16
                archive.writestr(info, path.read_bytes())
        os.replace(temporary, output)
    finally:
        if temporary.exists():
            temporary.unlink()

    with zipfile.ZipFile(output, "r") as archive:
        names = archive.namelist()
        expected = [name for name, _ in files]
        if names != expected:
            raise ValueError("ZIP inventory differs from the public mirror.")
        if len(names) != len(set(names)):
            raise ValueError("ZIP contains duplicate paths.")
        for name, path in files:
            if archive.read(name) != path.read_bytes():
                raise ValueError(f"Archived bytes differ: {name}")

    game = source / "officewarsautobattler.html"
    summary = {
        "source": str(source),
        "output": str(output),
        "fileCount": len(files),
        "zipBytes": output.stat().st_size,
        "zipSha256": sha256(output.read_bytes()),
        "gameSha256": sha256(game.read_bytes()) if game.is_file() else None,
        "hiddenRepositoryFiles": {
            ".agents": any(name.startswith(".agents/") for name, _ in files),
            ".github": any(name.startswith(".github/") for name, _ in files),
            ".gitignore": any(name == ".gitignore" for name, _ in files),
            ".nojekyll": any(name == ".nojekyll" for name, _ in files),
        },
    }
    if not all(summary["hiddenRepositoryFiles"].values()):
        raise ValueError("Required hidden repository files are missing.")
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    print(json.dumps(build(args.source, args.output), indent=2))


if __name__ == "__main__":
    main()
