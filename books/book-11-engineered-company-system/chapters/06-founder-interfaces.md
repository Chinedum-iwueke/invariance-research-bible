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
- RI-008 canonical graph exploration after deployment.

Mutating local API calls require `X-Hermes-Intent: founder-action`. Demo mode disables
mutations. The launch agent runs as user `ice`; environment and token files are mode
`0600`. Local text graph/search remains useful for founder notes but is not canonical
Research Intelligence. RI-008 replaces it as the primary scientific graph explorer.

## 6.2 Folder ingestion

The protected research inbox accepts PDF, Markdown and text. Refresh is digest
idempotent, retains originals, creates scientific-ingestion jobs, processes canonical
or quarantine outcomes, records an RI-007 inventory and rebuilds projections. Long
recovery refreshes run Mac-locally under `caffeinate` with protected logs so SSH loss
does not interrupt them.

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
