# Validation: web-fetch-mcp v1

Verdict: PARTIAL. 5 of 20 requirements are READY. 3 BLOCKING questions are open. All priorities are UNPRIORITIZED (OQ-010).

## Counts

Requirements (FR 17, NFR 3 = 20):

| Status | Count | IDs |
|---|---|---|
| STATED | 10 | FR-001, 002, 003, 005, 006, 007, 008, 011, 012; NFR-001 |
| INFERRED | 2 | FR-014, FR-016 |
| EXTERNALLY_SUPPORTED | 4 | FR-009, 010, 013, 017 |
| UNRESOLVED | 4 | FR-004, FR-015; NFR-002, NFR-003 |
| CONFIRMED | 0 | |

| Readiness | Count | IDs |
|---|---|---|
| READY | 5 | FR-001, 005, 008, 011; NFR-001 |
| NEEDS_CLARIFICATION | 15 | all others |

Open questions by severity: BLOCKING 3 (OQ-001, 002, 003); HIGH 2 (OQ-004, 006); MEDIUM 4 (OQ-005, 007, 009, 010); LOW 3 (OQ-008, 011, 012).

## Checks

| Check | Result | Detail |
|---|---|---|
| Completeness | PASS | Every actor has an FR. Every FR and NFR has an AC or `pending`. Gap categories below |
| Consistency | PASS | No contradictions or mixed units. "Fetch" versus `fetch` recorded as ASM-001 |
| Traceability | PASS | Every FR, NFR, CON traces to an anchor, ASM or EV. Every AC has one parent. No orphan IDs |
| Feasibility | PASS | AT_RISK items linked to RSK: FR-002, 015 (RSK-002); FR-003, 004, 014 (RSK-001); FR-012 (RSK-003). UNVERIFIED: FR-006, 013, 017 |
| Testability | FAIL | Undefined terms or missing thresholds: FR-002 (GLO-006), FR-004 (GLO-003), FR-006 (timeout), FR-007 (GLO-004), FR-010, FR-012, FR-013, FR-015, FR-017, NFR-002, NFR-003. All wait on stakeholder answers, so repair passes did not apply |

Gap checklist:

| Category | Result |
|---|---|
| Actors, goals | Items ACT-001, ACT-002. Success metrics: gap (OQ-010) |
| Scope and exclusions | CON-002, CON-003 |
| Core workflows | FR-001, FR-002 |
| Data (volume, retention, ownership, residency) | Gap: ASM-005, OQ-012 |
| Integrations | DEP-001, FR-012 |
| Deployment | CON-001, FR-008 (local only) |
| Security | FR-003, FR-004, FR-014, FR-016, RSK-001, RSK-002 |
| Privacy and compliance | Gap: OQ-012 |
| Performance | NFR-002 (UNRESOLVED) |
| Availability and recovery | NFR-003 (UNRESOLVED), NFR-001 |
| Usability and accessibility | Gap: not applicable to a stdio tool, not confirmed |
| Operability | FR-009, FR-010 |
| Maintainability | Gap: no input |
| Constraints | CON-001 to CON-004 |
| Autonomy and human oversight | Gap: ASM-006, OQ-012 |

## Tool log

All calls used server `fetch`, tool `fetch`, on 2026-10-18. Details in `evidence/`.

| EV | URL | Result |
|---|---|---|
| EV-001 | https://modelcontextprotocol.io/specification/ | retrieved |
| EV-002 | https://modelcontextprotocol.io/specification/latest/server/tools | retrieved in 2 calls (first truncated at 14000 characters) |
| EV-003 | https://modelcontextprotocol.io/specification/latest/basic/transports/stdio | retrieved |
| EV-004 | https://modelcontextprotocol.io/specification/latest/basic/transports | retrieved |

Not retrieved: lifecycle, versioning, cancellation and authorization pages. Authorization is out of scope (S7). Claims that need those pages are marked UNVERIFIED.
