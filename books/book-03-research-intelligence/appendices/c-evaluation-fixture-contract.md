<a id="b3-app-c"></a>
# Appendix C — Evaluation-Fixture Contract

An evaluation fixture identifies the task and decision context, corpus and system versions, query or input, expected relevant objects or rubric, independent judges, adjudication, uncertainty, protected status, contamination controls, scoring procedure, failure slices, and expiry.

Fixtures are stratified by source form, domain, claim type, consequence, language, access class, and known difficulty. They include positive, negative, contradiction, abstention, invalid-source, and adversarial cases.

Model and index developers cannot access protected labels or exact production-like fixtures outside the evaluation service. Results retain raw outputs and version identity so aggregate improvements cannot hide severe regressions.
