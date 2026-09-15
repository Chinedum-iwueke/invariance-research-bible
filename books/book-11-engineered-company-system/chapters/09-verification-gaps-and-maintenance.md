<a id="verification-gaps-and-maintenance"></a>
# 9. Verification, Gaps and Maintenance

## 9.1 Current milestone ledger

| Package | Source state | Runtime/evidence state at 2026-08-22 |
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
