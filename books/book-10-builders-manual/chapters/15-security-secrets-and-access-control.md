<a id="b10-c15"></a>
# Chapter 15 — Security, Secrets, and Access Control

Security protects evidence integrity, credentials, data, capital, production, and decision authority.

## 15.1 Identity and access

Use human and workload identity, least privilege, short-lived credentials, environment isolation, separation of duties, strong approval, revocation, and periodic review. Authorization is enforced at services and tools.

## 15.2 Secrets

Store secrets in a dedicated manager; inject at runtime; never expose to models, logs, prompts, source, artifacts, or broad environment dumps. Rotate and scope by venue and environment.

## 15.3 Supply chain

Pin dependencies, verify provenance and hashes, scan code and images, generate bills of materials, protect build and release signing, and isolate untrusted execution.

## 15.4 Data security

Classify, encrypt, minimize, retain, delete, and audit. Retrieval and agent context obey access. Backups preserve protection.

## 15.5 Threat response

Model confused-deputy, prompt injection, credential theft, insider misuse, vendor compromise, artifact tampering, and destructive automation. Practice containment and recovery.

> **Builder rule B10-BD15 — Secrets never become context**  
> Cognitive systems receive capability-mediated tools, not raw credentials or unrestricted network authority.

## Source note

Agent security follows Book IX and execution protection Book VIII.
