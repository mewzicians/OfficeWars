import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
temp_root = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if temp_root:
    sys.path.insert(0, os.path.join(temp_root, "officewars-python"))

from playwright.sync_api import sync_playwright


GAME = ROOT / "officewarsautobattler.html"
GAME_URL = GAME.as_uri()
READY = "document.documentElement.dataset.officewarsReady === 'true'"


def main():
    source = GAME.read_text(encoding="utf-8")
    static = {
        "save_schema_9": "const OW_SAVE_SCHEMA=9;" in source,
        "dynamic_identity_table": "const OW_COWORKER_IDENTITIES=" in source,
        "office_politics_board": 'id="office-politics-board"' in source,
        "new_one_on_one_text": (
            "Your first successful solo political choice today grants +2 PP." in source
            and "first coworker bonus triggered today" not in source
        ),
        "new_social_paths": all(
            value in source
            for value in (
                "Favor capacity 1",
                "deterministically cancel",
                "full-office caucus",
            )
        ),
        "new_checkpoints": all(
            value in source
            for value in (
                "'nightInvitation'",
                "'favorOverflow'",
                "'delegateCampaign'",
                "'alumniInbox'",
            )
        ),
    }

    page_errors = []
    responsive = {}
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            args=[
                "--allow-file-access-from-files",
                "--disable-extensions",
                "--no-first-run",
            ],
        )
        try:
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            page.on("pageerror", lambda error: page_errors.append(str(error)))
            page.goto(GAME_URL, wait_until="load", timeout=30_000)
            page.wait_for_function(READY, timeout=15_000)
            runtime = page.evaluate(
                """() => {
                  localStorage.clear();
                  const checks = {};
                  const evidence = {};
                  const expect = (name, value, detail) => {
                    checks[name] = !!value;
                    evidence[name] = detail;
                  };

                  startRun({seed:940001});
                  const state = OfficeWarsTest.phase4State();
                  const identities = OW_COWORKER_IDENTITIES;
                  const scenes = identities.flatMap(identity =>
                    Object.values(identity.scenes)
                  );
                  expect(
                    'identity_inventory',
                    identities.length === 42 &&
                      new Set(identities.map(item=>item.id)).size === 42 &&
                      state.identityCount === 42,
                    identities.map(item=>item.id)
                  );
                  expect(
                    'scene_inventory',
                    scenes.length === 168 &&
                      new Set(scenes.map(item=>item.id)).size === 168 &&
                      scenes.every(scene =>
                        scene.options.length === 3 &&
                        scene.options.some(option =>
                          option.odds === 100 &&
                          Number(option.cost.cash || 0) === 0
                        )
                      ),
                    {count:scenes.length}
                  );
                  const roster = state.roster;
                  const rosterStates = roster.ids.map(id=>roster.coworkers[id]);
                  expect(
                    'intern_roster',
                    roster.ids.join('|') ===
                      'INT-GAT|INT-WIL|INT-PRA|INT-ACH|INT-NET|INT-IDE' &&
                      rosterStates.map(item=>item.relationship)
                        .sort((a,b)=>a-b).join('|') === '2|3|4|5|6|7' &&
                      rosterStates.filter(item=>item.agenda === 'player').length === 3 &&
                      roster.stakeholderIds.length === 2,
                    roster
                  );
                  expect(
                    'relationship_bands',
                    [0,2,3,6,7,9,10].map(
                      OfficeWarsTest.relationshipBand
                    ).join('|') ===
                      'hostile|hostile|ordinary|ordinary|trusted|trusted|loyal',
                    [0,2,3,6,7,9,10].map(
                      OfficeWarsTest.relationshipBand
                    )
                  );

                  const target = 'INT-WIL';
                  R.floorRoster.coworkers[target].relationship = 6;
                  OfficeWarsTest.gainRelationship(target, 2);
                  expect(
                    'scene_queue_crossing',
                    R.floorRoster.coworkers[target].relationship === 8 &&
                      R.floorRoster.coworkers[target].sceneQueue.includes('trusted'),
                    R.floorRoster.coworkers[target]
                  );
                  R.floorRoster.coworkers[target].relationship = 10;
                  R.floorRoster.coworkers[target].loyal = true;
                  const before = R.floorRoster.coworkers[target].playerStanding;
                  const blocked = OfficeWarsTest.shiftStanding(target,'chad',10);
                  expect(
                    'loyalty_lock',
                    blocked === 0 &&
                      R.floorRoster.coworkers[target].playerStanding === before &&
                      owPhase4VoteFor(target) === 'player',
                    R.floorRoster.coworkers[target]
                  );

                  R.day = 1;
                  R.today = R.today || {cardFlags:{},log:[]};
                  R.roleVoteState = null;
                  R.floorRoster.roleResolved = false;
                  const vote = OfficeWarsTest.freezeRoleVote();
                  expect(
                    'role_vote',
                    !!vote &&
                      vote.ballots.length === 6 &&
                      ['player','chad'].includes(vote.owner),
                    vote
                  );

                  nightState = {
                    outingUsed:false,
                    panelOpen:true,
                    panelMode:'planner',
                    tab:'outings',
                    startCash:R.cash,
                    startCredit:R.expenseCredit || 0,
                    homeUsed:0,
                    homeLimit:1,
                    dealUsed:0,
                    dealLimit:0,
                    extraPurchaseCredits:0,
                    bought:new Set(),
                    purchasedDealIds:new Set()
                  };
                  R.phase = 'night';
                  R.nightInvitations = null;
                  const invitations = OfficeWarsTest.prepareInvitations();
                  expect(
                    'night_invitations',
                    invitations.entries.length >= 3 &&
                      invitations.entries[0].coworkerId ===
                        R.floorRoster.todayChadTargetId ||
                      invitations.entries.length >= 3,
                    invitations
                  );

                  openOfficePoliticsBoard();
                  const board = document.getElementById(
                    'office-politics-board-content'
                  );
                  expect(
                    'board_surface',
                    board.querySelectorAll('.office-politics-card').length === 6 &&
                      !!board.querySelector('.office-politics-detail'),
                    {
                      cards:board.querySelectorAll(
                        '.office-politics-card'
                      ).length,
                      text:board.textContent.slice(0,200)
                    }
                  );
                  expect(
                    'schema_and_checkpoints',
                    OW_SAVE_SCHEMA === 9 &&
                      ['nightInvitation','favorOverflow','delegateCampaign',
                       'alumniInbox','roleVote','floorBriefing'].every(
                        item=>OW_STABLE_CHECKPOINTS.has(item)
                      ),
                    OfficeWarsTest.phase2State()
                  );
                  return {checks,evidence};
                }"""
            )

            for name, viewport in (
                ("desktop", {"width": 1440, "height": 900}),
                ("landscape", {"width": 900, "height": 430}),
            ):
                page.set_viewport_size(viewport)
                page.evaluate("() => { openOfficePoliticsBoard(); }")
                responsive[name] = page.evaluate(
                    """() => {
                      const dialog = document.querySelector(
                        '#office-politics-board .hud-modal-dialog'
                      );
                      const rect = dialog.getBoundingClientRect();
                      return {
                        visible:rect.width > 0 && rect.height > 0,
                        withinViewport:
                          rect.left >= -1 &&
                          rect.right <= innerWidth + 1 &&
                          rect.top >= -1 &&
                          rect.bottom <= innerHeight + 1,
                        cards:document.querySelectorAll(
                          '#office-politics-board .office-politics-card'
                        ).length
                      };
                    }"""
                )
        finally:
            browser.close()

    checks = dict(static)
    checks.update(runtime["checks"])
    checks["no_page_errors"] = not page_errors
    checks["responsive_board"] = all(
        item["visible"] and item["withinViewport"] and item["cards"] == 6
        for item in responsive.values()
    )
    detail = {
        "static": static,
        "runtime": runtime["evidence"],
        "responsive": responsive,
        "page_errors": page_errors,
    }
    print(json.dumps({"checks": checks, "detail": detail}, indent=2))
    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        print("FAILED=" + ",".join(failed))
        raise SystemExit(1)
    print("PASS:OFFICE_POLITICS_PHASE4")


if __name__ == "__main__":
    main()
