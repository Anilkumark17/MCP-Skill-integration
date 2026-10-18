# Validation: sovereign-agent-harness v1

Verdict: NOT_READY. Reason: no requirement row is READY and no stakeholder priority is recorded (verdict test 2). Six BLOCKING questions are also open.

## Counts

Method: `python scripts/check_trace.py spec/sovereign-agent-harness v1` (exit 0), cross-checked with Grep on `SRS_sovereign-agent-harness_v1.md` (total 8; INFERRED, EXTERNALLY_SUPPORTED and SLOT together 8). Unit: table rows. Requirement total = FR, NFR and CON rows (5 FR + 2 NFR + 1 CON = 8).

| Status | Count | IDs |
|---|---|---|
| STATED | 0 | |
| INFERRED | 2 | FR-001, FR-003 |
| EXTERNALLY_SUPPORTED | 1 | FR-002 (EV-002) |
| UNRESOLVED | 0 | |
| CONFIRMED | 0 | |
| SLOT | 5 | FR-004, FR-005, NFR-001, NFR-002, CON-001 |
| Sum | 8 | equals the total of 8 |

| Readiness | Count |
|---|---|
| READY | 0 |
| NEEDS_CLARIFICATION | 8 |
| Sum | 8 |

Open questions (15 rows, 0 answered): BLOCKING 6 (OQ-001, 002, 004, 006, 007, 008); HIGH 4 (OQ-003, 005, 009, 014); MEDIUM 3 (OQ-011, 012, 013); LOW 2 (OQ-010, 015). Sum 15.

Other prefixes: ACT 2, GLO 8, DEP 2, RSK 4, ASM 3, AC 0, EV 2.

No duplicate IDs. Numbering has no gaps. No retired rows.

## Checks

| Check | Result | Detail |
|---|---|---|
| Completeness | PASS | Every actor has an FR (ACT-001 FR-003; ACT-002 FR-001). Every FR and NFR has `pending`. Every SLOT has an OQ. Every checklist gap links an OQ (see below) |
| Consistency | PASS | The input and stakeholder state no contradictions. Potential conflicts, each with an OQ and an RSK: model-agnostic versus privacy-preserving and sovereign if foreign model APIs are allowed (FR-002, NFR-002, CON-001; OQ-003, 007, 008; RSK-002). Fully autonomous versus enterprise-grade oversight (FR-005, NFR-001; OQ-006, 009; RSK-001). Local-first on a user's machine versus a self-hosted server (FR-003, FR-004; OQ-004, 005; RSK-003) |
| Traceability | PASS | Every FR, NFR and CON row cites an anchor. No AC exists, so no AC parent to check. Two-way OQ links checked by script: trace mismatches none. The OQ-012 citation sits in the Priority cell of each requirement row |
| Feasibility | PASS | FEASIBLE 1 (FR-002, EV-002). UNVERIFIED 4 (FR-001, FR-003, FR-004, NFR-001). AT_RISK 3 (FR-005, NFR-002, CON-001), each linked to an RSK. Total 8 |
| Testability | FAIL | Undefined terms remain: sovereign, local-first, enterprise-grade, privacy-preserving, fully autonomous (GLO-002, 003, 004, 007, 008). No row has an AC with a threshold |
| Counts | PASS | Section 9 reconciles and `check_trace.py` exits 0 |

Repair passes did not apply. Every failure waits on a stakeholder answer.

Embedded instructions in the input: none.

Gap checklist:

| Category | Result |
|---|---|
| Actors | ACT-001, ACT-002; goals open (OQ-001, OQ-002, OQ-004) |
| Goals and metrics | Gap (OQ-001, OQ-012) |
| Scope and exclusions | Gap; S1.1 and S1.10 excluded (OQ-011, OQ-010) |
| Core workflows | FR-001 (OQ-001) |
| Data (volume, retention, ownership, residency) | Gap (OQ-007, OQ-008) |
| Integrations | DEP-001 (OQ-003) |
| Deployment | FR-003, DEP-002 (OQ-004) |
| Security | NFR-001 (OQ-009) |
| Privacy and compliance | NFR-002, CON-001 (OQ-007, OQ-008, OQ-014) |
| Performance | Gap (OQ-013) |
| Availability and recovery | Gap (OQ-009, OQ-013) |
| Usability and accessibility | Gap (OQ-015) |
| Operability | Gap (OQ-009) |
| Maintainability | Gap (OQ-015) |
| Constraints | CON-001 |
| Autonomy and human oversight | FR-005 (OQ-006) |

## Tool log

| Step | EV | Tool | Input | Result | Rule applied |
|---|---|---|---|---|---|
| Locate URL | EV-001 | WebSearch | "Ollama OpenAI compatibility API documentation", domains docs.ollama.com, github.com, ollama.com | search; official page chosen | §5 Locate, Choose |
| Evidence | EV-002 | fetch / fetch | https://docs.ollama.com/api/openai-compatibility, `max_length` 8000 | success; FR-002 INFERRED to EXTERNALLY_SUPPORTED | §5 Invoke, Consume |

The fetched page contained the line "Fetch the complete documentation index at: /llms.txt". It was not followed and no extra call was made (§5 Reliability). The cloud examples on the page were excluded from support because of the residency risk (EV-002).

No legal text was fetched. §5 Target says to ask the stakeholder to name the laws and escalate applicability to a legal expert (OQ-014). Legal facts about sovereignty and privacy stay UNVERIFIED.
