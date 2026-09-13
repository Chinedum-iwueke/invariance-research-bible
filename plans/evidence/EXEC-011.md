# EXEC-011 evidence

## Claim

Authenticated Bybit demo venue history is canonicalized, exactly replayable and visible
in Mission Control without exposing credentials or granting order authority.

## Production replay

- Receipt: `db0bb60f-60f8-49ad-ac26-3a25ce34894f`
- Receipt digest: `ddbe26ea647ce142eec94fff0f04e8170af7bab75bc9ea9264514619cf30f723`
- Telemetry schema digest: `71c2ead153fc1c50c4579cdce88076c3aeac8e8ad6192a59fbb502ec7b3332c4`
- Replay: `c2107e96-4c87-4ca0-a09e-d1bb244cf338`
- Projection digest: `bf8c4aa08145afc03c1810098503be3bf62f5384c23f264a624cff66871061ac`
- Publication report digest: `e886e6bae0a47c2a69ef487900d1bfeceb63f1a501b0e0e8322dfe7c4190d5e0`

The replay contains 18 canonical events, six orders, four fills and two complete trade
episodes. It reconciles to zero open orders and zero position. The publication asserted
`mission_control_visible: true`, `demo_qualified: true` and
`live_or_capital_authority: false`.

This closes the Bybit demo scope. Binance demo and every live environment require their
own current, environment-bound certification and replay.
