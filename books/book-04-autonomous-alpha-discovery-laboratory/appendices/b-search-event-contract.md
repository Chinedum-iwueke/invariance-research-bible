<a id="b4-app-b"></a>
# Appendix B — Search-Event Contract

Every material search event records event and session identities, causal parent, event type, actor or service, timestamp, space and policy versions, proposed configuration, execution or view identity, evidence available before the event, decision or selection, resource use, protected-evidence effect, output artifacts, and terminal status.

Controlled event types include propose, reject-before-run, schedule, start, complete, fail, retry, view-result, rank, select, prune, stop, amend-space, expose-protected-evidence, and close. Implementations may extend the vocabulary without collapsing distinct events.
