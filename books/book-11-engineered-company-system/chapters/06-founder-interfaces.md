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
- UI-003B canonical knowledge graph exploration.

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

### 6.1.2 Canonical Knowledge Graph Explorer

UI-003B turns the RI-008 read model into a bounded founder workbench. Mission Control
loads an access-filtered overview and may submit typed neighborhood, path or subgraph
queries to `/v1/research/graph/query`. Roots and optional targets are canonical UUIDs;
predicates come from the RI-008 vocabulary; direction is incoming, outgoing or both;
depth is at most five; and the browser renders no more than 100 nodes. Projection
freshness remains a control-plane gate and stale graphs fail closed.

The desktop visual is a deterministic SVG projection with categorical node shapes,
predicate-specific line styles, selection, zoom and fit controls. It is deliberately
not a browser-side force simulation or a second graph database. The accessible source
of truth is a native-button adjacency list with explicit source, predicate and target;
this list is the default on narrow screens. Selection exposes canonical type, project,
access class, digest and visible degree. Exact replay uses the same read-only coordinate
boundary as the Research Copilot.

A Copilot citation can become the root of a graph neighborhood without making the
answer or conversation canonical. The graph explorer cannot register edges, rebuild
projections, alter lifecycle state, approve hypotheses, run tasks or allocate capital.
Every displayed projection/query digest is evidence about a derived view, not authority
to change the evidence kernel.

Production acceptance on 2026-08-22 expanded a current-projection neighborhood to 50
nodes and 50 edges and replayed a canonical object exactly. The replay required 91.95
seconds at the current corpus scale, so Mission Control gives only that read-only call
a bounded 120-second timeout; the latency remains visible operational debt rather than
being hidden by an unbounded request.

### 6.1.3 Integrated Research Workspace

UI-003C presents Research Intelligence as one work surface rather than a stack of
unrelated tools. `Ask` contains the citation-grounded Copilot, `Explore` contains the
canonical graph and adjacency views, and `Library` contains Mac-local search, direct
source upload and digest-idempotent inbox refresh. Each mode is URL-restorable and
retains local state while hidden. Semantic tabs use roving keyboard focus, and the
mobile layout exposes the same content and actions rather than a reduced duplicate UI.

The shared working-context strip carries at most eight canonical identities between
modes. Citation inspection or explicit graph-node selection adds an ID, object type,
label and digest; duplicates collapse by ID. These entries exist only in browser memory
and can be individually removed or cleared. They do not silently constrain a Copilot
query, become a saved collection, enter an LLM prompt, register graph edges, alter
evidence lifecycle or write institutional memory. An entry is a navigation handle back
to canonical replay or a bounded graph query, never a new evidence object.

Production acceptance used canonical citation
`011a2e4b-25ff-572f-81f8-855433a2e961` as the same bounded graph root, returning
three nodes and two edges, then replayed the object exactly. This demonstrates that the
workspace handoff preserves canonical identity rather than passing labels, excerpts or
model prose between tools.

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
