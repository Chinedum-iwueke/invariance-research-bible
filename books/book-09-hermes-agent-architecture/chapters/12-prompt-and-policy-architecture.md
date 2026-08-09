<a id="b9-c12"></a>
# Chapter 12 — Prompt and Policy Architecture

Prompts specify task behavior; policies constrain actions through enforceable services. Mixing the two creates brittle security and unclear versioning.

## 12.1 Prompt layers

Separate constitutional rules, role instructions, task charter, tool schemas, context, examples, and user content. Version and test material prompt changes. Retrieved text remains quoted or structured data.

## 12.2 Policy layers

Identity, authorization, data access, budgets, network, destructive action, approvals, and environment controls execute outside the model. Refusals and escalation are typed outcomes.

## 12.3 Injection

Prompt injection exploits confusion between instructions and untrusted content. OWASP’s [official guidance](../../../bibliography/references.md#owasp-prompt-injection) recommends architectural defenses including separating trusted instructions, validating outputs, least privilege, and human approval for high-risk actions. No filter makes arbitrary untrusted content safe to grant authority.

## 12.4 Testing

Use benign, adversarial, multilingual, indirect-injection, tool-confusion, and long-context suites. Test action consequences, not only textual refusal.

> **Agent rule B9-AG12 — Policy is not prompt text**  
> Security and authority controls remain effective even if an agent follows a malicious instruction, because tools independently enforce permissions and limits.

## Source note

Security guidance links to the maintained OWASP source. Prompt behavior remains model- and version-dependent.
