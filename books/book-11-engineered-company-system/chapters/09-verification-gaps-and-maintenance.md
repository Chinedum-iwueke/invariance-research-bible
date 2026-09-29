<a id="verification-gaps-and-maintenance"></a>
# 9. Verification, Gaps and Maintenance

## 9.1 Current milestone ledger

| Package | Source state | Latest recorded runtime/evidence state |
|---|---|---|
| BASE-001..003 | Implemented/tested | Completion evidence retained |
| RI-001..006 | Implemented/tested | Isolated/database rehearsals retained; live health must be queried |
| RI-007/012/013 | Implemented/tested/deployed | Incremental inbox, bounded Codex-advised recovery and two-item terminal action register observed |
| RI-008 | Implemented/tested/observed | Live 762,232-node, 1,331,231-edge graph plus replay and tool receipts retained |
| RI-009/009B/011/016 | Implemented/tested/deployed/observed | Thirteen-domain `1.2.0` portfolio qualified; automatic derived-state convergence and incremental/full digest parity passed at epoch `577353` |
| RI-010 | Implemented/tested/deployed/observed | Lifecycle, consolidation, supersession, retraction, lawful deletion and projection invalidation pilot passed |
| RI-015 | Implemented/tested; deployment pending | Immutable hidden-suite evaluator and Mission Control truth surface pass locally; no live-corpus reasoning qualification is claimed before VM2 activation and an independent held-out run |
| UI-003A/B/C | Implemented/tested/deployed/observed | Mac Research Workspace, grounded Copilot, graph exploration and canonical replay production-observed |
| OPS-001 | Implemented/tested/deployed/observed | Durable approval outbox and readiness-race closure production-activated |
| OPS-004 | Implemented/tested/deployed/partial | VM1/VM2 probes and the enrolled EXEC1 external observer are active; restricted direct-watchdog activation and correlated-outage rehearsal remain |
| OPS-005 | Implemented/tested/deployed/observed | Two verified generations, isolated 77-table restore drill and persistent VM2 timers retained |
| OPS-006/CHAN-002 | Implemented/tested/deployed/observed | Canonical conversations and durable threaded Telegram transport passed a two-thread restart replay |
| UI-007 | Implemented/tested | Integrated conversation-to-proposal/task/approval/evidence workspace passes source and responsive checks; Mac reinstall and live execution replay remain |
| GOV-001 | Implemented/tested/deployed/observed | VM2 migration and policy active; Mission Control current; immutable live allow/deny replay retained |
| GOV-002 | Implemented/tested/deployed/observed | Four independent lifecycle projections active on VM2; five-event live replay proved research/evidence do not imply operations or capital authority |
| GOV-003 | Implemented/tested/deployed/observed | Typed consequence dossiers active on VM2; eight-record live promotion/reversal/expiry, quarantine/reinstatement and retirement/reinstatement replay retained |
| GOV-004 | Implemented/tested/deployed/observed | Signed 2,204-event portable audit export retained; fresh-client reconstruction and tamper rejection passed |
| AGT-001 | Implemented/tested/deployed/observed | Exact-package charters/grants enforced at lease time; 14-agent/41-grant bootstrap and live allow/revoke/deny replay retained; Mac UI live with 14 active charters and 41 active grants |
| PLAT-002 | Implemented/tested/deployed/observed | Fourteen identities and zero uncovered active-package credentials; central scope enforcement, secret-policy and emergency-access lifecycles, credential rollback and Mac identity inventory passed live replay |
| AGT-002 | Implemented/tested/deployed/observed | Exact task-attempt context replay binds live authority and canonical evidence; protected/stale/contaminated/oversized packs fail closed; digest-only scratch was discarded in a non-executing live pilot |
| ALPHA-008 | Implemented/tested/deployed/observed | Initial BTC-scoped no-capital certificate: two terminal one-year negative BT-009 outcomes and exactly-once replenishment retained; broad catalog visibility does not imply broad execution authority |
| ALPHA-009 | Implemented/tested/deployed/observed | Terminal one-year SOLUSDT-to-ETHUSDT negative publication closes the declared adaptive multi-asset boundary; arbitrary panels/transforms remain outside it |
| ALPHA-010 | Source policy only | Capacity executors are active but the eligible queue is empty; queue-depth control, fallback work and Mission Control utilization evidence remain open |
| RI-017 | Source trust policy only | External public evidence is not yet fetched by a deployed isolated worker; current ALPHA reasoning agents remain network-disabled |
| DISC-010 | Planned | Native components exist, but no continuous universe-wide outcome-separated OHLCV surveillance producer is deployed |
| Codex authentication recovery | Implemented/tested/deployed/observed | VM1 real-probe watcher, VM2 recovery registry, restricted Telegram notice/retry and Mission Control recovery panel observed on 2026-09-27; no task or financial authority added |
| BT-001 | Implemented/tested/merged | Canonical Python 3.11 contract matrix closes recorded collection and drift defects |
| BT-002 | Implemented/tested/merged | Immutable bounded dataset, availability and correction-lineage contract merged |
| BT-003 | Implemented/tested/merged | Atomic digest-finalized bundle and compatible Hermes producer contract merged; production run not yet claimed |
| Fast-path deprecation | Implemented/tested/merged | Classic event-driven execution is authoritative; legacy accelerated modes fall back explicitly |
| OPS-002, BT-004..009, WS-001 and later packages | Planned or partial as individually recorded | Do not infer completion from historical Hermes M-number pilots or prerequisite completion |

## 9.2 Backlog maintenance rule

Every task heading in `plans/CODEX_IMPLEMENTATION_BACKLOG.md` must acquire an
`Implementation status` paragraph when work begins and be updated at each gate:

1. branch/PR created;
2. source and automated acceptance complete;
3. merged to canonical branch;
4. migration/deployment complete;
5. live or parity evidence captured;
6. known limitations and next dependency recorded.

“Completed” is reserved for the package's stated done condition. If deployment or live
corpus evidence is part of that condition, merged code alone is `implemented`, not
`completed`.

The capability map and executable backlog are now structurally synchronized. All 110
canonical capability IDs in `plans/BIBLE_CAPABILITY_COVERAGE.md` have dedicated backlog
headings. The 80 packages that previously appeared only in compact coverage tables now
have explicit scope, reuse, missing-gap, contract, dependency, test, evidence, rollback
and done boundaries; this includes the full `BT-004` through `BT-008` laboratory chain.
Ledger validation fails if a future capability is added without an executable backlog
heading. This establishes complete planning coverage only: each new packet remains
`planned` until its individual implementation and operating evidence satisfy its done
condition.

## 9.3 Book XI update rule

Every merged feature that changes architecture, data, agents, permissions, workflows,
interfaces, infrastructure or verification must update this book in the same PR or a
linked documentation PR. The author must:

- update the snapshot date only for facts actually rechecked;
- cite repository, commit/PR, migration and validation record;
- classify source, test, rehearsal and deployment separately;
- update the agent table from manifests and the live count from API inventory;
- update diagrams when data flow or authority changes;
- describe migration, rollback, secret and compatibility effects;
- state non-goals and material gaps;
- avoid copying credentials, private payloads or raw corpus data.

## 9.4 Required snapshot commands

The following inventories must be refreshed before a release-level edition:

```text
Control plane: Git SHA, dirty state, Alembic head, OpenAPI routes, test totals
Workers: role-package manifests, workflow digests, systemd units, active deployments
Runtime: agents/heartbeats, tasks, package inventory, migrations, container health
RI: corpus coverage manifest, projection digests, graph manifest, replay samples, SLOs
Bulletproof: Git SHA, dirty state, test/collection matrix, schemas, lake manifest profile
Mac: Mission Control SHA/service status/inbox coverage
VM2: API image/health, broker/worker status, database/app/certificate/backup evidence
```

Runtime snapshots must be redacted and digest-bound. Secrets and authorization headers
must never be stored in this repository.

## 9.5 Immediate next gates

1. `CHAN-002` passed its live VM2 two-thread restart replay on 2026-08-24: reciprocal
   replies selected the correct canonical threads, revisions advanced exactly once per
   accepted reply and the gateway remained active with zero restarts. UI-007's joined
   execution timeline and evidence inspector are source-complete; reinstall Mission
   Control and retain one live proposal-to-task-to-artifact replay before upgrading it
   to production-observed.
2. Preserve BT-001 through BT-009 contract closure while extending real dataset and
   market-model coverage; do not reintroduce the deprecated fast path.
3. Execute `WS-001` to extend BT-009's bounded synthetic VM2 replay into the broader
   company walking skeleton without capital authority.
5. Install EXEC1's restricted direct-watchdog credential and rehearse correlated
   VM1/VM2 outage detection before upgrading OPS-004 from partial to
   production-qualified. Keep its Oregon egress limited to observability. Use the
   separate Lagos EXEC2 host for demo/live venue qualification.
6. Add encrypted off-host control-plane backup replication under PLAT-007; OPS-005's
   local verified lifecycle remains active but is not a substitute for disaster-domain
   separation.
7. Continue the company backlog while maintaining Book XI at every merge, deployment
   and production-evidence gate.

## 9.6 Reconciled merge boundary

The 2026-08-22 laboratory source boundary is:

| Repository | Capability | Canonical merge |
|---|---|---|
| `bulletproof_bt` | BT-001 contract-drift closure | `6a1cbbfbc69bd84281d466316e42e04698c1b3c5` |
| `bulletproof_bt` | BT-002 immutable dataset contract | `54220e21ad1b4b2110c00d243bd4326b7d67c76d` |
| `bulletproof_bt` | BT-003 atomic run bundle | `8f1418415cad4e2327f7e9a6dbb78257609f65e7` |
| `swarm-control-plane` | BT-003 canonical bundle reference producer | `4b7f7d1685c0af5a4cb81b621f49dfeabea5eff8` |
| `bulletproof_bt` | BT-009 governed proposal compiler and native qualification | `3cc4a49ee5189894f132a315d8adcc8f9edaa3dc` |
| `swarm-control-plane` | BT-009 registry-to-dual-memory bridge and VM2 completion evidence | `35001f5492f33b3ac976bf2c18e7827081faf05a` |

The BT-009 pins additionally have a bounded VM2 operational replay with a completed
digest-bound dossier. They do not prove a profitable market claim, capital readiness,
or the broader WS-001 company walking skeleton.

## 9.7 Visibility and intelligence truth gaps observed on 2026-08-24

A live corpus projection recovery exposed an operational visibility defect. The API and
PostgreSQL continued substantial background work after the initiating client was
interrupted, but Mission Control had no durable operation identity, phase, measurable
progress, heartbeat or cancellation/rollback state. Its graph view reduced the real
stale-projection conflict to `Knowledge graph unavailable`. `OPS-007` now provides a
fleet-wide operation ledger and global activity center. Migration `b7c3e8a91d40`, task
reconciliation and independent retrieval/graph progress reporters close the original
invisible-work path. The VM2 deployment, Mac installation and production graph replay
are recorded in the OPS-007 evidence section below.

The same audit established a necessary epistemic boundary. Published scientific
objects retain type, extracted text, page/line coordinates, extraction method and a
confidence score, and coordinate replay detects later extraction drift. The current
pipeline recognizes equations with a bounded text heuristic, while retrieval combines
exact and lexical matching, a deterministic hashed-vector baseline and explicit graph
neighbors. These are useful and evidence-grounded capabilities, but they do **not**
prove lossless mathematical representation, semantic understanding of every accepted
artifact or discovery of every latent relationship. Born-digital font mappings and OCR
can still substitute or lose symbols; tables and equations do not yet have canonical
cell/expression trees, scoped symbol definitions or units; graph edges represent
registered lineage and relationships rather than universal conceptual understanding.

`RI-014` therefore owns equation, table, figure, symbol and unit fidelity with
multi-parser disagreement evidence. `RI-015` owns held-out tests of citation, formula,
table, contradiction, abstention and multi-hop reasoning. Until those packages pass,
`published` means safe, bounded and replayable extraction, and `curriculum qualified`
means the declared curriculum checks passed at named corpus/projection digests. Neither
label means complete comprehension. Mission Control must expose that distinction.

RI-014 was implemented in source on 2026-09-05. Migration `fae4c6b93d20` adds an
immutable derived-representation registry and digest-bound corpus fidelity manifests.
Each accepted equation, table or figure remains linked to its canonical scientific
object and rendered-region digest. Unicode-normalized content, ordered mathematical
tokens, scoped symbol definitions, declared units and dimensions, table cell grids,
figure captions and canonical cross-references are retained alongside every parser
output. Two independent parsers must agree; OCR-only evidence, confidence below 0.90,
material disagreement or conflicting dimensions is retained as `review_required` and
cannot qualify a corpus manifest. This is a fidelity and replay contract, not a claim
that tokenization alone proves mathematical understanding. VM2 activation and the
held-out live corpus measurement remain visible production gates.

The first production measurement on 2026-09-05 exercised that boundary rather
than weakening it. VM2 manifest `73f09651-5f97-4eb0-9122-37aeadfe6706`, digest
`43e31d9d5d91b47e3703f593604c43b6bf67d1b2a289d73d0d115a8e657adf11`,
accepted three of 20 held-out equation regions and routed 17 to review; four
additional candidates had empty independent regions. Its `not_qualified` state
is the correct institutional conclusion. The equation-only pilot did not measure
table fidelity, so its placeholder cell score is not evidence. RI-014 remains
open for material-versus-layout disagreement analysis and a properly stratified
equation, table and figure corpus evaluation.

The forward path is deliberately utility-led. RI-014A reconstructs mathematical
structure and retains unresolved notation rather than guessing it. RI-014B creates
immutable independent adjudications and measures precision, recall, coverage and
abstention against real labels. RI-014C makes accepted formulae, symbol definitions,
units, tables and cross-references separately retrievable and supplies them to agents
in provenance-bearing context packs. Mathematical transformations and calculations
must run through bounded deterministic tools and retain expression, unit, output and
citation evidence. Mission Control reports what each agent has demonstrated it can
do, what portion of the corpus has usable structure, and what remains uncertain.

This makes the corpus useful before it is perfect: high-confidence accepted objects
can support explanation, comparison, hypothesis formation and Bulletproof
specification work immediately; uncertain objects remain searchable with source
images and prose context but cannot silently drive calculations. Progress is judged
by held-out company research tasks and reduced unsupported claims, not by asserting
that every page has been understood.

ALPHA-004 applies the same rule during continuous discovery. An LLM may act as a
source-bound locator, transcription assistant and explanation generator. It is not an
independent verifier of its own reconstruction. Exact source replay supports locating
and explanation only while RI-014 is unqualified. A separately identified deterministic
or independent receipt is required before an equation can drive a calculation or
qualification; otherwise the candidate records pending equation assurance and abstains.
This makes more of the corpus usable without converting model confidence into invented
mathematical truth.

RI-014D implements the just-in-time path rather than asking a founder to label every
equation in advance. Requests are cached by immutable evidence identity, automatic
machine verification uses two parser families plus exact source/token/AST checks, and
only failures or genuinely stronger assurance requests enter an exception queue.
Independent model output is admissible only with an AGT-006 receipt bound to that
request. Mission Control exposes pending, awaiting-independent, needs-attention and
verified counts. Global RI-014 corpus qualification and RI-015 reasoning qualification
remain unchanged; a successful just-in-time receipt must never be generalized beyond
its exact expression.

RI-014A entered source at control-plane commit `428bffa`. Its v2 reconstruction
contract removes the single-line whitespace table heuristic, retains complete bounded
equation continuations, separates glyph-faithful content from safe layout
normalization, and expands deterministic syntax trees to sets, tuples, vectors,
indexed symbols and implicit products. Unsupported or incomplete notation remains
lossless and review-required. Historical representation versions remain immutable;
production reconstruction must publish new v2 evidence and fail when a required
scientific stratum is absent.

RI-014B now supplies the missing ground-truth boundary in source. A representation
producer cannot adjudicate its own output. Independent reviewers record one of six
typed decisions with a substantive rationale, reviewer identity and role, corpus
digest, exact source-region digest, immutable record digest and hash-chained creation
event. Disagreement between reviewers is retained as a conflict and blocks benchmark
qualification; it is not resolved by majority inference or parser confidence.

Held-out benchmark membership is reproducibly selected by scientific type with a
declared seed and a digest-bound sampling algorithm. Precision, recall, coverage,
abstention accuracy, material-error escape rate, per-type confusion matrices and
Wilson confidence intervals are computed from adjudications, never supplied by the
parser under test. Recovery and parser workers may propose a corrected payload only
after a material decision, under a new representation version and in
`pending_approval`; they cannot self-adjudicate, mutate historical evidence or publish
the correction. Mission Control exposes the outstanding review queue and benchmark
progress. Deployment, independent live-corpus adjudication and the first live
benchmark remain required before this capability can be described as qualified.

RI-014C now adds the first deterministic utility layer over those representations.
Search is restricted to v2 evidence that is parser-accepted or independently labelled
equivalent and can match formula tokens, scoped symbol names and definitions, units and
dimensions, expression trees, table grids, captions and canonical cross-references.
Selections become immutable mathematics context packs containing canonical source IDs,
source-region and representation digests, exact structured content, uncertainties and
an explicit abstention rule. The Research Copilot may consult this pack beside ordinary
canonical retrieval, but mathematical claims still cite canonical source objects and
retain the separate mathematics-pack digest.

A bounded Decimal evaluator supports only deterministic numeric, symbol, grouping,
implicit-product and basic arithmetic AST nodes. It requires a registered context pack
that contains the exact accepted representation, retains substitutions, tree, units,
result and digests, and refuses missing symbols, material uncertainty, unsupported
operators, division by zero and unsafe exponent forms. It has no code, network,
filesystem, approval, deployment, order or capital authority. Immutable per-role
capability profiles bind demonstrated tasks, limitations and independent utility
metrics to exact corpus and representation versions. Fidelity qualification never
automatically qualifies an agent's mathematical reasoning.

The joint RI-014 production pilot now has an honest two-stage contract: freeze a
deterministic equation/table/figure sample and expose it for independent adjudication;
then refuse finalization until every item has one non-conflicting label. Its terminal
result is either an immutable qualified evaluation digest or a retained failure. No
automated parser or recovery worker fabricates the ground truth needed to pass.

RI-016 replaces disconnected post-publication calls with a durable retrieval, graph,
curriculum, portfolio and verification DAG. Its bounded delta path is gated by
continuous change history and has a full-rebuild fallback; per-phase receipts support
restart, concurrent epoch movement fails closed, and Mission Control shows active
reconciliation. Production migration `d2e8f5b13a70`, the VM2 orchestrator and the
thirteen-domain RI-009B `1.2.0` baseline are active. At epoch `577353`, forced-full run
`43885a98-501b-436a-9162-6f8fe4c9cdd5` reproduced the existing retrieval and graph
content digests exactly, with zero pending changes and `current=true`. Production
freshness and incremental/full equivalence are therefore evidenced rather than inferred.

## September 15 production truth audit

The native capacity director and two registered executor slots are active and
authenticated, but their queue is empty. Operational closure still requires two
overlapping terminal BT-009 attempts. Discovery workers restarted with the corrected
jitless subprocess environment; a successful fresh attempt is still required.
The current weekly mandate binds an old engine commit and a 30-day BTC window.
Only a distinct founder-approved mandate can authorize the reviewed engine and
one-year admitted window. Existing approvals must not be silently expanded.

RI-014D demonstrates just-in-time source-bound assurance, not global mathematical
accuracy. Twenty scientific benchmark regions remain unadjudicated, and RI-015
has no live reasoning evaluation runs. RI-016 freshness does not close either gap.
The senior researcher has literature retrieval and independent review wiring;
productive discovery is not yet demonstrated by the current zero-hypothesis mandate.

Mission Control's backtest activity projection exposes waiting/running/finished
tasks, tiers, frozen bindings, heartbeat phases, native summary metrics, failed
gates and receipts. It preserves failures and makes unknowns visible; Hermes
does not recompute quantitative results or infer admission from task success.

The backtest view is deployed on VM2 and reinstalled on Mac; live desktop/mobile
checks show 12 historical tasks and the eight-trial negative Tier2B attempt without
scroll jumps. A new one-year mandate first failed because the real-data admission
receipt bound the old native commit. The unchanged panel was re-admitted under an
explicitly verified native import path and `a864ac0` checkout, then registered on
VM2. The founder approved `ALPHA004-CAPACITY-20260915` on September 15.
Its first intelligence task `A4-aae38741-001-I` failed three attempts on
read-only Codex runtime initialization. The correction directs SQLite and logs
to a private attempt directory without making credentials writable. A live
startup probe then reached authentication but returned `refresh_token_reused`;
operator reauthentication remains required. Recovery requires a later explicit
task-resume event with exact mandate, cycle and stage bindings; original failure
events remain authoritative. Approval and online services are not productive
discovery proof. Two overlapping terminal BT-009 receipts remain outstanding.

Operator reauthentication and restart were followed by an audited resume at
20:04 UTC on September 15. Attempt 4 still failed startup. A read-only namespace
trace identified `CODEX_HOME/installation_id`, opened read-write, as the remaining
mandatory write. Hermes PR #265 gives discovery a private runtime home and binds
the original authentication file read-only into it; credentials are not copied
and `ProtectSystem=strict` remains enabled. Plugin/app integration is disabled
for bounded discovery. The corrected namespace completed authenticated inference
with `runtime-ok` after one temporary capacity response. The production units
still require privileged reinstall before another audited discovery resume.

The founder completed that reinstall at 20:10 UTC on September 15. Audited
attempt 5 completed intelligence inference at 20:13 UTC, but abstained because
its immutable context contained no literature citations. The abstention and
earlier failures remain evidence. Focused data-aware retrieval, under unchanged
calibration, now supplies canonical citations and bounded query receipts.
An initial recovery transaction failed atomically because two pending events
shared a sequence under `autoflush=False`; PR #267 fixes append ordering and
tests it against isolated PostgreSQL, rather than relying only on mocks.
The rebuilt VM2 API is healthy. Fresh cycle
`6ac128cf-9163-48d3-a1a7-e925db4a2704` contains nine citations and is processing
intelligence synthesis. Productive hypothesis acceptance, native qualification,
and two overlapping terminal BT-009 publications are still separate unclosed
gates. Neither LLM inference nor retrieved literature qualifies whole-corpus
mathematical fidelity or demonstrates RI-015 reasoning independence.

At 20:29 UTC that fresh cycle finished both inference stages and retained three
proposals, but accepted none. The worker output schema permitted underscore
domain/cluster keys that the canonical API schema rejects. All three therefore
remain `candidate_schema_invalid`, not scientifically falsified results.
Discovery runtime and citation recovery are demonstrated; producer/consumer
contract repair and two qualified concurrent native publications remain open.

The founder explicitly set full-lake autonomous integration as the next active
goal, tracked by ALPHA-007. Extend existing native DATA catalog/quality producers,
then hypothesis-driven representation and mixed-basket selection, discovery
contract closure, governed native strategy engineering, shared-budget concurrent
execution, and terminal publication with continuous replenishment, in that order.
Stable/volatile groups are optional descriptive metadata, not mandatory research
universes. Completion requires file-level catalog accounting and two genuine
qualified one-year native jobs with overlapping execution and terminal receipts;
online agents, fixture replay and BTC-only template reuse are insufficient.

ALPHA-007 now has native content-bound inventory and protected CLI source at
`ed2367b`, with 14 inventory/admission/producer tests passing. Hermes source at
`b75c22e` registers only that exact inventory producer, exposes its summary and
scoped operation reports, and corrects discovery identifiers and liquidity
context. The full backend suite passes 831 tests (one optional database skip),
and the worker suite passes 289. Actual full-lake scanning, registration, quality
qualification, broader approved execution and concurrent terminal publications
remain unproven. No expanded mandate, native-code approval or capital action
is inferred from this source evidence.

Production full-lake inspection subsequently counted 1,846,467 raw files and
2,769 canonical files. The single-envelope inventory limit was inadequate, so
the tracked production attempt was stopped explicitly; its failed ledger record
and progress were preserved and no scanner was orphaned. Full registration is
still open: bounded content-bound shard custody and a complete root receipt must
replace the oversized envelope. Native window-specific panel quality checks are
being added separately; neither inventory nor base OHLCV quality grants execution
authority or verifies auxiliary timing. This correction retains the entire lake
scope rather than treating the canonical subset as the full accounting goal.

The bounded custody correction is pushed in native PR #308 (`19d361c`) and
Hermes PR #269 (`7346bc8`). Native shard receipts retain at most 10,000 objects,
globally ordered paths and a source-bound completeness root; dataset identity
stays stable across scan IDs. Window quality consumes verified shards without
rebuilding the million-object envelope. Hermes checks complete custody and the
exact named quality gates without computing quantitative estimates. Fresh tests:
850 backend passed (one optional database skip), 295 worker passed and 32 native
focused tests passed. Corrective CI and production replay remain open; no full
registration, admitted candidate, broadened mandate or concurrent backtest is
claimed from these tests.

PR #270 subsequently merged and deployed to VM2 at `40ca4c759`, with container
verification of the all-eligible default. Eight CI gates passed; final full suites
passed 852 backend tests (one optional skip) and 302 worker. One unchanged
child-start timeout failed during a concurrent run, then passed isolated and full
reruns; this is retained rather than erased. The exact inventory unit remains
active. Long-running VM1 planner/researcher prompt loading still requires a
controlled restart, and full-lake completion and concurrent scientific execution
remain unproven.

The next engineering handoff source pass supplies the coder and independent
reviewer identical bounded, validated JSON scientific evidence rather than
leaving RI citations only in approval metadata. Evidence binds exact question,
candidate, campaign, admitted dataset, window and variant ceiling; altered source
evidence blocks task creation. New code remains explicitly approved, with native
draft-pipeline/runner integration included in the proposed scope and historical
approvals unchanged. Focused tests passed 20 campaign, eight proposal and 30
worker engineering/planner. Actual generated/qualified strategies and concurrent
native backtest receipts remain unproven.

PR #271 subsequently pushes the reviewed handoff, with deep-JSON and changed
question rejection confirmed by independent source review. Fresh full suites
passed 852 backend tests (one optional skip) and 309 worker; all eight CI checks passed, with deployment pending.
Independent live API readback confirms the exact inventory operation's running
state and fresh heartbeat. New native template discovery and independent
evaluator receipt binding remain necessary before claiming genuinely qualified
backtests; a constant boolean in qualification output is not sufficient proof.

Native exact-question generated-card discovery now has ten passing source tests.
It preserves immutable dataset/window bindings, rejects self-approval and unsafe
files, and computes the real grid size. This is source engineering evidence,
not scientific semantic qualification. The active roadmap is complete lake
accounting and admission, catalog-grounded adaptive discovery, genuinely
independent native strategy qualification, overlapping one-year classic runs,
terminal publication and automatic replenishment. Shadow and capital remain
separately gated on an actual survivor.

Independent review of the ALPHA-007 catalog-grounding pass caught chat/planner
overrides of the new universe default. Hermes `9c03a1f`, PR #270, corrects both;
conversation tests passed seven and planner tests 17. Full pre-correction suites
passed 852 backend tests (one optional database skip) and 301 worker tests. CI and
deployment for this follow-up remain pending, and the original full-lake scan is
still supervised under its exact unit/PID rather than restarted.

The next ALPHA-007 source pass exposes receipt-backed full-lake catalog grounding
to discovery without modifying executable mandate bindings. Universe hints default
to all eligible assets; fixed stable/volatile labels are optional. Tests reject
catalog-only ETH execution without an admitted binding. Focused backend tests
passed 57 cases, strengthened context tests 23, worker prompt/contracts seven and
lint passed. Deployment and genuine adaptive basket execution remain open.

ALPHA-007 production continuation merged native PR #308 and Hermes PR #269 after
ten native and eight Hermes CI checks passed. The worker suite passed 300 tests.
VM2 deployed healthy merge `2e3750da0`. VM1 user systemd unit
`alpha007-full-lake-20260915.service` supervises ledger-acknowledged run
`0767bfbe-206f-4290-9900-f9771b7a83b8`, bound to native `19d361c`. Incremental
shard publication must finish before complete-root registration and frozen
2025-05-01 through 2026-05-01 UTC panel quality. Full-lake registration remains
in progress, not completed; adaptive baskets, broader approved execution and two
concurrent terminal scientific backtests remain unproven. Service activity alone
does not close this boundary.

Independent ALPHA-007 pre-landing review caught incomplete traversal, unsafe file
reopening, special files, incorrect nested-column time bounds, fabricated summary
acceptance and concurrent report resurrection. Corrections at native `aa82838`
and Hermes `1743cf7` pass 19 native and 834 backend tests (one optional database
skip). PRs #307 and #268 are open with CI running. This is stronger source/test
evidence, not production registration or the requested concurrent backtest proof.

The subsequent ALPHA-007 source pass freezes actual authorized producer profiles
at lease and binds explicit immutable specification/causality reviews to the exact
approved card, data, window and grid. Drafter and qualifier identities remain
excluded even when the same agent changes package versions. Native execution
fails before compute without a bound approving review; zero-trial engineering
failures are retained without being called scientific falsification. Thirty-one
native regressions pass. Actual supervised reviewer registration/execution,
engineering-author provenance, deployment, broader approved lake admission and
two concurrent terminal BT-009 results remain open. The unchanged supervised
inventory run has progressed to 1,600 objects, not complete-root registration.

Automatic strategy/causality routing now creates a bound immutable route after
approval replay and excludes every frozen producer identity before evaluator
selection. Missing reviewer capacity is explicitly blocked and surfaced through
campaign planning detail. Source validation passes 49 focused and 875 backend
tests (one optional skip), with clean lint. Reviewer execution, blocked-route
recovery after profile registration and deployment remain open. The unchanged
native inventory child is verified live after 47 minutes; this is ongoing work,
not proof of full-lake admission or concurrent backtest completion.

Blocked strategy-review recovery now watches active evaluator catalog changes,
retries the same frozen request and appends audit evidence. It preserves producer
exclusions and avoids duplicate retries or replacing assigned reviews. Fifty-one
focused routing/campaign tests and lint pass. Reviewer provisioning/execution and
production deployment remain open. The original supervised lake inventory has
reached 1,730 objects without a restart; full registration is still unproven.

Later runtime evidence supersedes those live observations: VM1's prior boot ends
at 22:15 UTC and the next boot begins at 22:32 UTC. The transient inventory unit
was lost without complete receipts. Its operation is preserved as failed with
1,874 partial objects. Persistent user supervision with verified lingering now
runs replacement `93a00b1f-e9ae-4dca-931c-efc6bf9dd99a` under the same source
and window; no receipt or registration is invented. Read-only strategy-review
executor source passes the full 319-test worker suite, but actual role deployment,
workflow dispatch and authenticated completion remain open. This is stronger
delivery evidence, not a qualified review or a functioning end-to-end loop.

Reviewer source now integrates with existing workflow policy and restricted
dispatch. Assigned routes materialize governed tasks bound to source/evaluator
profile/package; completion records typed verdicts only under an authenticated
running lease after routed-subject and frozen identity replay. Full validation:
885 backend tests (one optional skip), 320 worker tests and clean lint. Actual
role/grant provisioning, deployment and genuine independent review remain open.
Replacement inventory continues under the same supervisor, reaching 1,221 objects;
neither complete-root admission nor concurrent scientific execution is inferred.

#### September 16: Deployed Review Contracts, Interrupted Inventory

The prior live-scan observation is superseded. VM1 rebooted again and replacement
run `93a00b1f-e9ae-4dca-931c-efc6bf9dd99a` stopped at 1,753 objects without a
root receipt. The Mac update was started after the freezes and is not their cause.
No recorded guest OOM/panic establishes the interruption mechanism; host evidence
is still needed. The scan remains stopped. VM2 now runs merged review-completion
contracts with healthy image/source verification; reviewer packages/profile
provisioning have 21 focused passing tests but actual services/review receipts are
not established.

Native recovery no longer needs to wait for a 10,000-file publication boundary:
per-object private checkpoints retain metadata, with root/source and filesystem
fingerprint invalidation and fresh traversal for added/deleted files. Fixture
recovery avoids rehashing unchanged objects. A reused digest remains a prior-byte
observation, not fresh integrity proof; selected execution inputs require separate
validation. This implementation is not a production scan success, data admission,
reasoning qualification or autonomous-loop closure. Two concurrent one-year
scientific results and automatic replenishment remain required evidence.

Reviewer runtime packaging follows existing worker sandboxing, with separate
private writable directories and read-only credential mounts; credentials are
neither copied nor rotated. Explicit installation/start are separate actions.
Per-service resource limits constrain memory, CPU and process count. A lease-loss
test exposed an orphaned shielded process-wait coroutine; the executor now owns
one wait task and cancels/joins it during cleanup. Native DATA-003 still freshly
hashes selected panel bytes. Template/tests are engineering evidence, not actual
independent judgment, scientific qualification or loop closure.

Live catalog inspection confirmed only two generic evaluator profiles and no
alpha review routes. Existing native executor producer profiles have now been
registered against their actual active signed packages and registry runtime
`hermes/0.3.2`: profile digests
`7569997c5724a8944b70691bad31194982a2cc86acfbe223714ce09afa5bc7ee`
and `d7fa26097c1752db2a087a1ba5a7b899fefbf516cde43cd19c89eaed87208857`.
The provider/model declaration describes native deterministic production, not an
LLM evaluation. Future leases can freeze this provenance; historical missing
provenance is not retroactively invented. No package, grant, credential, scope,
approval or reviewer authority changed. Strategy engineering, real evaluator
services and two concurrent terminal scientific attempts remain outstanding.

Digest-bound recovery preserved the terminal predeployment ungrounded cycle and
created a new cycle with current context. Cycle
`f838efba-d2bf-4aa1-a226-8b6c652d914d` has queued task
`A4-aae38741-009-I`, nine retained literature citations and explicit research
constraints: eight variants, the approved 2025-05-01 through 2026-05-01 window,
and the unchanged native source/mandate digest. This corrects the missing-context
handoff without rewriting prior outputs or treating historical commands as approval.
The task is not yet leased; complete lake registration and scientific execution
remain unproven. Grounding recovery is not loop closure.

#### September 16: Manifest-First Admission And Native Capability Binding

ALPHA-008 corrects the operational interpretation of “full-lake access.” Normal
research cycles do not recursively scan raw storage. They consume the immutable
native manifest catalog, which exposes 689 assets and 123 one-year candidates in
the current production receipt. Only a hypothesis's preregistered panel set is
then opened, freshly hashed, checked and registered through DATA-001/002/003.
A separate rare custody audit may still traverse every file, but it is neither a
per-cycle dependency nor a substitute for selected-input integrity.

The same weekly mandate freezes a native strategy-capability catalog at the exact
Bulletproof source commit. Reuse is an explicit senior-research decision and
requires matching mechanism, timeframe, input cardinality, finite grid, truth
semantics and logging contract. The resulting card binds the exact registered
YAML digest and does not pretend an LLM reconstructed its feature logic. Novel
mechanisms still require founder-approved code. Current registered strategies are
single-instrument: basket questions remain valid, but must route to engineering
rather than silently dropping every asset after the first.

Focused verification passes 89 backend, 28 worker and 37 native tests. Full
control-plane suites pass 897 backend tests with one optional skip and 333 worker
tests. Migration `c2a8e4f61d90` is the sole head. These are source claims only.
Native full-suite completion, reviewed merges, production deployment, a fresh
founder-approved weekly mandate, two overlapping genuine one-year Bulletproof
runs, terminal BT-009 publication and automatic replenishment remain the active
closure sequence. No alpha, shadow or capital authority is inferred.

#### September 23: Reconciled Production Truth

Control-plane PRs #346 through #352 are deployed. They stop repeated terminal-cycle
accounting, reconstruct counters from immutable evidence, rotate native execution to
bounded measured runtimes without widening authority, preserve charter compatibility,
rebaseline all 13 RI retrieval domains at corpus epoch 577456 without weakening
thresholds, and prevent an active native task from being discarded solely because
its campaign deadline passed. PR #352 additionally recovers a completed full native
receipt through a compact, identity-bound handoff when the evidence exceeds the
bounded worker-result contract.

Measured classic-engine throughput subsequently established that eight hours was
still below the real one-year runtime. PR #351 passed the complete 373-test worker
suite and raised only the bounded worker ceiling to 12 hours. The executor package
was rotated to version 1.3.0, and the unchanged risk-zero task entered its final
attempt with the same immutable plan digest.

The first genuine one-year result is a retained negative with eight trials and a
complete BT-009 publication/memory chain. Two approved jobs demonstrably overlapped,
although memory-calibrated admission correctly limited the replacement funding run
to four workers. That second run also completed negative, retaining four trials and
the failed matched-control-support gate. BT-009 bridge
`596171f2-2e8b-57e8-a405-186552478300` is complete through publication and memory.
RI-016 subsequently closed at corpus epoch 577480 with digest parity. Automatic
cycle-12 replenishment exists exactly once and novel code remains paused for founder
approval.

The operational claim must stay narrow. Manifest visibility covers 689 assets, but
current execution is authorized only for an admitted Bybit BTCUSDT panel. The
initial no-capital autonomous-loop certificate is therefore complete, but adaptive
multi-asset and mixed-basket execution remain ALPHA-007 work. RI-014D remains
source-bound just-in-time assurance rather than whole-corpus mathematical fidelity,
and RI-015 still lacks a live independent reasoning qualification. Nothing in this
evidence grants shadow, order or capital authority or claims profitability.

## 9.8 Autonomous laboratory state observed on 2026-09-27

ALPHA-008 has an initial BTC-scoped, no-capital operational certificate. Two genuine
one-year negative outcomes reached terminal BT-009 publication, duplicate mandate
accounting was reconstructed from immutable evidence and a successor discovery cycle
was created exactly once. The catalog exposes 689 assets and 123 one-year candidates.
This proves narrow loop closure, not broad multi-asset execution, alpha or capital
readiness.

ALPHA-009 adds the supervised outcome-blind representation role and native causal
materialization contract. The current multi-asset path is not yet qualified. Three
generated strategy revisions passed the full Bulletproof deterministic suite but were
rejected by independent reviewers. The latest review exposed a runner grid-type
mismatch, self-asserted caller-frame digests, incompatible required logging, an unused
grid dimension and missing runner-level regression coverage. The failures are retained;
shared runner, evidence and logging contracts require another correction. It must pass
deterministic checks, independent review and governed publication before the milestone
can close.

The shared Codex authentication runtime now has a deployed recovery watcher. A real
fixed-output probe detects rejected server-side credentials, one durable incident
carries short-lived device authorization state, and Telegram and Mission Control can
request a fresh code on the same incident. Tokens never leave VM1 and authentication
recovery grants no task or financial authority.

Defect closure is cross-context by policy. Shared dispatch, evidence, lifecycle,
outcome, held-out, logging, resource and validation defects must be fixed in their
common producer or validator and tested against both the original failure and a
materially different context. A patch that only makes the current ETH, BTC or SOL
fixture pass is not sufficient evidence of a sustained system correction.
