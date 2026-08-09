<a id="b9-c03"></a>
# Chapter 3 — Role and Capability Taxonomy

Roles describe institutional purpose; capabilities describe actions a worker can perform. Permissions grant specific capabilities over resources under conditions.

## 3.1 Roles

Roles include researcher, discovery worker, statistician, adversarial reviewer, evidence curator, knowledge organizer, software engineer, data engineer, execution analyst, risk analyst, operator, and governance clerk. One agent may receive several roles for a task only when separation-of-duty policy permits.

## 3.2 Capabilities

Capabilities include read, retrieve, compute, propose, edit workspace artifacts, run tests, submit experiments, request review, publish derived evidence, operate sandbox resources, and perform narrowly approved external actions. Promotion, capital authorization, credential administration, and emergency controls are distinct authorities.

## 3.3 Capability tokens

A grant names subject, action, resource, environment, limits, purpose, task, issuer, effective time, expiry, and revocation. It is checked by the tool or service, not inferred from prompt text.

## 3.4 Conflict

The same worker does not generate a candidate, independently validate it, and approve it. Model diversity does not establish organizational independence when prompts, evidence, owner, or incentives are shared.

> **Agent rule B9-AG03 — Capability is explicit and scoped**  
> No role name or natural-language instruction grants an action unless an enforcing service verifies a valid capability for the exact resource and environment.

## Source note

Decision rights follow Book II; this chapter defines their agent-system projection.
