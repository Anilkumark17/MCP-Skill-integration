# SpecGate + MCP Fetch

SpecGate is a Claude Code skill (`.claude/skills/specgate/SKILL.md`) that turns a rough problem statement into a reviewable requirements specification. Nothing becomes a requirement until it passes the gate. The skill uses an MCP `fetch` server to gather citable evidence instead of relying on recall.

The skill produces a specification only. It never writes code, design, architecture or estimates.

## System overview

```mermaid
flowchart LR
    U([User]) -->|"/specgate + problem statement"| CC[Claude Code]
    CC -->|loads| SK[.claude/skills/specgate/SKILL.md]
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
    H --> I[9. Validate<br/>six checks and check_trace.py,<br/>at most 2 repair passes]
    I --> J[10. Deliver<br/>verdict, counts,<br/>blocking questions, paths]
    J -->|stakeholder answers| C
```

## Status model

Each item carries exactly one status. Only a stakeholder answer can make an item CONFIRMED.

```mermaid
stateDiagram-v2
    [*] --> STATED: in the input, verbatim, with anchor
    [*] --> INFERRED: derived by the agent, with reasoning
    [*] --> SLOT: undefined term, question opened
    [*] --> UNRESOLVED: sources conflict
    SLOT --> INFERRED: draft claim written
    INFERRED --> EXTERNALLY_SUPPORTED: fetched quote matches claim scope
    STATED --> CONFIRMED: stakeholder answer
    INFERRED --> CONFIRMED: stakeholder answer
    EXTERNALLY_SUPPORTED --> CONFIRMED: stakeholder answer
    UNRESOLVED --> CONFIRMED: stakeholder decision
    CONFIRMED --> [*]
```

Readiness is separate from status:

```mermaid
flowchart LR
    S{Status is<br/>STATED or CONFIRMED?} -->|no| NC[NEEDS_CLARIFICATION]
    S -->|yes| P{Checks pass<br/>for the item?}
    P -->|no| NC
    P -->|yes| A{AC with<br/>threshold?}
    A -->|no| NC
    A -->|yes| B{Blocking question<br/>linked?}
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
    V[Six checks<br/>Completeness<br/>Consistency<br/>Traceability<br/>Feasibility<br/>Testability<br/>Counts] --> K{Result}
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

## Skill location

Claude Code registers `/specgate` only from one of these paths:

* `.claude/skills/specgate/SKILL.md` (used here)
* `.claude/commands/specgate.md`

A file named `specskill.md` in the project root does not create the command. The command name comes from the `name: specgate` line in the skill's frontmatter and the folder name. Restart Claude Code after adding the file so it picks up the skill.

## Use

```
/specgate <problem statement text or file path>
```

The skill runs only when you invoke it. Answer the questions it asks, and it writes the next version of the three files.

## Tests

The test suite lives with the skill in `.claude/skills/specgate/tests/`. `TESTS.md` lists six cases (vague input, clarification round, numeric input, well-specified input, adversarial input, tool reliability) with the outcome each SpecGate rule requires. Run each case with `/specgate`, then audit the output:

```
python .claude/skills/specgate/scripts/check_trace.py spec/<slug> vN
```

## Files

| Path | Purpose |
|---|---|
| `.claude/skills/specgate/SKILL.md` | The SpecGate skill. This is the file Claude Code loads |
| `.claude/skills/specgate/scripts/mcp_fetch.py` | Calls the Fetch MCP server over stdio and saves the raw exchange. Used when the session has no `mcp__fetch__fetch` tool |
| `.claude/skills/specgate/scripts/check_trace.py` | Audits a run: counts by status and readiness, OQs by severity, duplicate IDs, two-way OQ links |
| `.claude/skills/specgate/tests/` | Test cases and expected outcomes |
| `.mcp.json` | Registers the Fetch MCP server (`uvx mcp-server-fetch`) for this project |
| `spec/<slug>/` | Output for one problem statement (created by a run) |
