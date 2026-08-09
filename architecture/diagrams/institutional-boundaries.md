# Institutional Authority Boundaries

**Diagram ID:** SERIES-F02  
**Status:** Canonical source

```mermaid
flowchart TB
    A["Accountable human authority"] --> H["Hermes operating system and organization"]
    H --> R["Research organization"]
    H --> E["Engineering organization"]
    H --> K["Knowledge organization"]
    H --> G["Governance organization"]
    H --> P["Production organization"]
    R <--> RI["Research Intelligence<br/>brain, corpus, memory"]
    E <--> RI
    K <--> RI
    G <--> RI
    P <--> RI
    R --> BT["Bulletproof BT<br/>deterministic laboratory"]
    BT --> RI
    P --> DS["Deterministic risk, portfolio,<br/>execution, and state services"]
    DS --> RI
    MR["Replaceable model runtimes"] --> CS["Governed cognitive services"]
    CS <--> RI
    CS --> H
    G -. "authorizes promotion" .-> P
    R -. "cannot self-promote" .-> G
```

Research Intelligence is not the model runtime, Hermes is not the language model, and Bulletproof BT is not the production trading system. Deterministic services remain authoritative for calculation and state transitions; governance authorizes promotion independently of proposal and execution.

