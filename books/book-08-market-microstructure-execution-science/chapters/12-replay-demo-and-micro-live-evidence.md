<a id="b8-c12"></a>
# Chapter 12 — Replay, Demo, and Micro-live Evidence

Execution evidence advances through environments without conflating their meanings.

## 12.1 Replay

Replay feeds captured market and venue events through frozen policy and adapters. It tests determinism, mapping, lifecycle, and alternative tactics within captured support. It cannot reproduce unobserved queue or the market response to counterfactual orders exactly.

## 12.2 Demo

Demo tests connectivity, authentication, mappings, rate limits, lifecycle, state, and recovery against a non-production venue environment. Matching quality, liquidity, and operational behavior may differ from production.

## 12.3 Micro-live

Micro-live uses tightly bounded real orders under independent authorization. Limits cover venue, symbol, quantity, notional, loss, time, order count, participation, and kill. It tests real interaction while minimizing consequence; it does not establish scale capacity.

## 12.4 Parity dossier

Compare canonical intent, native payload, acknowledgement, fill, cancel, position, fees, latency, and reconciliation across environments. Every mismatch has disposition and owner.

> **Execution rule B8-EX12 — Environment evidence is non-substitutable**  
> Replay, demo, micro-live, and production results retain separate status, limitations, and authorization conditions.

## Source note

This chapter aligns with Book II environment states and Book V replay extensions.
