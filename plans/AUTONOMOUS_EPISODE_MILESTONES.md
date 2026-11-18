# Autonomous research episodes: implementation milestones

Date: 2026-11-17. Status: proposed executable sequence; no milestone below is
certified by this document. Work one milestone at a time, in order. This plan
does not authorize new mandates, paid campaigns, source transitions or trading.

## Goal and architecture

Prove unattended discovery -> scientifically defensible design -> strategy
implementation -> native execution -> terminal result -> publication and memory
-> next eligible work. A valid rejection or explicit deferral is a correct outcome;
forcing every hypothesis to pass is not the goal.

Use durable stage episodes with retained workspace, evidence and bounded reasoning.
Keep deterministic control of authority, budgets and acceptance. Separate method
design from implementation and keep independent review outside author authority.
Prefer extending existing controllers over adding agents or a second scheduler.

Existing foundation in swarm-control-plane:
- `worker/src/swarm_worker/engineering_episode.py`: durable state, locking,
  call/repair/deadline budgets, evidence-bound review rechecks.
- `worker/src/swarm_worker/executors/engineering_episode.py`: retained patches,
  focused checks, separate review/adjudication and validation/bundle adapter.
- `docs/durable-engineering-episodes.md`: deployed opt-in foundation; genuine
  candidate end-to-end commissioning remains unproved.
- `docs/offline-precision-review-scope.md`: diagnostic evidence and unresolved
  scientific obligations. Local bootstrap pilots are not native certifications.

The implemented continuity is not a persisted Codex conversation: calls are
ephemeral and reconstruct bounded context from retained artifacts. Evaluate true
conversation continuation against this baseline; do not assume either is superior.

Bulletproof owns authoritative quantitative computation. Hermes/control-plane owns
contracts, scheduling, authority and receipt custody. Prototype probes may remain
independent validators, but cannot substitute for native estimator receipts.

## AEP-001 - Freeze the failure corpus and acceptance contract

**Status:** implementation complete; label adjudication and overall acceptance
tracked at end-to-end commissioning, per owner direction. **Depends on:** none.
Evidence: [frozen corpus and acceptance contract](evidence/AEP-001/ACCEPTANCE.md).
Thirteen pinned cases and a reproducible report-only baseline exist. This is not
production certification or independently adjudicated ground truth.
- Inventory current controllers, producers, tools and recovery routes before edits.
- Build a redacted, digest-bound case manifest from actual failures: support/power,
  timing/leakage, semantic mismatch, coverage gaps, review disagreement, interrupted
  work and quota. Keep failure labels independently reviewed, with uncertainty.
- Include at least four materially different mechanisms and held-out cases; do not
  copy private lake data or credentials into Git. Retain source/spec versions.
- Define denominators for autonomous completion, correct rejection/deferral,
  interventions, repeat failures, latency, tool/model usage and unknown cost.
- Predeclare numerical commissioning thresholds before trials; separate code-test
  completion, simulation evidence and production certification.
**Done:** reproducible baseline run and agreed scorecard; negative controls cannot
be counted as successful backtests. No candidate-specific success exceptions.
**Rollback/review:** fixtures only; independent review of labels and rubric.

## AEP-002 - Typed findings and stage-owned recovery decisions

**Status:** deployed via control-plane `70aafc4`, with focused regressions, real
PostgreSQL ledger concurrency validation and deployed contract smoke; genuine
candidate commissioning remains pending. **Depends on:** 001.
Implementation record: swarm-control-plane `docs/aep-002-structured-recovery.md`.
- Extend existing six dispositions: repair, await_data, scientifically_infeasible,
  requirements_conflict, requires_new_question, await_authority_or_capacity.
- Each finding binds requirement, evidence, owning stage, allowed change scope,
  severity, recovery condition and verification procedure. Unknown claims stay unknown.
- Distinguish missing design logic from observations unavailable before execution.
- Add a correction ledger keyed by subject/evidence fingerprints; identical input
  and findings cannot trigger another paid attempt without new evidence or authority.
**Done:** all frozen cases route correctly; duplicate deliveries are idempotent;
unknown classifications cannot approve or silently mutate a scientific question.
**Rollback/review:** compatibility reader and feature flag; contract/security review.

## AEP-003 - Native diagnostic tools and design adequacy contracts

**Status:** bounded diagnostic tooling implemented and locally verified: fixed
native tool registry, design contracts, seeded residual calibration, clean-source
CLI and feasibility receipt custody. 137 native and 360 control-plane tests pass.
Cross-repository CLI replay is identical and backend-verified. Deployment, full
case-corpus commissioning and independent quantitative acceptance remain open;
this does not certify a real candidate. **Depends on:** 002.
Evidence: Bulletproof `docs/aep-003-native-diagnostics.md` and swarm-control-plane
`docs/aep-003-native-diagnostics.md` (replay digest and measured limitations).
The frozen-residual calibration is not a fitted strategy, paired power or joint
Holm analysis. Unsupported estimators/DGPs/policies explicitly await engineering.
Model-driven tool selection and missing-tool task creation remain episode/controller
integration work in AEP-004/AEP-007, not behavior claimed by this substrate.
- Expose bounded native tools for units, splits, feature history, coverage, support,
  estimator/uncertainty calibration and causal timing. Reuse existing implementations.
- Model selects an applicable tool and states assumptions; deterministic admission
  validates arguments, compute caps, data boundary and outputs before execution.
- Power planning must name estimand, justified meaningful effect, dependence envelope,
  multiplicity and eligibility losses. No universal event-count or power threshold.
- Exact estimator calibration is separate from approximations; undefined bootstrap
  draws and unsupported estimators receive explicit outcomes, not silent omission.
- Missing tools route to bounded engineering approval, not invented receipts.
**Done:** source/config/seed-bound native receipts reproduce across the case corpus;
arithmetic, synthetic calibration and observed data evidence cannot be interchanged.
**Rollback/review:** disable individual tool versions; independent quantitative review.

## AEP-004 - Durable scientific-method correction episode

**Status:** opt-in method episode and native/Codex adapters implemented and locally
verified. Reuses the durable engineering store; reservations survive crash/quota;
identity/scope and explicit deferrals are enforced before handoff for independent
review. Scripted reasoning fixtures and real native CLI integration are not proof
of autonomous scientific reasoning. Production scheduling (AEP-007), independent
design review and genuine commissioning remain open. **Depends on:** 003.
Implementation: swarm-control-plane `docs/aep-004-method-episodes.md`; 195 focused
tests passed, including three actual Bulletproof CLI integration cases.
- Extend durable-episode primitives for inspect -> diagnose -> propose correction ->
  run tools -> compare evidence -> checkpoint. Preserve full evidence by reference.
- Provide a compact ledger of attempted changes, remaining findings and tool results;
  budget context without dropping scientific requirements or provenance.
- Freeze scientific identity and authorization envelope. Changes to identity require
  a separately reviewed successor; within-scope repairs preserve immutable lineage.
- Enforce call, elapsed-time, compute and repair limits across crash/restart/quota.
**Done:** multiple repairable fixture classes correct without operator prompting;
infeasible cases defer/reject accurately; interrupted runs retain budgets and work.
**Rollback/review:** opt-in only; recovery/integrity tests and independent design review.

## AEP-005 - Evidence-based independent review and adjudication

**Status:** method-stage controller and governed model adapters implemented locally;
exact-packet reviews, concrete findings, custody/relevance-checked counterexamples,
bounded separate adjudication and fresh review by both fixed evaluators are covered
by controlled tests. No production routing or genuine scientific certification is
claimed. Independent fixture-label adjudication remains commissioning work.
**Depends on:** 004. Implementation: swarm-control-plane `docs/aep-005-method-review.md`.
- Review exact changed requirements and relevant evidence. Reuse reviews only when
  all reviewed bindings and relevant dependencies remain unchanged and valid.
- Findings require concrete violated criteria; bounded counterexample tools can
  reproduce defects or supply contradictory evidence for fresh review.
- Adjudication cannot approve its own correction. An unrelated passing test cannot
  dismiss a rejection. Unresolved disagreements remain visible and bounded.
**Done:** deliberate defects remain rejected; independently labelled unsupported
findings resolve without relaxing gates; no review-chasing or unlimited model calls.
**Rollback/review:** preserve all old verdicts; independent adjudication evaluation.

## AEP-006 - Session-like engineering continuity and native handoff

**Status:** accepted-method handoff and optional explicit-ID author session mode
implemented locally on the existing engineering episode. Synthetic paired cases
exercise reconstructed/session repair, real pytest, independent scripted review
and code/plan-bound bundles. Live-model mode comparison and genuine native
commissioning remain unproved. **Depends on:** 005.
Implementation: swarm-control-plane `docs/aep-006-engineering-handoff.md`.
- Route accepted methods into existing scaffolder and engineering episodes with
  native dependencies, exact pinned source and complete contracts.
- Compare reconstructed-context episodes with true author-session continuation on
  the same frozen cases/budgets where supported. Keep reviewer contexts separate.
- Preserve workspace and diagnostics; repair in place within scope. General engine
  modifications require their own approval, not a hypothesis-authoring exemption.
- Bind accepted bundle to focused/full tests, independent review and executable
  smoke/scientific plans. Source upgrades require explicit rebinding and invalidation.
**Done:** materially different implementations and injected defects complete the
bounded repair/handoff tests; every result traces to its exact code and contract.
**Rollback/review:** retain prior executor path; compare completion, correctness and
usage, not merely model-call count. No silent old-task migration.

## AEP-007 - Autonomous scheduling, authority and visible recovery

**Latest checkpoint, 2026-11-18:** still in progress, not end-to-end certified.
Real method task `2eb5b85a-9f1f-4aef-ad21-85d57bc8534c` completed one author
correction and two native diagnostics on Bulletproof `f81fb7d`; both independent
method reviews accepted. One verdict required operator-assisted publication after
interruption, so autonomous recovery is not proven. Fresh native coverage and
successor planning completed; both smoke/scientific plans are ready. CP `72d58ae`
deployed bounded artifact-backed engineering evidence after 58 backend and 18
worker checks. Adding those plans to a fresh method review still exceeds the
100 KB review context bound; this was caught before paid calls.

The old campaign is `needs_attention`, with zero trials. The separately approved
handoff mandate was active at November 18 02:56 UTC, expiring 04:03 UTC; it does
not rebind the old campaign or activate an engineering successor. Next: repair the
review handoff, separately authorize the successor, then commission genuine
engineering before separately authorized market-data execution. Source and IDs:
[Book XI Chapter 12](../books/book-11-engineered-company-system/chapters/12-requirements-recovery-and-current-certification.md).

The following implementation history is retained; earlier inactive/pending labels
describe those checkpoints, not current registrations or authority.

**Status:** in progress; integrated proof open. Engineering episodes now have
stage-boundary lease checks, provider-permit gating before reservations,
changed-circuit-only capacity recovery and budget/usage telemetry. Production
method publication was deployed in `200e09f`; `6631a6d` adds exact-packet,
independently assigned method reviews and source-bound engineering materialization.
The latter requires ready native smoke/scientific plans with task custody and
explicit engineering approval during commissioning. Mission Control now serves a
bounded-episode task inspector with unknown usage kept explicit. This is not the
production default. A local follow-on adds immutable rejected-review correction
successors conserving original budgets/deadlines and requiring fresh review;
duplicate delivery, altered lineage and revoked authority are covered. Synthetic
desktop/mobile inspector verification is complete, including expandable evidence
and terminal-result precedence over old heartbeats. Release `2112f09` deployed
bounded correction and a separate third-party interpretation adjudicator. It cannot
approve a method; rechecks require new native receipts and two fresh reviews.
The method designer and adjudicator now have live registrations with distinct
contexts and remain inactive pending exact commissioning approval. Integrated
commissioning remains open. Provisioning repair `85cc7db` persists credentials and
attests the installed worker before creating its profile, without leasing work;
missing native planning now defers before paid review with explicit ownership and
successor conditions. Follow-on tests: 175 backend, 113 worker and one executable UI
renderer check. Three worker
checks used the real Bulletproof CLI with synthetic contracts/scripted corrections.
No genuine candidate or backtest is certified by these controlled fixtures.
The initially pending mandate `ALPHA004-AEP007-COMMISSIONING-20261117` had digest
`078aecffa81580c3a1c10eeda238d39fca6c90a72b5a64fccf9230aa2dc1df19`.
Its initially pending method-only campaign `e17260b6-2d51-4f21-95af-1b96a7d4b8d0` had digest
`a5eb727506c26ee77882fd2cf345edeefd9a795bb01eb7aae31e0fc977645291`.
These were subsequently approved for method-only commissioning and superseded by
bounded corrections; they do not authorize current engineering or backtests.
See swarm-control-plane `docs/aep-007-scheduling-integration.md`.
**Depends on:** 006.
- Wire method and engineering episodes to existing campaign/replenishment controllers.
- Repair within approved scope and budgets without fresh approval per internal step;
  exhausted/expanded authority waits explicitly. Never reset mandate counters.
- Deferred candidates cannot block eligible siblings; reconsider only on recorded
  condition changes. Capacity/quota defers model work without disabling safe lanes.
- Mission Control exposes stage, attempts, blockers, evidence, next action, budgets,
  unknown usage, and drain-pause/resume. Old failed work stays distinguishable.
**Done:** restart, duplicate delivery, quota, unavailable data and exhausted budgets
cause no repeated spend, lost lineage or unauthorized work; eligible siblings advance.
**Rollback/review:** drain pause and feature flags; integration and authorization tests.

## AEP-008 - End-to-end commissioning and autonomy certificate

**Status:** not certified. **Depends on:** 007.
- Start with mock/provider-stub failure injection, then authorized genuine candidates:
  statistical-screen, public-evidence and corpus-reasoned origins where admitted.
- Do not handpick only easy successes or count deferred cases as executed backtests.
- Require at least two materially different genuine candidates to pass engineering,
  independent review, bounded smoke and one-year native execution with terminal
  BT-009 outcomes, artifact checks, publication, memory and automatic replenishment.
- Valid negative outcomes count as completed science; positive profitability is not
  required. Deferrals and rejection correctness are measured separately.
- Demonstrate recovery after interruption and quota, and an unattended observation
  window fixed under 001. No ad hoc manual edits during a claimed autonomous attempt.
- Report every intervention, cost/usage gap, failure and certification scope.
**Done:** predefined rubric passes on retained evidence; update backlog/Book XI and
publish a scoped certificate. Failure remains open, never relabelled as completion.
**Rollback/review:** drain pause; independent operational and scientific evidence
review. No shadow, demo orders, live trading or capital authority is granted here.

## Working agreement

Before each milestone: explain current code, options and acceptance boundary.
After each: run the named tests, record evidence, review and state precisely what
is implemented versus demonstrated. Maintain one task ID per branch/review.
Do not start broad discovery to test infrastructure defects. Use cheap deterministic
checks first, bounded synthetic trials next and paid/genuine commissioning last.
