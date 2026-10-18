# SRS: Sovereign Agentic Harness (sovereign-agent-harness) v1

Date: 2026-10-18. Verdict: NOT_READY (see VALIDATION_sovereign-agent-harness_v1.md).

## Purpose

A self-hosted agentic harness described by the stakeholder with nine adjectives. Five adjectives are undefined vague terms, so each becomes a placeholder row (status SLOT) with a question. Three rows are agent-derived readings of the other terms. No requirement is invented to fill a placeholder. No design, code or estimates are included.

## Sources

The problem statement is one sentence. It is split into clauses so each item can cite an anchor:

* S1: Let’s make India’s first sovereign local-first, enterprise-grade, model-agnostic, self-hosted, privacy-preserving, fully autonomous agentic harness, and let's really push it.
  * S1.1 India’s first
  * S1.2 sovereign
  * S1.3 local-first
  * S1.4 enterprise-grade
  * S1.5 model-agnostic
  * S1.6 self-hosted
  * S1.7 privacy-preserving
  * S1.8 fully autonomous
  * S1.9 agentic harness
  * S1.10 let's really push it

Stakeholder notes: none.

Evidence: EV-001 (search), EV-002 (vendor documentation, supports FR-002 only).

Not requirements:
* S1.1 is a market-position claim. No evidence can confirm it and no test can check it. It is excluded (ASM-001).
* S1.10 gives no testable content. It adds no requirement (ASM-002).

Embedded instructions in the input: none.

Retired rows: none.

## Glossary

| ID | Term | Definition | Status | Trace |
|---|---|---|---|---|
| GLO-001 | agentic harness | Runtime that runs AI agents which call tools to complete tasks. What tasks is open | INFERRED | S1.9, OQ-001 |
| GLO-002 | sovereign | UNRESOLVED | SLOT | S1.2, OQ-008 |
| GLO-003 | local-first | UNRESOLVED | SLOT | S1.3, OQ-005 |
| GLO-004 | enterprise-grade | UNRESOLVED | SLOT | S1.4, OQ-009 |
| GLO-005 | model-agnostic | Agents can run on more than one model through one interface. Which models is open | INFERRED | S1.5, OQ-003 |
| GLO-006 | self-hosted | Runs on infrastructure the customer controls. Which infrastructure is open | INFERRED | S1.6, OQ-004 |
| GLO-007 | privacy-preserving | UNRESOLVED | SLOT | S1.7, OQ-007 |
| GLO-008 | fully autonomous | UNRESOLVED | SLOT | S1.8, OQ-006 |

## Actors

Actors are people or roles. Models and infrastructure are dependencies.

| ID | Role | Goal | Trace |
|---|---|---|---|
| ACT-001 | Operator who installs and runs the harness | UNRESOLVED | S1.6, OQ-004 |
| ACT-002 | User who gives work to agents | UNRESOLVED | S1.9, OQ-001, OQ-002 |

## Functional Requirements

| ID | Statement | Status | Readiness | Priority | Trace | Feas | AC |
|---|---|---|---|---|---|---|---|
| FR-001 | The system shall run AI agents that use tools to complete tasks given by a user. | INFERRED | NEEDS_CLARIFICATION | UNPRIORITIZED (OQ-012) | S1.9, GLO-001, ASM-003, OQ-001, OQ-002 | UNVERIFIED | pending: OQ-001 |
| FR-002 | The system shall run its agents against more than one model through a single interface. | EXTERNALLY_SUPPORTED | NEEDS_CLARIFICATION | UNPRIORITIZED (OQ-012) | S1.5, GLO-005, EV-002, OQ-003 | FEASIBLE | pending: OQ-003 |
| FR-003 | The system shall be installable and run on infrastructure controlled by the customer. | INFERRED | NEEDS_CLARIFICATION | UNPRIORITIZED (OQ-012) | S1.6, GLO-006, OQ-004 | UNVERIFIED | pending: OQ-004 |
| FR-004 | Local-first behaviour (placeholder, no statement yet). | SLOT | NEEDS_CLARIFICATION | UNPRIORITIZED (OQ-012) | S1.3, GLO-003, OQ-005 | UNVERIFIED | pending: OQ-005 |
| FR-005 | Limits on what agents may do without human approval (placeholder, no statement yet). | SLOT | NEEDS_CLARIFICATION | UNPRIORITIZED (OQ-012) | S1.8, GLO-008, OQ-006 | AT_RISK (RSK-001) | pending: OQ-006 |

## Non-Functional Requirements

| ID | Category | Statement | Status | Readiness | Priority | Trace | Feas | AC |
|---|---|---|---|---|---|---|---|---|
| NFR-001 | Enterprise readiness | Measurable limits for security, audit, access control, availability and support (placeholder, no limit yet). | SLOT | NEEDS_CLARIFICATION | UNPRIORITIZED (OQ-012) | S1.4, GLO-004, OQ-009 | UNVERIFIED | pending: OQ-009 |
| NFR-002 | Privacy | Which data is protected, from whom, and how (placeholder, no limit yet). | SLOT | NEEDS_CLARIFICATION | UNPRIORITIZED (OQ-012) | S1.7, GLO-007, OQ-007, OQ-014 | AT_RISK (RSK-002) | pending: OQ-007 |

Performance, scale and availability targets are recorded as gaps in the validation report (OQ-013). They have no anchor in the input, so they are not rows.

## Constraints

| ID | Type | Statement | Status | Readiness | Priority | Trace | Feas | AC |
|---|---|---|---|---|---|---|---|---|
| CON-001 | Legal and jurisdiction | Sovereignty requirement (placeholder: residency, ownership, supply chain, regulation all open). | SLOT | NEEDS_CLARIFICATION | UNPRIORITIZED (OQ-012) | S1.2, GLO-002, OQ-008, OQ-014 | AT_RISK (RSK-002) | pending: OQ-008 |

## Dependencies

| ID | Target | Owner | Trace |
|---|---|---|---|
| DEP-001 | Models the harness must run on (unspecified; local models and model providers) | Stakeholder | S1.5, EV-002, OQ-003 |
| DEP-002 | Customer infrastructure (unspecified) | Customer | S1.6, OQ-004 |

## Risks

| ID | Risk | Likelihood | Impact | Affects | Owner | Mitigation | Resolving OQ |
|---|---|---|---|---|---|---|---|
| RSK-001 | Agents act without approval and cause irreversible or external harm | Not assessed | High | FR-005 | Stakeholder | Settle approval limits before any autonomy requirement is written | OQ-006 |
| RSK-002 | Model-agnostic support lets data reach foreign model APIs, which conflicts with privacy and sovereignty | Not assessed | High | FR-002, NFR-002, CON-001 | Stakeholder | Settle models, privacy and sovereignty together | OQ-003, OQ-007, OQ-008 |
| RSK-003 | Undefined adjectives let scope grow without limit and nothing can be tested | Not assessed | High | FR-001 to FR-005, NFR-001, NFR-002, CON-001 | Requirements engineer | Keep every placeholder until its question is answered | none |
| RSK-004 | Local models may be too weak or too slow for the autonomy and enterprise targets that get set | Not assessed | Medium | FR-002 | Stakeholder | Review after the model scope is answered | OQ-003 |

Likelihood is not assessed because no stakeholder or evidence supports a rating.

## Acceptance Criteria

None written. Every requirement row is `pending` on a question. SpecGate forbids an AC for a placeholder, and the other rows have no measurable threshold.

## Traceability

Every FR, NFR and CON row cites an anchor. OQ links are checked both ways by `scripts/check_trace.py` and reported in the validation report.

## Change log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-10-18 | First draft. EV-002 raised FR-002 from INFERRED to EXTERNALLY_SUPPORTED |
