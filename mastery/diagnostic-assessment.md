# Diagnostic Assessment

## Purpose

This assessment establishes what the founder can independently explain, design,
implement, test, and defend. It is not an exam of memorized terminology. Answers may
use repository source and official documentation, but should be completed without a
model generating the reasoning or implementation.

## Rules

1. Record start/end time, references consulted, and any assistance.
2. Predict behavior before executing a test.
3. Submit diagrams, code, tests, and explanations as applicable.
4. Mark uncertainty explicitly.
5. A working artifact without an explanation does not demonstrate mastery.
6. Use isolated fixtures only. Do not modify production or exercise capital authority.

## Evaluation rubric

| Result | Meaning |
|---|---|
| `Observe` | Can recognize the concept after explanation. |
| `Explain` | Can accurately explain the existing mechanism and its limits. |
| `Apply` | Can use the concept in a bounded implementation. |
| `Analyze` | Can diagnose failures and compare alternatives. |
| `Design` | Can create and defend a system under explicit constraints. |
| `Teach` | Can derive the design, anticipate objections, and teach it clearly. |

A result is supported by artifacts and reasoning, not self-rating.

## Diagnostic 1: Trace a durable task

Choose one task type. Trace request, persistence, approval, lease, heartbeat, executor,
attempt, terminal result, and parent reconciliation.

**Deliverables:** a sequence diagram; source symbols; transaction boundaries; five
failure points; expected recovery; and the evidence proving completion.

**Tests:** Can you distinguish task status from campaign phase? Can you identify the
single writer for each field? Can you explain what happens after a worker dies?

## Diagnostic 2: Implement a lease queue

In a temporary project, implement a PostgreSQL-backed or rigorously simulated queue
with two concurrent workers, lease expiry, heartbeat, bounded retry, idempotent
completion, and cancellation.

**Deliverables:** implementation, tests, invariant list, and a failure log.

**Injected cases:** duplicate claim, late heartbeat, completion after expiry, worker
death, poison task, and concurrent cancellation.

## Diagnostic 3: Explain one agent

Select one actual role and answer:

- What observation does it receive?
- Which decision truly requires a model?
- Which tools and state can it access?
- What authority can it exercise?
- How does it terminate?
- How is its output verified?
- What deterministic baseline could replace it?

**Deliverable:** an `AgentCapabilityContract` draft and a recommendation to retain,
simplify, merge, or remove the role.

## Diagnostic 4: Context and provenance

Select one research answer. Reconstruct every source object and transformation that
entered model context. Identify unavailable, truncated, or derived material.

**Deliverables:** provenance graph, context token accounting, unsupported-claim audit,
and a retrieval-improvement hypothesis.

## Diagnostic 5: Scientific contract

Given a research question, write a falsifiable hypothesis card and typed strategy
intent. Specify event timing, data availability, representation, target, bounded
variants, costs, OOS design, failure criteria, and promotion criteria.

**Injected defects:** future join, incomplete resampled bar, target/exit mismatch,
survivorship bias, and uncounted variant expansion. Explain how each is detected.

## Diagnostic 6: Distributed failure reasoning

Without executing it first, predict the state of a campaign when:

1. VM1 loses network after leasing a task.
2. VM2 restarts during result publication.
3. The worker completes after its lease expires.
4. Redis is unavailable but PostgreSQL remains healthy.
5. The only worker with a required capability is offline.

Then compare predictions with an isolated simulation or existing tests.

## Diagnostic 7: Authority and threat model

Create a data-flow diagram for an external paper entering the corpus and influencing a
strategy proposal. Apply STRIDE or an equivalent method. Include prompt injection,
malicious files, stale grants, approval replay, and credential exposure.

**Deliverable:** threats, existing controls, gaps, and tests. Any recommendation that
lets research content acquire capital authority fails the exercise.

## Diagnostic 8: Observability

Starting from one Mission Control activity item, recover conversation, plan, task,
attempt, agent, campaign, native run, receipt, and decision. State which links are
direct, inferred, missing, or stale.

**Deliverable:** trace, metric-definition critique, and one redesign that prevents an
activity success from masquerading as a completed backtest.

## Diagnostic 9: Architectural comparison

For a fixed corpus-to-question task, design:

1. a deterministic pipeline;
2. a single-agent path; and
3. the current specialized multi-agent path.

Define hypotheses, controls, metrics, budget, sample, and failure criteria before
running anything.

## Diagnostic 10: Production recovery

In staging, deploy a bounded service, introduce one process failure and one dependency
failure, recover it, and write a postmortem.

**Deliverables:** release manifest, timeline, telemetry, recovery objectives, observed
loss/duplication, root cause, and durable corrective action.

## Five difficult architecture questions

These are the first oral-defense questions from Phase 1:

1. If PostgreSQL is the durable coordination point, which exact invariants prevent two
   workers from producing two authoritative terminal outcomes after lease expiry?
2. Where should the boundary lie between a model-generated research plan and a
   deterministic task graph, and what information is lost at compilation?
3. How would you demonstrate that the independent reviewer is meaningfully independent
   rather than a correlated second sample from similar training and context?
4. Which state is canonical when task, campaign, native Bulletproof run, Mission
   Control projection, and receipt disagree, and how does the system converge?
5. What controlled evidence would persuade you that the multi-agent research loop is
   superior to one well-tooled agent, and what result would make you remove agents?

## Placement decision

After completion, record each domain's strongest demonstrated level in the learning
journal. The roadmap may accelerate demonstrated material, but no stage is skipped
solely because related code already exists.
