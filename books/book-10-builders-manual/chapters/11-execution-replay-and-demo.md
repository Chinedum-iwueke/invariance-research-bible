<a id="b10-c11"></a>
# Chapter 11 — Execution Replay and Demo

Replay and demo qualify order logic, adapters, and recovery before real mutation.

## 11.1 Replay stack

Capture immutable public and private events; replay receive-time order; run canonical OMS, risk, and adapters against simulated transport; compare state and outcomes; and publish discrepancy artifacts.

## 11.2 Demo stack

Use isolated demo endpoints and credentials, certified instruments, bounded order types, durable state, streams, reconciliation, and kill controls. Demo data never enters production evidence without environment labels.

## 11.3 Certification

Test submit, amend, cancel, partial and duplicate fill, rejection, rate limits, timeouts, sequence gaps, restart, external activity, stale streams, and reconciliation policy.

## 11.4 Acceptance

No unsupported native mapping, no duplicate mutation on retry, complete event journal, recoverable state, and explicit parity limitations.

> **Builder rule B10-BD11 — Certify lifecycle before strategy**  
> Adapter and OMS qualification proves order-state handling and recovery independently of whether a strategy is profitable.

## Source note

Execution contracts and certification criteria come from Book VIII.
