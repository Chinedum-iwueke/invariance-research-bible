# Book II Founder’s Edition Chapter Ledger

**Source:** *The Hermes Research Operating System*, Founder’s Edition, 138 pages  
**Status:** Working disposition register  
**Disposition vocabulary:** retain, revise, split, relocate, consolidate, supersede

The Founder’s Edition uses a compact specification template: purpose, constitutional basis, operating principles, control flow, required artifacts, failure modes, assurance questions, acceptance criteria, and implementation note. Version 2 retains this contract discipline but replaces repeated boilerplate with book-level controls and develops each chapter as publication-quality explanatory prose.

| FE chapter | Pages | Governing contribution | V2 disposition | Authoritative destination or action |
|---|---:|---|---|---|
| 1. From Doctrine to Operation | 10–12 | Constitution-to-policy-to-control chain | Retain and develop | V2 ch. 1 |
| 2. System Boundaries and Non-Goals | 13–15 | Hermes boundary; deterministic capital controls; human authority | Retain and reconcile | V2 ch. 2; apply ADR-0002 |
| 3. The Hermes Operating Model | 16–18 | Durable capabilities, typed artifacts, bounded workers | Retain and develop | V2 ch. 2 |
| 4. Institutional Organization | 20–22 | Divisions, executives, accountability | Supersede and map | V2 ch. 3; replace seven divisions with five organizations |
| 5. Decision Rights and RACI | 23–25 | Accountable owner, approval, veto, consultation | Retain | V2 ch. 4; place detailed matrix in appendix |
| 6. Separation of Duties | 26–28 | Originator, executor, validator, approver separation | Retain | V2 ch. 5 |
| 7. The End-to-End Production Loop | 30–32 | Lifecycle gates from question to allocation | Revise | V2 ch. 7; add replay and demo |
| 8. Research Programs and Bounded Autonomy | 33–35 | Charters, scope, trial/compute budgets, stopping | Retain | V2 ch. 6 |
| 9. Signal Discovery Before Strategy Construction | 36–38 | Predictive content before monetization wrapper | Split | Operating gate in V2 ch. 7; research method in IV |
| 10. Experiment Lifecycle | 39–41 | Registered intent, immutable execution and review records | Split | State authority in V2 chs. 8–9; execution contracts in V |
| 11. Research Intelligence Platform | 43–45 | Shared knowledge service and constitutional dependency | Narrow | V2 ch. 12; internals owned by III |
| 12. Knowledge Ingestion and Evidence Compilation | 46–48 | Operating ingestion and dossier requirements | Relocate | Book III; retain service-level dependency in V2 ch. 12 |
| 13. Graph and Memory Architecture | 49–51 | Graph views over common evidence and lineage | Relocate | Book III |
| 14. Retrieval, Dossiers, and Corpus Reasoning | 52–54 | Task-specific evidence retrieval and provenance | Relocate | Book III |
| 15. Agent Taxonomy and Profiles | 56–58 | Role profiles, tools, context, permissions, outputs | Split | Decision-role interface in II; implementation in IX |
| 16. The Senior Quantitative Researcher | 59–61 | Research direction and synthesis role | Revise | V2 chs. 3–4; agent design in IX |
| 17. Specialist Research Agents | 62–64 | Bounded specialist capabilities | Relocate | Book IX; authority interface in II |
| 18. Independent Validation Agents | 65–67 | Frozen evidence, adversarial and independent review | Split | Separation requirement in II; construction in IX |
| 19. Orchestration and Task Graphs | 68–70 | Dependency-aware tasks, retries, budgets, artifacts | Split | Workflow authority in II; implementation in IX/X |
| 20. Research Governor | 72–74 | Policy, budgets, sealed data, exceptions, gates | Retain | V2 ch. 8 and ch. 15 |
| 21. Trial Registry and Multiple Testing | 75–77 | Registration, attempt accounting, protected evaluation | Retain and develop | V2 ch. 8; statistical methods in IV |
| 22. Promotion State Machine | 78–80 | Governed evidence-based transitions | Retain | V2 chs. 9–10 |
| 23. Audit, Security, and Access Control | 81–83 | Identity, least privilege, audit, sealed evidence | Retain | V2 ch. 15; implementation in X |
| 24. Portfolio Admission and Allocation | 85–87 | Organizational admission authority and evidence | Narrow | V2 ch. 10; portfolio science in VII |
| 25. Shadow Trading and Prospective Evidence | 88–90 | No-order prospective scientific validation | Retain and correct | V2 ch. 14; distinguish replay/demo |
| 26. Micro-Live and Controlled Scaling | 91–93 | Tiny-capital operational evidence | Split | Governance in V2 ch. 14; mechanics in VII/VIII |
| 27. Prop-Firm and Account Constraint Overlays | 94–96 | External rule contracts and vetoes | Narrow | Authority in V2 ch. 13; risk engineering in VII |
| 28. Data Architecture and Point-in-Time APIs | 98–100 | Data authority and temporal correctness | Narrow | Organizational requirements in II; architecture in V/X |
| 29. Service and API Architecture | 101–103 | Stable domain services and contract boundaries | Relocate | Book X; retain operating dependency |
| 30. Deployment Topology: Mac, VM1, VM2 | 104–106 | Historical/provisional physical topology | Supersede | Logical environments in X; named hosts noncanonical |
| 31. Repository and Configuration Architecture | 107–109 | Source/config separation, releases, provenance | Relocate | Book X |
| 32. Human-Agent Collaboration | 111–113 | Human authority, agent assistance, escalation | Retain | V2 ch. 11 |
| 33. Dashboards and Decision Surfaces | 114–116 | Evidence-oriented operational views | Split | Decision requirements in II; implementation in X |
| 34. Operating Cadence and Reviews | 117–119 | Daily, weekly, monthly, quarterly review clocks | Retain | V2 ch. 16 |
| 35. Incident, Degradation, and Retirement | 120–122 | Incident response, demotion, quarantine, retirement | Retain | V2 chs. 10, 15–16 |
| 36. Phased Implementation Roadmap | 124–126 | Incremental institution build | Relocate and supersede | Book X; align with current five-phase roadmap |
| 37. Quality, Evaluation, and Acceptance | 127–129 | Conformance and operational acceptance | Split | Book-level acceptance in II; system implementation in X |
| 38. Definition of Done for Hermes v1 | 130–132 | Thin end-to-end institutional loop | Split | V2 ch. 17; build checklist in X |

Appendix material on pages 133–138 is migrated by object type: canonical objects and event vocabulary to Book X schemas; hypothesis and evidence contracts to Books IV–V; promotion evidence and readiness rules to Book II appendices.

## Part I–III evidence notes

### Part I — Operating Mandate

The first three chapters correctly convert doctrine into versioned policy, machine-enforced controls, observable outcomes, and auditable decisions. They require explicit authority, typed artifacts, immutable history, replay, negative-result memory, failure containment, and narrow permissions. Chapter 2 uses the earlier formulation “Hermes is the research institution”; Version 2 will state that Invariance Research is the institution and Hermes is its governed operating system and organization. The deterministic-boundary test—if failure can immediately lose capital, keep the critical path deterministic—is retained but expanded: calculation, simulation, risk verdicts, state transitions, and primary evidence remain deterministic even when capital is not immediately at risk.

The identical assurance and acceptance boilerplate repeated in every chapter weakens the book’s prose and occasionally imposes irrelevant requirements. Version 2 will define series-wide and book-wide control matrices once, then add chapter-specific tests.

### Part II — Organization and Decision Rights

The Founder’s Edition specifies seven divisions and named human roles. The later architecture supersedes this with five cooperating organizations: Research, Engineering, Knowledge, Governance, and Production. Useful responsibilities are mapped rather than lost: portfolio/risk authority spans Governance and Production; data/platform belongs to Engineering; Research Intelligence curation belongs to Knowledge. RACI is helpful for concrete workflows but “exactly one accountable owner” requires a defined decision scope and does not eliminate independent veto authority. Human responsibility for material capital risk remains explicit.

Separation of duties is a constitutional operating requirement: proposal, experimental execution, independent evaluation, governance authorization, and production operation must not collapse into one actor. Separation applies to capabilities and permissions, not merely agent names; spawning two agents with the same model, context, incentives, and authority does not create meaningful independence.

### Part III — The Research Production Loop

The loop correctly begins with a question and registered hypothesis, distinguishes signal evidence from strategy construction, and treats failed or rejected attempts as part of the search history. Bounded autonomy requires scope, datasets, transformations, tools, trial and compute budgets, elapsed-time limits, stopping rules, and closeout artifacts. Expected information value is a governance judgment under uncertainty, not a precisely observable stopping metric.

The Founder’s gate sequence moves from historical validation to shadow and micro-live, omitting execution replay and demo. Version 2 adopts the complete evidentiary sequence and distinguishes scientific gates from engineering gates. Chapter 9’s default studies—quantiles, information coefficient, monotonicity, breadth, turnover, and horizon decay—are useful for some cross-sectional signals but not universal acceptance criteria. Chapter 10 correctly separates an experiment specification from executable runs and immutable artifacts, while its requirement to hash a “container” is implementation-specific; a reproducible environment fingerprint and dependency lock are the actual contract.

## Terminology candidates from Parts I–III

`operating policy`, `machine-enforced control`, `institutional ledger`, `department`, `organization`, `decision right`, `veto`, `separation of duties`, `research program`, `bounded autonomy`, `search history`, `signal evidence`, `monetization design`, `experiment`, `run`, `artifact bundle`, and `environment fingerprint` require controlled entries or confirmation.

## Part IV–VI evidence notes

### Part IV — Research Intelligence and Memory

The four chapters contain strong Research Intelligence design: the model reasons over institutional intelligence but does not contain it; source evidence, structured claims, experiments, procedures, beliefs, and inference remain distinct; opposition is retrieved deliberately; scientific objects preserve coordinates and extraction quality; graphs are evidence-linked projections over canonical identities; and dossiers are task-specific, balanced, and citation-replayable. These internals now belong to Book III. Book II retains the organizational requirement that every governed task can request an evidence dossier and publish its resulting records back to Research Intelligence.

The retrieval service-level objective of recall at least 0.90 for “critical evidence” is not meaningful without a versioned benchmark, relevance judgments, confidence intervals, query strata, and the cost of omission. It becomes an illustrative acceptance measure in Book III, not a constitutional threshold. Likewise, “every major claim receives an opposition search” is a workflow policy whose scope and stopping condition must be defined.

### Part V — Agents and Orchestration

The agent chapters distinguish reusable capability profiles from task instances, give the Senior Quantitative Researcher a synthesis and direction role, preserve specialist boundaries, require validators to work from frozen evidence, and use dependency-aware task graphs with bounded retries and budgets. These are valuable interfaces. Book IX owns model-runtime selection, prompts, tool composition, communication, context, evaluation, and deployment; Book II owns which role may request, evaluate, approve, or veto work.

Independence cannot be established solely by a different agent profile. Evaluation must consider shared model lineage, prompts, training information, retrieved evidence, code, incentives, and failure correlation. Frozen evidence packages protect review from post-result manipulation but can also omit material context; validators need a governed mechanism to request additions without allowing the originator to rewrite the reviewed artifact. Orchestration retries must create new attempts with lineage rather than erase or overwrite failures.

### Part VI — Governance, Registries, and Control

The Research Governor is correctly prohibited from becoming a research collaborator. It enforces budgets, sealed-data boundaries, promotion requirements, tool scopes, credential boundaries, exceptions, and kill authority. Governance rules require their own change control, expiry, appeal, emergency behavior, and independent audit; a policy service must not become an unreviewable source of power.

The Trial Registry usefully distinguishes hypothesis, specification, parameter, selection, and holdout-exposure events. These are not necessarily disjoint trial units, and statistical correction cannot be derived from counts alone; selection mechanisms and dependence among tests matter. The registry preserves the actual adaptive search history so Book IV can choose defensible adjustments.

The promotion machine is structurally sound—states have entry evidence, permitted actions, exit criteria, expiry, and rollback—but its state order is inconsistent and incomplete. The printed flow places “production” before “portfolio eligible” and advances shadow directly to micro-live. Version 2 separates candidate maturity from environment execution and includes execution replay and demo explicitly. Production eligibility requires portfolio admission and risk budget before production operation, not afterward.

The security chapter correctly enforces least privilege, signed packages, sealed-data access events, credential isolation, revocation, and risk-reducing emergency authority. Logging “prompt/tool inputs” must be subject to secret redaction, privacy, data minimization, and retention policy. The A–E access classes are provisional examples; permissions should be capabilities scoped to identity, resource, action, environment, time, and purpose rather than a single ordinal class.

## Terminology candidates from Parts IV–VI

`evidence dossier`, `belief registry`, `graph projection`, `retrieval benchmark`, `agent profile`, `task instance`, `validator evidence package`, `Research Governor`, `policy exception`, `trial family`, `selection event`, `holdout exposure`, `candidate maturity`, `validation environment`, `permission capability`, and `kill authority` require controlled definitions.

## Part VII–X evidence notes

### Part VII — Portfolio, Shadow, and Production

Book II should govern portfolio admission—who decides, which evidence package is required, what vetoes apply, when approval expires, and how demotion occurs—while Book VII owns forecast normalization, covariance, capacity, constraints, allocation, and risk budgets. Mechanism dependence complements but cannot replace return, residual, exposure, liquidity, and stress dependence. A generic “confidence” input must be a calibrated, typed uncertainty object before it can affect allocation.

Shadow is correctly described as live prospective scientific observation with frozen logic, feature and signal parity, skipped-decision records, and visible outcomes. Its use of “simulated orders,” fill models, and “cost parity” crosses into execution replay. Version 2 restricts shadow to hypothetical intents and realized outcome observation; replay passes the live/recorded event stream through production-equivalent decision, risk, OMS, and adapter logic. Demo then tests a venue’s paper/test API and order lifecycle.

Micro-live is correctly framed as information and safety validation rather than income. “Small enough to lose completely” is necessary but not a sufficient risk policy: exposure, daily and total loss, leverage, operational reach, venue permissions, and correlated portfolio effects still require hard limits. Scale requires portfolio eligibility, measured evidence, incident closure, capacity assessment, and CIO/Risk authority; a few profitable outcomes never suffice.

Prop-firm rules remain versioned external constraints rather than alpha logic. The chapter’s proposed pass probability, breach probability, funded lifetime, and time-to-target outputs are model estimates with potentially severe uncertainty, not guaranteed service outputs. Current terms must be verified by effective date, authoritative source, account type, jurisdiction, and applicable exceptions. Book VII owns the quantitative models and survival controls.

### Part VIII — Data, Platform, and Engineering

Point-in-time data requirements are strong: distinguish event, receive, and availability time; preserve historical universe membership and delisted instruments; create corrections as new versions; and align batch and stream semantics. A raw/curated/snapshot pattern is illustrative rather than a mandated physical architecture. Direct file access is not inherently invalid, but every authoritative research input must resolve through a logged, versioned dataset contract with explicit availability.

Stable services should enforce policy, identity, schema validation, lineage, idempotency, budgets, and explicit errors. The listed APIs are capability groupings, not a settled deployment topology. Book X will decide service granularity from reliability, coupling, security, and operational cost rather than presume microservices.

The Mac/VM1/VM2 design is a historical target proposal, not current implementation or constitutional architecture. Version 2 retains logical research, control, data, and production environments with segmented permissions and signed promotion; Book X maps them to deployable infrastructure. The proposed multi-repository layout is also nonbinding. A monorepo does not inherently grant excessive access, and multiple repositories do not inherently create isolation; authorization, build boundaries, secret scopes, ownership, and release controls determine the security boundary.

### Part IX — Operations and Human Collaboration

Human–agent decision packets should present evidence, alternatives, dissent, uncertainty, authority needed, conditions, and expiry. Human approval must be substantive rather than a ceremonial signature. Material risk remains under accountable human authority until a later canonical decision explicitly changes that boundary; agents cannot infer permission from capability.

Dashboards are decision instruments with owners, freshness, lineage, thresholds, and runbooks. Role-specific views can share underlying components and canonical metrics, so “one dashboard serves everyone” is not automatically a failure. Operating cadence separates fast observation from slower scientific and capital change; urgency and incidents may invoke documented exceptions without allowing live noise to rewrite research retrospectively.

The incident doctrine—contain, preserve evidence, diagnose, recover or retire—is retained. Severity depends on impact and potential impact, not only the affected subsystem. P&L loss does not prove model decay, while stable P&L does not prove operational correctness. Postmortems distinguish root, contributing, detection, and response factors and publish lessons to Research Intelligence without exposing secrets improperly.

### Part X — Implementation and Assurance

The phased roadmap correctly prioritizes constitutional mapping, identities, schemas, evidence, registries, and governance before broad autonomy. It is superseded by the later Phase 0–5 roadmap, which introduces a shadow MVP early and explicitly adds execution replay, demo, micro-live, prop-firm readiness, portfolio eligibility, and scaling. Book X owns implementation sequence; Book II defines organizational acceptance.

Evaluation must cover retrieval, citations, prior-test detection, methodological fit, reproduction, calibration, leakage, security policy denial, prompt injection, parity, recovery, and audit completeness. “Gold-standard” suites require provenance, protected evaluation data, versioning, contamination controls, and ongoing maintenance. A model upgrade is a system change and receives regression evaluation in context.

The Hermes v1 definition is a target acceptance contract, not evidence of an existing system. A first complete loop must ingest and retrieve evidence, register a question and hypothesis, execute deterministic experiments, perform independent evaluation, issue a governed decision, publish all outcomes to memory, and collect prospective shadow evidence. Execution replay and demo may follow v1 if explicitly outside its acceptance boundary; micro-live and production cannot be implied by a shadow demonstration. The phrase “memory update creates better follow-up questions” is not deterministically testable; acceptance should instead verify that the update is retrievable, attributable, linked, and available to a subsequent governed task.

## Terminology candidates from Parts VII–X

`portfolio eligibility`, `risk budget`, `shadow intent`, `execution replay`, `demo`, `micro-live`, `constraint overlay`, `event time`, `receive time`, `availability time`, `dataset contract`, `logical environment`, `decision packet`, `operating cadence`, `incident severity`, `postmortem`, `system evaluation`, and `Hermes v1` require controlled definitions.

## Book II audit conclusion

All thirty-eight chapters and appendices have received dispositions and evidence review. The Founder’s Edition provides a strong contract-oriented skeleton but reads as repeated specification cards rather than a developed authored book. Version 2 will preserve its operational precision, centralize repeated controls, adopt the five-organization model, distinguish maturity from validation environment, and relocate specialist internals to Books III–X without weakening Book II’s authority over lifecycle and decision rights.
