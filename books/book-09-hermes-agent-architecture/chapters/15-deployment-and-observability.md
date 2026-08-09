<a id="b9-c15"></a>
# Chapter 15 — Deployment and Observability

Agent deployment binds a versioned workflow to identities, resources, policies, and telemetry. Observability must reconstruct decisions without exposing protected reasoning or secrets.

## 15.1 Deployment unit

Version model route, prompts, tools, schemas, policy, context builder, retrieval indexes, evaluation suite, and runtime image. Rollouts use shadow, canary, staged scope, and rollback.

## 15.2 Telemetry

Record task state, model and prompt identity, tool calls and outcomes, token and compute use, latency, retries, policy decisions, approvals, errors, side effects, and artifact references. Sensitive content is minimized and access-controlled.

## 15.3 Service levels

Define availability, latency, cost, completion, safety, and recovery objectives by task class. A graceful fallback may be abstention or human handoff.

## 15.4 Replay

Reconstruct workflow from versioned inputs and recorded tool results where external state cannot be repeated. Distinguish deterministic replay from resampling a probabilistic model.

> **Agent rule B9-AG15 — Observe consequence and context**  
> Agent telemetry records enough identity, state, policy, tool, and artifact lineage to diagnose outcomes without treating hidden reasoning as authoritative evidence.

## Source note

This chapter defines logical requirements; Book X supplies concrete deployment components.
