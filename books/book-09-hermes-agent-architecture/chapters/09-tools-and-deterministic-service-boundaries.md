<a id="b9-c09"></a>
# Chapter 9 — Tools and Deterministic Service Boundaries

Tools turn proposals into observations or actions. Their schemas and enforcement boundaries determine consequence more reliably than prompt wording.

## 9.1 Tool contract

Define name and version, input and output schema, side effects, idempotency, authorization, resource bounds, timeout, errors, audit, rollback, and data classification. Destructive tools require exact targets and previews where possible.

## 9.2 Separation

Use read tools for discovery, proposal tools for plans, and mutation tools for authorized change. High-risk tools require independent policy checks or approval. The model never receives raw secrets.

## 9.3 Validation

Arguments are parsed structurally, canonicalized, checked against grants, and rejected on ambiguity. Tool results are untrusted data until validated; success responses can still contain semantic failure.

## 9.4 Composition

Workflows use typed artifacts between steps. A deterministic service computes hashes, schemas, risk, orders, or deployments; the agent chooses among allowed calls and interprets results.

> **Agent rule B9-AG09 — Tools are the action boundary**  
> Safety claims are grounded in schema validation, authorization, idempotency, and side-effect control at the tool, not in an agent’s stated intention.

## Source note

Learned tool-use research is represented by [Toolformer](../../../bibliography/references.md#schick-et-al-2023-toolformer); institutional enforcement is a separate architecture requirement.
