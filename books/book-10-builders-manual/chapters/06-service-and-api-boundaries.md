<a id="b10-c06"></a>
# Chapter 6 — Service and API Boundaries

Services own coherent state transitions and enforce authorization. APIs expose typed contracts rather than database tables.

## 6.1 Core services

Identity and policy; research registry; trial and scheduler; evidence and artifact; knowledge and retrieval; data catalog; model registry; portfolio risk; OMS and execution; agent task orchestration; and deployment control form the principal boundaries.

## 6.2 API rules

Authenticate, authorize, validate schema, require idempotency for mutation, return typed errors, paginate, rate limit, trace, and version. Reads expose immutable versions or explicit consistency.

## 6.3 Workflow

Long operations return task identity and lifecycle events. Retries do not duplicate scientific trials, orders, or deployments. Cancellation preserves partial evidence.

## 6.4 Compatibility

Consumers declare accepted schema ranges. Contract tests run across versions. Breaking change uses migration and parallel operation.

> **Builder rule B10-BD06 — Services enforce ownership**  
> Only the owning service mutates its canonical state; other components request transitions through authorized contracts.

## Source note

Domain ownership follows Books II–IX.
