# SpecGate + MCP Fetch

SpecGate is a Claude Code skill (`specskill.md`) that turns a rough problem statement into a reviewable requirements specification. Nothing becomes a requirement until it passes the gate. The skill uses an MCP `fetch` server to gather citable evidence instead of relying on recall.

The skill produces a specification only. It never writes code, design, architecture or estimates.

## System overview

```mermaid
flowchart LR
    U([User]) -->|"/specgate + problem statement"| CC[Claude Code]
    CC -->|loads| SK[specskill.md]
    CC <-->|stdio, JSON-RPC| MCP[MCP fetch server<br/>uvx mcp-server-fetch]
    MCP -->|HTTPS GET| WEB[(Standards and docs<br/>on the web)]
    CC -->|writes| OUT[spec/&lt;slug&gt;/]
    CC <-->|questions and answers| U
```

## Workflow

Steps 3 to 9 repeat after each clarification round.

```mermaid
flowchart TD
    A[1. Confirm<br/>check invocation and input,<br/>create spec/slug/] --> B[2. Ingest<br/>read inputs,<br/>number sentences S1, S2...]
    B --> C[3. Extract<br/>STATED items with anchors]
    C --> D[4. Define<br/>vague terms to glossary<br/>as UNRESOLVED]
    D --> E[5. Detect<br/>gap checklist, conflicts,<br/>duplicates, mixed units]
    E --> F[6. Evidence<br/>MCP lookups for INFERRED<br/>and high-risk items]
    F --> G{7. Decide<br/>blocking gap<br/>or conflict?}
    G -->|yes| Q[Ask at most 7 questions<br/>ordered by severity]
    G -->|no| H
    Q --> H[8. Draft<br/>three artifacts and readiness]
    H --> I[9. Validate<br/>five checks,<br/>at most 2 repair passes]
    I --> J[10. Deliver<br/>verdict, counts,<br/>blocking questions, paths]
    J -->|stakeholder answers| C
```

## Status model

Each item carries exactly one status. Only a stakeholder answer can make an item CONFIRMED.

```mermaid
stateDiagram-v2
    [*] --> STATED: in the input, with anchor
    [*] --> INFERRED: derived by the agent
    [*] --> UNRESOLVED: cannot be specified yet
    INFERRED --> EXTERNALLY_SUPPORTED: evidence directly supports it
    STATED --> CONFIRMED: stakeholder answer
    INFERRED --> CONFIRMED: stakeholder answer
    EXTERNALLY_SUPPORTED --> CONFIRMED: stakeholder answer
    UNRESOLVED --> CONFIRMED: stakeholder answer
    CONFIRMED --> [*]
```

Readiness is separate from status:

```mermaid
flowchart LR
    S{Status is<br/>STATED or CONFIRMED?} -->|no| NC[NEEDS_CLARIFICATION]
    S -->|yes| P{Checks pass<br/>for the item?}
    P -->|no| NC
    P -->|yes| B{Blocking question<br/>linked?}
    B -->|yes| NC
    B -->|no| R[READY]
```

## Who establishes what

```mermaid
flowchart TB
    subgraph PS[Problem statement]
        P1[Stated actors, goals,<br/>constraints, wording]
    end
    subgraph EX[External evidence via MCP]
        E1[Feasibility, norms, standards,<br/>library behaviour]
    end
    subgraph SH[Stakeholder]
        S1[Intent, scope, priority,<br/>thresholds, deployment,<br/>risk acceptance]
    end
```

## Tool use (MCP)

```mermaid
flowchart TD
    D[Discover session tools] --> T{Matching tool<br/>available?}
    T -->|no| L[Log: tool unavailable,<br/>continue]
    T -->|yes| S{Question is about feasibility,<br/>standards or comparable behaviour?}
    S -->|no, it is stakeholder intent| X[Do not call a tool]
    S -->|yes| Q[One narrow query]
    Q --> R{Result}
    R -->|error or timeout| RT[Retry once,<br/>try alternate tool]
    RT -->|still failing| UV[Mark UNVERIFIED,<br/>open a question]
    R -->|irrelevant| DS[Discard, log query]
    R -->|conflicting| CF[Keep both,<br/>mark UNRESOLVED, escalate]
    R -->|relevant| EV[Write EV record,<br/>link its ID,<br/>raise status if source supports it]
```

## Validation and verdict

```mermaid
flowchart LR
    V[Five checks<br/>Completeness<br/>Consistency<br/>Traceability<br/>Feasibility<br/>Testability] --> K{Result}
    K --> A[IMPLEMENTATION_READY<br/>all Must items READY,<br/>no blocking question open]
    K --> B[PARTIAL<br/>some READY,<br/>blocking questions remain]
    K --> C[NOT_READY<br/>none READY,<br/>or core priorities unknown]
```

## Output layout

```mermaid
flowchart TD
    R[spec/slug/] --> SRS[SRS_slug_vN.md<br/>requirements, risks,<br/>traceability, change log]
    R --> REG[REGISTER_slug_vN.md<br/>assumptions and open questions]
    R --> VAL[VALIDATION_slug_vN.md<br/>verdict, counts, check results,<br/>tool log]
    R --> EVD[evidence/]
    EVD --> E1[EV-001.md]
    EVD --> E2[EV-002.md ...]
```

Each clarification round writes a new version (`v1`, `v2`, ...). Earlier versions are kept.

## Element IDs

| Prefix | Element |
|---|---|
| ACT | Actor |
| FR | Functional requirement |
| NFR | Non-functional requirement |
| CON | Constraint |
| ASM | Assumption |
| DEP | Dependency |
| RSK | Risk |
| AC | Acceptance criterion |
| OQ | Open question |
| EV | Evidence |
| GLO | Glossary term |

IDs are assigned once and never reused.

## Setup

Register the MCP fetch server in Claude Code:

```
claude mcp add fetch -- uvx mcp-server-fetch
claude mcp list
```

`claude mcp list` should show `fetch` as connected. The first start can time out while `uvx` downloads the package. Run `/mcp` to reconnect.

## Use

```
/specgate <problem statement text or file path>
```

The skill runs only when you invoke it. Answer the questions it asks, and it writes the next version of the three files.

## Specifications produced so far

| Slug | Verdict |
|---|---|
| `web-fetch-mcp` | PARTIAL |
| `multitenant-doc-editor` | NOT_READY |
| `sovereign-agent-harness` | NOT_READY |

## Files

| Path | Purpose |
|---|---|
| `specskill.md` | The SpecGate skill definition |
| `spec/<slug>/` | Output for one problem statement |
