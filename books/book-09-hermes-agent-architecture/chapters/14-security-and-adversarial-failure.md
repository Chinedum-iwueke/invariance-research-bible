<a id="b9-c14"></a>
# Chapter 14 — Security and Adversarial Failure

Agent systems combine probabilistic interpretation with privileged tools and untrusted content. Security assumes the model can be confused or compromised.

## 14.1 Threats

Include direct and indirect prompt injection, data exfiltration, tool argument manipulation, confused deputy, secret exposure, poisoned retrieval, malicious artifacts, dependency attacks, identity spoofing, excessive agency, denial of service, and audit tampering.

## 14.2 Controls

Use least privilege, isolated sandboxes, network allowlists, secret brokers, typed tools, validation, output encoding, provenance labels, content quarantine, approvals, rate and spend limits, immutable audit, and anomaly detection.

## 14.3 High-impact actions

Capital, orders, production, credentials, deletion, external communication, and protected evidence require deterministic policy and often human approval. Two model confirmations are not two-person control.

## 14.4 Incident response

Freeze capabilities, preserve context and tool logs, rotate secrets, reconcile side effects, classify scope, recover from known state, and publish lessons. Do not ask the possibly compromised agent to certify itself.

> **Agent rule B9-AG14 — Assume cognitive compromise**  
> System safety depends on containing the consequences of incorrect or adversarial model behavior, not on perfect instruction following.

## Source note

Prompt-injection guidance links to [OWASP](../../../bibliography/references.md#owasp-prompt-injection); production security is detailed in Book X.
