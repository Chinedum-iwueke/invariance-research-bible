<a id="b9-c11"></a>
# Chapter 11 — Communication, Task Graphs, and Deliberation

Multi-agent work is coordinated through explicit task graphs rather than free-form organizational theater.

## 11.1 Task graph

Nodes contain objective, inputs, outputs, owner, capabilities, dependencies, budget, deadline, state, and acceptance. Edges express data or completion dependencies. Cycles require explicit iteration limits.

## 11.2 Messages

Messages carry task and sender identity, schema, evidence references, requested action, urgency, and expiry. A message does not confer permission. Final artifacts outrank conversational assertions.

## 11.3 Deliberation

Parallel proposals can increase coverage; critics can expose failure; synthesis can reconcile. Shared evidence and prompts create correlated error. The system preserves minority reports and does not equate majority vote with truth.

## 11.4 Termination

Stop on acceptance, invalidity, budget, no-progress threshold, safety, or required user decision. Orchestrators detect duplicate work and abandoned branches.

> **Agent rule B9-AG11 — Coordination preserves accountability**  
> Every delegated task has one accountable owner, bounded resources, typed output, and terminal disposition even when many agents contribute.

## Source note

This chapter implements Book II workflow and Book IV session closeout for agent systems.
