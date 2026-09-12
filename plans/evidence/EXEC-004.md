# EXEC-004 completion evidence

Date: 2026-09-12

- Authoritative producer: `bt.institutional.oms.oms_reconciliation_receipt`
- Bulletproof source commit: `b0865ca1d2aa57acac1015d8ba088c34bf0fb2c4`
- Bulletproof merge: `e7100d9345ef419d0deccdee49bc1c6e4896e610` (PR #286)
- OMS specification digest: `4b102ffd35b8ce6d4b4c506d23028def8ef024ff5e721a2b3563fa86475233e2`
- Producer receipt: `4a35c72296052fbb45bce1b3a9dfb70e2a1ae5bcb753f89d19e92fe439fbd72f`
- Journal digest: `7d510e212a4f56bc84ffdb4cf48422a5c555d7414793dad36b5032cfe3f84df7`
- Reconciliation digest: `ef6435f3213e523f816fde2435365122bd0a66030c4582028f80bcbcbdfe749a`
- Native report SHA-256: `2080397bbc60472c08df9f6a62cdf0b93e268620f04a92bb913a9a6d46129d58`
- Bulletproof verification: 18 new tests and 28 combined focused tests passed; full suite 1,379 passed with 28 declared skips; Ruff passed
- Hermes registry and receipt commit: `c2604a76bffa271e44630dedbbcea751aa74767c`
- Hermes merge: `cdd6179291ee5acbf3fc08b69a830061a905c398` (PR #225)
- Hermes verification: 15 focused tests and 734 full backend tests passed with two pre-existing warnings; Ruff passed
- Migration head: `e5a9c3f16d40`
- Duplicate commands suppressed in pilot: 1
- Ambiguous submissions recovered from independent venue evidence: 1
- Adversarial stale-snapshot action: `freeze_and_investigate`
- Allocation, capital, order, promotion, routing and cancellation authority: false
- VM2 migration: `e5a9c3f16d40`; rebuilt API image `sha256:63eb575d2329d84cf53be84182e336baeccf8bda5857e8b659f59c8dd0619bd7` healthy
- Live OMS-schema record: `2f823ef3-92ad-4199-bc33-b18a99cd5a48`
- Live quantitative-receipt record: `9e572f47-6fd6-4706-a7d0-79e5dd2e47d5`
- Cross-repository report digest: `d2346e630f3ac0bcaa665416ee8557f5c96a4d6818e975d8a28eedcf29a412f1`
- Live reconciliation result: qualified with `submission_allowed: true`
- Production activation: complete; exact replay succeeded

The deterministic fixture proves command and event idempotency, partial-fill lifecycle,
cancel-race handling, terminal-state protection, ambiguous-submission recovery from a
fresh independent venue snapshot, material-discrepancy freeze and digest-replayable
Hermes admission. The production replay proves the deployed registry and exact receipt
path for this no-order fixture. It does not certify an exchange adapter, authenticated
venue behavior, demo execution, risk admission or permission to submit an order.
