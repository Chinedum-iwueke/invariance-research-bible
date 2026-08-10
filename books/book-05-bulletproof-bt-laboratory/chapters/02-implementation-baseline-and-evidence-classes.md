<a id="b5-c02"></a>
# Chapter 2 — Implementation Baseline and Evidence Classes

Implementation prose becomes unreliable when repository aspiration, documentation, source code, tests, and observed operation are treated as one evidence class. Book V uses a version-pinned baseline and states what each source can establish.

## 2.1 The pin

The public baseline is `Chinedum-iwueke/bulletproof_bt` at commit `ba2a0314817607c5c79d604a0846e008c14379c2`, inspected on 2026-08-08. The package identifies itself as version `0.1.0`, requires Python 3.11 or later, and declares NumPy, pandas, PyArrow, Matplotlib, PyYAML, and websocket-client as direct runtime dependencies. No resolved lock file forms part of this audit, so exact transitive dependency identity is not established by the repository metadata alone.

The inspected snapshot contains 843 Python files, 347 test modules, 23 public JSON schemas, and 117 documentation files. Quantity is orientation, not quality evidence.

## 2.2 Evidence hierarchy

The implementation hierarchy is:

1. observed behavior under a recorded command and environment;
2. passing focused tests that exercise the claimed behavior;
3. executable source and validated schemas;
4. configuration examples and runbooks consistent with code;
5. descriptive documentation; and
6. road maps, prompts, plans, and architectural intent.

Higher evidence can narrow a lower claim. It cannot establish production reliability without production evidence. A unit test can show that a safety branch rejects an input; it cannot show that a venue, network, credential store, supervisor, and human response process behave correctly together.

## 2.3 Controlled claim labels

Every implementation passage uses the following meanings when status could be confused:

- **Current:** directly present in inspected implementation evidence.
- **Partial:** part of the required contract exists, but one or more necessary behaviors or proofs do not.
- **Documented:** documentation makes the claim, but implementation evidence is absent or contradictory.
- **Tested:** an identified passing test exercises the bounded claim.
- **Observed:** a recorded controlled run demonstrates the bounded behavior.
- **Target:** required by the Bible but not currently implemented.
- **Extension:** a planned evolution grounded in a verified current seam.
- **Deferred:** intentionally postponed with its prerequisite or reason stated.
- **Unknown:** available evidence cannot resolve the claim.
- **Blocked:** validation requires unavailable authority, credentials, services, or infrastructure.

Labels compose. A surface may be `current; tested` while its end-to-end institutional contract remains `partial`. The chapter heading and explicit boundary paragraphs control the reading when labels are not repeated before every sentence.

## 2.4 Contradictions are evidence

The root README calls multi-strategy blending, portfolio allocation engines, and web dashboards out of scope. The same snapshot contains `bt.portfolio_engine`, portfolio documentation, portfolio tests, dashboard services, and dashboard orchestration. A planning document describes portfolio work in future tense although many listed artifacts and entry points exist.

The correct conclusion is not that the README is useless or that every new package is complete. It is that scope documentation is stale relative to later slices. Code and tests support a current portfolio backtest aggregation layer and a guarded live-readiness scaffold. They do not establish a same-clock multi-strategy matching engine or complete live portfolio routing.

## 2.5 Negative boundaries

The audit does not have private branches, proprietary data, venue credentials, production telemetry, incident records, or live account evidence. It does not establish profitability, regulatory fitness, capacity, real market impact, operational resilience, or security posture. Tick simulation, order-book reconstruction, queue position, and general impact modeling are not demonstrated as core backtest behavior.

These are not footnotes. They define what downstream decisions may not infer.

> **Laboratory rule B5-LR02 — Claims inherit the weakest necessary evidence link**  
> If a conclusion requires data fidelity, engine correctness, cost realism, and operational equivalence, failure to establish any one limits the conclusion even when the other three are strong.

## 2.6 Maintaining the baseline

Every later audit records repository identity, commit, inspection date, environment, commands, result counts, failures and skips, inspected surfaces, discrepancies, and unavailable evidence. Changes are reviewed by contract surface rather than commit size. A documentation-only change can alter user behavior; a one-line timing change can alter causality.

Book V may be revised only against a new pin or with language that remains invariant across pins. The register remains the authority for pin-specific facts.

## Source note

The repository pin and inspected findings are recorded in the [Implementation Reference Register](../../../registers/IMPLEMENTATION_REFERENCES.md). This chapter applies the provenance and evidence rules of Books I and III to software behavior.
