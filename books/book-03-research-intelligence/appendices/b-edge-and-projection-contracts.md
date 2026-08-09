<a id="b3-app-b"></a>
# Appendix B — Edge and Projection Contracts

Every canonical relationship identifies subject, predicate, object, scope, provenance, edge type, producer, review state, effective interval, access policy, and supersession.

Controlled edge types distinguish direct observation, deterministic derivation, statistical estimate, reviewed inference, and agent-proposed inference. Interfaces must expose this type and may not render all edges as equivalent facts.

Every projection declares:

- projection identity and version;
- source-core cutoff or event cursor;
- included object and relationship types;
- derivation rules and model versions;
- access-policy propagation;
- rebuild and invalidation behavior;
- evaluation benchmark and known limitations.

Projection deletion or rebuild does not delete canonical evidence. A source access change, invalidation, or lawful deletion propagates to all derived views.
