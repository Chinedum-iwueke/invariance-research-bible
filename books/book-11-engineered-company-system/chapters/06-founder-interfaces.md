<a id="founder-interfaces"></a>
# 6. Founder Interfaces and Operating Channels

## 6.1 Mission Control

Mission Control is a loopback-only FastAPI application on the Mac with a static
operational UI and a local SQLite index for explicitly approved local text knowledge.
Its control-plane client uses the protected orchestrator token. The application exposes:

- fleet agents, roles, capabilities, permissions and package deployments;
- tasks, lifecycle state, missions, approvals and proposals;
- evidence artifacts, operational notes and service controls;
- research programs/cycles, domains, intelligence runs and memory exports;
- dataset manifests/builds, dossiers and surveillance records;
- founder intake and proposal/approval decisions;
- document upload and folder-based research inbox refresh;
- Bulletproof memory-sync proposal creation;
- UI-003A citation-grounded Research Copilot;
- RI-008 canonical graph exploration after deployment.

Mutating local API calls require `X-Hermes-Intent: founder-action`. Demo mode disables
mutations. The launch agent runs as user `ice`; environment and token files are mode
`0600`. Local text graph/search remains useful for founder notes but is not canonical
Research Intelligence. RI-008 replaces it as the primary scientific graph explorer.

### 6.1.1 Citation-grounded Research Copilot

UI-003A adds a conversational research surface without creating a general document
chatbot. Mission Control submits the founder question and optional project scope to the
canonical `hybrid-retrieval-v1.1.0` service. The control plane applies access and
lifecycle policy, calibrated hybrid ranking and graph-neighbor expansion, then creates
a bounded `citation-context-pack-v1.0.0`. Only that context pack is passed to the
configured protected Codex identity in a read-only ephemeral sandbox.

The model must return a strict answer document. Each claim is either `source_evidence`
with one or more exact context object IDs or `agent_inference` with no citation. Any
unknown citation rejects the complete answer. Retrieval abstention bypasses the model
and returns `insufficient_evidence`. Mission Control exposes retrieval confidence,
limitations, corpus/context/graph digests and an evidence rail whose citations replay
canonical coordinates through the control plane.

The founder experience is a dense three-pane workspace: conversation, bounded corpus
selection and answer evidence. Model output is not canonical evidence, a belief
revision, an approved hypothesis or permission to execute work. The initial source
boundary submits each turn independently; displayed prior answers never become
retrieval evidence. Raw source files, database credentials, protected tokens and
chain-of-thought remain outside the model boundary. The model adapter is replaceable
under LLM-001 without altering canonical retrieval or citation contracts.

## 6.2 Folder ingestion

The protected research inbox accepts PDF, Markdown and text. Refresh is digest
idempotent, retains originals, creates scientific-ingestion jobs, processes canonical
or quarantine outcomes, records an RI-007 inventory and rebuilds projections. Long
recovery refreshes run Mac-locally under `caffeinate` with protected logs so SSH loss
does not interrupt them.

The Research view also presents the canonical blocked-artifact register. Founder-facing
rows show classification, required action, attempt count and digest; the inspector
shows the bounded method ledger and whether a redacted-edition proposal exists. The UI
cannot reset terminal classifications or authorize publication. Recovered derived
artifacts are deliberately absent so one underlying source cannot appear as several
independent decisions.

## 6.3 Telegram gateway

The restricted Telegram gateway accepts messages only from the configured founder user
and chat IDs. It polls Bot API updates, forwards plain-English intake to the founder
planner, publishes bounded status notifications and presents approval/rejection links.
It stores neither sudo passwords nor arbitrary commands. Approval links are scoped,
expiring handoffs bound to the control-plane proposal/approval identity.

Telegram is an intent and approval channel, not a privileged terminal. Root operations
still require typed, approved broker actions; a password must never be sent in chat.

## 6.4 Plain-English request path

The founder planner converts natural language into a strict proposal containing
interpretation, assumptions, clarification questions, target role/reason, constraints,
task contract, expected outputs, acceptance criteria, risk, machine and capabilities.
The founder reviews that structure before materialization. Unsupported or ambiguous
requests stay proposals; the planner cannot invent role permissions.
