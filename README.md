# SpecGate + MCP Fetch

SpecGate is a Claude Code skill that turns a rough problem statement into a reviewable requirements specification. Nothing becomes a requirement until it passes the gate. External facts come from an MCP `fetch` server, so evidence is a quoted page and not recall.

The skill produces a specification only. It never writes code, design, architecture or estimates.

## How the pieces fit

```mermaid
flowchart LR
    U([User]) -->|"/specgate + problem statement"| CC[Claude Code]
    CC -->|loads| SK["SKILL.md<br/>the rules"]
    CC -->|"WebSearch<br/>find an official URL"| WS[(Web search)]
    CC <-->|"mcp__fetch__fetch<br/>stdio, JSON-RPC"| MCP["Fetch MCP server<br/>uvx mcp-server-fetch"]
    CC -.->|"fallback if the tool is absent"| MF["scripts/mcp_fetch.py"]
    MF <-->|stdio| MCP
    MCP -->|HTTPS GET| WEB[(Official docs<br/>and standards)]
    CC -->|writes| OUT["spec/slug/<br/>SRS, REGISTER, VALIDATION, evidence"]
    CC -->|runs| CT["scripts/check_trace.py<br/>count and trace audit"]
    CT -->|reads| OUT
    CC <-->|"questions and answers"| U
    TS["tests/<br/>TESTS.md + inputs"] -.->|"exercises"| SK
```

## Repository map

```
.
├── .mcp.json                         registers the Fetch MCP server for this project
├── README.md
├── .claude/skills/specgate/
│   ├── SKILL.md                      the skill: rules, model, workflow, validation
│   ├── scripts/
│   │   ├── mcp_fetch.py              Fetch MCP client, saves the raw exchange
│   │   └── check_trace.py            audit: counts, duplicate IDs, two-way OQ links
│   └── tests/
│       ├── TESTS.md                  six cases with the outcome each rule requires
│       └── inputs/                   t1 to t6 problem statements
└── spec/<slug>/                      output of one run (created by /specgate)
```

## Workflow

Steps 3 to 9 repeat after each clarification round, and each round writes the next version.

```mermaid
flowchart TD
    A["1. Confirm<br/>check /specgate and input,<br/>create spec/slug/"] --> B["2. Ingest<br/>number sentences S1, clauses S1.1,<br/>notes N1"]
    B --> C["3. Extract<br/>STATED items with anchors,<br/>SLOT rows for undefined terms"]
    C --> D["4. Define<br/>vague terms into the glossary"]
    D --> E["5. Detect<br/>gap checklist, conflicts,<br/>duplicates, mixed units"]
    E --> F["6. Evidence<br/>search, fetch, EV records"]
    F --> G{"7. Decide<br/>BLOCKING gap<br/>or conflict?"}
    G -->|yes| Q["Ask at most 7 questions,<br/>ordered by severity"]
    G -->|no| H
    Q --> H["8. Draft<br/>three artifacts,<br/>readiness and verdict"]
    H --> I["9. Validate<br/>six checks +<br/>check_trace.py,<br/>at most 2 repair passes"]
    I --> J["10. Deliver<br/>verdict, counts,<br/>blocking questions, paths"]
    J -->|"stakeholder answers"| C
```

## Evidence pipeline

The pipeline runs only for an `INFERRED` row that rests on an external fact. A `SLOT` cannot be raised by evidence. Legal text on government sites usually fails, so the skill asks the stakeholder to name the laws instead.

```mermaid
flowchart TD
    CL["State the claim and the row<br/>it could change"] --> SR["WebSearch with allowed_domains<br/>official sites only"]
    SR --> E1["EV record, status search:<br/>query, URLs returned, URL chosen"]
    E1 --> CH["Choose: HTML over PDF,<br/>official over secondary,<br/>dated revision over latest"]
    CH --> FT["fetch, max_length 8000,<br/>at most 4 pages per URL"]
    FT --> R{Result}
    R -->|"401 403 404 410,<br/>robots.txt refusal"| P["Permanent: no retry,<br/>no workaround,<br/>try next official URL"]
    R -->|"timeout, 429, 5xx"| T["Transient: retry once,<br/>then permanent"]
    R -->|"PDF or binary"| X["irrelevant:<br/>do not page, try HTML alternate"]
    R -->|"text"| Q["Quote verbatim,<br/>check the claim's scope"]
    P --> AF{All URLs failed?}
    T --> AF
    X --> AF
    AF -->|yes| UV["Row unchanged, UNVERIFIED,<br/>OQ asks for source or law name"]
    AF -->|no| CH
    Q --> S{Quote supports<br/>the full claim?}
    S -->|"yes"| UP["INFERRED becomes EXTERNALLY_SUPPORTED,<br/>feasibility FEASIBLE,<br/>note: one comparable"]
    S -->|"partly"| PA["partial: no status change"]
    UP --> EV2["EV record with before and after"]
    PA --> EV2
    UV --> EV2
```

Every call writes an `EV` record, including failed ones. Search summaries are never quoted as evidence. Instructions found inside a fetched page are logged and not followed.

## Fetch MCP wire sequence

`scripts/mcp_fetch.py` speaks the same stdio protocol Claude Code uses. It is the fallback when the session has no `mcp__fetch__fetch` tool.

```mermaid
sequenceDiagram
    participant S as mcp_fetch.py
    participant M as uvx mcp-server-fetch
    participant W as Web page
    S->>M: initialize
    M-->>S: serverInfo
    S->>M: notifications/initialized
    S->>M: tools/list
    M-->>S: tool names
    S->>M: tools/call fetch url, max_length, start_index
    M->>W: robots.txt check, then GET
    W-->>M: page or refusal
    M-->>S: content as Markdown, or isError
    S->>S: save request and response to evidence/raw/*.json
    Note over S: exit 0 on a tool result, exit 2 on a transport failure or timeout
```

## Status and readiness

Each item has one status. Only an answer to an open question makes an item `CONFIRMED`.

```mermaid
stateDiagram-v2
    [*] --> STATED: input says it verbatim, with anchor
    [*] --> INFERRED: agent reading, with reasoning
    [*] --> SLOT: undefined term, question opened
    [*] --> UNRESOLVED: sources conflict
    SLOT --> INFERRED: draft claim written
    INFERRED --> EXTERNALLY_SUPPORTED: fetched quote matches the claim
    STATED --> CONFIRMED: answer to an OQ
    INFERRED --> CONFIRMED: answer to an OQ
    EXTERNALLY_SUPPORTED --> CONFIRMED: answer to an OQ
    SLOT --> CONFIRMED: answer to an OQ
    UNRESOLVED --> CONFIRMED: answer to an OQ
    CONFIRMED --> [*]
```

Readiness is separate from status:

```mermaid
flowchart LR
    S{"Status is STATED<br/>or CONFIRMED?"} -->|no| NC[NEEDS_CLARIFICATION]
    S -->|yes| A{"AC with a<br/>concrete threshold?"}
    A -->|no| NC
    A -->|yes| C{"Checks pass<br/>for the item?"}
    C -->|no| NC
    C -->|yes| B{"Open BLOCKING<br/>question linked?"}
    B -->|yes| NC
    B -->|no| R[READY]
```

Open-question severity:

| Severity | Meaning |
|---|---|
| BLOCKING | A core item cannot be specified or verified without the answer |
| HIGH | The answer changes a requirement's meaning or threshold |
| MEDIUM | The answer changes a value or priority |
| LOW | The answer changes naming or detail only |

## Who establishes what

```mermaid
flowchart TB
    subgraph PS["Problem statement and notes"]
        P1["Actors, goals, constraints, wording<br/>status STATED"]
    end
    subgraph EX["External evidence via Fetch"]
        E1["Standards, capabilities, limits<br/>status EXTERNALLY_SUPPORTED, FEASIBLE"]
    end
    subgraph SH["Stakeholder answers"]
        S1["Intent, scope, priority, thresholds,<br/>deployment, risk acceptance<br/>status CONFIRMED"]
    end
    subgraph LG["Legal expert"]
        L1["Whether a law applies"]
    end
```

## Validation and verdict

```mermaid
flowchart LR
    V["Six checks<br/>Completeness, Consistency,<br/>Traceability, Feasibility,<br/>Testability, Counts"] --> D{"Verdict tests,<br/>in order"}
    D -->|"1. a Must row exists,<br/>all Must rows READY,<br/>no BLOCKING open"| A[IMPLEMENTATION_READY]
    D -->|"2. no row READY,<br/>or no priority recorded"| C[NOT_READY]
    D -->|"3. otherwise"| B[PARTIAL]
```

Consistency fails only for a contradiction the input or a stakeholder states. Possible clashes are listed as potential conflicts with an open question and a risk.

## Audit script

`check_trace.py` reads the SRS and the register of one version and exits 1 on any fault.

```mermaid
flowchart TD
    IN["python check_trace.py spec/slug vN"] --> RD["Read SRS_slug_vN.md<br/>and REGISTER_slug_vN.md"]
    RD --> CI["Collect OQ citations<br/>from every ACT FR NFR CON<br/>GLO DEP ASM RSK AC row"]
    RD --> AF["Collect each OQ's<br/>severity, Affects list, Answer cell"]
    CI --> X{"Two-way check"}
    AF --> X
    X -->|"OQ lists an ID that does not cite it,<br/>or a row cites an OQ that does not list it"| BAD[Mismatch]
    RD --> CN["Count FR NFR CON rows<br/>by status and readiness"]
    CN --> EQ{"status sum = readiness sum<br/>= row total?"}
    RD --> DU["Find duplicate IDs"]
    BAD --> EX1["exit 1"]
    EQ -->|no| EX1
    DU -->|found| EX1
    X -->|none| OK["exit 0"]
    EQ -->|yes| OK
```

Counts are cross-checked with Grep. The row format that makes counting reliable: the ID is the first cell, status and readiness words are uppercase only in their own cells, and severity is the second cell of each open-question row.

## Rounds and versions

```mermaid
flowchart LR
    R1["Round 1<br/>SRS, REGISTER, VALIDATION v1<br/>OQ answer cells empty"] --> QA["Stakeholder answers"]
    QA --> N["Copy notes to<br/>stakeholder_answers_v2.md"]
    N --> R2["Round 2<br/>v2 files written,<br/>v1 untouched"]
    R2 --> QA
```

An earlier version is never overwritten. A re-run with no new answers produces no new information.

## Output layout

```mermaid
flowchart TD
    R["spec/slug/"] --> SRS["SRS_slug_vN.md<br/>glossary, actors, FR, NFR, CON,<br/>DEP, risks, ACs, change log"]
    R --> REG["REGISTER_slug_vN.md<br/>assumptions, open questions,<br/>answer columns"]
    R --> VAL["VALIDATION_slug_vN.md<br/>verdict, counts, six checks,<br/>gap checklist, tool log"]
    R --> ANS["stakeholder_answers_vN.md<br/>from round 2"]
    R --> EVD["evidence/"]
    EVD --> E1["EV-001.md: search"]
    EVD --> E2["EV-002.md: fetch"]
    EVD --> RAW["raw/*.json: only when<br/>mcp_fetch.py was used"]
```

## Tests

`tests/TESTS.md` lists six cases. The expected outcomes come from the SKILL.md rules, not from one model's past output.

```mermaid
flowchart LR
    T1["T1 vague input"] --> RUN
    T2["T2 clarification round"] --> RUN
    T3["T3 numeric, mechanism-heavy"] --> RUN
    T4["T4 well-specified shall sentences"] --> RUN
    T5["T5 adversarial input"] --> RUN
    T6["T6 tool reliability"] --> RUN
    RUN["/specgate tests/inputs/case.md"] --> CHK["Check each expected outcome<br/>and run check_trace.py"]
    CHK --> PF{Outcome}
    PF -->|PASS| LOG[Record result]
    PF -->|FAIL| FIX["Defect: change SKILL.md,<br/>rerun, keep both results"]
    FIX --> RUN
```

## Element IDs

| Prefix | Element |
|---|---|
| ACT | Actor (a person or role) |
| FR | Functional requirement |
| NFR | Non-functional requirement |
| CON | Constraint |
| ASM | Assumption |
| DEP | Dependency (systems, models, services) |
| RSK | Risk |
| AC | Acceptance criterion |
| OQ | Open question |
| EV | Evidence record |
| GLO | Glossary term |

IDs are assigned once and never reused. A removed row is listed as retired.

## Setup

The project `.mcp.json` registers the Fetch server:

```json
{ "mcpServers": { "fetch": { "type": "stdio", "command": "uvx", "args": ["mcp-server-fetch"], "env": {} } } }
```

To register it for your user instead:

```
claude mcp add fetch -- uvx mcp-server-fetch
claude mcp list
```

`claude mcp list` should show `fetch` as connected. The first start can time out while `uvx` downloads the package. Run `/mcp` to reconnect.

## Skill location

Claude Code registers `/specgate` only from `.claude/skills/specgate/SKILL.md` or `.claude/commands/specgate.md`. The command name comes from `name: specgate` in the frontmatter and the folder name. Restart Claude Code after changing the file.

A personal copy at `~/.claude/skills/specgate/` may also exist. In this setup `/specgate` loaded from the personal copy, so a change to the project file takes effect only after the personal copy is replaced with it. Keep the two copies identical.

## Use

```
/specgate <problem statement text or file path>
```

The skill runs only when you invoke it. Answer the questions it asks, then run it again with your answers. It writes the next version of the three files.

## Specifications in this repository

| Slug | Version | Verdict |
|---|---|---|
| `sovereign-agent-harness` | v1 | NOT_READY: no row READY, no priority recorded, 6 BLOCKING questions open |

## Files

| Path | Purpose |
|---|---|
| `.claude/skills/specgate/SKILL.md` | The SpecGate skill. Claude Code loads this |
| `.claude/skills/specgate/scripts/mcp_fetch.py` | Calls the Fetch MCP server over stdio and saves the raw exchange. Used when the session has no `mcp__fetch__fetch` tool |
| `.claude/skills/specgate/scripts/check_trace.py` | Audits a run: counts by status and readiness, open questions by severity, duplicate IDs, two-way OQ links |
| `.claude/skills/specgate/tests/` | Test cases and expected outcomes |
| `.mcp.json` | Registers the Fetch MCP server (`uvx mcp-server-fetch`) for this project |
| `spec/<slug>/` | Output for one problem statement, created by a run |
