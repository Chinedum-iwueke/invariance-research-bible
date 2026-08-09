<a id="b2-c04"></a>
# Chapter 4 — Roles, Authority, and Decision Rights

A role is a bounded bundle of duties and permitted actions. Authority is the institution’s grant to make a specified decision. Capability is merely the ability to act. Hermes prevents capability from being mistaken for authority.

## 4.1 Decisions are scoped objects

“The researcher approves” is incomplete. A decision right identifies the decision type, object, environment, limits, prerequisites, duration, and accountable role. Approval to run a bounded backtest does not authorize holdout access, shadow observation, capital allocation, or production deployment.

Every material decision record contains:

- decision identity, type, and object version;
- accountable decision owner and participating roles;
- applicable policy and evidence requirements;
- evidence dossier and dissent considered;
- approval, rejection, deferral, or conditional disposition;
- conditions, limits, expiry, and required monitoring;
- vetoes exercised or explicitly cleared;
- signatures or authenticated attestations.

The record distinguishes recommendation from authorization and authorization from execution.

## 4.2 Role assignment

Roles attach to verified identities for defined intervals. A human or service may hold several roles where policy permits. An agent receives a task-specific role instance rather than an open-ended institutional title. Delegation states what may be delegated and what remains with the accountable authority.

Role assignment follows least privilege and conflict review. Permissions expire when the task, appointment, or emergency ends. Revocation takes effect independently of the worker’s cooperation.

## 4.3 Accountability and veto

A bounded decision normally has one accountable owner so that responsibility cannot disappear among participants. This does not create absolute power. Independent vetoes can prevent action when scientific validity, security, risk, legal duty, or operational readiness fails.

A veto is typed and scoped. It states the failed requirement, evidence, authority, affected action, remediation path, and appeal route. Vetoes cannot be used as unreviewable preferences, and an accountable owner cannot ignore a valid veto by restating the decision.

> **Operating rule B2-OR04 — Authority is explicit**  
> No material action derives authority from model confidence, technical capability, urgency alone, or an ambiguous organizational title; its decision right and applicable limits must be resolvable before execution.

## 4.4 Responsibility mappings

Hermes may use RACI mappings for recurring workflows:

- **Responsible** roles perform the work.
- The **Accountable** role owns the bounded decision or outcome.
- **Consulted** roles contribute required expertise before decision.
- **Informed** roles receive the decision or outcome.

RACI is descriptive, not an authorization mechanism. Permissions and transition policy enforce authority. A role listed as responsible for deployment cannot deploy an artifact lacking the required approval and signature.

## 4.5 Human and automated authority

Deterministic services may execute pre-authorized transitions whose policy, inputs, bounds, and failure behavior are explicit. Examples include rejecting an invalid schema, halting on a hard risk limit, or expiring an approval. Such automation exercises delegated policy, not independent judgment.

Agents can recommend and perform bounded work but do not infer broader permission from successful completion. Material capital risk remains under accountable human authority unless later constitutional governance explicitly changes that boundary. Human approval must be substantive: the decision surface supplies evidence, alternatives, uncertainty, dissent, and consequences.

## 4.6 Exceptions and emergencies

An exception identifies the policy departed from, justification, scope, risk, compensating controls, approver, effective interval, and review. It cannot waive a constitutional invariant through an operating record.

Emergency authority favors risk reduction: halt, isolate, revoke, quarantine, or reduce exposure. Expanding exposure, disclosing sealed evidence, or promoting maturity requires ordinary authority unless a separately adopted emergency policy permits the exact action. Emergency use receives retrospective review without delaying necessary containment.

## 4.7 Authority assurance

The institution tests decision rights through both positive and negative cases. Authorized actors must be able to complete legitimate work; unauthorized actors must be denied. Tests cover expired roles, conflicting duties, stale policy, replayed requests, resource boundaries, and degraded control services.

Audit logs record who or what requested, evaluated, authorized, executed, and observed an action. Logging follows minimization and secret-redaction policy; comprehensive audit does not justify storing credentials or unrestricted private content.

Authority becomes credible when a later reviewer can answer not only who acted, but why the action was permitted, which evidence supported it, which constraints applied, and whether the resulting obligations were fulfilled.

## Source note

This chapter revises the Founder’s Edition, Chapter 5 (pp. 23–25), and incorporates decision-role interfaces from Chapters 15–20 and 32–33. The detailed responsibility and veto matrix will be maintained as a Book II appendix after lifecycle chapters fix every decision object.
