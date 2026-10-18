# Register: web-fetch-mcp v1

## Assumptions

| ID | Assumption | Owner | Impact if false | Resolving OQ |
|---|---|---|---|---|
| ASM-001 | The tool identifier is `fetch` (lowercase). S2 writes "Fetch". Tool names are case-sensitive (EV-002). | Stakeholder | Client config and prompts that name the tool break | OQ-011 |
| ASM-002 | An oversized response returns an error. It is not truncated. | Stakeholder | FR-007 behaviour and AC-006 change | OQ-001 |
| ASM-003 | Conversion covers the whole page. Script and style content is dropped. Page text is treated as untrusted data. | Stakeholder | FR-002 and FR-015 change | OQ-004 |
| ASM-004 | Static HTML only. The server runs no JavaScript. | Stakeholder | Pages that render client-side return little content | OQ-005 |
| ASM-005 | The server keeps no cache and persists no page content. | Stakeholder | Data retention and privacy requirements are added | OQ-012 |
| ASM-006 | Consent for each tool call is handled by the host (Claude Code). The server adds no confirmation step. EV-001 states hosts must obtain consent before invoking any tool. | Stakeholder | Server needs its own oversight controls | OQ-012 |

## Open Questions

| ID | Severity | Question | Options (default first) | Owner | Affects |
|---|---|---|---|---|---|
| OQ-001 | BLOCKING | What is the maximum response size? | 5 MB; 1 MB; 10 MB | Stakeholder | FR-007, GLO-004, AC-006 |
| OQ-002 | BLOCKING | What counts as private and internal? | Non-public IP ranges (loopback, RFC 1918, link-local, unique-local) checked on the resolved address, plus single-label names and suffixes `.local`, `.internal`, `.lan`, `.localdomain`; or IP ranges only; or an operator-configured deny list | Stakeholder | FR-003, FR-004, GLO-002, GLO-003 |
| OQ-003 | BLOCKING | How are redirects and DNS results handled? | Follow up to 5 redirects and re-check each target and resolved address; reject all redirects; follow redirects without re-checking | Stakeholder | FR-014, RSK-001 |
| OQ-004 | HIGH | Which response content types does `fetch` convert? | `text/html` and `text/plain`, others return an error; `text/html` only; any `text/*` plus JSON | Stakeholder | FR-002, FR-015, ASM-003 |
| OQ-005 | MEDIUM | Does `fetch` need JavaScript rendering? | No, static HTML only; yes | Stakeholder | ASM-004 |
| OQ-006 | HIGH | Which MCP revision and Claude Code version must the server support? | Both the current per-request revision and the earlier `initialize` revision; current only; earlier only | Stakeholder | FR-012, DEP-001, DEP-002, RSK-003 |
| OQ-007 | MEDIUM | What are the timeout, performance and availability targets? S8 defers them. | 30 s request timeout, no other target; 10 s; 60 s | Stakeholder | FR-006, FR-010, FR-017, NFR-002, NFR-003 |
| OQ-008 | LOW | Are plain `http` URLs rejected? | Reject; allow | Stakeholder | FR-016 |
| OQ-009 | MEDIUM | What is the rate limit? EV-002 says servers MUST rate limit. | 60 calls per minute; 30; 120 | Stakeholder | FR-013 |
| OQ-010 | MEDIUM | Which requirements are Must for the initial release? | FR-001 to FR-008, FR-011, FR-012, NFR-001 Must; the rest Should | Stakeholder | All |
| OQ-011 | LOW | Is the tool identifier `fetch` or `Fetch`? | `fetch`; `Fetch` | Stakeholder | FR-001, ASM-001 |
| OQ-012 | LOW | Are caching, URL logging and extra oversight needed? | No cache, no persistence, host handles consent; add a cache; add server-side confirmation | Stakeholder | ASM-005, ASM-006 |

No-answer impact: OQ-001, OQ-002 and OQ-003 keep FR-003, FR-004, FR-007 and FR-014 unfinished and block IMPLEMENTATION_READY. Other questions fall back to the default as a labelled assumption.
