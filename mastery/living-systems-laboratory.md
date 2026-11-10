# Living Systems Laboratory Protocol

## Purpose

Every substantial improvement to Invariance Research should improve two systems: the
software institution and the founder's ability to design it independently. This
protocol governs learning-oriented changes. It does not delay emergency containment,
security response, or capital-safety action.

## When the protocol applies

Use it for new agents, orchestration changes, state models, cross-repository contracts,
memory or retrieval mechanisms, schedulers, authority changes, consequential UI
projections, scientific gates, and execution/risk architecture.

Small copy edits, mechanical dependency updates, and well-understood repairs can use a
lighter review. If a change alters who decides, what is canonical, what can execute,
or what proves success, it is substantial.

## The ten-step cycle

### 1. Observe

Inspect actual source, tests, runtime evidence, and historical failures. Record what is
implemented, verified, planned, and unknown. Do not begin with a preferred technology.

**Founder output:** annotated execution path and questions.<br>
**Codex role:** help locate evidence and challenge unsupported claims.

### 2. Explain

Study the underlying concepts until the current design can be explained without
repository jargon. Include state, concurrency, authority, and failure semantics.

**Founder output:** teach-back explanation.<br>
**Codex role:** correct inaccuracies and supply targeted references.

### 3. Hypothesize

State one falsifiable limitation. Example: “Repeated strategy-engineering failure is
primarily caused by semantic card/code mismatch detectable before model invocation.”

Specify observations that would reject the hypothesis.

### 4. Compare

Produce at least two viable designs plus a simpler baseline. Compare correctness,
operational complexity, failure modes, migration, cost, and reversibility.

**Forbidden shortcut:** “multi-agent” is not inherently an alternative unless roles,
information boundaries, and coordination are explicit.

### 5. Design

The founder proposes the architecture first: components, contracts, state, sequence,
authority, observability, rollout, and rollback. Unknowns remain marked.

### 6. Review

Codex performs adversarial review. It should look for race conditions, ambiguous
ownership, hidden shared state, leakage, confused authority, irrecoverable partial
effects, missing baselines, and unmeasurable success.

The founder accepts, rejects, or revises each material criticism with reasons.

### 7. Implement

Responsibility follows the assistance ladder in ADR-0006. The founder implements a
meaningful, coherent part rather than typing ceremonial fragments. Generated code is
reviewed line by line before acceptance.

### 8. Test

Use deterministic unit and property tests, integration contracts, simulation, and
fault injection. Model-based evaluators supplement but do not replace executable
invariants. Capital remains disabled unless separately authorized.

### 9. Measure

Compare against the prior system and baselines using preregistered metrics. Include
reliability, latency, cost, interventions, duplicate work, and reproducibility. A
negative result is retained.

### 10. Reflect

Record what was predicted, what occurred, why they differed, what was learned, what
remains uncertain, and whether the change should ship, revise, or be abandoned.

## Required design packet

Before implementation, a substantial change should have:

- problem and evidence;
- current execution path;
- concepts to learn;
- alternatives and simple baseline;
- founder's proposed design;
- state and sequence diagrams;
- authority and data boundaries;
- failure model and recovery;
- test and benchmark plan;
- rollout, rollback, and evidence criteria.

## Safe experimentation levels

| Level | Environment | Permitted effects |
|---|---|---|
| `S0` | Static/source | Read and model only |
| `S1` | Unit fixture | Temporary local state |
| `S2` | Isolated integration | Disposable database, mock tools |
| `S3` | Staging/paper | Governed services, no capital |
| `S4` | Demo venue | Explicit drill authority, no live capital |
| `S5` | Live | Separate approval, risk controls, and runbook required |

The apprenticeship defaults to `S0-S3`. This document grants no `S4` or `S5`
authority.

## Model-assistance disclosure

Every learning artifact records whether a model:

- located evidence;
- explained concepts;
- proposed architecture;
- wrote code;
- wrote tests;
- interpreted results; or
- edited the final explanation.

The founder repeats critical reasoning independently. Model output is not evidence of
understanding or independent verification.

## Exit review

Before a change is considered learned and complete, the founder should answer:

1. What invariant does this preserve?
2. Where is canonical state?
3. What happens under duplicate, delay, crash, and restart?
4. Why is this more complex than the baseline?
5. What measurement justifies that complexity?
6. Which evidence would make us revert it?
7. What can it authorize, and what can it never authorize?
