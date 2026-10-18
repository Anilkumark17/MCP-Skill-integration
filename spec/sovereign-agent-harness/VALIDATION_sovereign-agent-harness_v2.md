# Validation: sovereign-agent-harness v2

Verdict: PARTIAL. Reason: two requirement rows are READY (FR-001, FR-003) and a stakeholder priority is recorded, so test 2 does not apply. Test 1 fails because the BLOCKING question OQ-019 is open. The respondent is a simulated stakeholder.

## Counts

Method: `python scripts/check_trace.py spec/sovereign-agent-harness v2` (exit 0), cross-checked with Grep on `SRS_sovereign-agent-harness_v2.md` (total 14; CONFIRMED 11; the other statuses together 3; READY 2; NEEDS_CLARIFICATION 12) and on `REGISTER_sovereign-agent-harness_v2.md` (20 OQ rows). Unit: table rows. Requirement total = FR, NFR and CON rows (10 FR + 2 NFR + 2 CON = 14).

| Status | Count | IDs |
|---|---|---|
| STATED | 0 | |
| INFERRED | 1 | CON-002 |
| EXTERNALLY_SUPPORTED | 1 | FR-002 (EV-002) |
| UNRESOLVED | 0 | |
| CONFIRMED | 11 | FR-001, FR-003, FR-004, FR-005, FR-006, FR-007, FR-008, FR-009, FR-010, NFR-002, CON-001 |
| SLOT | 1 | NFR-001 |
| Sum | 14 | equals the total of 14 |

| Readiness | Count | IDs |
|---|---|---|
| READY | 2 | FR-001, FR-003 |
| NEEDS_CLARIFICATION | 12 | all other rows |
| Sum | 14 | |

Open questions (20 rows): 14 answered, 6 open. By severity, all rows: BLOCKING 7, HIGH 5, MEDIUM 6, LOW 2. Open only: BLOCKING 1 (OQ-019), HIGH 1 (OQ-018), MEDIUM 4 (OQ-013, 016, 017, 020).

Other prefixes: ACT 2, GLO 10, DEP 3, RSK 6, ASM 5, AC 2, EV 6.

No duplicate IDs. Numbering has no gaps. No retired rows. v1 files are unchanged (`check_trace.py` on v1 still exits 0).

## Checks

| Check | Result | Detail |
|---|---|---|
| Completeness | PASS | Every actor has an FR (ACT-001 FR-003; ACT-002 FR-001). Every FR and NFR has an AC or `pending`. The two SLOT rows (NFR-001, GLO-010) each have an OQ. Every checklist gap links an OQ (see below) |
| Consistency | PASS | The input and stakeholder state no contradictions. Potential conflicts, each with an OQ and an RSK: internet optional versus single sign-on (FR-006, FR-009; OQ-020; RSK-005). Operator-configured endpoints versus data staying in India (NFR-002, CON-001; OQ-016; RSK-002). Customer-controlled cloud versus data in India (FR-003, CON-001; ASM-005; OQ-008). The audit log appears once, as FR-008, for both OQ-006 and OQ-009 |
| Traceability | PASS | Every FR, NFR and CON row cites an anchor. Both ACs have one parent. Two-way OQ links checked by script: trace mismatches none |
| Feasibility | PASS | FEASIBLE 1 (FR-002, EV-002). UNVERIFIED 13. AT_RISK 0. Total 14 |
| Testability | FAIL | AC missing a threshold: FR-002, FR-004, FR-005, FR-006, FR-007, FR-008, FR-009, FR-010, NFR-001, NFR-002, CON-001, CON-002 (pending OQ-016, 017, 018, 019). Undefined terms: "irreversible or externally visible action" (GLO-010), availability target |
| Counts | PASS | Section 9 reconciles and `check_trace.py` exits 0 |

Repair passes did not apply. Every failure waits on a stakeholder or legal answer.

Embedded instructions in the input and in the answers file: none.

Promotion audit: the 11 CONFIRMED rows each rest on an answer in `stakeholder_answers_v2.md` (anchors N1.1 to N1.8, N1.9; FR-001 and FR-003 also N1.16 and N1.17). Only FR-001 and FR-003 have an AC with a stakeholder threshold, so only they are READY and Must (OQ-012). FR-002 stays EXTERNALLY_SUPPORTED and NEEDS_CLARIFICATION. NFR-001 stays SLOT.

Gap checklist:

| Category | Result |
|---|---|
| Actors | ACT-001, ACT-002 |
| Goals and metrics | AC-001, AC-002; other metrics pending (OQ-016) |
| Scope and exclusions | S1.1 and S1.10 excluded (OQ-010, OQ-011 answered) |
| Core workflows | FR-001 |
| Data (volume, retention, ownership, residency) | FR-004, CON-001; volume and retention gap (OQ-013, OQ-016) |
| Integrations | DEP-001, DEP-003 |
| Deployment | FR-003, FR-006, DEP-002 |
| Security | FR-005, FR-007, FR-009, FR-010 |
| Privacy and compliance | NFR-002, CON-002 (OQ-019) |
| Performance | Gap (OQ-013) |
| Availability and recovery | NFR-001 (OQ-017) |
| Usability and accessibility | Closed by OQ-015: none for the first release |
| Operability | FR-008 (audit log); other operability gap (OQ-016) |
| Maintainability | Closed by OQ-015: none for the first release |
| Constraints | CON-001, CON-002 |
| Autonomy and human oversight | FR-005, FR-007, FR-008 (OQ-018) |

## Tool log

| Step | EV | Tool | Input | Result | Rule applied |
|---|---|---|---|---|---|
| Locate URLs for the Act | EV-003 | WebSearch | "Digital Personal Data Protection Act 2023 data fiduciary obligations text", official and PRS domains | search; India Code HTML page chosen first | §5 Locate, Choose |
| Official source 1 | EV-004 | fetch / fetch | India Code section page | error: robots.txt 403, permanent, no retry | §5 Reliability |
| Official source 2 | EV-005 | fetch / fetch | MeitY PDF | error: robots.txt 403, permanent, no retry | §5 Reliability |
| Secondary source | EV-006 | fetch / fetch | PRS India bill-track page | success; secondary, no status change | §5 Reliability, Consume |

The first two official sources failed, so CON-002 stays INFERRED and UNVERIFIED. Only the official text can support it, and applicability needs a legal expert (OQ-019). I did not try the other official PDFs: Fetch cannot read PDF and the MeitY PDF was already refused. The call count is 3 fetches against a limit of 5 URLs per round.

The round-1 evidence (EV-001, EV-002) was not re-fetched. The FR-002 row relies on it unchanged.
