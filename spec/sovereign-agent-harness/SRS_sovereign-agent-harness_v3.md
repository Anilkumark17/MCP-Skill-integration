# SRS: Sovereign Agentic Harness (sovereign-agent-harness) v3

Date: 2026-10-18. Verdict: PARTIAL (see VALIDATION_sovereign-agent-harness_v3.md).

## Purpose

A self-hosted agentic harness for enterprise engineering teams doing software engineering tasks. Round 3 applies the answers in `stakeholder_answers_v3.md`: the approval, kill-switch, audit-log and boundary behaviours get thresholds, and the action classes and single sign-on location are settled. The respondent is a simulated stakeholder. No design, code or estimates are included.

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

Stakeholder notes, round 2 (`stakeholder_answers_v2.md`, simulated stakeholder, 2026-10-18), numbered by line:

* N1.1 OQ-001, N1.2 OQ-002, N1.3 OQ-003, N1.4 OQ-004, N1.5 OQ-005, N1.6 OQ-006, N1.7 OQ-007, N1.8 OQ-008, N1.9 OQ-009
* N1.10 OQ-012 (priorities), N1.11 OQ-013 (not decided), N1.12 OQ-014 (law named), N1.13 OQ-010, N1.14 OQ-011, N1.15 OQ-015
* N1.16 threshold for FR-001: at least 95 of 100 test runs; N1.17 threshold for FR-003: 60 minutes or less

Stakeholder notes, round 3 (`stakeholder_answers_v3.md`, simulated stakeholder, 2026-10-18), numbered by line:

* N2.1 OQ-019 (not decided, legal expert), N2.2 OQ-018 (accepted), N2.3 OQ-016 (thresholds only for the four behaviours below), N2.8 OQ-017 (not decided), N2.9 OQ-020 (accepted), N2.10 OQ-013 (not decided)
* N2.4 approval: in 50 test runs that attempt an irreversible or externally visible action, 100 percent are blocked until a human approves
* N2.5 kill switch: all running agents stop within 5 seconds of activation, in 10 of 10 test runs
* N2.6 audit log: every agent action produces an audit record in 100 of 100 test runs
* N2.7 boundary: in 50 test runs with no operator configuration, 0 requests leave the customer boundary

Evidence: EV-001 and EV-002 (search and vendor documentation, support FR-002). EV-003 (search), EV-004 and EV-005 (official legal sources, both refused), EV-006 (secondary source, no status change). No new evidence call this round.

Not requirements:
* S1.1 is a market-position claim, excluded by N1.13 (ASM-001).
* S1.10 adds no requirement, confirmed by N1.14 (ASM-002).

Embedded instructions in the input and the answers: none.

Retired rows: none.

## Glossary

| ID | Term | Definition | Status | Trace |
|---|---|---|---|---|
| GLO-001 | agentic harness | Runtime that runs AI agents which call tools to complete software engineering tasks. The runtime reading is the agent's | INFERRED | S1.9, OQ-001 |
| GLO-002 | sovereign | Data stays in India | CONFIRMED | S1.2, N1.8, OQ-008 |
| GLO-003 | local-first | Local data with optional sync to a customer server | CONFIRMED | S1.3, N1.5, OQ-005 |
| GLO-004 | enterprise-grade | Single sign-on, role-based access and an audit log. The availability target is open | CONFIRMED | S1.4, N1.9, OQ-009, OQ-017 |
| GLO-005 | model-agnostic | Agents can run on more than one model through one interface. The agent's reading | INFERRED | S1.5, OQ-003 |
| GLO-006 | self-hosted | Runs on customer on-premises servers or customer-controlled cloud | CONFIRMED | S1.6, N1.4, OQ-004 |
| GLO-007 | privacy-preserving | Task data and source code are protected from any party outside the customer boundary, and no data leaves the boundary unless an operator explicitly configures it | CONFIRMED | S1.7, N1.7, OQ-007 |
| GLO-008 | fully autonomous | Agents act without a human step, except approval for irreversible and externally visible actions; a kill switch and an audit log of every agent action exist | CONFIRMED | S1.8, N1.6, OQ-006 |
| GLO-009 | customer boundary | The customer's on-premises servers or customer-controlled cloud. The agent's reading of N1.4 | INFERRED | N1.4, OQ-004, OQ-007 |
| GLO-010 | irreversible or externally visible action | Deleting files outside the working tree, pushing to a remote repository, and any request outside the customer boundary | CONFIRMED | N1.6, N2.2, OQ-018 |

## Actors

Actors are people or roles. Models, infrastructure and identity providers are dependencies.

| ID | Role | Goal | Trace |
|---|---|---|---|
| ACT-001 | Operator who installs and runs the harness | Install the harness on a customer server from the documented procedure | S1.6, N1.4, N1.17, OQ-004 |
| ACT-002 | Enterprise engineering team member who gives software engineering tasks to agents | Have a submitted task completed with a recorded result | S1.9, N1.1, N1.2, N1.16, OQ-001, OQ-002 |

## Functional Requirements

| ID | Statement | Status | Readiness | Priority | Trace | Feas | AC |
|---|---|---|---|---|---|---|---|
| FR-001 | The system shall run AI agents that use tools to complete software engineering tasks given by a user. | CONFIRMED | READY | Must (OQ-012) | S1.9, N1.1, N1.10, N1.16, GLO-001, ASM-003, OQ-001, OQ-002, OQ-012 | UNVERIFIED | AC-001 |
| FR-002 | The system shall run its agents against more than one local open-weight model or customer-hosted endpoint through a single interface. | EXTERNALLY_SUPPORTED | NEEDS_CLARIFICATION | Should (OQ-012) | S1.5, N1.3, GLO-005, EV-002, OQ-003, OQ-012, OQ-016 | FEASIBLE | pending: OQ-016 |
| FR-003 | The system shall be installable on, and run on, customer on-premises servers or customer-controlled cloud. | CONFIRMED | READY | Must (OQ-012) | S1.6, N1.4, N1.10, N1.17, GLO-006, OQ-004, OQ-012 | UNVERIFIED | AC-002 |
| FR-004 | The system shall store task data locally and shall support optional synchronisation to a customer server. | CONFIRMED | NEEDS_CLARIFICATION | Should (OQ-012) | S1.3, N1.5, GLO-003, OQ-005, OQ-012, OQ-016 | UNVERIFIED | pending: OQ-016 |
| FR-005 | The system shall require human approval before an agent performs an irreversible or externally visible action. | CONFIRMED | READY | Should (OQ-012) | S1.8, N1.6, N2.2, N2.4, GLO-008, GLO-010, OQ-006, OQ-012, OQ-018 | UNVERIFIED | AC-003 |
| FR-006 | The system shall run with or without internet access at runtime. | CONFIRMED | NEEDS_CLARIFICATION | Should (OQ-012) | S1.6, N1.4, OQ-004, OQ-012, OQ-016 | UNVERIFIED | pending: OQ-016 |
| FR-007 | The system shall provide a kill switch. | CONFIRMED | READY | Should (OQ-012) | S1.8, N1.6, N2.5, GLO-008, OQ-006, OQ-012 | UNVERIFIED | AC-004 |
| FR-008 | The system shall record an audit log of every agent action. | CONFIRMED | READY | Should (OQ-012) | S1.4, S1.8, N1.6, N1.9, N2.6, GLO-004, GLO-008, OQ-006, OQ-009, OQ-012 | UNVERIFIED | AC-005 |
| FR-009 | The system shall authenticate users through single sign-on. | CONFIRMED | NEEDS_CLARIFICATION | Should (OQ-012) | S1.4, N1.9, N2.9, GLO-004, OQ-009, OQ-012, OQ-016, OQ-020 | UNVERIFIED | pending: OQ-016 |
| FR-010 | The system shall restrict actions by user role. | CONFIRMED | NEEDS_CLARIFICATION | Should (OQ-012) | S1.4, N1.9, GLO-004, OQ-009, OQ-012, OQ-016 | UNVERIFIED | pending: OQ-016 |

## Non-Functional Requirements

| ID | Category | Statement | Status | Readiness | Priority | Trace | Feas | AC |
|---|---|---|---|---|---|---|---|---|
| NFR-001 | Availability | Availability target (placeholder, no limit yet). | SLOT | NEEDS_CLARIFICATION | Should (OQ-012) | S1.4, N1.9, GLO-004, OQ-009, OQ-012, OQ-017 | UNVERIFIED | pending: OQ-017 |
| NFR-002 | Privacy | No data shall leave the customer boundary unless an operator explicitly configures it. | CONFIRMED | READY | Should (OQ-012) | S1.7, N1.7, N2.7, GLO-007, GLO-009, OQ-007, OQ-012 | UNVERIFIED | AC-006 |
| NFR-003 | Privacy | Task data and source code shall be protected from any party outside the customer boundary. | CONFIRMED | NEEDS_CLARIFICATION | Should (OQ-012) | S1.7, N1.7, GLO-007, GLO-009, OQ-007, OQ-012, OQ-016 | UNVERIFIED | pending: OQ-016 |

Performance and scale targets are a recorded gap (OQ-013). They have no anchor in the input, so they are not rows.

## Constraints

| ID | Type | Statement | Status | Readiness | Priority | Trace | Feas | AC |
|---|---|---|---|---|---|---|---|---|
| CON-001 | Data residency | Data shall stay in India. | CONFIRMED | NEEDS_CLARIFICATION | Should (OQ-012) | S1.2, N1.8, GLO-002, ASM-005, OQ-008, OQ-012, OQ-016 | UNVERIFIED | pending: OQ-016 |
| CON-002 | Legal | The system shall meet the duties the Digital Personal Data Protection Act 2023 places on it, where the Act applies. | INFERRED | NEEDS_CLARIFICATION | Should (OQ-012) | N1.12, N2.1, EV-006, OQ-012, OQ-014, OQ-019 | UNVERIFIED | pending: OQ-019 |

## Dependencies

| ID | Target | Owner | Trace |
|---|---|---|---|
| DEP-001 | Local open-weight models and customer-hosted model endpoints | Stakeholder | S1.5, N1.3, EV-002, OQ-003 |
| DEP-002 | Customer on-premises servers or customer-controlled cloud | Customer | S1.6, N1.4, OQ-004 |
| DEP-003 | Single sign-on identity provider, running inside the customer boundary | Customer | N1.9, N2.9, OQ-020 |

## Risks

| ID | Risk | Likelihood | Impact | Affects | Owner | Mitigation | Resolving OQ |
|---|---|---|---|---|---|---|---|
| RSK-001 | An agent performs an irreversible or externally visible action without approval | Not assessed | High | FR-005, FR-007, FR-008 | Stakeholder | Approval gate, kill switch and audit log are confirmed and tested by AC-003, AC-004 and AC-005 | OQ-006, OQ-018 |
| RSK-002 | An operator-configured external endpoint lets data leave the customer boundary and India, which conflicts with data residency | Not assessed | High | FR-002, NFR-002, CON-001 | Stakeholder | AC-006 tests the unconfigured case; a threshold for the residency constraint is still needed | OQ-016 |
| RSK-003 | The availability target is undefined, so nothing can be tested for it | Not assessed | Medium | NFR-001 | Requirements engineer | Keep the placeholder until the question is answered | OQ-017 |
| RSK-004 | Local open-weight models may be too weak or too slow to meet the 95-of-100 task threshold | Not assessed | Medium | FR-001, FR-002 | Stakeholder | Run AC-001 on the chosen models early | OQ-003 |
| RSK-005 | Single sign-on needs an identity provider, which could conflict with running without internet access. Settled by placing the provider inside the boundary | Not assessed | Low | FR-006, FR-009 | Stakeholder | Provider inside the customer boundary (DEP-003); confirm with a sign-in test once a threshold is set | OQ-020 |
| RSK-006 | The Act's applicability and duties are unknown, so a legal duty could be missed | Not assessed | High | CON-001, CON-002 | Legal expert | Obtain a legal opinion | OQ-019, OQ-014 |

Likelihood is not assessed because no stakeholder or evidence supports a rating.

## Acceptance Criteria

| ID | Parent | Method | Pass threshold |
|---|---|---|---|
| AC-001 | FR-001 | Submit a software engineering task to the harness 100 times and count the runs that make at least one tool call and write a recorded result. The task set is chosen by the test owner (test design) | At least 95 of 100 runs (N1.16) |
| AC-002 | FR-003 | An operator follows the documented procedure to install the harness on a clean customer server and the elapsed time is measured | 60 minutes or less (N1.17) |
| AC-003 | FR-005 | Run 50 tests in which an agent attempts an irreversible or externally visible action (the three classes in GLO-010) and count the attempts blocked until a human approves | 100 percent of 50 runs blocked until approval (N2.4) |
| AC-004 | FR-007 | Start agents, activate the kill switch, and measure the time until all running agents stop. Repeat 10 times | All running agents stop within 5 seconds, in 10 of 10 runs (N2.5) |
| AC-005 | FR-008 | Run 100 tests in which agents perform actions and check that each action has an audit record | Every agent action has an audit record in 100 of 100 runs (N2.6) |
| AC-006 | NFR-002 | Run 50 tests with no operator configuration and count the requests that leave the customer boundary | 0 requests leave the boundary in 50 runs (N2.7) |

## Traceability

Every FR, NFR and CON row cites an anchor. OQ links are checked both ways by `scripts/check_trace.py` and reported in the validation report.

## Change log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-10-18 | First draft. EV-002 raised FR-002 from INFERRED to EXTERNALLY_SUPPORTED |
| v2 | 2026-10-18 | Round 2 with `stakeholder_answers_v2.md`. FR-001 and FR-003 CONFIRMED with AC-001 and AC-002. FR-004, FR-005, NFR-002, CON-001 SLOT to CONFIRMED. New rows FR-006 to FR-010 and CON-002. EV-003 to EV-006 added: no status change |
| v3 | 2026-10-18 | Round 3 with `stakeholder_answers_v3.md`. GLO-010 SLOT to CONFIRMED (OQ-018 accepted). FR-005, FR-007, FR-008 and NFR-002 get AC-003 to AC-006 from the stated thresholds, so they become READY (priority stays Should). NFR-002 narrowed to the boundary clause, because its threshold tests only that clause; the protection clause moved to new NFR-003, still pending a threshold. DEP-003 set inside the boundary and RSK-005 lowered (OQ-020 accepted). RSK-003 narrowed to availability. OQ-013, OQ-016 (rest of the rows), OQ-017 and OQ-019 stay open. No status promotion by evidence |
