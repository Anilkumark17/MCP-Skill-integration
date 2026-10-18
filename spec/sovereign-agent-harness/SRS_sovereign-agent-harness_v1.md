# SRS: Sovereign Agentic Harness (sovereign-agent-harness) v1

Date: 2026-10-18. Verdict: NOT_READY (see VALIDATION_sovereign-agent-harness_v1.md).

## Purpose

A self-hosted agentic harness described by the stakeholder with nine adjectives. Almost every adjective is a vague term under the SpecGate rules, so this round turns each into a requirement slot and opens a question for it. No requirement is invented to fill a slot. No design, code or estimates are included.

## Sources

The problem statement is one fragment plus one remark. It is split into clauses so each item can cite an anchor:

* S1: India's first sovereign local-first, enterprise-grade, model-agnostic, self-hosted, privacy-preserving, fully autonomous agentic harness
  * S1.1 India's first
  * S1.2 sovereign
  * S1.3 local-first
  * S1.4 enterprise-grade
  * S1.5 model-agnostic
  * S1.6 self-hosted
  * S1.7 privacy-preserving
  * S1.8 fully autonomous
  * S1.9 agentic harness
* S2: and let's really push it.

Evidence: EV-001 (attempted, failed).

Not requirements:
* S1.1 is a market-position claim. No evidence can confirm it and no test can check it. It is excluded (ASM-001, OQ-010).
* S2 gives no testable content. It adds no requirement (ASM-002, OQ-011).

## Glossary

| ID | Term | Definition | Status |
|---|---|---|---|
| GLO-001 | agentic harness | Runtime that runs AI agents which call tools to complete tasks. What tasks is open | INFERRED, ASM-003, OQ-001 |
| GLO-002 | sovereign | UNRESOLVED | OQ-008 |
| GLO-003 | local-first | UNRESOLVED | OQ-005 |
| GLO-004 | enterprise-grade | UNRESOLVED | OQ-009 |
| GLO-005 | model-agnostic | Agents can run on more than one model through one interface. Which models is open | INFERRED, OQ-003 |
| GLO-006 | self-hosted | Runs on infrastructure the customer controls. Which infrastructure is open | INFERRED, OQ-004 |
| GLO-007 | privacy-preserving | UNRESOLVED | OQ-007 |
| GLO-008 | fully autonomous | UNRESOLVED | OQ-006 |

## Actors

| ID | Role | Goal | Status |
|---|---|---|---|
| ACT-001 | Operator who installs and runs the harness | UNRESOLVED (OQ-004) | INFERRED from S1.6 |
| ACT-002 | User who gives work to agents | UNRESOLVED (OQ-001, OQ-002) | INFERRED from S1.9 |
| ACT-003 | Model provider or local model | Serve inference to agents | INFERRED from S1.5 |

## Functional Requirements

Priority is UNPRIORITIZED for every row (OQ-012).

| ID | Statement | Status | Readiness | Feas | Trace | AC |
|---|---|---|---|---|---|---|
| FR-001 | The system shall run AI agents that use tools to complete tasks given by a user. | STATED | NEEDS_CLARIFICATION | AT_RISK (RSK-003) | S1.9, GLO-001, ASM-003, OQ-001, OQ-002 | pending: OQ-001 |
| FR-002 | The system shall run its agents against more than one model through a single interface. | STATED | NEEDS_CLARIFICATION | UNVERIFIED | S1.5, GLO-005, OQ-003 | pending: OQ-003 |
| FR-003 | The system shall be installable and run on infrastructure controlled by the customer. | STATED | NEEDS_CLARIFICATION | UNVERIFIED | S1.6, GLO-006, OQ-004 | pending: OQ-004 |
| FR-004 | Local-first behaviour. | UNRESOLVED | NEEDS_CLARIFICATION | UNVERIFIED | S1.3, GLO-003, OQ-005 | pending: OQ-005 |
| FR-005 | Limits on what agents may do without human approval. | UNRESOLVED | NEEDS_CLARIFICATION | AT_RISK (RSK-001) | S1.8, GLO-008, OQ-006 | pending: OQ-006 |

## Non-Functional Requirements

| ID | Category | Statement | Status | Readiness | Trace | AC |
|---|---|---|---|---|---|---|
| NFR-001 | Enterprise readiness | Measurable limits for security, audit, access control, availability and support. | UNRESOLVED | NEEDS_CLARIFICATION | S1.4, GLO-004, OQ-009 | pending: OQ-009 |
| NFR-002 | Privacy | Which data is protected, from whom, and how. | UNRESOLVED | NEEDS_CLARIFICATION | S1.7, GLO-007, OQ-007 | pending: OQ-007 |
| NFR-003 | Performance and scale | Number of users, concurrent agents, tasks and latency. Nothing is stated. | UNRESOLVED | NEEDS_CLARIFICATION | OQ-013 | pending: OQ-013 |

## Constraints

| ID | Type | Statement | Source |
|---|---|---|---|
| CON-001 | Legal and jurisdiction | Sovereignty requirement. Content UNRESOLVED (residency, ownership, supply chain, regulation) | S1.2, OQ-008 |

## Dependencies

| ID | Target | Owner |
|---|---|---|
| DEP-001 | Models the harness must run on (unspecified) | Stakeholder, OQ-003 |
| DEP-002 | Customer infrastructure (unspecified) | Customer, OQ-004 |

## Risks

| ID | Risk | Likelihood | Impact | Affects |
|---|---|---|---|---|
| RSK-001 | Agents act without approval and cause irreversible or external harm | Not assessed | High | FR-005 |
| RSK-002 | "Sovereign" is defined wrongly or too loosely and the product fails a legal or buyer test | Not assessed | High | CON-001 |
| RSK-003 | Undefined adjectives let scope grow without limit and nothing can be tested | Not assessed | High | FR-001 to FR-005 |
| RSK-004 | Local models may be too weak or too slow for the autonomy and enterprise targets that get set | Not assessed | Medium | FR-002, FR-005, NFR-001 |

Likelihood is not assessed because no stakeholder or evidence supports a rating.

## Traceability

Acceptance criteria: none written. Every row is `pending` on a question. SpecGate forbids an AC for an UNRESOLVED item, and the STATED items have no measurable threshold.

Trace summary: every FR, NFR and CON traces to an anchor, ASM or OQ. No orphan IDs.

## Change log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-10-18 | First draft from the problem statement; one evidence attempt failed |
