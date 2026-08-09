# Founder’s Edition Source Audit

**Status:** Complete — source integrity, chapter dispositions, conflict adjudication, and migration controls recorded

## Source integrity

| Source | Pages | SHA-256 verified | Role |
|---|---:|---|---|
| Book I Founder’s Edition | 384 | `a7f72ccc9c93a816692f6a372958ab10ebf038f297ddda2f807abab6fc4a6391` | Constitutional doctrine |
| Book II Founder’s Edition | 138 | `5964661ba58e1de955dcb88fee5aeb0bf6dbecd3bcb20bc5e0ed55ba92ffd2be` | Operating specification |
| Book III Founder’s Edition | 208 | `c76eff6b82bedf5ad04b7b39b5f54b2ecf307c4c8f0fd2f0951bc8145b294b43` | Cognitive and memory architecture |

The checksums match `canon/README.md`. The source PDFs remain unchanged. Text extraction is a working aid and is not canonical.

## Initial findings

Book I contains thirty chapters spanning mission, scientific discovery, knowledge compounding, anomaly-first research, falsification, evidence, memory, representation, portfolios, autonomy, learning, complex adaptive markets, alpha, uncertainty, non-stationarity, information, causality, humility, invariants, and manifesto. Its doctrinal core remains authoritative, while operational and specialist treatments require cross-volume migration.

Book II contains thirty-eight chapters in ten parts. Its strongest material is the conversion of doctrine into organization, decision rights, separation of duties, lifecycle, registries, promotion, audit, and operating cadence. Later roadmap decisions supersede its broad ownership of Research Intelligence internals, agent construction, portfolio science, and platform implementation; Book II retains the organizational interfaces to those systems.

Book III contains sixty chapters in twelve parts. Its knowledge architecture, ingestion, retrieval, provenance, memory, evidence dossiers, graph projections, and corpus defense belong in Book III. Discovery methodology, ML instruction, specialist agent construction, deployment topology, and general implementation are redistributed to Books IV, VI, IX, and X, with Book III retaining only their cognitive-service and knowledge contracts.

## Gap, conflict, duplication, and supersession register

| ID | Type | Finding | Resolution |
|---|---|---|---|
| SA-001 | Supersession | Earlier roadmaps do not match the controlled ten-book sequence. | ADR-0001 adopts the ten-book sequence. |
| SA-002 | Duplication | Research Intelligence is described in Books II and III. | II owns operating dependency; III owns internal architecture. |
| SA-003 | Duplication | Agent taxonomies appear in Books II and III. | II owns decision rights; IX owns agent implementation. |
| SA-004 | Duplication | Discovery and representation recur across all founders’ volumes. | I owns doctrine, III knowledge support, IV discovery, VI learned representations. |
| SA-005 | Conflict risk | “Autonomous” language may imply self-promotion or unconstrained search. | Autonomy is bounded; exploration, evaluation, governance, and promotion remain separate. |
| SA-006 | Gap | Founder’s Editions predate the explicit shadow/replay/demo/micro-live/production distinction. | II defines gates; V/VIII/X define evidence and implementation. |
| SA-007 | Gap | Book V requires a version-pinned public implementation audit. | Resolved through the audit of Bulletproof BT commit `ba2a0314817607c5c79d604a0846e008c14379c2`; scope, checks, failures, and evidence limits are recorded in the [implementation reference register](IMPLEMENTATION_REFERENCES.md). |
| SA-008 | Conflict risk | Model-centric phrasing can collapse RI into an LLM. | Models are replaceable runtimes; deterministic evidence and durable memory remain external. |
| SA-009 | Gap | Claim types and evidence precedence were not uniformly marked. | Editorial and citation standards now control labels and authority. |
| SA-010 | Gap | Crypto-first scope could hard-code institutional abstractions. | Crypto is the initial model organism; generic contracts remain market-agnostic. |
| SA-011 | Supersession | Book I’s eleven “cortices” compete with the later five-organization Hermes model. | Treat cortices as capability projections only; five organizations remain authoritative. |
| SA-012 | Conflict | Book I sometimes calls Research Intelligence a library and Hermes the faculty/cortex. | Apply ADR-0002: RI is brain, corpus, and memory; Hermes is operating system and organization. |
| SA-013 | Gap | Book I’s discovery loop advances from shadow directly to micro-live. | Insert execution replay and demo as distinct environments under Book II governance. |
| SA-014 | Implementation overclaim | The Daily Research Cycle describes mature automated ingestion, monitoring, and scale as present behavior. | Label as target architecture and define phased acceptance in Book X. |
| SA-015 | Internal conflict | Book I defines alpha as cost-surviving information but also declares alpha independent of implementation. | Separate predictive edge, realizable alpha, and realized active return. |
| SA-016 | Category error | “Governance Alpha” and “Research Alpha” conflate institutional process quality with market alpha. | Replace the Alpha Atlas with a typed opportunity taxonomy. |
| SA-017 | Statistical ambiguity | Generic “confidence” language risks mixing confidence intervals, posterior probability, predictive coverage, and belief scores. | Type every uncertainty and confidence object; define its interpretation and calibration evidence. |
| SA-018 | Governance conflict | Book I treats doctrine as the highest level of ordinary organizational learning. | Constitutional doctrine changes only through explicit governance and ADR/canonical revision. |
| SA-019 | Technical ambiguity | Book I uses entropy, mutual information, and information gain partly as metaphors for knowledge and alpha. | Type probability objects and estimators; separate Shannon information from economic value and causal evidence. |
| SA-020 | Claim-class conflict | Book I requires mechanisms for every significant correlation. | Distinguish predictive, explanatory, and causal claims with different evidence burdens. |
| SA-021 | State-model duplication | Book I’s belief states combine evidentiary confidence and operational promotion. | Maintain independent epistemic and promotion state machines with explicit links. |
| SA-022 | Constitutional conflict | “Every belief is provisional” conflicts with permanent invariants. | Empirical beliefs are revisable; constitutional change requires explicit canonical governance. |
| SA-023 | Series conflict | Book I closes by calling every later book implementation. | Apply ADR-0001: Books II–III remain constitutional organization and cognition; IV–X extend the series by owned domain. |
| SA-024 | Organizational supersession | Book II defines seven divisions while later context defines five organizations. | Map responsibilities into Research, Engineering, Knowledge, Governance, and Production. |
| SA-025 | Evidence gap | Book II assigns a fixed 0.90 retrieval recall SLO without a benchmark contract. | Treat thresholds as evaluated, versioned operating targets defined in Book III. |
| SA-026 | Independence ambiguity | Separate agent profiles are treated as independent validation. | Evaluate shared runtimes, evidence, prompts, code, incentives, and correlated failure modes. |
| SA-027 | State conflict | Book II’s promotion flow omits replay/demo and orders production before portfolio eligibility. | Separate maturity from environment; require eligibility and risk budget before production. |
| SA-028 | Security risk | Comprehensive prompt/tool logging can retain secrets or protected data. | Apply redaction, minimization, access, and retention controls before persistence. |
| SA-029 | Environment conflict | Book II’s shadow stage includes simulated orders and fill/cost parity. | Shadow records no-order intents and outcomes; execution replay owns production-stack simulation. |
| SA-030 | Risk insufficiency | Micro-live capital “small enough to lose completely” is treated as the principal bound. | Add exposure, loss, leverage, permission, venue, and portfolio hard limits. |
| SA-031 | Implementation assumption | Mac/VM1/VM2 and a multi-repository layout are presented as architecture. | Preserve logical boundaries; defer physical topology and repository form to Book X. |
| SA-032 | Acceptance ambiguity | “Memory creates better questions” is used as a Hermes v1 acceptance criterion. | Test provenance, retrieval, linkage, and subsequent task availability; evaluate question quality separately. |
| SA-033 | Roadmap supersession | Book II’s phases omit execution replay and demo. | Apply the later Phase 0–5 roadmap and explicit validation environments. |
| SA-034 | Implementation overclaim | Book III specifies Bulletproof BT outputs before the required implementation audit. | Treat fields as target integration contracts until verified against pinned code and artifacts. |
| SA-035 | Replay ambiguity | Book III implies current retrieval must reproduce decisions after index upgrades. | Replay recorded immutable versions or candidate sets; evaluate current indexes separately. |
| SA-036 | Statistical ambiguity | Institutional beliefs are described generically as confidence-weighted priors. | Type belief and uncertainty semantics; reserve Bayesian terminology for defined probability models. |
| SA-037 | Information ambiguity | Graph “information” edges mix Shannon, predictive, novelty, and institutional-value meanings. | Require an explicit definition, estimator, scope, and evidence for every information relation. |
| SA-038 | Retention conflict | Immutable lineage and permanent memory can conflict with privacy, security, and lawful deletion. | Preserve auditable tombstones and derivation metadata while enforcing governed retention and erasure. |
| SA-039 | Ownership conflict | Book III makes hypothesis generation and research agenda management RI internals. | RI supplies evidence and memory; Book IV owns discovery, while Book II owns authority and budgets. |
| SA-040 | Method overreach | Book III lists specialist statistical methods as if they form a generic validation contract. | Treat as sourced examples selected from estimand, dependence, design, and search history. |
| SA-041 | Role overclaim | The Senior Quantitative Researcher is described as an available integrated cognition. | Label as target role architecture and preserve independent promotion authority. |
| SA-042 | Anomaly overconstraint | Temporal consistency and plausible mechanism are required before an anomaly is retained. | Preserve transient and mechanism-unknown deviations; require evidence before hypothesis or trade promotion. |
| SA-043 | Runtime assumption | Mathematical reasoning is defined as an LLM delegating to tools. | Keep the reasoning runtime replaceable; deterministic tools remain authoritative. |
| SA-044 | Technology overcommitment | PostgreSQL, pgvector, object storage, and Mac/VM topology are described as architecture. | Preserve catalog/index/object/logical-boundary requirements; decide technologies in Book X. |
| SA-045 | Event semantics | Append-only events are described as facts. | Treat events as immutable historical assertions whose content may later be corrected or disputed. |
| SA-046 | Taxonomy conflict | Sealed holdouts, shadow, and micro-live are listed as one partition hierarchy. | Separate data-access classes from validation environments and add replay/demo. |
| SA-047 | Evidence integrity risk | “Instruction stripping” may mutate source documents during corpus defense. | Preserve raw protected sources; create sanitized derived views with lineage. |
| SA-048 | Calibration ambiguity | Confidence is scored against generic “later survival.” | Define event, horizon, censoring, scoring rule, and claim type before calibration. |
| SA-049 | Acceptance overreach | RI v1 must autonomously produce a nonredundant research program and learn correctly. | Accept demonstrable evidence, memory, dossier, registration, ingestion, update, and later-task reuse capabilities. |
