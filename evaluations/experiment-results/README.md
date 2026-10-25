# Experiment Result Records

Create one immutable Markdown record and one machine-readable manifest per completed
experiment. Do not overwrite a result after discovering an error; publish a successor
that identifies and supersedes the original.

## Record template

```markdown
# <Experiment ID>: <Title>

**Status:** completed / invalid / failed / retracted
**Protocol digest:**
**Environment manifest digest:**
**Dataset digest:**
**Started / ended:**
**Producers and reviewers:**

## Preregistered question and hypothesis
## Architecture arms and controls
## Data and provenance
## Metrics and failure criteria
## Deviations
## Results with uncertainty
## Failures and anomalies
## Reproducibility status
## Interpretation
## Decision: retain / simplify / revise / reject
## Limitations and next falsification
## Artifact inventory
```

## Publication rules

- Include negative, invalid, timed-out, and failed runs.
- Report all preregistered primary outcomes.
- Separate raw observations from interpretations.
- Identify model-assisted adjudication.
- Link every aggregate to raw attempt identifiers.
- Do not use trading return as evidence of orchestration quality.
