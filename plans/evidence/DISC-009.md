# DISC-009 Completion Evidence

Date: 2026-08-27

## Delivered

- immutable discovery portfolios with digest-chained events;
- canonical verification for curricula, opportunity maps, mechanism evaluations,
  selection-bias audits and completed autonomous sessions;
- server-derived uncertainty and deterministic novelty scoring;
- expected-information-gain-per-attention ranking;
- domain diversity floors plus total, selection, domain and cluster caps;
- retained selected and excluded candidates with explicit counterfactual reasons;
- typed `ResearchProgram.project` lineage and compatibility boundary;
- exact allocation replay without task, execution, promotion, order or capital authority.

## Source and deployment

- Control-plane merge sequence: `22d82980dbfacaa88dc3933d4da11e0106406c11`,
  `0e2a80a01294231b148104aedaf57133257c15b7`,
  `4fb66107e77d7162769562b82aaa3b447424b664`,
  `7b38b8a6d5164cebfe7e5e3b5b6cc97bf354712e`, and
  `6dc3c6cad0a61d0d138fe5df11e10adc05bf10ad`.
- VM2 migration head includes `c2e6f9a31b50` and `d3f7a2b41c60`.
- The rebuilt VM2 API was healthy before the production replay.
- Full backend suite: 542 passed, with two pre-existing warnings.
- All GitHub CI suites passed for PRs #177 through #181.

## Live replay

- Portfolio ID: `18fe8f06-ff9a-45f5-8d1c-6d8a5b41419e`
- Portfolio key/version: `DISC009-LIVE-PORTFOLIO` / `1.0.0`
- Candidate count: 3
- Selected count: 2
- Attention used: 2
- Selected domains: `autonomous-research`, `causal-reasoning`
- Counterfactual source: `map-358f8ec0`
- Counterfactual reason: `attention_budget`
- Policy digest: `dc4d3615baac45aa0ae100edb7212cb993b77178d01ec5cca1ecb70b29113af3`
- Allocation digest: `a86537d6ea9c4dede83f5054789298b9c41fa7002d4e758fb8209f337b42a309`
- Event-chain head: `cc02b42e3c192aca52dee52a1b346daf116129c8559cb752456005874d3deca9`
- Exact replay: true
- Pilot report digest: `fc017b527cf0740e8c6763074894cd25d59f0cd85799b598decc0d716363646d`
- Retained report SHA-256: `6cc512fb877f205b744f13a564935739498e49cab7880ddb14e742c161c4d4de`
- Retained report path on VM2: `/home/omenka/disc009-evidence/report.json`

## Retained negative evidence

The first live attempt exposed that project identity had been inferred from an incompatible
legacy `mandate` shape. The request failed with HTTP 500. The repair added the typed
`ResearchProgram.project` field and a migration instead of adding another heuristic.

The next attempt rejected a DISC-007 selection audit with HTTP 409 because its upstream
mechanism evaluation had been superseded. The source-currentness gate remained strict;
the pilot was corrected to use the active mechanism evaluation. Neither failure was
discarded or bypassed.

## Rollback and authority boundary

Rollback stops creation of new portfolios. Existing portfolios, rankings, events, source
lineage and excluded alternatives remain readable and replayable. A portfolio allocates
research attention only. It cannot create or execute tasks, approve work, promote a result,
submit an order or authorize capital.
