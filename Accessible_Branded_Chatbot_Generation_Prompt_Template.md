# Accessible branded chatbot generation prompt template

Version 1.2 · 24 September 2026 · Paste the completed template into an implementation task and attach the companion *Inclusive Chatbot Interfaces Reference* as retrieval material.

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
| Accessibility and legal baseline | [SELECT APPLICABLE: WCAG 2.2 A/AA; US REVISED SECTION 508; EN 301 549 AND VERSION; EUROPEAN ACCESSIBILITY ACT (DIRECTIVE (EU) 2019/882) AND RELEVANT NATIONAL IMPLEMENTATION; OTHER CONTRACTUAL REQUIREMENTS. STATE JURISDICTION, COVERED SERVICE, OWNER AND EXCEPTIONS] |
| Supported environments | [BROWSERS, DEVICES, SCREEN READERS, INPUT METHODS] |
| Analytics, feedback and privacy | [CONSENT, EVENT POLICY, REGULAR ACCESSIBLE SURVEY CHANNELS AND CADENCE, OPTIONAL SEGMENTATION, RETENTION, OWNERS, DATA RULES] |
| Build and release workflow | [REPOSITORY, CI COMMANDS, DEPLOYMENT ENVIRONMENTS, REVIEW OWNERS] |
| Research access | [RECRUITMENT, PARTICIPANT PAYMENT, APPROVALS, RESEARCH CADENCE] |

## Prompt to the implementing AI

You are designing and implementing an inclusive, branded chatbot within the host application described above. Retrieve the companion **Inclusive Chatbot Interfaces Reference** by section as needed and use the authoritative framework, design system, brand and chosen chat platform documentation supplied above. Treat vendor-specific examples in the reference as conditional. If those sources conflict, identify the conflict, choose a safe implementation within the project’s obligations and document the decision. Never assert that a vendor component is accessible merely because it is supplied by a design system. Confirm its behaviour in the integrated page and the installed version.

**Goal.** Deliver a working chatbot interface for the requested embedded and/or modal variant, aligned with the supplied branding and design system, with understandable messages, recoverable errors and user control. Target WCAG 2.2 A/AA as the default design baseline; additionally assess each selected legal or contractual regime on its own terms. Do not equate WCAG 2.2 with Section 508, EN 301 549 or the EAA, and do not claim a regime applies solely because it is selected as a design reference. Have the responsible organisation establish jurisdiction, scope and applicable version. Label additional inclusive design recommendations separately. Preserve existing SDK transcript navigation and announcement behaviour when it meets the requirement. If an input is unavailable, record an assumption and its impact; request only information that blocks an irreversible or consequential decision, while progressing with reversible work.

### 1. Investigate and specify

1. Inspect existing page landmarks, focus order, responsive layout, components, brand tokens, SDK version, live regions and test infrastructure. Map each proposed chat element to an existing component or document why a new one is needed. Establish whether the chat is embedded, modal or both at each viewport; do not turn an embedded panel into a modal with `aria-modal` alone.
2. Produce a compact architecture and interaction specification: launcher, transcript, message, composer, suggested prompts, status, alert, close/collapse/end/new conversation, feedback, help and handoff. Include a state model covering closed, open, submitting, streaming, complete, interrupted, error, reconnecting and expired.
3. Specify the entry point’s discoverability, purpose and disclosure, semantic name, reading order and initial focus. Specify exactly how focus enters, moves within and leaves each variant. For a real modal, include an accessible name, inert background, contained focus, Escape, visible close, focus restoration and mobile viewport behaviour. For embedded chat, permit normal keyboard exit and leave the host page operable.
4. Define transcript navigation independently from focus transitions. Design navigation through long histories, interactive cards, new message arrival while reading earlier content, return to composer and scroll preservation.
5. Produce an **announcement ownership table** for every event: who renders it, who announces it, politeness, visible wording, focus effect and duplicate-announcement prevention. Cover page invitation, open, send, upload, generation start and completion, answer availability, new messages, connectivity, recoverable errors, urgent alerts and expiry. Assess the SDK’s actual implementation first. Avoid token-by-token speech and forced focus.
6. Define content constraints for readable prompts, responses and error messages, and identify the separately governed accessibility of generated rich media, cards, attachments and downloadable artifacts. Specify safe rendering and links. Record privacy and retention decisions for drafts, transcripts, analytics and model data.
7. Produce a **baseline applicability matrix**: source, version, jurisdiction, covered product or service, applicable provision, implementation implication, evidence and owner. Keep the US Revised Section 508 Standards, the European standard EN 301 549, and the EAA with its relevant national implementation distinct. Where the EAA applies, evaluate its relevant service requirements as well as Annex I Section VII Functional Performance Criteria (FPC). Do not treat the FPC as a general substitute for the more specific Annex I requirements. Seek an accountable legal or compliance decision on unresolved applicability.

### 2. Build

Implement production-ready components and integration code in the specified framework. Use semantic HTML and the design system’s tokens and components where appropriate. Implement the documented focus, navigation, announcement and recovery rules as state-driven behaviour. Support zoom and reflow, keyboard and touch input, forced colours, reduced motion, readable focus and adequate target size. Explain and expose session time limits where applicable. Preserve draft text and task context where permitted. Ensure the chatbot never blocks the host page unless a true modal is open.

Do not guess component APIs, SDK hooks, source locations, authentication or back-end contracts. Inspect linked documentation or local code and record what cannot be implemented without them. Any mocked back end must be identified as a mock in documentation and tests.

### 3. Produce reviewable deliverables

Return all of the following, with file paths or links and enough detail to review:

1. **Implementation:** source code, configuration, component mapping and run/build instructions. State any incomplete integration, assumptions and dependencies.
2. **Approach document:** user tasks; variant decision; baseline applicability matrix; semantic and interaction architecture; focus and transcript navigation flows; notification ownership; SDK behaviours retained or overridden; branding and responsive decisions; AI disclosure; privacy, content boundary, errors and human handoff; known risks and decision log. Provide a requirement-to-code-to-test traceability matrix with stable IDs. Distinguish applicable obligations, technical standards and outcome research themes.
3. **Full test catalogue:** atomic ID, initial state, steps, expected outcome, applicable WCAG 2.2 A/AA criterion and any separately applicable Section 508, EN 301 549 or EAA provision, or additional design rule; mode (automatable, manual assisted, or user research), platform, owner and evidence field. Cover every state and both variants if present. Include positive, negative and recovery paths. Do not infer legal conformity from a survey result.
4. **Automated tests:** static checks, component and browser integration tests, axe-core scans in meaningful interaction states, deterministic focus and DOM assertions, and CI commands. Store failures and `incomplete` results for review. Name what automation cannot verify. Avoid treating an axe pass as proof of conformance.
5. **Manual test script:** keyboard traversal and transcript shortcuts; focus entry/exit/restoration; screen reader spoken order and live notifications; modal inertness; zoom/reflow, text spacing, forced colours and motion; mobile virtual keyboard; timeout, long history, cards, offline/retry, alternate support and regenerated answers. Include AT/browser combinations and a result log format.
6. **User research and survey plan:** tasks for sighted and vision-impaired participants and people with relevant motor, cognitive and literacy needs; success signals for discovery, understanding, task completion, interruption and recovery; regular accessible feedback surveys using the FPC themes below; recruitment, invitation, cadence, question wording, accessible formats, consent, privacy, response bias and synthesis of observed barriers and proposed changes. Synthetic personas may help plan questions but cannot stand in for research with people.
7. **Release and optimisation plan:** baseline metrics, event definitions, accessibility regressions, survey and qualitative feedback, segment definitions, multivariate experiment design, owners, review cadence, issue triage and rollback triggers. Ensure all experiment variants meet the same baseline. Clearly assign accountable people to approve consequential changes.

### 4. Operate in an AI managed pipeline

At each change to chat SDK, framework, design tokens, model output schema or host page, identify affected requirements, rerun relevant automated tests, request the manual and user checks that automated evidence cannot cover, and update the approach document and test catalogue. Use accessible design and code review gates before release. Collect privacy-respecting task and feedback signals; group failures by user barrier, propose hypotheses, prioritise experiments, and compare results with a documented baseline.

Run **regular, accessible feedback surveys** at the cadence set in the project inputs, with a route outside the chatbot for people who cannot use it. Use the eleven FPC in [Annex I Section VII of Directive (EU) 2019/882](https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng) as outcome themes for survey design, not as a claim that surveys are legally mandated or that responses establish conformity. Ask whether people could complete a specific task independently, what made it difficult, what alternative they used and what change would help. Adapt questions to features actually present; offer “not applicable” and “prefer not to say”. Keep invitations and the survey itself keyboard and assistive technology accessible, understandable, optional and free of disruptive time pressure.

| FPC outcome theme | Example survey focus for a chatbot |
| --- | --- |
| Without vision | Could you find, operate and review the conversation without seeing the screen? |
| Limited vision | Could you use the chat with your preferred magnification, contrast and text settings? |
| Without perception of colour | Could you identify message states, errors and actions without relying on colour? |
| Without hearing | If the chat uses sound, could you obtain the same information without hearing it? |
| Limited hearing | If it uses audio, could you understand and control it with your preferred settings or aids? |
| Without vocal capability | If it accepts voice input, could you complete the task without speaking? |
| Limited manipulation or strength | Could you operate the controls without precise movements, strong grip or simultaneous actions? |
| Limited reach | Could you reach the controls using your device and preferred posture or setup? |
| Photosensitive seizure risk | Did flashing or animation prevent comfortable use? Treat any reported trigger as urgent. |
| Limited cognition | Could you understand the options, follow progress, correct errors and finish without undue memory demands? |
| Privacy | Could you use any accessibility features without unwanted disclosure to others? |

Analyse survey answers alongside moderated research, accessibility tests, task analytics and support contacts. Where participants voluntarily describe their interaction needs or preferred modes, use those **self-reported needs** for consented segmentation; do not infer disability, diagnosis or assistive technology from telemetry. Check whether invitations exclude users who abandon early, and report sample sizes, uncertainty and missing groups. Segment by task and context as well as access mode where the data supports it. Use multivariate tests to examine plausible improvements, with accessible variants, predefined success and barrier measures, enough observations for interpretation, and review of adverse results for any segment. Small groups and sensitive attributes require particular privacy safeguards and careful interpretation. Feed findings into prioritised fixes, retest with affected users, update requirements and record outcomes. Keep an auditable record of prompts, retrieved source versions, code changes, test evidence, exceptions and human decisions. Do not automatically ship a change solely on a generated accessibility score.

**Legal source distinction:** [US Revised Section 508 Standards](https://www.access-board.gov/ict/) incorporate WCAG 2.0 A/AA for covered web content; [EN 301 549](https://accessible-eu-centre.ec.europa.eu/content-corner/digital-library/en-3015492021-accessibility-requirements-ict-products-and-services_en) is an ICT accessibility standard; the [EAA](https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng) is a directive implemented in national law. The FPC supplement the EAA's specific Annex I requirements under the conditions stated in Section VII. Record the applicable text and edition for the project instead of assuming these are interchangeable.

**Final response format:** concise implementation summary; files and paths; requirement coverage and test results by method; decisions and source versions; outstanding blockers and named review owners. Distinguish tested outcomes from proposed ones.
