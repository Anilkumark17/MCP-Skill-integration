# Validation: sovereign-agent-harness v3

Verdict: PARTIAL. Reason: six requirement rows are READY and priorities are recorded, so test 2 does not apply. Test 1 fails because the BLOCKING question OQ-019 is open, although both Must rows (FR-001, FR-003) are READY. The respondent is a simulated stakeholder.

## Counts

Method: `python scripts/check_trace.py spec/sovereign-agent-harness v3` (exit 0), cross-checked with Grep on `SRS_sovereign-agent-harness_v3.md` (total 15; CONFIRMED 12; the other statuses together 3; READY 6) and on `REGISTER_sovereign-agent-harness_v3.md` (20 OQ rows). Unit: table rows. Requirement total = FR, NFR and CON rows (10 FR + 3 NFR + 2 CON = 15).

| Status | Count | IDs |
|---|---|---|
| STATED | 0 | |
| INFERRED | 1 | CON-002 |
| EXTERNALLY_SUPPORTED | 1 | FR-002 (EV-002) |
| UNRESOLVED | 0 | |
| CONFIRMED | 12 | FR-001, FR-003, FR-004, FR-005, FR-006, FR-007, FR-008, FR-009, FR-010, NFR-002, NFR-003, CON-001 |
| SLOT | 1 | NFR-001 |
| Sum | 15 | equals the total of 15 |

| Readiness | Count | IDs |
|---|---|---|
| READY | 6 | FR-001, FR-003, FR-005, FR-007, FR-008, NFR-002 |
| NEEDS_CLARIFICATION | 9 | FR-002, FR-004, FR-006, FR-009, FR-010, NFR-001, NFR-003, CON-001, CON-002 |
| Sum | 15 | |

Priority: Must 2 (FR-001, FR-003, both READY), Should 13.

Open questions (20 rows): 16 answered, 4 open. By severity, all rows: BLOCKING 7, HIGH 5, MEDIUM 6, LOW 2. Open only: BLOCKING 1 (OQ-019), MEDIUM 3 (OQ-013, 016, 017).

Other prefixes: ACT 2, GLO 10, DEP 3, RSK 6, ASM 5, AC 6, EV 6.

Change since v2: READY 2 to 6, CONFIRMED 11 to 12 (NFR-003 added), SLOT 1 unchanged, open OQs 6 to 4, AC 2 to 6. v1 and v2 files are unchanged (`check_trace.py` on both still exits 0).

No duplicate IDs. Numbering has no gaps. No retired rows.

## Checks

| Check | Result | Detail |
|---|---|---|
| Completeness | PASS | Every actor has an FR (ACT-001 FR-003; ACT-002 FR-001). Every FR and NFR has an AC or `pending`. The one SLOT row (NFR-001) has an OQ. Every checklist gap links an OQ (see below) |
| Consistency | PASS | The input and stakeholder state no contradictions. Potential conflicts, each with an OQ and an RSK: operator-configured endpoints versus data staying in India (NFR-002, CON-001; OQ-016; RSK-002); customer-controlled cloud versus data in India (FR-003, CON-001; ASM-005; OQ-008). Internet optional versus single sign-on is settled by DEP-003 inside the boundary (OQ-020; RSK-005, now Low). The audit log appears once, as FR-008 |
| Traceability | PASS | Every FR, NFR and CON row cites an anchor. All six ACs have one parent. Two-way OQ links checked by script: trace mismatches none |
| Feasibility | PASS | FEASIBLE 1 (FR-002, EV-002). UNVERIFIED 14. AT_RISK 0. Total 15 |
| Testability | FAIL | No AC threshold yet for FR-002, FR-004, FR-006, FR-009, FR-010, NFR-001, NFR-003, CON-001, CON-002 (pending OQ-016, 017, 019). Undefined term: the availability target. The six ACs each have a method and a concrete threshold |
| Counts | PASS | Section 9 reconciles and `check_trace.py` exits 0 |

Repair passes did not apply. The failures wait on stakeholder or legal answers.

Embedded instructions in the input and in the answers files: none.

Promotion audit:
- FR-005 and FR-007 are READY because each is CONFIRMED, has an AC with the stakeholder's threshold, and has no open BLOCKING OQ linked. FR-008 and NFR-002 likewise.
- NFR-002 was narrowed to its boundary clause before it was graded READY, because the stakeholder's threshold (0 requests leave) tests only that clause. The protection clause is NFR-003 and has no threshold, so it is not READY.
- No row was raised by evidence this round. No evidence was gathered.
- The OQ-016 answer covers four behaviours only. It does not apply to the other rows ("All other rows are not decided").
- The respondent is simulated, so no row is a real stakeholder commitment.

Gap checklist:

| Category | Result |
|---|---|
| Actors | ACT-001, ACT-002 |
| Goals and metrics | AC-001 to AC-006; other metrics pending (OQ-016) |
| Scope and exclusions | S1.1 and S1.10 excluded (OQ-010, OQ-011 answered) |
| Core workflows | FR-001 |
| Data (volume, retention, ownership, residency) | FR-004, CON-001; volume and retention gap (OQ-013, OQ-016) |
| Integrations | DEP-001, DEP-003 |
| Deployment | FR-003, FR-006, DEP-002 |
| Security | FR-005, FR-007, FR-009, FR-010 |
| Privacy and compliance | NFR-002, NFR-003, CON-002 (OQ-019) |
| Performance | Gap (OQ-013) |
| Availability and recovery | NFR-001 (OQ-017) |
| Usability and accessibility | Closed by OQ-015: none for the first release |
| Operability | FR-008 (audit log); other operability gap (OQ-016) |
| Maintainability | Closed by OQ-015: none for the first release |
| Constraints | CON-001, CON-002 |
| Autonomy and human oversight | FR-005, FR-007, FR-008 |

## Tool log

No tool call this round. The only open evidence need is the text and applicability of the Digital Personal Data Protection Act 2023 (CON-002). The official sources were refused in round 2 (EV-004, EV-005, permanent errors under §5 Reliability), and a fetch cannot settle applicability, which needs a legal expert (§5 Target, §8 Escalate; OQ-019, N2.1). Nothing else in the answers rests on an external fact. EV-001 to EV-006 are carried forward unchanged.
