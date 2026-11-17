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

**Status:** started: native design-adequacy contract and 112 focused native tests;
tool dispatch, calibration producers and live integration remain open. **Depends on:** 002.
Evidence: Bulletproof `docs/aep-003-native-diagnostics.md` (local first increment).
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

**Status:** missing generalized episode integration. **Depends on:** 003.
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

**Status:** engineering foundation exists; method-stage extension open. **Depends on:** 004.
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

**Status:** deployed opt-in foundation; genuine path unproved. **Depends on:** 005.
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

**Status:** existing components; integrated proof open. **Depends on:** 006.
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
