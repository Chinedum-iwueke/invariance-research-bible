<a id="series-f03"></a>
# Current, Target, and Migration Architecture

**Diagram ID:** SERIES-F03
**Status:** Controlled implementation map as of 2026-08-10

## Current verified/partial state

```mermaid
flowchart LR
    U[Founder via Mission Control/Telegram] --> H[Hermes control plane]
    H --> W[Restricted workers]
    W --> BT[Bulletproof engines and artifacts]
    H --> RR[Research registry]
    H --> KD[Documents, chunks, lexical retrieval]
    BT -. bounded memory export .-> KD
    BT --> DL[Ignored local data lake and manifests]
    RR --> PG[(PostgreSQL)]
    KD --> PG
```

The current system has real governed task and registry slices. Research Intelligence is partial: canonical research lineage and document retrieval exist, but comprehensive scientific objects, hybrid retrieval, citation replay, beliefs, corpus defenses, and recovery proof do not. Bulletproof has substantial tested components, but universal data/run identity and full regression closure do not.

## Target state

```mermaid
flowchart LR
    A[Accountable authorities] --> H[Hermes governance and orchestration]
    H --> D[Bounded replaceable agents]
    D --> T[Typed deterministic tools]
    T --> BT[Bulletproof laboratory]
    T --> PR[Portfolio, risk, execution services]
    BT --> CE[Canonical evidence store]
    PR --> CE
    H --> CE
    CE --> LX[Lexical projection]
    CE --> VX[Vector projection]
    CE --> GX[Graph projection]
    LX --> Q[Hybrid retrieval and citation replay]
    VX --> Q
    GX --> Q
    Q --> H
    H -. separate approval .-> PR
```

Canonical evidence owns truth; indexes and graphs are rebuildable. Research success does not imply portfolio admission, allocation, execution, or production promotion.

## Migration sequence

```mermaid
flowchart LR
    B[Baseline and compatibility] --> R[RI foundation]
    B --> O[Agent reliability]
    R --> L[Laboratory contract closure]
    O --> L
    L --> S[No-capital walking skeleton]
    S --> D[Discovery and surveillance]
    D --> P[Prospective shadow and replay]
    P --> M[ML and portfolio candidates]
    M --> C[Separately approved capital canaries]
    C --> X[Resilient production and evolution]
```

Migration is additive and compatibility-preserving. Each transition requires the evidence gate in the [System Acceptance Matrix](../../registers/SYSTEM_ACCEPTANCE_EVIDENCE.md) and may be rolled back without deleting canonical history.
