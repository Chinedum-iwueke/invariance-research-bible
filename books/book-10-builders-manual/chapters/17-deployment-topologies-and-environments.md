<a id="b10-c17"></a>
# Chapter 17 — Deployment Topologies and Environments

Topology follows trust, latency, data gravity, scaling, and recovery needs. Environments represent evidence and authority states, not just configuration names.

## 17.1 Topology

Separate control plane from workers; transactional services from analytical jobs; research compute from production execution; public data from private account streams; and secrets from cognitive runtimes. Use queues and object references for large asynchronous work.

## 17.2 Environments

Local, test, backtest, replay, shadow, demo, micro-live, and production have distinct identities, credentials, networks, data, policies, and stores. Promotion copies versioned artifacts, not mutable working directories.

## 17.3 Isolation

Research failure cannot reach production mutation. Live adapters cannot start with demo or test policy. Cross-environment data movement is explicit and audited.

## 17.4 Scale and resilience

Workers are disposable; canonical state is durable; leases and idempotency support retry; capacity limits protect dependencies; regions and vendors have explicit failure policy.

> **Builder rule B10-BD17 — Environments are security boundaries**  
> Credentials, network paths, authority, data, and mutation capability enforce environment separation independently of application intent.

## Source note

Environment semantics originate in Book II and execution requirements in Book VIII.
