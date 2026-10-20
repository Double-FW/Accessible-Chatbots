Accessible chatbot delivery methodologies

Design, engineering and governance guidance

Version 1.0 | 19 October 2026 | Companion: Accessible Chatbot Testing Brief

# 1\. Purpose and delivery outcome

An accessible chatbot enables people to discover support, ask a question, understand the response, check earlier information, correct mistakes and complete their task using their preferred way of interacting. The quality of the surrounding website, authentication, generated content and handoff service is part of that experience. A usable composer inside an otherwise inaccessible journey is insufficient.

This guidance translates the Double FW Accessible Chatbots repository into a delivery method for product owners, designers, content specialists, engineers, testers and service teams. It applies to bespoke implementations and vendor platforms. Microsoft-specific behaviours are conditional examples, not requirements for other platforms. The companion testing brief gives executable scenarios and observable outcomes. Requirement IDs M01–M16 connect the two documents.

Use three distinct classifications. A baseline requirement is an applicable WCAG 2.2 Level A or AA requirement. A delivery requirement is an additional behaviour adopted for this chatbot, such as preserving reading position. A research target is an outcome to validate with users, such as finding help without prompting. Passing a research target does not establish conformance, and a conformance result does not establish that a task is usable.

# 2\. M01 — Define scope, responsibilities and evidence

Start with the tasks people need to accomplish, including when they are tired, distracted, using a small screen, unable to speak, or working with limited connectivity. Include disabled people in discovery and prototype evaluation. Ask about interaction needs and task barriers rather than requiring diagnoses. Do not assume one participant represents every person using the same assistive technology.

Record the host pages, routes, languages, framework, design system, chat SDK and installed versions. Identify embedded, floating non-modal and modal presentations, including any breakpoint-dependent change. Inventory streaming, suggested prompts, interactive cards, voice, uploads, downloads, account access, saved history, time limits and human handoff. Mark absent features explicitly; do not leave their accessibility ownership unresolved.

Create an applicability record for WCAG 2.2 A/AA and any contractual or jurisdiction-specific obligations. Record each source, edition, covered service, owner, evidence and decision. Section 508, EN 301 549 and the European Accessibility Act are distinct instruments. Do not infer applicability or legal conformity from a WCAG score. The responsible organisation must resolve its applicable obligations and versions before a conformity claim.

The product owner owns the scope and release decision. UX owns interaction and recovery behaviour. Content design owns prompts, explanations and error wording. Engineering owns semantics, state, rendering and integration. QA owns reproducible coverage and results. Research owns recruitment, consent and interpretation. An accessibility specialist or a suitably qualified reviewer challenges decisions and evidence. Assign named people even when roles are combined; an AI agent cannot be the accountable approver.

For each requirement retain: ID, user outcome, trigger, applicable presentation, classification, criterion where relevant, implementation owner, component or code location, test IDs, evidence, status and review date. Record a rationale for exceptions and a remediation owner. Never count an unresolved question as a pass.

# 3\. M02 — Design complete interactions before implementation

Prepare both visual and nonvisual interaction specifications. A screenshot alone cannot describe message announcements, focus destinations or what a user encounters when navigating by headings. For every component specify its visible label, accessible name, role, state, reading position, keyboard behaviour, touch behaviour, announcement and error response. Reuse design-system components only after checking the installed component within the integrated page.

Describe a state model: closed; ready; submitting; generating; complete; stopped; failed; reconnecting; session warning; expired; and human handoff where offered. Separate the message delivery state from answer generation and session state. A sent message can coexist with a failed response; a reopened panel can contain an ongoing conversation. Preserve stable message identifiers so an update does not become an apparently new message.

Define transitions before adding event handlers. Sending creates one pending user message; server acknowledgement changes its delivery state; answer generation exposes progress; completion makes the answer available; failure provides recovery. Stopping generation labels partial content and ends the loading state. Closing the panel does not silently end the session. End conversation, clear history and start new conversation need distinct labels and consequences.

Design review must consider waiting, mistakes and interruptions with the same care as success. The handover should include a component inventory, state-transition record, focus map, announcement ownership map, content examples, responsive layouts and acceptance criteria.

# 4\. M03 — Provide a discoverable and controllable entry point

Use a real button with a clear purpose, for example "Open support chat". Put it in a predictable visual and document location. Do not make a floating icon the only explanation of what the service does. State that the service is automated, what it can help with and how to obtain other support. Do not claim human availability where there is none.

The launcher must remain usable at enlarged text sizes and must not cover essential host-page controls. Opening is deliberate: no focus theft, automatic speech or unexpected modal on arrival. If a contextual invitation is necessary, make it dismissible, avoid repeated invitations after dismissal and prevent it obscuring the task. A static launcher needs no live announcement.

For an expandable embedded panel expose the expanded state and a reliable relationship to the panel. Name the chat using its visible heading. Use a landmark only where it helps orientation. When collapsed, remove hidden controls from both keyboard navigation and the accessibility tree. Distinguish collapse from ending or deleting the conversation.

# 5\. M04 — Choose the correct container and focus behaviour

An embedded or floating non-modal chatbot leaves the host page usable. Users must be able to Tab into and out of it. It must not declare itself modal or make the rest of the page inert. On opening, specify whether focus remains on the launcher or moves to a useful heading or composer. Choose through task and user evaluation, then make the behaviour consistent.

A genuine modal is a temporary, exclusive interaction. Prefer the native dialog element opened with showModal() where supported by the chosen environment, or implement the full modal pattern. Give it a name from its visible title, move focus inside, make the outside page inert, contain sequential focus, provide a visible close button, support Escape and restore focus on closure. If closing would discard important work, provide an accessible confirmation rather than silently losing it. Do not close on backdrop clicks where this creates accidental loss.

Choose initial focus according to content: a heading may orient users to a lengthy introduction; the composer may suit a returning conversation. Do not force a screen reader to read a whole transcript as the dialog description. If the invoker disappears, define a stable replacement focus destination. At a responsive change between embedded and modal presentation, preserve the conversation, update semantics and focus containment together, and avoid unexpected relocation.

An iframe needs a meaningful title and a tested boundary between parent page, container and child document. The parent owns outer modal behaviour. Verify cross-document focus and closure in the real integration; same-origin assumptions and a widget demonstration are inadequate evidence.

# 6\. M05 — Make input predictable across interaction modes

Use a labelled textarea or an equivalently tested editor, with persistent instructions for submission and limits. Provide a Send button. If Enter sends, explain how to insert a new line and preserve input-method composition: accepting an IME candidate must not submit the message. Do not override standard editing, selection, dictation or browser shortcuts. Allow paste.

Suggested prompts are buttons. Make clear whether activation fills the composer for review or sends immediately. A reviewable draft is a useful default for complex requests. Controls must expose names that include their visible wording, enabling speech-control users to address them. Avoid instructions that depend solely on colour, position, sound or shape.

Support keyboard, touch, pointer and relevant alternative input throughout the same journey. Do not require dragging, precise gestures, sustained pressure or simultaneous key presses where an ordinary control can achieve the task. Any author-defined single-character shortcuts need an appropriate disable, remap or focus-only mechanism. Offer help for composite navigation without requiring memorisation of hidden commands.

# 7\. M06 — Separate transcript reading from new-message delivery

Provide a named, structured conversation history. Expose the sender, content and meaningful state of each message. Use headings, paragraphs, lists and meaningful links in answers. Keep chronology consistent in the DOM and visual layout. Give users efficient routes to history, new messages and the composer without requiring a long Tab sequence through every historical action.

Incoming messages must not move keyboard focus. When a person is reading earlier turns, preserve the reading anchor and scroll position; show an action such as "Go to latest message". Preserve that anchor when loading older content. Virtualisation must not remove the active or reviewed message or destroy its controls. Prefer a simpler non-virtualised history when the performance benefit does not justify the navigation risk.

For a vendor composite transcript, preserve its documented, tested navigation. Bot Framework Web Chat describes a composite history and a separate announcement mechanism; its arrow-key and card-entry behaviour must be checked against the installed version. Do not transplant this interaction model to an ordinary list. Screen reader browse navigation and keyboard focus are different mechanisms and both need testing.

When replacing or regenerating an answer, maintain the relationship to the original prompt and expose whether the previous answer is retained, replaced or available as a version. Do not silently rewrite information the user is reviewing. Ensure a chosen card answer remains perceivable after its controls become inactive.

# 8\. M07 — Allocate one announcement owner per event

Inventory live regions already supplied by the host, SDK and custom components. Choose one mechanism for each event. For a simple bespoke transcript, a named log can expose appended messages. An alternative is a navigable transcript with a controlled live region. Do not combine both for the same message, or wrap a vendor widget in another live region without evidence that it is needed.

Define visible feedback, announcement content, politeness, timing and focus effect together. Ordinary progress and completion should not interrupt ongoing work. Reserve assertive alerts for genuinely urgent information. Announcements must supplement a persistent, readable interface; users must be able to find the information again.

Use the following event contract as the starting point. The implementation record must replace "chat announcement owner" with the actual SDK or component responsible.

| **Event**                | **Visible outcome**                                   | **Announcement and focus contract**                                                                |
| ------------------------ | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Deliberate open          | Chat title and controls appear                        | Container communicates its name; no duplicate open alert. Apply M04 focus rule.                    |
| Send                     | One message with delivery state                       | Do not echo the full input unnecessarily. Keep focus in composer or the documented stable control. |
| Generation starts        | Persistent generating status and Stop where supported | Chat announcement owner gives one brief polite status. No focus movement.                          |
| Stream updates           | Answer grows without moving the reader                | Do not speak tokens. Use agreed chunks or completion notification.                                 |
| Complete                 | Answer and meaningful actions available               | Announce once, or announce availability and offer a direct reading route.                          |
| New answer during review | New-message control and count where useful            | Brief notification; keep reading and scroll position.                                              |
| Error or lost connection | Explanation, retained input and recovery              | Announce actionable status once. Do not repeatedly interrupt.                                      |
| Session warning          | Time remaining, consequences and extension action     | Timely notification with a reachable persistent action.                                            |
| Handoff                  | Human or queue status and alternatives                | Announce actual service state, not an unverified promise.                                          |

For streaming, separate the visual renderer from the announcement scheduler. Establish the live-region node before updating it, avoid repeatedly replacing its container, and deduplicate events using stable identifiers. Do not treat DOM assertions as proof of spoken output. Test rapid completion, stalled output, several responses arriving together and cancellation. Queued speech may continue after cancellation depending on the screen reader; avoid queuing long repeated content and record limitations.

# 9\. M08 — Design visual adaptation as part of the system

Specify text, control, icon and focus tokens for every supported theme and interaction state. Text contrast normally needs 4.5:1, or 3:1 for qualifying large text; apply the standard's exceptions correctly. Meaningful component boundaries and graphics need applicable non-text contrast. Colour alone must not distinguish sender, failure, success or selection.

Support text resizing to 200% and reflow at the equivalent of 320 CSS pixels for vertically scrolling content. Test browser zoom independently of operating-system magnification. Permit user text-spacing overrides and mobile zoom. Avoid fixed-height transcript or composer containers that clip expanded content. Keep long strings, links and generated code from widening the whole page; scope genuine two-dimensional exceptions to the relevant content.

Keep focus visible and prevent author-created overlays from entirely obscuring it; adopt fully visible focus as a stronger delivery target. A robust, high-contrast focus outline is valuable, but WCAG Focus Appearance 2.4.13 is AAA. Similarly, prefer 44 by 44 CSS pixel controls as a design target while assessing the AA target-size criterion of 24 by 24 CSS pixels and its permitted exceptions separately.

Respect forced colours and reduced motion. Do not rely on shadows or background fills as the only boundary or focus cue. Avoid disabling forced colours across the widget. Provide static progress feedback when animation is reduced. Check sticky controls, safe areas, portrait and landscape layouts, and the mobile software keyboard together. Design adaptation must preserve the same task and information.

# 10\. M09 — Support understanding without unnecessary disclosure

Use short, direct prompts; put the required action before optional explanation. Break long answers into meaningful sections. Offer a shorter explanation or a step-by-step route where useful, while retaining the full information. Test comprehension of names, limits and consequences with intended users. A fixed reading grade or line-length target is not a substitute for this work and is not a universal AA requirement.

Use disclosure patterns for genuinely supplementary detail, such as supporting sources, rather than hiding the answer or essential instructions. Native details and summary are suitable candidates. A user should be able to identify the label and expanded state, operate the control and reach the revealed content. Plan for find, print and transcript export so collapsed content is not accidentally lost.

Prefer persistent visible labels to icon-only controls or tooltip-dependent instructions. Tooltips should contain supplementary, noninteractive information; they must not become hidden forms or the sole route to help. Where hover or focus reveals content, address dismissal, persistence and pointer access. Do not add tabs, menus or carousels simply to compress a chat panel if a simpler presentation is easier to use.

State AI identity and limits plainly. Distinguish source-backed information, uncertainty and unavailable information. Make citations and source controls understandable and operable where provided. Never infer disability from language, typing speed or assistive-technology use, and do not require a disability disclosure to obtain a simpler response or alternative input method.

# 11\. M10 — Make failure and time pressure recoverable

Prepare wording and behaviour for empty input, exceeded limits, invalid uploads, failed delivery, unavailable knowledge, blocked requests, interrupted generation and service outages. Explain what happened, what remains saved and what to do next. Associate field errors with their fields. Validate at a useful point rather than producing a stream of errors while someone is exploring or typing.

Preserve the draft after a recoverable failure. Distinguish pending, sent, failed and uncertain delivery. Retrying must not duplicate a consequential request: reconcile server acknowledgement and use request identifiers where the backend supports them. Provide an alternative support route during prolonged failure. Do not claim a transaction failed if its actual outcome is unknown.

Avoid unnecessary time limits. Where one exists, document the applicable route under Timing Adjustable. For the extension route, give at least 20 seconds to act and allow at least ten extensions; verify real server timing. If an exception is used, record its evidence. Explain expiry consequences, preserve recoverable state where permitted and make reauthentication understandable. Security and privacy constraints on draft retention must be explicit rather than a reason for unpredictable loss.

For legal, financial or user-data-changing actions, provide the applicable review, correction, confirmation or reversal mechanism. A conversational sentence such as "yes" should not silently authorise a different action from the one presented. Clear outcomes and transaction identifiers help both users and support staff recover.

# 12\. M11 — Govern cards, media and generated artifacts

Treat the output renderer as a controlled component boundary. Render supported structures through tested components, sanitise untrusted markup and reject unsafe interactive HTML. A model instruction to "produce accessible content" cannot enforce names, keyboard behaviour or safe focus management. Unsupported output needs a useful accessible fallback.

Cards need readable grouping, labels, instructions, validation and complete keyboard operation. Images need context-appropriate alternatives; decorative images should not add noise. Charts need the meaningful conclusion and access to the underlying values where needed. Structured tables need meaningful headers. Audio and video require the alternatives applicable to their content and use, plus accessible controls.

Uploads require an accessible picker, advance restrictions, progress, cancellation and recovery. Downloaded documents and exported transcripts need their own accessibility review: structured headings, reading order, tables, alternatives and meaningful file names. The original repository separates rich artifacts from its interface scope; delivery must give that work a named owner and acceptance gate whenever those artifacts are shipped. Excluding it from one team's scope does not make it accessible.

# 13\. M12 — Provide voice choice and accessible service handoff

Voice should be an optional mode unless the service has an explicitly justified, independently assessed scope. Users must be able to complete equivalent tasks without speaking or hearing. Provide editable recognition text, clear recording state, microphone permission recovery and a way to stop recording. Never start audio output unexpectedly. Keep controls for speech distinct from controls for screen reader announcements.

Make human handoff visible and usable where offered. Explain availability, queue state, likely next step and any alternative channel. Obtain appropriate consent before transferring the transcript. Allow users to correct the handoff summary; do not force them to repeat information already available within the same process unnecessarily. Ensure the human service can continue with the person's communication needs, rather than moving an accessible text exchange to mandatory telephone contact.

# 14\. M13 — Protect privacy and sustain the host journey

Define retention, access and deletion rules separately for drafts, transcripts, model input, diagnostic logs and research recordings. Keep ordinary analytics free of raw conversation text and sensitive attachments. Use synthetic content for automated tests and redact evidence before sharing. Do not assume local storage is safe for sensitive drafts on a shared device.

The host page must still offer useful information and support when the chat script, network or storage fails. Provide a clear unavailable state and an accessible alternative rather than an inert launcher or endless spinner. This is a resilience requirement, not a claim that every dynamic conversation must work without JavaScript. Check route changes, back navigation, multiple widgets and cookie dialogs for focus and announcement conflicts.

# 15\. M14 — Verify through complementary methods

Use component and browser integration checks for deterministic behaviours: accessible names, expanded states, focus restoration, no focus movement on answer arrival, stable identifiers and draft preservation. Run automated accessibility scans in meaningful states, retaining failures, incomplete checks and tool versions. A clean scan cannot establish readable announcements, understandable content or independent task completion.

Manual expert testing must cover keyboard and alternative input, screen reader reading and interaction modes, mobile touch exploration, zoom, spacing, contrast, forced colours, motion and failure recovery. Record the observed output, not only "works". User research must then evaluate discovery, orientation, comprehension, control, recovery and effort with disabled people using familiar tools. These methods answer different questions and should not be collapsed into one score.

Use the companion brief to establish the feature and environment matrix before execution. A missing test, an unsupported result or a skipped optional feature must remain visible in coverage reporting. Changes to SDKs, renderers, model output format, design tokens or host pages trigger impact review and relevant retesting.

# 16\. M15 — Release with accountable decisions

Review evidence against requirements rather than accepting a general "accessible" label. Block release where an essential task is inaccessible, focus is trapped, required information is unavailable or critical recovery fails. Record remaining findings with affected tasks, users, severity, owner, target date and retest evidence. A business acceptance of risk does not change a failed WCAG criterion into a pass.

The release record should identify the build, scope, supported environments, requirement coverage, outstanding limitations, approval and rollback plan. Use an accessible feedback channel outside the chatbot so excluded users can report a barrier. If a serious regression appears, disable the affected feature or restore a previously tested version while preserving access to the service.

# 17\. M16 — Improve using task outcomes and lived experience

Collect consent-based task completion, abandonment, repeat attempts, recovery and support-contact signals. Pair these with moderated observation and optional accessible surveys. Ask whether people could finish, where they lost control, what they misunderstood and what would help. Provide response formats and an external route that do not require successful chatbot use.

Where relevant, organise inquiry around interaction outcomes: use without vision; with limited vision; without colour; without hearing; with limited hearing; without speech; with limited manipulation or strength; with limited reach; without harmful flashing; with cognitive support; and with privacy. These themes support research planning; they do not replace technical or legal assessment.

Segment only by consented, self-reported needs and appropriate task context. Report sample sizes, missing groups and uncertainty; do not infer disability from telemetry. Every experimental variant must meet the baseline. Define success and adverse-outcome measures before an experiment, and investigate harm to a subgroup even where aggregate completion improves. AI can help identify patterns and propose fixes, but evidence and accountable review govern release.

# 18\. Implementation handover checklist

- Scope and installed platform versions are recorded; feature applicability has an owner.
- Visual and nonvisual journeys cover normal, interrupted and recovery states.
- Container, focus, history navigation and announcement contracts are explicit.
- Components and generated output structures have named implementation owners.
- Baseline requirements, delivery rules and research targets remain distinguishable.
- Test cases trace to requirements, components and retained evidence.
- Disabled-user research informs the task design and outstanding barriers.
- Release, feedback, retention, regression and rollback responsibilities are assigned.

# 19\. Basis and document control

Primary implementation basis: Double FW, Inclusive Chatbot Interfaces Reference, version 1.1; and Accessible Branded Chatbot Generation Prompt Template, version 1.2, both dated 24 September 2026. Technical interpretation was checked against W3C WCAG 2.2, WAI-ARIA Authoring Practices modal-dialog guidance, native-dialog technique H102, chat-log technique ARIA23 and status-message guidance. Microsoft Bot Framework Web Chat accessibility documentation informs only the conditional SDK discussion. Copilot Studio documentation and axe-core documentation inform platform and verification boundaries.

This document defines delivery expectations. It is not evidence that any particular chatbot has passed testing. Review it when the baseline, supported platforms, SDK, output formats or service scope changes. Version 1.0 establishes the linked methodology and testing structure on 19 October 2026.