<a id="b6-app-c"></a>
# Appendix C — Uncertainty Object Schema

An uncertainty object contains prediction identity; model and data identity; target, population, horizon, and units; point estimate or distribution; interval or set; confidence or coverage definition; calibration method and window; assumptions; support diagnostics; generation and expiry times; abstention state and reason; evaluation summary; and known failure modes.

Consumers reject stale, incompatible, unsupported, or semantically ambiguous objects. No field is named merely `confidence` without a controlled subtype.
