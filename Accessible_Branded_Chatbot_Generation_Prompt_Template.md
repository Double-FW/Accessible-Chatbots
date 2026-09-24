# Accessible branded chatbot generation prompt template

Version 1.1 · 24 September 2026 · Paste the completed template into an implementation task and attach the companion *Inclusive Chatbot Interfaces Reference* as retrieval material.

**Platform rule.** This template works with a bespoke chatbot, Microsoft products or another provider. Complete the platform field before implementation. The reference's Microsoft examples apply only when the named Microsoft product and feature are used. For any other stack, derive the equivalent interaction behaviour from the user outcomes in the reference, inspect the chosen platform's current documentation and integrated behaviour, and document any gaps. Never copy platform-specific keyboard shortcuts, announcement architecture or APIs into a different implementation without evidence.

## Fill in the project inputs

Replace each bracketed field. Use “not supplied” where information is unavailable; do not leave a placeholder that might be mistaken for a requirement.

| Input | Project value |
| --- | --- |
| Organisation and product | [NAME AND PURPOSE] |
| Users and key tasks | [AUDIENCES, TASKS, CONTEXTS, LANGUAGES] |
| Site or application and relevant page links | [HOST PAGES, REPOSITORY, ROUTES] |
| JavaScript framework, version and links | [FRAMEWORK, VERSION, OFFICIAL DOCS, ROUTING, STATE MANAGEMENT, TEST SETUP] |
| UX design system and links | [NAME, VERSION, TOKENS, COMPONENT DOCS, ACCESSIBILITY GUIDANCE] |
| Branding system and links | [NAME, LOGO USAGE, COLOUR, TYPOGRAPHY, VOICE, ICONS] |
| Chat platform, SDK and version | [BESPOKE OR COPILOT STUDIO OR BOT FRAMEWORK WEB CHAT OR OTHER; LINKS] |
| RAG sources and assistant behaviour | [KNOWLEDGE SOURCES, CITATION RULES, PERSONALISATION, PRIVACY, SAFETY, HUMAN HANDOFF] |
| Presentation variant | [EMBEDDED PANEL, MODAL DIALOG, BOTH; BREAKPOINT BEHAVIOUR] |
| Entry point and content | [LAUNCHER PLACEMENT, VISIBLE PURPOSE, AI DISCLOSURE, INITIAL CONTENT] |
| Features | [STREAMING, FILES, VOICE, CARDS, HISTORY, AUTHENTICATION, SESSION LIMITS] |
| Accessibility and legal baseline | [DEFAULT WCAG 2.2 A/AA; CONTRACTUAL REQUIREMENTS AND EXCEPTIONS] |
| Supported environments | [BROWSERS, DEVICES, SCREEN READERS, INPUT METHODS] |
| Analytics, feedback and privacy | [CONSENT, EVENT POLICY, RETENTION, OWNERS, DATA RULES] |
| Build and release workflow | [REPOSITORY, CI COMMANDS, DEPLOYMENT ENVIRONMENTS, REVIEW OWNERS] |
| Research access | [RECRUITMENT, PARTICIPANT PAYMENT, APPROVALS, RESEARCH CADENCE] |

## Prompt to the implementing AI

You are designing and implementing an inclusive, branded chatbot within the host application described above. Retrieve the companion **Inclusive Chatbot Interfaces Reference** by section as needed and use the authoritative framework, design system, brand and chosen chat platform documentation supplied above. Treat vendor-specific examples in the reference as conditional. If those sources conflict, identify the conflict, choose a safe implementation within the project’s obligations and document the decision. Never assert that a vendor component is accessible merely because it is supplied by a design system. Confirm its behaviour in the integrated page and the installed version.

**Goal.** Deliver a working chatbot interface for the requested embedded and/or modal variant, aligned with the supplied branding and design system, with understandable messages, recoverable errors and user control. Target WCAG 2.2 A/AA unless a contractual target is provided; label additional inclusive design recommendations separately. Preserve existing SDK transcript navigation and announcement behaviour when it meets the requirement. If an input is unavailable, record an assumption and its impact; request only information that blocks an irreversible or consequential decision, while progressing with reversible work.

### 1. Investigate and specify

1. Inspect existing page landmarks, focus order, responsive layout, components, brand tokens, SDK version, live regions and test infrastructure. Map each proposed chat element to an existing component or document why a new one is needed. Establish whether the chat is embedded, modal or both at each viewport; do not turn an embedded panel into a modal with `aria-modal` alone.
2. Produce a compact architecture and interaction specification: launcher, transcript, message, composer, suggested prompts, status, alert, close/collapse/end/new conversation, feedback, help and handoff. Include a state model covering closed, open, submitting, streaming, complete, interrupted, error, reconnecting and expired.
3. Specify the entry point’s discoverability, purpose and disclosure, semantic name, reading order and initial focus. Specify exactly how focus enters, moves within and leaves each variant. For a real modal, include an accessible name, inert background, contained focus, Escape, visible close, focus restoration and mobile viewport behaviour. For embedded chat, permit normal keyboard exit and leave the host page operable.
4. Define transcript navigation independently from focus transitions. Design navigation through long histories, interactive cards, new message arrival while reading earlier content, return to composer and scroll preservation.
5. Produce an **announcement ownership table** for every event: who renders it, who announces it, politeness, visible wording, focus effect and duplicate-announcement prevention. Cover page invitation, open, send, upload, generation start and completion, answer availability, new messages, connectivity, recoverable errors, urgent alerts and expiry. Assess the SDK’s actual implementation first. Avoid token-by-token speech and forced focus.
6. Define content constraints for readable prompts, responses and error messages, and identify the separately governed accessibility of generated rich media, cards, attachments and downloadable artifacts. Specify safe rendering and links. Record privacy and retention decisions for drafts, transcripts, analytics and model data.

### 2. Build

Implement production-ready components and integration code in the specified framework. Use semantic HTML and the design system’s tokens and components where appropriate. Implement the documented focus, navigation, announcement and recovery rules as state-driven behaviour. Support zoom and reflow, keyboard and touch input, forced colours, reduced motion, readable focus and adequate target size. Explain and expose session time limits where applicable. Preserve draft text and task context where permitted. Ensure the chatbot never blocks the host page unless a true modal is open.

Do not guess component APIs, SDK hooks, source locations, authentication or back-end contracts. Inspect linked documentation or local code and record what cannot be implemented without them. Any mocked back end must be identified as a mock in documentation and tests.

### 3. Produce reviewable deliverables

Return all of the following, with file paths or links and enough detail to review:

1. **Implementation:** source code, configuration, component mapping and run/build instructions. State any incomplete integration, assumptions and dependencies.
2. **Approach document:** user tasks; variant decision; accessibility baseline; semantic and interaction architecture; focus and transcript navigation flows; notification ownership; SDK behaviours retained or overridden; branding and responsive decisions; AI disclosure; privacy, content boundary, errors and human handoff; known risks and decision log. Provide a requirement-to-code-to-test traceability matrix with stable IDs.
3. **Full test catalogue:** atomic ID, initial state, steps, expected outcome, applicable WCAG 2.2 A/AA criterion or additional design rule, mode (automatable, manual assisted, or user research), platform, owner and evidence field. Cover every state and both variants if present. Include positive, negative and recovery paths.
4. **Automated tests:** static checks, component and browser integration tests, axe-core scans in meaningful interaction states, deterministic focus and DOM assertions, and CI commands. Store failures and `incomplete` results for review. Name what automation cannot verify. Avoid treating an axe pass as proof of conformance.
5. **Manual test script:** keyboard traversal and transcript shortcuts; focus entry/exit/restoration; screen reader spoken order and live notifications; modal inertness; zoom/reflow, text spacing, forced colours and motion; mobile virtual keyboard; timeout, long history, cards, offline/retry, alternate support and regenerated answers. Include AT/browser combinations and a result log format.
6. **User research plan:** tasks for sighted and vision-impaired participants and people with relevant motor, cognitive and literacy needs; success signals for discovery, understanding, task completion, interruption and recovery; consent and privacy approach; synthesis of observed barriers and proposed changes. Synthetic personas may help plan questions but cannot stand in for research with people.
7. **Release and optimisation plan:** baseline metrics, event definitions, accessibility regressions, qualitative feedback, owners, review cadence, issue triage and rollback triggers. Ensure all experiment variants meet the same baseline. Clearly assign accountable people to approve consequential changes.

### 4. Operate in an AI managed pipeline

At each change to chat SDK, framework, design tokens, model output schema or host page, identify affected requirements, rerun relevant automated tests, request the manual and user checks that automated evidence cannot cover, and update the approach document and test catalogue. Use accessible design and code review gates before release. Collect privacy-respecting task and feedback signals; group failures by user barrier, propose hypotheses, prioritise experiments, and compare results with a documented baseline. Keep an auditable record of prompts, retrieved source versions, code changes, test evidence, exceptions and human decisions. Do not automatically ship a change solely on a generated accessibility score.

**Final response format:** concise implementation summary; files and paths; requirement coverage and test results by method; decisions and source versions; outstanding blockers and named review owners. Distinguish tested outcomes from proposed ones.
