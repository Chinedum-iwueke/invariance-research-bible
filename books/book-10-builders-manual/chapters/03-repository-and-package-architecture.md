<a id="b10-c03"></a>
# Chapter 3 — Repository and Package Architecture

Repository structure should make ownership, contracts, and deployment units visible without forcing one repository per concept or one monolith for convenience.

## 3.1 Layers

Use domain contracts, deterministic domain services, application workflows, adapters, storage, interfaces, and deployment configuration. Dependency direction points inward toward stable contracts. Vendor SDKs remain at adapter edges.

## 3.2 Suggested domains

Domains include identity and governance, research contracts and trials, evidence and knowledge, data and representations, backtesting, ML, portfolio risk, execution, agent orchestration, and platform operations. Shared libraries contain genuinely stable primitives, not miscellaneous utilities.

## 3.3 Repository policy

Every package has owner, public API, version policy, tests, docs, examples, changelog, and deprecation path. Generated artifacts are not edited by hand. Secrets and mutable runtime data stay outside source control.

## 3.4 Monorepo and services

A monorepo can simplify atomic contract changes; separate services can isolate scaling and authority. Choose by deployment and trust boundary. Network separation is not domain design by itself.

> **Builder rule B10-BD03 — Package boundaries follow stable contracts**  
> Code is grouped around owned semantics and change coupling, while adapters and deployment remain replaceable.

## Source note

Concept ownership is controlled by [CONCEPT_OWNERSHIP.md](../../../registers/CONCEPT_OWNERSHIP.md).
