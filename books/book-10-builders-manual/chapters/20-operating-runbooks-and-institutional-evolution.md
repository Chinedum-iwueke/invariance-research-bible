<a id="b10-c20"></a>
# Chapter 20 — Operating Runbooks and Institutional Evolution

Runbooks convert known operating conditions into safe, repeatable action. Institutional evolution uses incidents and evidence to change systems without erasing accountability.

## 20.1 Required runbooks

Data gap and corruption; failed experiment and stuck worker; schema incompatibility; model degradation; portfolio limit or drawdown; margin stress; venue outage; stale private stream; reconciliation mismatch; kill and flatten; credential compromise; agent injection; service outage; backup restore; deployment rollback; and evidence-access incident.

## 20.2 Runbook form

State trigger, severity, owner, prerequisites, exact read checks, decision points, authorized actions, safety limits, communication, evidence preservation, recovery verification, escalation, and closeout. Commands use explicit targets and avoid hidden destructive expansion.

## 20.3 Exercises

Review on schedule and after change; run tabletop and technical game days; measure detection, decision, containment, recovery, reconciliation, and learning. A runbook not rehearsed is a hypothesis.

## 20.4 Evolution

ADRs, schemas, policies, services, and books change through proposals, evidence, review, migration, and versioning. New capabilities do not silently broaden existing authority.

## 20.5 Series acceptance

The institution is buildable when requirements trace to services and evidence; primary artifacts remain immutable; experiments and models reproduce; capital and execution are constrained; agents are bounded; production is observable and recoverable; and every material decision retains accountable lineage.

> **Builder rule B10-BD20 — Operations complete the architecture**  
> A design becomes institutional only when ordinary work, degraded states, incidents, recovery, and controlled change can be performed from tested contracts and runbooks.

## Source note

This final chapter closes the implementation path from Books I–IX without redefining their ownership.
