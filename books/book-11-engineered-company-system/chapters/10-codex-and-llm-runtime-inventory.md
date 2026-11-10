<a id="codex-and-llm-runtime-inventory"></a>
# 10. Codex and LLM Runtime Inventory

## 10.1 Purpose and claim boundary

This chapter inventories executable call sites where Codex or another language model
performs company work. It records roles and authority boundaries, not a claim that a
model is intelligent, correct, continuously active or scientifically qualified.
Configuration that names a model, a stored `model_family` field, a prompt fixture and a
test double are not model invocations.

The living [Hermes runtime register](../appendices/B-hermes-codex-and-llm-runtime-register.md)
records later operational detail for control-plane invocations. The chapter remains
the cross-repository inventory, including Bulletproof and the public Invariance
application.

The inventory is source-observed at these revisions:

| Repository | Audited revision | Scope |
|---|---|---|
| `swarm-control-plane` | `329ebd59f85949a8c9fa7183cb350b45bdc7ac52` | Hermes workers, planner, Mission Control, ingestion recovery and Codex authentication continuity |
| `bulletproof_bt` | `fd0ffae9d04583fcd4300e8308405fe2e32a0571` | Native adaptive-representation execution and optional experiment-result interpretation |
| `invariance_research` | `234ebb0337a27166a81aa8727259bd00ce0d1614` | Public research assistant and analysis synthesis |

These pins establish the audited source, not deployment. Only service evidence can
prove that a call site is deployed or active. Runtime state
below is the state observed on VM1 on 2026-09-27 unless another location is named.

### 10.1.1 Targeted authoring-runtime update, 2026-11-09

The strategy-engineering boundary changed after the pinned whole-system audit.
Production-systemd rehearsal now uses GitHub Copilot CLI as the primary bounded patch
author and Codex as the correction, independent code-review and infrastructure-fallback
runtime. The primary author runs in a disposable worktree with network and shell tools
denied; the observed successful rehearsal used only `apply_patch`, `glob`, `rg` and
`view`, selected model `gpt-6-luna`, and did not invoke the fallback. Its retained
report digest is
`c972634b810edfeb3019706256fab25fee98336d51bc9f0fbed04becfa5d5879`.

This is deployed runtime and rehearsal evidence backed by versioned source. The
implementation was merged to `swarm-control-plane` `main` by PR `#426` at commit
`37e6c14335cb28057b9b20a9d0c9f7423a2e135b`. The complete boundary and rollout
evidence are recorded in
`swarm-control-plane/docs/alpha-013-copilot-hybrid-authoring.md`.

## 10.2 Hermes and Research Intelligence invocations

| Invocation boundary | Real work performed | Access and output | Authority | Observed state |
|---|---|---|---|---|
| Founder conversational planner | Interprets a founder message against supplied grounding, decides whether to answer, clarify or compile, and emits a schema-bound proposal. A grounded request can use one reasoning call plus one proposal-compilation call. | Ephemeral read-only Codex directory; structured reasoning and proposal documents. | Cannot execute the proposal, approve it, deploy code, place orders or allocate capital. | `invariance-swarm-founder-planner.service` active on VM1 at audit time. |
| ALPHA-004 Research Intelligence director and senior researcher | Produces evidence-bound briefs and predictive, falsifiable questions from bounded corpus, failure, observation, portfolio, signal-screen, data and native-mechanism context. CSI, indexes and proxies are supplied as falsifiable priors, never empirical facts. | `codex exec`, read-only, network disabled, plugins/apps disabled; strict stage-specific JSON. | Proposes only. Deterministic validation, data admission, independent review and approval remain separate. | Supervised units were active on VM1 on 2026-09-30 under the single canonical weekly mandate; one previously leased legacy task was allowed to finish as immutable evidence. |
| ALPHA-009 data representation scientist | Selects a pre-outcome 1-100 asset proposal by default, member roles, clocks, transformations and rejected alternatives for an exact question. It may mix optional stable/volatile labels when causally justified. | `codex exec`, read-only, network disabled, plugins/apps disabled; `adaptive-representation-plan-v1.0.0` output only. Raw lake bytes and target outcomes are excluded. | Proposes data shape only. Deterministic point-in-time, common-window, liquidity, capacity and DATA-002/003 admission decide executability; it cannot tune on outcomes or run a backtest. | Supervised unit was active on VM1 on 2026-09-30; the canonical mandate exposes 120 instruments, permits proposals up to 100 and fixes the latest complete one-year window. |
| Engineering mission patch author | Writes only the unresolved bounded patch after deterministic feasibility, typed `StrategyIntent` compilation and scaffolding. | GitHub Copilot CLI is the observed primary provider in a disposable worktree. Network and shell tools are denied; allowed paths, tools, file count, diff size and duration are enforced before tests. Codex is used only for a correction pass or an infrastructure-unavailability fallback, never to provider-shop around a semantic failure. | Cannot push, merge, approve, trade, alter the frozen hypothesis or exceed the leased contract. | Hybrid authoring is deployed, production-systemd rehearsal passed on 2026-11-09, and the implementation is versioned on `swarm-control-plane` `main` at `37e6c14335cb28057b9b20a9d0c9f7423a2e135b`. |
| Engineering mission code reviewer | Reviews the generated patch after focused deterministic tests and full Bulletproof validation and emits a schema-bound approval/findings document. | A separate ephemeral, read-only Codex call in the engineering workspace. | Can reject the patch bundle; cannot approve scientific validity, merge code or authorize execution. | Invoked by engineering missions that reach review. It is not a substitute for AGT-006 scientific independence. |
| Independent alpha strategy reviewers | Compares the pinned implementation with the exact hypothesis card for either strategy fidelity or causality/leakage semantics. | Separate evaluator identities, read-only Codex, network/plugins/apps disabled; digest-bound verdict. | Review-only. No engineering, backtest, promotion, order or capital authority. | `spec` and `causality` reviewer units active on VM1 at audit time. |
| Mission Control Research Copilot | Answers founder research questions from canonical retrieval and optional mathematics context packs, separating cited source claims from uncited agent inference. | Read-only ephemeral Codex call over a bounded context pack; citations outside the pack are rejected. | Cannot approve research, execute strategies, deploy software or allocate capital. Mathematical context is not self-verification. | Mac service reinstalled and observed serving on `127.0.0.1:8790` on 2026-09-27. |
| Scientific-ingestion recovery adviser | Chooses among available deterministic repair, independent-parser and offline-OCR attempts from bounded diagnostics. | Advisory-only read-only Codex call; no artifact bytes, database or tools. Deterministic fallback remains available. | Cannot suppress scanner findings or authorize publication. | Implemented; recovery-steward unit inactive on VM1 at audit time. |
| M14B daily director script | Generates five cited, falsifiable research questions from bounded passages and prior evidence. | Manual/standalone read-only Codex invocation with structured candidate output. | No execution or approval authority. | Legacy/operator-invoked surface; not evidence that the current ALPHA-004 service ran it. |
| Alpha-loop production-parity rehearsal | Exercises the real engineering coder and reviewer against a synthetic disposable repository before activation. | Same Codex executor path as production, but no production API, market data, orders or capital. | Qualifies only the runtime boundary. It cannot qualify alpha or create a production scientific receipt. | The production executor is active; each scientific bundle still requires its own deterministic and independent qualification. |
| Codex authentication watcher | Runs a fixed-output real Codex probe so stale local login state is not mistaken for a usable server-side session. | Shared VM1 credential runtime under an exclusive refresh lock; only redacted state, verification URL, short-lived device code and expiry leave the host. | Authentication continuity only. It cannot reason about research, edit code, approve tasks or consume an experiment attempt. | Watcher active and recovery observed through VM1, VM2, Telegram and Mission Control on 2026-09-27. |

RI-014D does not ask a model to certify its own mathematics. It accepts deterministic
verification or a separately identified independent receipt. A model may locate,
transcribe or explain an equation, but that output alone cannot become calculation or
qualification authority.

The 2026-09-27 ALPHA-009 cycle 2 provides live evidence for these two research roles.
The senior researcher received exact recent-question exclusions plus a rotating
catalog frontier and proposed SOL-to-ETH, RUNE and XAUT/PAXG questions at 2h and 4h,
rather than paraphrasing another BTC question. The representation scientist retained
both assets in the two relative/cross-asset questions, kept RUNE single-asset because
another member was not causally necessary, and rejected fractional differentiation
because the frozen return and spread semantics did not require it. Deterministic data
gates then rejected the unavailable XAUT/PAXG panel and admitted ETH, SOL and RUNE.
This is evidence of proposal and representation range. It is not evidence of alpha or
a certified mixed-basket backtest; campaign `221c7817-f638-4a47-b4b2-7698ee62eedf`
still requires approved native engineering and independent evaluation.

## 10.3 Bulletproof BT invocation

Bulletproof's backtest, resampling, accounting, cost, walk-forward and metric
calculations are native deterministic code. They do not call an LLM.

The research daemon can invoke `orchestrator/interpret_experiment_results.py` after a
completed experiment. It sends a compact packet of measured run summaries,
diagnostics, stable/volatile comparisons and rule-based preliminary constraints to
either Ollama or the OpenAI Responses API. The model may choose only an allowed
interpretive verdict and recommend follow-up tests. Invalid output, timeout or provider
failure falls back to the rule-based verdict, and raw output/error evidence is retained.

The registered verdict has `approved_by_user=0`; therefore model interpretation is
not a promotion, deployment or trading authorization. The current implementation uses
the returned `human_approval_required` field to decide whether to enqueue an approval.
That flag must be forced true by deterministic policy before this interpreter is used
as part of an autonomous promotion path. Until then, treat the surface as analyst
synthesis only. The checked-in daemon default names Ollama, but live daemon/provider
health was not rechecked for this chapter.

## 10.4 Public Invariance application invocations

| Invocation boundary | Real work performed | Failure behavior | Authority |
|---|---|---|---|
| Research-brief clarification | Generates concise missing-assumption questions for a submitted market intuition. | Falls back to deterministic required-field questions. | Cannot confirm assumptions or start a backtest. |
| Program Research Copilot | Converts conversation and selected source chunks into schema-bound explanations and candidate hypotheses; OpenAI BYOK or configured hosted OpenAI/Ollama may be used. Read tools gather program state, sources and artifacts before inference. | Provider circuit breaker and deterministic fallback; canonical artifact-analysis mode bypasses model arithmetic. | Proposals remain proposed until user confirmation. It cannot approve, queue, deploy or trade. |
| Analysis insight synthesis | Explains deterministic diagnostics, distribution, Monte Carlo, execution and ruin outputs and suggests follow-up work. | Schema and contradiction checks reject invalid claims; provider failure preserves deterministic report content. | Presentation and recommendation only. It does not change measured metrics or create deployment authority. |

These public-application surfaces are configuration-dependent. Their presence in source
does not establish that hosted inference, Ollama or a customer BYOK connection is
currently enabled.

## 10.5 Human-operated Codex

Codex is also used interactively by the founder/operator to inspect repositories,
write and review changes, run tests, prepare deployment commands, diagnose production
evidence and update documentation. This is real engineering work, but it is outside
the autonomous agent loop. Its authority is the operator's current machine account and
tool permissions; Git history, pull requests, CI and retained rollout evidence are the
durable record. A conversational claim that Codex changed or deployed something is not
evidence without those records.

The fleet operation ledger does not yet provide a complete call-by-call inventory of
interactive Codex sessions, token use, model identity and resulting commits. This
chapter inventories executable roles, not every historical inference request.

## 10.6 Durable correction boundary

An experiment failure does not justify a fixture-shaped patch. Dispatch, evidence
binding, lifecycle accounting, outcome taxonomy, held-out evaluation, logging,
resource control and validation are shared contracts. A defect in one of those
contracts must be corrected at the shared producer or validator and receive both an
original regression and a materially different hypothesis, asset, timeframe or
failure fixture. Hypothesis-specific mechanisms and calculations remain in the native
strategy module.

This rule is active evidence, not retrospective polish. Three recent multi-asset
engineering revisions passed Bulletproof's full deterministic suite but were rejected
by independent reviewers. The latest review found that direct unit coverage concealed
a runner grid-type mismatch, evidence digests were derived from the same untrusted
caller frames they purported to authenticate, required logging remained incompatible,
one grid dimension was not consumed and no runner-level regression exercised the
governed path. The rejected bundles remain immutable evidence and are not merged or
called certified. Another shared-contract correction must complete deterministic
tests, independent review and governed publication.

## 10.7 Surfaces that do not invoke an LLM

- Telegram is a restricted transport and approval interface; it does not reason by
  itself. Conversational reasoning belongs to the founder planner.
- Native Bulletproof execution, dataset admission, resampling, backtest metrics,
  deterministic risk and venue/order controls do not use model output as arithmetic or
  action authority.
- `AGT-004`, `AGT-006` and `DISC-005` pilot records containing model names describe
  governance evidence; those fields do not prove a live invocation.
- Research graph, retrieval, curriculum, freshness and operation-ledger services are
  deterministic services unless an explicitly listed caller supplies their bounded
  output to a model.
- ALPHA-010 resource allocation is deterministic. Worker/RAM allocation, queue
  priority and idle-state classification do not use an LLM.
- DISC-010 basket rotation, resampling, transforms, empirical nulls, family correction
  and question-candidate receipts are native deterministic Bulletproof computations.
  No model selects assets from outcomes, calculates an effect or opens final OOS.
- RI-017 external retrieval and quarantine are deterministic connector functions. The
  senior researcher may reason over sanitized publication metadata through its already
  listed bounded invocation, but fetching a feed is not itself an LLM call. The worker
  may fetch allowlisted RSS/Atom, podcast transcript, publisher-abstract, exact-DID
  social and YouTube-metadata sources, but supplies only sanitized title, provenance
  and deterministic assessment to the model; bodies and retrieved instructions do not
  enter model context or gain tool authority.
- The AGT-009A source gate is deterministic. It applies SkillOpt-inspired trace,
  held-out, independence, authority and regression checks; no optimizer-model call is
  currently implemented or claimed.

## 10.8 Required maintenance

Any new model call must update this chapter in the same change or a linked
documentation change. The entry must name the executable call site, runtime identity,
input boundary, output schema, model/provider configuration, timeout and fallback,
retained evidence, authority denied, deployment location and last observed health.
Mission Control should ultimately expose this inventory and per-invocation telemetry so
model work cannot occur invisibly.

## 10.9 Executable source map

| Boundary | Authoritative source path |
|---|---|
| Founder planner | `swarm-control-plane/worker/src/swarm_worker/planner/engine.py` |
| ALPHA-004 discovery | `swarm-control-plane/worker/src/swarm_worker/executors/alpha_discovery.py` |
| Engineering coder and code review | `swarm-control-plane/worker/src/swarm_worker/executors/engineering_mission.py` |
| Independent strategy review | `swarm-control-plane/worker/src/swarm_worker/executors/alpha_strategy_review.py` |
| Mission Control Research Copilot | `swarm-control-plane/mission-control/src/hermes_mission_control/research_copilot.py` |
| Ingestion recovery adviser | `swarm-control-plane/backend/app/ingestion/recovery_controller.py` |
| M14B director | `swarm-control-plane/worker/scripts/m14b_director.py` |
| Production-parity rehearsal | `swarm-control-plane/worker/scripts/alpha_loop_rehearsal.py` |
| Codex authentication watcher | `swarm-control-plane/worker/src/swarm_worker/codex_auth_watcher.py` |
| Bulletproof interpretation | `bulletproof_bt/orchestrator/interpret_experiment_results.py` and `bulletproof_bt/orchestrator/analysis/llm_client.py` |
| Public clarification | `invariance_research/src/lib/server/research-programs/clarification.ts` |
| Public Research Copilot | `invariance_research/src/lib/server/research-copilot/reasoning.ts` and `invariance_research/src/lib/server/llm/chat-provider.ts` |
| Public analysis synthesis | `invariance_research/src/lib/server/llm/insight-service.ts` |
