# Register: multitenant-doc-editor v1

## Assumptions

| ID | Assumption | Owner | Impact if false | Resolving OQ |
|---|---|---|---|---|
| ASM-001 | A concurrent user is a user with an active session in the last 5 minutes. | Stakeholder | Load profile and NFR-002 change | OQ-009 |
| ASM-002 | 2,000 requests per second is the total sustained peak across reads and writes. | Stakeholder | Load profile and NFR-003 change by up to a factor of 2 | OQ-009 |
| ASM-003 | Documents are rich text, with no real-time co-editing. A concurrent save is resolved by FR-003 conflict rejection. | Stakeholder | FR-001, FR-003 change; co-editing needs a different model | OQ-001, OQ-002 |
| ASM-004 | The client supplies the idempotency key on each write; keys are kept for 24 hours. No external standard is followed (EV-001). | Stakeholder | FR-004 and AC-002 change | OQ-010 |
| ASM-005 | Replicas serve reads. The author reads their own writes from the primary. | Stakeholder | FR-005 changes | OQ-007 |
| ASM-006 | A tenant is an organization with many users. Each document belongs to one tenant. | Stakeholder | FR-002, GLO-002 change | OQ-005 |

## Open Questions

| ID | Severity | Question | Options (default first) | Owner | Affects |
|---|---|---|---|---|---|
| OQ-001 | BLOCKING | How do two users editing the same document interact? | One user saves at a time; the other gets a conflict and merges by hand; real-time co-editing; auto-merge on save | Stakeholder | FR-001, FR-003, ASM-003 |
| OQ-002 | HIGH | What is a document? | Rich text; Markdown; both | Stakeholder | FR-001, GLO-001 |
| OQ-003 | BLOCKING | What latency and error limits apply at 2,000 req/s? S1.9 asks for validation but gives no targets. | Proposal, not stated by stakeholder: reads p95 200 ms, writes p95 400 ms, errors under 0.1%; stricter p99 limits; stakeholder-defined | Stakeholder | NFR-004, FR-007, AC-003, AC-004 |
| OQ-004 | BLOCKING | How do users register and sign in? | Per-tenant single sign-on; email and password; both | Stakeholder | FR-006 |
| OQ-005 | BLOCKING | How strictly are tenants isolated? | Logical isolation, no cross-tenant read or write; dedicated storage for large tenants; dedicated storage for all tenants | Stakeholder | FR-002, GLO-002, ASM-006 |
| OQ-006 | BLOCKING | Which privacy, compliance and data-residency rules apply? | None beyond tenant isolation; GDPR; SOC 2; other (name them) | Stakeholder | NFR-007, FR-002 |
| OQ-007 | HIGH | What must a reader see after a write? | Author reads own writes, others may lag; all reads may lag; all reads current | Stakeholder | FR-005, ASM-005 |
| OQ-008 | HIGH | What are the availability, data-loss (RPO) and recovery-time (RTO) targets? Asynchronous replication means RPO above zero. | Stakeholder-defined; no default | Stakeholder | NFR-005, NFR-006 |
| OQ-009 | HIGH | What do "10,000 concurrent users" and "2,000 read/write requests per second" mean, and what is the read:write ratio? | Active sessions in 5 min; 2,000 total sustained peak; ratio stakeholder-defined | Stakeholder | NFR-002, NFR-003, GLO-003, GLO-004 |
| OQ-010 | MEDIUM | Which writes carry idempotency keys and for how long are keys kept? | All create and update writes, 24 hours; updates only; 7 days | Stakeholder | FR-004, ASM-004, DEP-002 |
| OQ-011 | MEDIUM | Which faults does injection cover? | Primary loss, replica lag, network partition, node crash; add disk full; add dependency timeout | Stakeholder | FR-007 |
| OQ-012 | MEDIUM | How many tenants, and how large is the largest? | Stakeholder-defined; no default | Stakeholder | NFR-001, RSK-002 |
| OQ-013 | LOW | What is the maximum document size? | 10 MB; 1 MB; 100 MB | Stakeholder | GLO-001 |
| OQ-014 | MEDIUM | Which requirements are Must for the first release? | FR-001, 003, 004, 006 and NFR-001 to NFR-004 Must; rest Should | Stakeholder | All |
| OQ-015 | BLOCKING | Where does the system run, and where are the load tests run? | Stakeholder-defined; no default | Stakeholder | DEP-001, FR-007 |

No-answer impact: the six BLOCKING questions (OQ-001, 003, 004, 005, 006, 015) keep their dependent requirements unspecified and block IMPLEMENTATION_READY. Other questions fall back to the default as a labelled assumption, where a default exists.
