<a id="b5-c14"></a>
# Chapter 14 — APIs and Institutional Interfaces

An institutional API is a versioned contract between authorities, not merely a callable function. It preserves identity, authorization, idempotency, validation, and lineage across process boundaries.

## 14.1 Current public surfaces

The pinned package exposes a Python API and CLI for backtests and analysis. It contains experiment and hypothesis runners, research-data commands, portfolio commands, a strategy robustness service, SaaS service models, execution-runtime CLIs, and contract modules for research specifications, lifecycle, qualification, artifact queries, trade memory, research-copilot exchange, and Pine interchange.

Public JSON schemas formalize several of those objects. Their existence provides a vocabulary and validation surface. End-to-end wiring, authorization, persistence, and service reliability must be established separately for each interface.

## 14.2 Submission

The target experiment-submission request contains actor and authority, hypothesis and experiment identities, requested code pin, dataset and representation identities, configuration or override patch, research tier, resource envelope, evidence policy, and idempotency key. The laboratory responds with accepted canonical specification or typed rejection.

It never accepts an unversioned strategy blob as sufficient scientific intent. Compilation readiness precedes scheduling.

## 14.3 Status and cancellation

Status exposes experiment, trial, and attempt states separately. Cancellation is an attributable transition that stops future work while preserving completed and partial evidence. Repeating a request with the same idempotency key returns the same accepted object rather than creating another trial.

## 14.4 Artifact access

Artifact APIs return manifests and authorized, immutable object references. A summary endpoint never masquerades as the bundle. Consumers can request schema-compatible projections but retain links to primary producer identities and digests.

## 14.5 Analysis from parsed artifacts

The repository includes a seam that analyzes normalized external trade artifacts and builds diagnostic payloads based on detected capabilities. This is useful for comparison and client analysis, but it is not equivalent to a native engine run. Parsed artifacts may lack decisions, rejected orders, configuration, data identity, or causal lineage. The service should label resulting evidence by capability and missing context, as its documentation describes.

## 14.6 Security and authority

The target system authenticates service and human identities, authorizes data and action classes, limits resource scopes, separates secrets from scientific configuration, signs service-to-service claims, and records immutable audit events. A public function signature or schema does not establish these controls.

> **Laboratory rule B5-LR14 — Interfaces preserve authority and provenance**  
> Crossing an API boundary must not erase who authorized the experiment, which version ran, or which primary evidence supports the response.

## Source note

Current statements derive from pinned API, CLI, SaaS, contract, schema, parsed-artifact, portfolio, execution, and research-data surfaces. Deployment and service topology belong to Book X.
