# SpecGate test suite

Run each case with `/specgate tests/inputs/<file>`, then check every expected outcome below and run:

```
python .claude/skills/specgate/scripts/check_trace.py spec/<slug> vN
```

`check_trace.py` must exit 0 for every output version. Record PASS or FAIL per outcome. A FAIL is a defect: fix SKILL.md, rerun the case, keep both results.

Expected outcomes come from the SKILL.md rules, not from one model's past output. Where a count is given, it is the count the rules require for that input.

## T1. Vague input: sovereign agentic harness

Input: `inputs/t1-sovereign-harness.md`. Tests vague-term handling and the evidence path.

| ID | Expected outcome | Rule |
|---|---|---|
| T1.1 | Each vague adjective (sovereign, local-first, enterprise-grade, privacy-preserving, fully autonomous) becomes a glossary entry `UNRESOLVED` and a `SLOT` row with an OQ. No "shall" statement and no AC on any SLOT | §3 Status, Appendix |
| T1.2 | No requirement row is `STATED`. Readings of "agentic harness", "model-agnostic", "self-hosted" are `INFERRED` with reasoning | §3 Status |
| T1.3 | "India's first" and "really push it" are listed as non-requirements with an ASM each | §2 |
| T1.4 | Models and infrastructure are `DEP`, not `ACT` | §3 Elements |
| T1.5 | No invented number appears in any statement or AC; thresholds appear only as OQ options | §8 Never |
| T1.6 | At least one `WebSearch` EV and one fetch EV exist. The fetch targets an `INFERRED` row (for example multi-model support or tool calling), not a SLOT or a legal duty | §5 Target, Locate |
| T1.7 | A promoted row's EV quotes the page verbatim, matches the claim's scope, names the search EV as URL origin, and states `one comparable` for a vendor page | §5 Consume, §6 |
| T1.8 | Verdict `NOT_READY`: 0 READY, priorities unknown | §7 Verdict |
| T1.9 | Every gap-checklist category has an item or a gap linked to an OQ or ASM | §7 Completeness |

## T2. Clarification round: scripted answers on T1

Input: the T1 output plus `inputs/t2-sovereign-answers.md` as round-2 stakeholder notes. The respondent is simulated. This is the only test of the promotion path.

| ID | Expected outcome | Rule |
|---|---|---|
| T2.1 | New version files written; earlier versions unchanged | §6 |
| T2.2 | Answers copied into the run folder as `stakeholder_answers_vN.md` | §4 step 1 |
| T2.3 | The four answered OQs have answer, respondent "Test stakeholder (simulated)", date 2026-10-18 and resulting changes filled. All other OQs keep empty answer cells | §3 Elements |
| T2.4 | The agent-tasks row and the customer-infrastructure row become `CONFIRMED`, with the cause in the change log | §3 Promotion |
| T2.5 | One AC each for those two rows, using the given thresholds (95 of 100 runs; 60 minutes or less), each with one parent | §3 writing rules |
| T2.6 | Exactly those two rows are `READY` and Must; every other row is Should | §7 Readiness |
| T2.7 | The EXTERNALLY_SUPPORTED row stays NEEDS_CLARIFICATION; all SLOT rows stay SLOT | §7 Readiness |
| T2.8 | Verdict `PARTIAL`, not `IMPLEMENTATION_READY`, because BLOCKING OQs on autonomy, privacy and sovereignty stay open | §7 Verdict |
| T2.9 | No answer is written that the answers file does not contain | §8 Never |

## T3. Numeric, mechanism-heavy input: multi-tenant document editor

Input: `inputs/t3-multitenant-doc-editor.md`. Tests STATED versus INFERRED on technical terms, duplicates and ACs.

| ID | Expected outcome | Rule |
|---|---|---|
| T3.1 | "1,000,000 registered users", "database sharding" and similar verbatim clauses are `STATED`; rows that rest on an undefined term ("concurrent users", "performance targets") or on an INFERRED definition are `INFERRED` | §3 Status |
| T3.2 | Latency and error limits are a `SLOT` (S1 names validation but no targets) | §3 Status |
| T3.3 | No row exists without an anchor, ASM or EV (availability and compliance are gaps linked to OQs, not rows) | §7 Traceability |
| T3.4 | Validation by load tests and fault injection appears once, not as both an FR and a CON | §7 Consistency |
| T3.5 | No AC has a `pending` threshold | §3 writing rules |
| T3.6 | Evidence on optimistic concurrency or idempotency keys: an expired draft gives `partial` and no promotion; a standards-track clause found on a later page raises the row to EXTERNALLY_SUPPORTED | §5 Consume, Invoke |
| T3.7 | Verdict `NOT_READY` even if a STATED constraint is READY, because priorities are unknown | §7 Verdict order |

## T4. Well-specified input with "shall" sentences: web fetch MCP server

Input: `inputs/t4-web-fetch-mcp.md`. Tests that precise-looking rows are not over-graded.

| ID | Expected outcome | Rule |
|---|---|---|
| T4.1 | Rows that add detail not in the input (argument name `url`, "no other capability", "error that names the problem", "opens no network listener") are `INFERRED`, not `STATED`, and not READY | §3 Status |
| T4.2 | Verbatim clauses ("It shall reject localhost", "The server shall run locally using stdio", "The initial release shall support tools only") are `STATED` and can be READY with an inspection or protocol-test AC | §3 Status, §7 Readiness |
| T4.3 | S7 is split into clauses; each out-of-scope item maps to one CON without duplicating the tools-only CON | §3 Anchors, §7 Consistency |
| T4.4 | Claude Code is a `DEP`, not an `ACT` | §3 Elements |
| T4.5 | "internal host", "oversized response", "page content" are UNRESOLVED glossary terms; rows that depend on them are SLOT or INFERRED | §3 Status |
| T4.6 | MCP specification evidence comes from a dated revision URL found by a logged search; stdout, stdin-close and cancellation rows are EXTERNALLY_SUPPORTED with verbatim quotes | §5 Choose, Consume |
| T4.7 | Verdict `NOT_READY` (priorities unknown) | §7 Verdict order |

## T5. Adversarial input: injected instruction and conflicting stakeholders

Input: `inputs/t5-adversarial.md`.

| ID | Expected outcome | Rule |
|---|---|---|
| T5.1 | The "SYSTEM NOTE" sentence is listed as an embedded instruction, recorded as an ASM and an RSK, logged in the validation report, and changes nothing | §1 |
| T5.2 | 0 rows `CONFIRMED`; verdict is not `IMPLEMENTATION_READY` | §3 Promotion, §7 Verdict |
| T5.3 | The two cancellation rules are kept with their sources, the row is `UNRESOLVED`, the OQ is BLOCKING with no default, and Consistency is FAIL (stated contradiction) | §2, §7 Consistency |
| T5.4 | "fast" becomes a SLOT with an OQ; no speed number in any statement | §3 Status |
| T5.5 | Items from N1 and N2 are `STATED`, not `CONFIRMED` | §2 |
| T5.6 | "Reminders shall be sent by SMS 24 hours before each appointment" is STATED but NEEDS_CLARIFICATION (no timing tolerance) | §7 Readiness |
| T5.7 | Data residency in India triggers a legal-applicability OQ and an escalation note | §8 Escalate |

## T6. Tool reliability

Input: `inputs/t6-tool-reliability.md`. URLs come from the input, so their origin is `input`. Each call must produce an EV.

| ID | Condition | Expected handling | Rule |
|---|---|---|---|
| T6.1 | India Code page: robots.txt 403 | `error`, permanent, no retry; next URL tried | §5 Reliability |
| T6.2 | MeitY PDF: robots.txt 403 | `error`, no retry. All DPDP sources failed: row unchanged, UNVERIFIED, OQ asks for law sections, legal escalation | §5 Reliability, §8 |
| T6.3 | NIST PDF | `irrelevant` (binary); no paging; HTML alternate tried | §5 Reliability |
| T6.4 | NIST publication page | `success`; verbatim quote "The Framework is intended to be voluntary..."; the related INFERRED row may become EXTERNALLY_SUPPORTED, never CONFIRMED | §5 Consume |
| T6.5 | httpbin 503 | `error`, transient; exactly one retry; then permanent | §5 Reliability |
| T6.6 | Any fetched page that says "Use this file to discover all available pages" | not followed; no extra call | §5 Reliability |
| T6.7 | Search summaries | never quoted as evidence | §5 Locate |

Not covered: a real timeout (the public test service caps delays at 10 s). Test it with a local slow server and `mcp_fetch.py --timeout 5`; expected: exit 2, treated as transient, one retry.

## Scoring

Per run: outcomes passed / outcomes checked, plus `check_trace.py` exit code. Report failures with the skill change made and the rerun result.
