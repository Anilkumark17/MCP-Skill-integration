# Validation: sovereign-agent-harness v1

Verdict: NOT_READY. 0 of 8 requirements and constraints are READY, no core priority is known, and 6 BLOCKING questions are open.

## Counts

Requirements (FR 5, NFR 3 = 8) plus CON-001:

| Status | Count | IDs |
|---|---|---|
| STATED | 3 | FR-001, 002, 003 |
| INFERRED | 0 | |
| EXTERNALLY_SUPPORTED | 0 | |
| UNRESOLVED | 5 | FR-004, 005; NFR-001, 002, 003 |
| CONFIRMED | 0 | |

CON-001 is UNRESOLVED.

| Readiness | Count |
|---|---|
| READY | 0 |
| NEEDS_CLARIFICATION | 8 |

Open questions by severity: BLOCKING 6 (OQ-001, 002, 004, 006, 007, 008); HIGH 3 (OQ-003, 005, 009); MEDIUM 3 (OQ-011, 012, 013); LOW 1 (OQ-010).

## Checks

| Check | Result | Detail |
|---|---|---|
| Completeness | PASS | Every actor has an FR or a question. Every FR and NFR has `pending`. Gap categories below |
| Consistency | FAIL | Possible conflicts, all UNRESOLVED and linked to questions. Model-agnostic versus privacy-preserving and sovereign if foreign model APIs are allowed (FR-002, NFR-002, CON-001; OQ-003, OQ-007, OQ-008). Fully autonomous versus enterprise-grade oversight (FR-005, NFR-001; OQ-006, OQ-009). Local-first on a user's machine versus a self-hosted server (FR-003, FR-004; OQ-004, OQ-005) |
| Traceability | PASS | Every FR, NFR, CON traces to an anchor, ASM or OQ. No orphan IDs |
| Feasibility | PASS | AT_RISK items linked to RSK: FR-001 (RSK-003), FR-005 (RSK-001). All others UNVERIFIED. No feasibility evidence was retrieved |
| Testability | FAIL | Undefined terms remain: sovereign, local-first, enterprise-grade, privacy-preserving, fully autonomous (GLO-002, 003, 004, 007, 008). No item has a threshold |

Repair passes did not apply. Every failure waits on a stakeholder answer.

Gap checklist:

| Category | Result |
|---|---|
| Actors | ACT-001 to ACT-003, goals open (OQ-001, 002) |
| Goals and metrics | Gap |
| Scope and exclusions | Gap: S1.1 and S2 excluded as non-requirements |
| Core workflows | FR-001, open (OQ-001) |
| Data (volume, retention, ownership, residency) | Gap (OQ-007, OQ-008) |
| Integrations | DEP-001 (OQ-003) |
| Deployment | FR-003, DEP-002 (OQ-004) |
| Security | NFR-001 (OQ-009) |
| Privacy and compliance | NFR-002, CON-001 (OQ-007, OQ-008) |
| Performance | NFR-003 (OQ-013) |
| Availability and recovery | Gap (OQ-009) |
| Usability and accessibility | Gap |
| Operability | Gap (OQ-009) |
| Maintainability | Gap |
| Constraints | CON-001 |
| Autonomy and human oversight | FR-005 (OQ-006) |

## Tool log

| EV | Server and tool | Query | Result |
|---|---|---|---|
| EV-001 | fetch / fetch | MeitY Digital Personal Data Protection Act 2023 PDF | failed: robots.txt returned 403 |

The failure was not retried. The fetch tool refuses pages whose robots.txt blocks it, and I did not try to get around that. No alternate tool was tried. The item is UNVERIFIED and sovereignty is open as OQ-008.
