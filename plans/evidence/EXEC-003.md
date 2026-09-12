# EXEC-003 completion evidence

Date: 2026-09-11

- Authoritative producer: `bt.institutional.venue.venue_identity_receipt`
- Bulletproof source commit: `ef842db13d2775c2edbf8c372224d4ad9a964814`
- Bulletproof merge: `6ea7656aa744d4a9356d71854b9727535dec1230` (PR #285)
- Native report SHA-256: `c8d5ab670c7f465a09f86ac8af61d9092086d3ad46713a84d7590302bc4dc438`
- Mapping-schema digest: `ae6a8354ad95b94daf036e8f9276ca11727d0989de201e605e98fe2faa14b74c`
- Mapping result digest: `605c8ae33b065ff32861ac2c801743a5d7353c7c81a9bab1d1b8161f8d9872dc`
- Producer receipt: `082e20bd3f77516d3b2370d601b00ed6f648095313b2897b278f29edbe2008d7`
- Bulletproof verification: 1,366 passed; 28 declared skips; two unrelated deprecation warnings; Ruff passed
- Hermes registry and receipt commit: `1d01d461208d7cbbfcc3b9d31102a42f2114f965`
- Hermes merge: `6477a0bc2b162d8142b6108ae804ecf1bf1ed012` (PR #224)
- Hermes verification: 730 passed with two pre-existing warnings; Ruff passed
- Migration head: `e4f8b2d05c30`
- Allocation, capital, order, promotion and routing authority: false
- VM2 migration: `e4f8b2d05c30`; rebuilt API image `sha256:efe6afd82de57d1519dc5ad78564b089e6c372aedb372c82c02054633700f2ad` healthy
- Live venue-identity record: `e498a6cc-58c4-4814-8839-b957c6fcb2e7`
- Live quantitative-receipt record: `f9322c93-08f4-4aa9-abc6-348e07b21039`
- Cross-repository report digest: `419af24787bdec980d8431d1094a9cf6be97d28486940065d0ebb90179a793e1`
- Production activation: complete; exact replay succeeded with exit code `0`

The deterministic fixture proves explicit point-in-time mapping, contract conversion,
venue-specific constraints, outage handling, quarantine behavior, dependency binding
and a digest-replayable Hermes admission path. It does not certify live venue identity
feeds, authenticated adapters, demo behavior, routing quality or an order path.
