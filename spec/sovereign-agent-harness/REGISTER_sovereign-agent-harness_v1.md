# Register: sovereign-agent-harness v1

## Assumptions

| ID | Assumption | Owner | Impact if false | Resolving OQ |
|---|---|---|---|---|
| ASM-001 | "India’s first" is a positioning claim, not a requirement. | Stakeholder | A verifiable "first" test would need a defined category and evidence | OQ-010 |
| ASM-002 | "Let's really push it" adds no requirement. No stretch targets are invented. | Stakeholder | Scope or targets grow once defined | OQ-011 |
| ASM-003 | The harness is a runtime for agents that call tools. It is not a model and not a single application. | Stakeholder | GLO-001 and FR-001 change | OQ-001 |

## Open Questions

Answer columns stay empty until a stakeholder replies.

| ID | Severity | Question | Options (default first) | Owner | Affects | Answer | Respondent | Date | Resulting changes |
|---|---|---|---|---|---|---|---|---|---|
| OQ-001 | BLOCKING | What work do the agents do? | No default (the input names no task domain). Software engineering tasks; business workflow tasks; both | Stakeholder | ACT-002, FR-001, GLO-001, ASM-003 | | | | |
| OQ-002 | BLOCKING | Who uses it? | Enterprise engineering teams; individual developers; regulated organizations such as banks or government | Stakeholder | ACT-002, FR-001 | | | | |
| OQ-003 | HIGH | Which models must it run? EV-002 shows one local interface can serve several models, so this is a scope choice. | Local open-weight models and customer-hosted endpoints only; those plus India-hosted APIs; any model including foreign APIs | Stakeholder | FR-002, GLO-005, DEP-001, RSK-002, RSK-004 | | | | |
| OQ-004 | BLOCKING | Where is it deployed? | Customer on-premises or customer-controlled cloud, internet optional; single machine; fully air-gapped | Stakeholder | ACT-001, FR-003, GLO-006, DEP-002 | | | | |
| OQ-005 | HIGH | What does local-first mean here? | No default (several readings are plausible and each changes the design). Works fully offline with data on the user's machine; local data with optional sync to a customer server; data only stays on customer infrastructure | Stakeholder | FR-004, GLO-003 | | | | |
| OQ-006 | BLOCKING | What may an agent do without human approval? | Approval needed for irreversible and externally visible actions, plus a kill switch and an audit log; approval for a named list only; no approvals | Stakeholder | FR-005, GLO-008, RSK-001 | | | | |
| OQ-007 | BLOCKING | What does privacy-preserving protect, and from whom? | No data leaves the customer boundary unless explicitly configured; redact before any external call; both | Stakeholder | NFR-002, GLO-007, RSK-002 | | | | |
| OQ-008 | BLOCKING | What does sovereign mean? | Data stays in India; data in India and the operating entity is Indian-controlled; those plus a domestic or auditable supply chain | Stakeholder | CON-001, GLO-002, RSK-002 | | | | |
| OQ-009 | HIGH | What does enterprise-grade require, including availability and operability? | Single sign-on, role-based access and audit log, with an availability target to be set; add certifications; add vendor support terms | Stakeholder | NFR-001, GLO-004 | | | | |
| OQ-010 | LOW | Is "India’s first" a requirement or a slogan? | Slogan, excluded; requirement with a defined category and evidence | Stakeholder | ASM-001 | | | | |
| OQ-011 | MEDIUM | What does "really push it" require, and what is out of scope? | No added requirements; named stretch targets for scale, autonomy or compliance; wider scope | Stakeholder | ASM-002 | | | | |
| OQ-012 | MEDIUM | Which requirements are Must, and what are the success metrics? | No default (priority is the stakeholder's to set) | Stakeholder | FR-001 to FR-005, NFR-001, NFR-002, CON-001 | | | | |
| OQ-013 | MEDIUM | What scale and speed targets apply? | No default (the input gives no numbers). Needs users, concurrent agents, tasks, latency | Stakeholder | none (gap: performance and scale) | | | | |
| OQ-014 | HIGH | Which laws, regulations or standards define the sovereignty and privacy duties? Name them. If you have a readable HTML copy on a site that allows automated fetching, send that link. Government PDFs and sites that block robots cannot be fetched. | No default (the law's name is the stakeholder's to give). Names of the laws; or a readable HTML link | Stakeholder | NFR-002, CON-001 | | | | |
| OQ-015 | LOW | Are there usability, accessibility or maintainability requirements? | None for the first release; name them | Stakeholder | none (gap: usability, accessibility, maintainability) | | | | |

No-answer impact: the six BLOCKING questions (OQ-001, 002, 004, 006, 007, 008) keep the core capability, deployment, autonomy limits, privacy and sovereignty unspecified. Without them no row can be READY. Without OQ-014 no legal claim can be checked.

Escalation: CON-001 may carry legal obligations that evidence cannot settle. A human with legal expertise must confirm OQ-008 before a final verdict.
