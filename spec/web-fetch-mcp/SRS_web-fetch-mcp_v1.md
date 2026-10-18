# SRS: Local Web Fetch MCP Server (web-fetch-mcp) v1

Date: 2026-10-18. Verdict: PARTIAL (see VALIDATION_web-fetch-mcp_v1.md).

## Purpose

A local MCP server that gives AI coding agents web page retrieval. It exposes one tool that fetches a public HTTPS page and returns Markdown, runs over stdio, and is used from Claude Code. Initial release: tools only.

## Sources

Problem statement, numbered sentences:

* S1: Build a local MCP server that provides web page retrieval to AI coding agents.
* S2: The server shall expose a Fetch tool that accepts a public HTTPS URL and returns the page content as Markdown.
* S3: It shall reject localhost, private IP addresses, and internal hosts.
* S4: The server shall run locally using stdio and be usable by Claude Code.
* S5: It shall handle invalid URLs, network failures, and oversized responses without crashing.
* S6: The initial release shall support tools only.
* S7: Authentication, remote deployment, and additional MCP capabilities are out of scope for the initial release.
* S8: Performance and availability targets are yet to be defined.

Evidence: EV-001 to EV-004 (modelcontextprotocol.io specification, retrieved 2026-10-18).

## Glossary

| ID | Term | Definition | Status |
|---|---|---|---|
| GLO-001 | public HTTPS URL | Absolute URL with scheme `https` whose host resolves only to public addresses | INFERRED (from S2, S3) |
| GLO-002 | private IP address | Loopback, RFC 1918, link-local, unique-local and similar non-public ranges. Exact list pending | INFERRED, OQ-002 |
| GLO-003 | internal host | UNRESOLVED | OQ-002 |
| GLO-004 | oversized response | UNRESOLVED (no byte limit stated) | OQ-001 |
| GLO-005 | network failure | DNS failure, connection refused or reset, TLS failure, timeout | INFERRED, OQ-007 |
| GLO-006 | page content | UNRESOLVED (full page or main content; content types) | OQ-004 |
| GLO-007 | crash | Server process exits, or stops answering later requests, because of a request | INFERRED |

## Actors

| ID | Role | Goal | Status |
|---|---|---|---|
| ACT-001 | AI coding agent | Retrieve a public web page as Markdown | STATED S1 |
| ACT-002 | Claude Code (MCP host) | Launch the server over stdio and call its tool | STATED S4 |

## Functional Requirements

Priority is UNPRIORITIZED for every row (no stakeholder priority given, OQ-010).

| ID | Statement | Status | Readiness | Feas | Trace | AC |
|---|---|---|---|---|---|---|
| FR-001 | The server shall expose one tool named `fetch` that takes a required string argument `url`. | STATED | READY | FEASIBLE | S2, S6, EV-002, ASM-001 | AC-001 |
| FR-002 | When `fetch` is called with a valid public HTTPS URL, the server shall return the page content as Markdown in a text content block. | STATED | NEEDS_CLARIFICATION | AT_RISK (RSK-002) | S2, OQ-004 | AC-002 |
| FR-003 | If the URL host is `localhost` or is, or resolves to, a private IP address, then the server shall return a tool execution error and shall make no request to that address. | STATED | NEEDS_CLARIFICATION | AT_RISK (RSK-001) | S3, GLO-002, OQ-002 | AC-003 |
| FR-004 | If the URL host is an internal host, then the server shall return a tool execution error. | UNRESOLVED | NEEDS_CLARIFICATION | AT_RISK (RSK-001) | S3, OQ-002 | pending: OQ-002 |
| FR-005 | If the `url` value is not a parseable absolute URL, then the server shall return a tool execution error that names the problem. | STATED | READY | FEASIBLE | S5, EV-002 | AC-004 |
| FR-006 | If a network failure occurs while fetching, then the server shall return a tool execution error that names the failure category. | STATED | NEEDS_CLARIFICATION | UNVERIFIED | S5, GLO-005, OQ-007 | AC-005 (pending: OQ-007) |
| FR-007 | If the response exceeds the size limit, then the server shall stop reading it and return a tool execution error. | STATED | NEEDS_CLARIFICATION | FEASIBLE (RSK-004) | S5, GLO-004, ASM-002, OQ-001 | AC-006 (pending: OQ-001) |
| FR-008 | The server shall run as a local process that speaks MCP over stdio and opens no network listener. | STATED | READY | FEASIBLE | S4, CON-001, EV-003 | AC-007 |
| FR-009 | The server shall write only valid MCP messages to stdout and shall send any logs to stderr. | EXTERNALLY_SUPPORTED | NEEDS_CLARIFICATION | FEASIBLE | S4, EV-003 | AC-008 |
| FR-010 | When its standard input closes, the server shall exit. | EXTERNALLY_SUPPORTED | NEEDS_CLARIFICATION | FEASIBLE | EV-003 | AC-009 (pending: OQ-007) |
| FR-011 | The server shall declare the `tools` capability and no other server capability. | STATED | READY | FEASIBLE | S6, S7, EV-001, EV-002 | AC-010 |
| FR-012 | The server shall be registrable in Claude Code with `claude mcp add` and callable by the agent. | STATED | NEEDS_CLARIFICATION | AT_RISK (RSK-003) | S4, DEP-001, OQ-006 | AC-011 (pending: OQ-006) |
| FR-013 | The server shall rate limit `fetch` invocations. | EXTERNALLY_SUPPORTED | NEEDS_CLARIFICATION | UNVERIFIED | EV-002, OQ-009 | pending: OQ-009 |
| FR-014 | When a response is a redirect, the server shall apply FR-003, FR-004 and FR-016 to the redirect target before following it. | INFERRED | NEEDS_CLARIFICATION | AT_RISK (RSK-001) | RSK-001, OQ-003 | pending: OQ-003 |
| FR-015 | The server shall define which response content types it converts and how it treats active or hidden content. | UNRESOLVED | NEEDS_CLARIFICATION | AT_RISK (RSK-002) | EV-002, OQ-004 | pending: OQ-004 |
| FR-016 | If the URL scheme is not `https`, then the server shall return a tool execution error. | INFERRED | NEEDS_CLARIFICATION | FEASIBLE | S2, CON-004, OQ-008 | AC-012 (pending: OQ-008) |
| FR-017 | When the client cancels an in-flight `fetch`, the server shall stop work and send no further message for that request. | EXTERNALLY_SUPPORTED | NEEDS_CLARIFICATION | UNVERIFIED | EV-003, OQ-007 | AC-013 (pending: OQ-007) |

## Non-Functional Requirements

| ID | Category | Statement | Status | Readiness | Trace | AC |
|---|---|---|---|---|---|---|
| NFR-001 | Reliability | The server shall stay running and answer the next valid request after every error case in FR-003, FR-005, FR-006 and FR-007. | STATED | READY | S5, GLO-007 | AC-014 |
| NFR-002 | Performance | UNRESOLVED. S8 defers targets. | UNRESOLVED | NEEDS_CLARIFICATION | S8, OQ-007 | pending: OQ-007 |
| NFR-003 | Availability | UNRESOLVED. S8 defers targets. | UNRESOLVED | NEEDS_CLARIFICATION | S8, OQ-007 | pending: OQ-007 |

## Constraints

| ID | Type | Statement | Source |
|---|---|---|---|
| CON-001 | Transport | stdio only | S4 |
| CON-002 | Scope | Tools only. No resources, prompts or other MCP capabilities in the initial release | S6, S7 |
| CON-003 | Scope | No authentication and no remote deployment in the initial release | S7 |
| CON-004 | Input | Public HTTPS URLs only | S2 |

## Dependencies

| ID | Target | Owner |
|---|---|---|
| DEP-001 | Claude Code as MCP host (version unspecified) | Anthropic |
| DEP-002 | MCP specification revision to implement (unspecified, OQ-006) | MCP project |

## Risks

| ID | Risk | Likelihood | Impact | Affects |
|---|---|---|---|---|
| RSK-001 | Host checks bypassed through redirects or DNS that resolves to a private address, giving server-side request forgery | Not assessed | High | FR-003, FR-004, FR-014 |
| RSK-002 | Fetched page text carries instructions aimed at the agent (prompt injection) | Not assessed | High | FR-002, FR-015 |
| RSK-003 | The current specification revision uses per-request metadata with no `initialize` handshake. Claude Code may expect the older revision. EV-004 describes fallback between the two. | Not assessed | High | FR-012, DEP-002 |
| RSK-004 | Memory use grows if size is checked after the full body is read | Not assessed | Medium | FR-007 |

Likelihood is not assessed because no stakeholder or evidence supports a rating.

## Traceability

Acceptance criteria (parent in brackets):

| ID | Parent | Method | Pass threshold |
|---|---|---|---|
| AC-001 | FR-001 | Protocol test: `tools/list` | Exactly 1 tool named `fetch`; `inputSchema` requires string `url` |
| AC-002 | FR-002 | pending: OQ-004 | pending: OQ-004 |
| AC-003 | FR-003 | Call with `https://localhost/`, `https://127.0.0.1/`, `https://[::1]/`, `https://10.0.0.1/`, `https://172.16.0.1/`, `https://192.168.1.1/`, `https://169.254.169.254/`, and a name that resolves to 127.0.0.1 | 100% return `isError: true`; 0 outbound connections to non-public addresses. Range list pending OQ-002 |
| AC-004 | FR-005 | Call with `""`, `not a url`, `https://`, `ftp://example.com` | Each returns `isError: true`; next valid request is answered |
| AC-005 | FR-006 | Simulate DNS failure, refused connection, bad TLS certificate, stalled server | `isError: true` with category; time limit pending OQ-007 |
| AC-006 | FR-007 | Serve a body above the limit | `isError: true`; reading stopped; limit pending OQ-001 |
| AC-007 | FR-008 | Launch via stdio, send `tools/list`, list open sockets | Response on stdout; 0 listening sockets |
| AC-008 | FR-009 | Capture stdout across the full test suite | 100% of stdout lines parse as MCP messages |
| AC-009 | FR-010 | Close stdin | Process exits; time limit pending OQ-007 |
| AC-010 | FR-011 | Inspect the capability declaration | Contains `tools` and no other capability key |
| AC-011 | FR-012 | `claude mcp add`, `claude mcp list`, agent calls `fetch` on a public page | All three succeed; Claude Code version pending OQ-006 |
| AC-012 | FR-016 | Call with `http://example.com` and `ftp://example.com` | `isError: true`; `http` case pending OQ-008 |
| AC-013 | FR-017 | Send `notifications/cancelled` during a slow fetch | No further message for that request; time limit pending OQ-007 |
| AC-014 | NFR-001 | Run every error case of AC-003 to AC-006 | 0 process exits; 100% of following valid requests answered |

Trace summary: every FR, NFR and CON traces to an anchor, ASM, or EV (see Trace columns). No orphan IDs.

## Change log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-10-18 | First draft from the problem statement; evidence gathered from the MCP specification |
