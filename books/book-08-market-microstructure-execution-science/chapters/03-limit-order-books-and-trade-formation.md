<a id="b8-c03"></a>
# Chapter 3 — Limit Order Books and Trade Formation

A limit order book is a venue-specific state of displayed buying and selling interest. Quotes, trades, cancellations, hidden liquidity, priority, and matching rules jointly determine execution.

## 3.1 Book state

At each price, visible quantity is conditional on feed depth and venue disclosure. Best bid and ask define quoted spread; midpoint and microprice are derived references. Displayed depth can vanish before an order arrives.

## 3.2 Formation and information

Classic microstructure models formalize different channels. [Glosten and Milgrom 1985](../../../bibliography/references.md#glosten-milgrom-1985) derives an information-related spread in a stylized dealer market with heterogeneous information. [Kyle 1985](../../../bibliography/references.md#kyle-1985) studies price impact and depth in a sequential-auction equilibrium. These models illuminate mechanisms under assumptions; they are not literal venue simulators.

## 3.3 Book events

New limit orders, cancellations, and marketable orders all change supply and demand. [Cont, Kukanov, and Stoikov 2014](../../../bibliography/references.md#cont-kukanov-stoikov-2014) reports an empirical relationship between short-horizon price changes and order-flow imbalance for its NYSE sample. Transport to crypto or other venues requires new evidence.

## 3.4 Reconstruction limits

Market-by-price feeds do not reveal individual queue identities. Hidden, iceberg, internalized, and off-book activity limit inference. A reconstructed book is a representation with coverage and gap diagnostics.

> **Execution rule B8-EX03 — Displayed liquidity is conditional supply**  
> Book quantity is evidence about visible interest under one venue and instant, not guaranteed executable capacity.

## Source note

Technical claims link to primary theoretical and empirical sources in the controlled bibliography.
