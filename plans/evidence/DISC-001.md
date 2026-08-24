# DISC-001 Completion Evidence

**Status:** Source complete; operational acceptance pending

**Control-plane commit:** `4bf9982`

## Implemented

- deterministic ranking of approved RI candidates by priority, novelty, evidence
  quality, freshness and search-family distance;
- exclusion of retracted, stale, previously selected and near-duplicate candidates;
- existing schedule and weekly budget enforcement with static-mandate fallback;
- replayable publication, routing, citation, ranking and question provenance;
- append-only digest-bound `proposal_created`, decision and `task_ready` events;
- optimistic concurrency on the reviewed question digest;
- explicit Mission Control founder approval/rejection;
- no execution, promotion, order or capital authority.

## Verification

The control-plane focused suite passes nine tests covering ranking ties, stale and
retracted evidence, semantic duplicates, fallback, budget, approval and races. The
complete Mission Control suite passes 70 tests, and JavaScript syntax plus scoped Ruff
checks pass. Control-plane validation and the live command are documented in
`docs/disc-001-validation.md` and
`docs/runbooks/disc-001-daily-research-director.md`.

## Remaining operational evidence

Merge the implementation, apply Alembic migration `a8c4e1d72b90`, deploy the VM2 API,
reinstall Mission Control on Mac and run `worker/scripts/disc001_pilot.py` against one
live cycle. The report must show source replay, founder decision, `task_ready`, and
`execution_authority: false` before DISC-001 is marked operationally complete.
