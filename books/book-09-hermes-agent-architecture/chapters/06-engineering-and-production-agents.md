<a id="b9-c06"></a>
# Chapter 6 — Engineering and Production Agents

Engineering agents propose and test code, schemas, migrations, infrastructure, and runbooks. Production agents observe, diagnose, and execute only preauthorized operational actions.

## 6.1 Change workflow

Inspect repository and contracts, formulate a change, edit in isolated scope, run tests and security checks, produce diff and evidence, request review, and publish through controlled deployment. Agents preserve unrelated user changes.

## 6.2 Production boundary

Read-only diagnosis is broader than mutation. Restart, rollback, scaling, credential change, order mutation, and data deletion require explicit capabilities and often approval. Emergency actions follow predeclared policy.

## 6.3 Deterministic systems

Agents call compilers, validators, test runners, deployment controllers, risk services, and OMS APIs. Those systems enforce semantics. Natural language never substitutes for a typed destructive target.

## 6.4 Evidence

Record task, code and config versions, commands, outputs, approvals, deployment identity, monitoring, and rollback. Failed deployments remain attributable.

> **Agent rule B9-AG06 — Agents propose; controllers enforce**  
> Infrastructure and production mutation occurs through typed, least-privilege services with validation, idempotency, approval, and rollback.

## Source note

This chapter connects Book VIII operational controls to Book X deployment architecture.
