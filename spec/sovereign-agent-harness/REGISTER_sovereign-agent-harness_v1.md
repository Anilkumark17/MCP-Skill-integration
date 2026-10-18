# Register: sovereign-agent-harness v1

## Assumptions

| ID | Assumption | Owner | Impact if false | Resolving OQ |
|---|---|---|---|---|
| ASM-001 | "India's first" is a positioning claim, not a requirement. | Stakeholder | A verifiable "first" test would need a defined category and evidence | OQ-010 |
| ASM-002 | "Let's really push it" adds no requirement. No stretch targets are invented. | Stakeholder | Scope or targets grow once defined | OQ-011 |
| ASM-003 | The harness is a runtime for agents that call tools. It is not a model and not a single application. | Stakeholder | GLO-001 and FR-001 change | OQ-001 |

## Open Questions

| ID | Severity | Question | Options (default first) | Owner | Affects |
|---|---|---|---|---|---|
| OQ-001 | BLOCKING | What work do the agents do? | No default. Software engineering tasks; business workflow tasks; both | Stakeholder | FR-001, GLO-001, ASM-003 |
| OQ-002 | BLOCKING | Who uses it? | Enterprise engineering teams; individual developers; regulated organizations such as banks or government | Stakeholder | ACT-002, FR-001 |
| OQ-003 | HIGH | Which models must it run? | Local open-weight models and customer-hosted endpoints only; those plus India-hosted APIs; any model including foreign APIs | Stakeholder | FR-002, DEP-001, NFR-002, CON-001 |
| OQ-004 | BLOCKING | Where is it deployed? | Customer on-premises or customer-controlled cloud, internet optional; single machine; fully air-gapped | Stakeholder | FR-003, DEP-002, ACT-001 |
| OQ-005 | HIGH | What does local-first mean here? | Works fully offline with data on the user's machine; local data with optional sync to a customer server; data only stays on customer infrastructure | Stakeholder | FR-004, GLO-003 |
| OQ-006 | BLOCKING | What may an agent do without human approval? | Approval needed for irreversible and externally visible actions, plus a kill switch and an audit log; approval for a named list only; no approvals | Stakeholder | FR-005, GLO-008, RSK-001 |
| OQ-007 | BLOCKING | What does privacy-preserving protect, and from whom? | No data leaves the customer boundary unless explicitly configured; redact before any external call; both | Stakeholder | NFR-002, GLO-007 |
| OQ-008 | BLOCKING | What does sovereign mean? | Data stays in India; data in India and the operating entity is Indian-controlled; those plus a domestic or auditable supply chain | Stakeholder | CON-001, GLO-002, RSK-002 |
| OQ-009 | HIGH | What does enterprise-grade require? | Single sign-on, role-based access and audit log, with an availability target to be set; add certifications; add vendor support terms | Stakeholder | NFR-001, GLO-004 |
| OQ-010 | LOW | Is "India's first" a requirement or a slogan? | Slogan, excluded; requirement with a defined category and evidence | Stakeholder | ASM-001 |
| OQ-011 | MEDIUM | What does "really push it" require? | No added requirements; named stretch targets for scale, autonomy or compliance; wider scope | Stakeholder | ASM-002 |
| OQ-012 | MEDIUM | Which requirements are Must? | No default | Stakeholder | All |
| OQ-013 | MEDIUM | What scale and speed targets apply? | No default. Needs users, concurrent agents, tasks, latency | Stakeholder | NFR-003 |

No-answer impact: the six BLOCKING questions (OQ-001, 002, 004, 006, 007, 008) keep the core capability, deployment, autonomy limits, privacy and sovereignty unspecified. Without them no requirement can be READY.

Legal point: CON-001 may carry legal obligations. EV-001 failed, so no source settles them. A human with legal expertise must confirm OQ-008 before a final verdict.
