# SRS: Multi-Tenant Web Document Editor (multitenant-doc-editor) v1

Date: 2026-10-18. Verdict: NOT_READY (see VALIDATION_multitenant-doc-editor_v1.md).

## Purpose

A multi-tenant web document editor for 1 million registered users. The stakeholder fixes scale targets and four mechanisms (sharding, optimistic concurrency, idempotent writes, asynchronous replication) and requires load tests and fault injection to validate the performance targets. This round records what was stated and what is missing. It contains no design, code or estimates.

## Sources

The problem statement is one sentence. It is split into clauses so each item can cite an anchor:

* S1: Build a multi-tenant web document editor for 1 million registered users, supporting 10,000 concurrent users and 2,000 read/write requests per second, using database sharding, optimistic concurrency control, idempotent writes, and asynchronous replication, with performance targets validated through load tests and fault injection.
  * S1.1 multi-tenant web document editor
  * S1.2 1 million registered users
  * S1.3 10,000 concurrent users
  * S1.4 2,000 read/write requests per second
  * S1.5 database sharding
  * S1.6 optimistic concurrency control
  * S1.7 idempotent writes
  * S1.8 asynchronous replication
  * S1.9 performance targets validated through load tests and fault injection

Evidence: EV-001 (IETF datatracker, retrieved 2026-10-18).

## Glossary

| ID | Term | Definition | Status |
|---|---|---|---|
| GLO-001 | document | UNRESOLVED (content model, size) | OQ-002 |
| GLO-002 | multi-tenant | UNRESOLVED (what a tenant is, isolation level) | OQ-005 |
| GLO-003 | concurrent users | UNRESOLVED (active sessions or in-flight requests) | OQ-009 |
| GLO-004 | read/write requests per second | UNRESOLVED (total or per type, sustained or peak, read:write ratio) | OQ-009 |
| GLO-005 | performance targets | UNRESOLVED (S1 names no latency or error limit) | OQ-003 |
| GLO-006 | optimistic concurrency control | A write succeeds only if the document version the client read is still current; otherwise it is rejected | INFERRED |
| GLO-007 | idempotent write | Repeating a write with the same key changes state once and returns the first result | INFERRED |
| GLO-008 | asynchronous replication | A write is acknowledged before replicas have applied it | INFERRED |

## Actors

| ID | Role | Goal | Status |
|---|---|---|---|
| ACT-001 | Registered user | Read and edit documents | STATED S1.1, S1.2 |
| ACT-002 | Tenant (organization) | Keep its users and documents separate from other tenants | INFERRED from S1.1 |
| ACT-003 | Operator | Run load tests and fault injection and read the results | INFERRED from S1.9 |

## Functional Requirements

Priority is UNPRIORITIZED for every row (OQ-014).

| ID | Statement | Status | Readiness | Feas | Trace | AC |
|---|---|---|---|---|---|---|
| FR-001 | The system shall provide a web interface in which a registered user reads and edits documents. | STATED | NEEDS_CLARIFICATION | UNVERIFIED | S1.1, GLO-001, OQ-001, OQ-002 | pending: OQ-002 |
| FR-002 | The system shall give a tenant's users access to that tenant's documents only. | INFERRED | NEEDS_CLARIFICATION | UNVERIFIED | S1.1, GLO-002, OQ-005, OQ-006 | pending: OQ-005 |
| FR-003 | When an update is submitted with a document version that is no longer current, the system shall reject the update with a conflict result and leave the stored document unchanged. | STATED | NEEDS_CLARIFICATION | AT_RISK (RSK-003) | S1.6, GLO-006, OQ-001 | AC-001 |
| FR-004 | When a write repeats an earlier write with the same idempotency key, the system shall return the first result and shall not apply the write again. | STATED | NEEDS_CLARIFICATION | AT_RISK (RSK-004) | S1.7, GLO-007, EV-001, ASM-004, OQ-010 | AC-002 (pending: OQ-010) |
| FR-005 | The system shall define what a reader sees after a write, given asynchronous replication. | UNRESOLVED | NEEDS_CLARIFICATION | AT_RISK (RSK-001) | S1.8, OQ-007 | pending: OQ-007 |
| FR-006 | The system shall let a user register and sign in. | UNRESOLVED | NEEDS_CLARIFICATION | UNVERIFIED | S1.2, OQ-004 | pending: OQ-004 |
| FR-007 | The system shall be validated against its performance targets by load tests and by fault-injection tests before release. | STATED | NEEDS_CLARIFICATION | AT_RISK (RSK-005) | S1.9, GLO-005, OQ-003, OQ-011 | AC-003 (pending: OQ-003) |

## Non-Functional Requirements

| ID | Category | Statement | Status | Readiness | Trace | AC |
|---|---|---|---|---|---|---|
| NFR-001 | Capacity | The system shall support 1,000,000 registered users. | STATED | NEEDS_CLARIFICATION | S1.2, OQ-012 | AC-004 (pending: OQ-003) |
| NFR-002 | Capacity | The system shall support 10,000 concurrent users. | STATED | NEEDS_CLARIFICATION | S1.3, GLO-003, ASM-001, OQ-009 | pending: OQ-009 |
| NFR-003 | Performance | The system shall sustain 2,000 read/write requests per second. | STATED | NEEDS_CLARIFICATION | S1.4, GLO-004, ASM-002, OQ-009 | pending: OQ-009 |
| NFR-004 | Performance | Latency and error-rate limits at the NFR-003 load. | UNRESOLVED | NEEDS_CLARIFICATION | S1.9, OQ-003 | pending: OQ-003 |
| NFR-005 | Availability | Availability target. | UNRESOLVED | NEEDS_CLARIFICATION | OQ-008 | pending: OQ-008 |
| NFR-006 | Durability | Data-loss and recovery limits, given asynchronous replication. | UNRESOLVED | NEEDS_CLARIFICATION | S1.8, OQ-008 | pending: OQ-008 |
| NFR-007 | Security, privacy, compliance | Obligations for tenant and user data. | UNRESOLVED | NEEDS_CLARIFICATION | OQ-006 | pending: OQ-006 |

## Constraints

| ID | Type | Statement | Source |
|---|---|---|---|
| CON-001 | Data | The database shall be sharded. Shard key is not stated | S1.5 |
| CON-002 | Data | Replication shall be asynchronous | S1.8 |
| CON-003 | Verification | Targets shall be validated by load tests and fault injection | S1.9 |

## Dependencies

| ID | Target | Owner |
|---|---|---|
| DEP-001 | Load-test and fault-injection environment and tooling (unspecified) | Stakeholder, OQ-015 |
| DEP-002 | Idempotency-key convention. The IETF `Idempotency-Key` header is an expired draft, not a standard (EV-001) | Stakeholder, OQ-010 |

## Risks

| ID | Risk | Likelihood | Impact | Affects |
|---|---|---|---|---|
| RSK-001 | Asynchronous replication gives stale reads and can lose acknowledged writes when a primary fails | Not assessed | High | FR-005, NFR-006 |
| RSK-002 | Uneven tenant sizes overload one shard and miss NFR-003 | Not assessed | High | NFR-003, CON-001 |
| RSK-003 | Frequent rejected updates under contention frustrate users or look like lost edits | Not assessed | Medium | FR-003 |
| RSK-004 | The idempotency record store grows without a retention rule or becomes a hot spot | Not assessed | Medium | FR-004 |
| RSK-005 | Load tests and fault injection have no pass or fail threshold, so they cannot validate anything | Not assessed | High | FR-007, NFR-004 |

Likelihood is not assessed because no stakeholder or evidence supports a rating.

## Traceability

Acceptance criteria:

| ID | Parent | Method | Pass threshold |
|---|---|---|---|
| AC-001 | FR-003 | Submit two updates with the same base version at the same time, repeat across the concurrency test | Exactly 1 applied and 1 rejected as conflict; 0 lost updates; 0 double applies |
| AC-002 | FR-004 | Send the same write with one key sequentially and in parallel | 1 state change; all replies identical; key retention pending OQ-010 |
| AC-003 | FR-007 | Run load tests at NFR-003 load and fault-injection tests from the OQ-011 list | pending: OQ-003 (no pass limits stated) |
| AC-004 | NFR-001 | Seed 1,000,000 registered users and run the AC-003 scenario | pending: OQ-003 |

Trace summary: every FR, NFR and CON traces to an anchor, ASM, OQ or EV. Every AC has one parent. No orphan IDs.

## Change log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-10-18 | First draft from the problem statement; one evidence record |
