# ADR-0006: Agentic systems apprenticeship and evaluation program

**Status:** Accepted<br>
**Date:** 2026-10-25<br>
**Decision owners:** Founder and Architecture authority

## Context

Invariance Research was built rapidly with substantial assistance from coding models.
The resulting system contains real distributed, scientific, and agentic mechanisms,
but implementation velocity has exceeded the founder's independent ability to explain,
challenge, reproduce, and redesign every mechanism. Continuing to generate complete
solutions would deepen that dependency.

The institution also needs evidence that its use of multiple agents is better than
simpler deterministic or single-agent designs. Agent activity, backtest results, and
software reliability are separate evaluation subjects.

## Constraints

- Learning must use the actual distributed system and its repositories.
- Production authority and live trading remain outside ordinary exercises.
- Architectural claims require source, test, or runtime evidence.
- Material improvements must remain compatible with constitutional authority and
  scientific-evidence rules.
- The program assumes approximately fifteen focused hours per week.
- Operational incidents may require immediate repair; the teaching loop must not make
  a safety response wait for an exercise.

## Alternatives considered

### Continue implementation-first assistance

This preserves delivery speed but leaves architectural knowledge concentrated in
generated code and conversations. It was rejected as the default because it does not
meet the founder's mastery objective.

### Pause the system and study a generic curriculum

This could strengthen fundamentals but loses the motivation, constraints, and
feedback supplied by the real platform. It was rejected as the primary approach,
though selected foundational study remains necessary.

### Use the operating system as a supervised living laboratory

Each substantial change becomes an observe, explain, hypothesize, compare, design,
review, implement, test, measure, and reflect cycle. The founder assumes progressively
greater design and implementation responsibility. This approach was selected.

## Decision

1. Adopt the two-year roadmap in `mastery/learning-roadmap.md`.
2. Use `mastery/living-systems-laboratory.md` for substantial non-incident changes.
3. Require explicit deterministic and single-agent baselines in multi-agent
   architecture experiments when meaningful.
4. Separate platform reliability metrics, scientific-validity metrics, and trading
   execution metrics as defined under `evaluations/`.
5. Preserve the initial reconnaissance and all later evaluation results as dated,
   evidence-bounded documents rather than silently rewriting history.
6. Record progress in the learning journal and require objective mastery checks.
7. Reduce Codex implementation ownership as demonstrated competence increases.

## Assistance ladder

| Level | Founder responsibility | Codex responsibility |
|---|---|---|
| `L0` Observe | Explain the traced path back in plain language | Inspect and teach |
| `L1` Complete | Fill bounded implementation or test gaps | Scaffold and review |
| `L2` Implement | Implement a module from an agreed contract | Review and challenge |
| `L3` Design | Propose alternatives and defend a design | Surface trade-offs and failure modes |
| `L4` Lead | Run and interpret a controlled experiment | Audit method and evidence |
| `L5` Architect | Own the decision, implementation plan, and defense | Provide adversarial peer review |

Movement between levels is based on demonstrated work, not elapsed time.

## Validation plan

- Complete the diagnostic assessment without model-generated answers.
- Produce one independently explained end-to-end task trace.
- Complete every stage's mastery criteria and retain evidence.
- Compare at least one deterministic, single-agent, and multi-agent implementation on
  controlled tasks.
- Conduct a distributed recovery exercise and defend its state model.
- Complete and defend one original orchestration experiment with reproducible results.

## Consequences

Short-term feature throughput may decrease because explanation, founder design, and
experimentation become first-class work. In return, architectural decisions should
become more deliberate, model dependence should decrease, and the institution gains a
repeatable way to test whether autonomy is actually useful.

This ADR does not approve a runtime refactor, modify an agent, or grant trading
authority.
