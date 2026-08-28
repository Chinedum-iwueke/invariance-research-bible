# PORT-003 completion evidence

Date: 2026-08-28

- Authoritative producer: `bt.institutional.construction.construction_dossier_receipt`
- Bulletproof source commit: `d4080a94149b3a36642562feda853d9403887a87`
- Bulletproof merge: `866e1c1c0ab23b0bb65fa795030eabf1daedfcb1`
- Native report SHA-256: `5436d3f0c3b24495297a1797f3f61bc0dd80118d3b683f3642aad9ca64cc5314`
- Solver specification digest: `4757287e9232b7ebf2ebc7a3fa7c99927164e848e45bff43cc7726cbed54ebcd`
- Producer receipt: `c196ca8f43a1c67c49284b111df44083ba8e076cdb75097b90844ebc5e414825`
- Bulletproof verification: 1,326 passed; 27 skipped; two pre-existing warnings
- Hermes solver-registry and receipt-consumer merge: `ffbb9bc5e39873672d3f260c6fb8a50f07b018c3`
- Hermes verification: 633 passed with two pre-existing warnings
- VM2 migration: `f5e1c7a93b20`; rebuilt API healthy
- Live solver registry ID: `902a8423-6732-46f3-bd1e-f90b7484a8c3`
- Live receipt record: `63ef6757-137c-4712-9d13-1b4e2b15a4cf`
- Live replay SHA-256: `525f6e0027b5b66c4cece4064d07fb957b9b026821616a4a2d6d3765fba1fe22`
- Allocation, capital, order and promotion authority: false

The deterministic native fixture retained equal-weight and risk-budget benchmarks,
accepted the robust optimizer after feasibility, replay, sensitivity, turnover and
rounding gates, and emitted weights summing exactly to one. Failure and fallback tests
prove the service boundary; the fixture does not prove market alpha or authorize a
production portfolio.
