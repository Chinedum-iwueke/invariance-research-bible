# DEMO-001 evidence

## Claim

Bybit demo execution is production-certified on the Lagos EXEC2 host. This evidence
does not authorize live trading, capital allocation, scaling or a profitability claim.

## Venue evidence

- All 16 required authenticated and in-session replay drills passed against
  `api-demo.bybit.com`.
- Dynamic instrument discovery bounded the mutation; submit, amend, cancel, typed
  rejection, minimum-size fill and immediate reduce-only flatten were observed.
- Private-stream reconnect, restart reconciliation, duplicate/stale/partial-fill replay,
  incident retention and independent runtime kill passed.
- The closure reconstructed 18 canonical events, six orders, four fills and two trade
  episodes. Terminal open orders and position quantity were both zero.
- Protected raw venue history remains mode `0600`, root-owned on EXEC2. No secret was
  published into Hermes or Mission Control.

## Immutable production evidence

- DEMO-001 receipt: `9c231639-9797-4824-be69-e3e809d22776`
- DEMO-001 receipt digest: `19750e4734a40ddda7d600a0fbc6eb96a5b2c8dc818ab5b718b0e078fba6b17f`
- DEMO-001 schema digest: `01f9a4c176f8fbed5e4a3a422b54f196ae7f74cd8fd87246a6d154970dbd7ffc`
- EXEC-008 receipt: `b6dd6547-6510-4aee-9154-033e468407de`
- RISK-005 fail-closed receipt: `c2938956-9c93-4482-a9f6-a3f108cd4d6a`
- EXEC-009 receipt: `f9d544ae-3ce0-4c3a-89d5-13a5b4758eb0`
- EXEC-011 receipt: `db0bb60f-60f8-49ad-ac26-3a25ce34894f`
- Publication report digest: `e886e6bae0a47c2a69ef487900d1bfeceb63f1a501b0e0e8322dfe7c4190d5e0`
- VM2 migration head: `e8b4c2d60f31`; rebuilt API healthy.

RISK-005 intentionally recorded missing candidate admission as a deterministic deny
with zero effective quantity. That proves the risk service remains available and closed
to exposure when no genuine RISK-004 admission exists.

## Rollback

Expire or revoke certification, freeze submission, cancel and flatten demo state under
separate emergency authority, and preserve all raw history, incidents and receipts.
