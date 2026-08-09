<a id="b2-c15"></a>
# Chapter 15 — Audit, Security, Exceptions, and Incidents

Governance must remain effective when systems degrade, credentials are threatened, data are restricted, or ordinary policy cannot fit an urgent case. Hermes combines least privilege, attributable audit, bounded exceptions, and incident containment without turning surveillance into institutional memory.

## 15.1 Capability permissions

Permission is scoped to identity, resource, action, environment, time, and purpose. Ordinal access classes may summarize but cannot replace this capability model. Credentials are isolated from model context and general logs; access is revocable and expires by default.

Sealed evidence receives separate authorization and exposure accounting. Derived summaries and indexes inherit source restrictions.

## 15.2 Audit records

Material actions record requester, evaluator, authorizer, executor, object identities, policy version, time, result, and relevant reason. Audit records are tamper-evident at the level required by risk and are independently reviewable.

Audit is purpose-limited. Secret values, irrelevant personal content, and unrestricted private reasoning are minimized or redacted. A record can prove that a controlled tool call occurred without storing a credential or every intermediate token.

## 15.3 Exceptions

An exception states the rule, reason, scope, risk, compensating controls, approval, effective interval, review, and terminal disposition. It expires automatically. Repeated exceptions trigger policy review rather than becoming an unofficial permanent process.

> **Operating rule B2-OR15 — Exceptions do not erase boundaries**  
> An operating exception may narrow or temporarily alter a policy within delegated authority; it cannot waive a constitutional invariant or conceal the evidence of departure.

## 15.4 Incident response

The incident sequence is contain, preserve evidence, assess impact and potential impact, diagnose, remediate, verify, recover or retire, and publish the postmortem. Containment authority favors halt, isolation, revocation, quarantine, and exposure reduction.

Severity considers scientific integrity, capital, legal or security exposure, data contamination, service reach, and potential impact. P&L alone neither diagnoses nor measures an incident.

## 15.5 Recovery and learning

Recovery defines safe state, reconciliation, repaired artifact or configuration, verification, authorization, and monitoring. Restoration of availability is not enough if integrity remains uncertain.

Postmortems distinguish root, contributing, detection, and response factors; compare expectation with observation; and assign corrective actions with owners and verification. The record returns to Research Intelligence under access controls.

## Source note

This chapter consolidates the Founder’s Edition, Chapters 20, 23, and 35 (pp. 72–83 and 120–122). Security and operational implementation belong to Book X; live execution controls belong to Books VII–VIII.
