# Accessible chatbot testing brief

Scope, execution instructions and expected outcomes

Version 1.0 | 19 October 2026 | Companion: Accessible Chatbot Delivery Methodologies

## 1\. Objective and status

Establish whether people can discover, operate, understand and complete the chatbot's supported tasks independently, including after errors or interruptions. Evaluate the integrated host page, chatbot, authentication, generated content and any handoff service. Assess applicable WCAG 2.2 A/AA requirements separately from additional delivery outcomes and user-research findings.

This is an execution brief, not a completed audit. Every case starts as Not run. A result requires evidence from the actual build and environment. The catalogue covers chatbot-specific behaviours and common host dependencies; a full-page and complete-process WCAG applicability review remains required before a conformance claim.

## 2\. Commissioning and scope record

Before testing, QA and the product owner must complete: product and build identifier; host URLs or routes; test environment; framework, SDK and renderer versions; design-system version; supported languages; model and knowledge configuration; presentation variants; feature inventory; and the named owners of engineering, content, accessibility review, research and release. Record the contractual baseline and any separately applicable legal or procurement requirements with the accountable compliance owner.

Run every applicable case in every shipped presentation. If desktop is embedded and mobile is modal, both count. Mark optional features Not applicable only with a recorded reason approved by the scope owner. Missing access to an enabled feature is Blocked, not Not applicable. Native applications require an additional platform-specific test plan; this brief is for the web experience and its connected service journey.

Core scope includes launcher, closed and open panel, composer, suggestions, message delivery, transcript, streaming, status, errors, stop/retry, close/reopen, long history and service fallback. Add authentication, files, cards, voice, saved history, consequential actions and human handoff whenever present. Scope includes overlays, navigation and other host features that can interfere with the chatbot.

## 3\. Environments and execution matrix

Record exact OS, browser, assistive technology, device, viewport and relevant preferences for every run. Select supported versions before execution; do not use the word "latest" as the retained evidence. The following is a proposed starting matrix to be confirmed against users and service support, not a universal compatibility guarantee.

| **Environment**                                | **Principal coverage**                                           |
| ---------------------------------------------- | ---------------------------------------------------------------- |
| Windows, Chrome, keyboard and NVDA             | Full core journey; browse and focus modes; live announcements    |
| Windows, Edge, JAWS                            | Full core journey and vendor composite controls                  |
| macOS, Safari, VoiceOver                       | Full core journey; dialog and transcript navigation              |
| iOS, Safari, VoiceOver on a physical device    | Touch exploration, reading order, software keyboard and rotation |
| Android, Chrome, TalkBack on a physical device | Touch navigation, announcements, cards and software keyboard     |
| Windows contrast themes and magnification      | Boundaries, focus, reading position and visual adaptation        |
| Platform voice control and switch access       | Named activation, scanning effort and complete task operation    |

Use keyboard-only checks without a screen reader as well as screen reader runs. Test touch and physical keyboard separately on supported mobile configurations. Browser emulation supports layout checks but does not replace device-based assistive-technology evidence. Include lower-powered devices and constrained connectivity where these are relevant to the audience.

For every supported combination, run the core journey: discover, open, send, receive, read history, recover from failure, close and resume. Run feature-specific cases across the combinations affected by that feature. Maintain a case-by-environment matrix so a pass in one combination does not conceal an untested one.

## 4\. Test data and controllable states

Use a test backend or controlled fixtures to produce predictable success, delayed acknowledgement, streaming, cancellation, connection loss, server failure, duplicate events, session warning and expiry. Then repeat the critical journey against the real integration. A mocked success cannot prove that production authentication, transport or handoff works.

Prepare synthetic data: a short plain-text response; a long answer with headings, lists and links; a transcript of at least 100 turns; a very long unbroken string; a multilingual answer and right-to-left text where supported; a structured card; a meaningful image and chart; valid and invalid uploads; a downloadable artifact; an uncertain answer; an unsupported request; and a reversible test transaction. The 100-turn history is a stress fixture, not a WCAG threshold.

Use representative real-model outputs as well as fixtures. For generative evaluation, retain the prompt, configuration, source set, response and reviewer judgement securely. Repeat the same input across an agreed number of runs and report observed variation. No finite sample proves that every future response will be accessible; enforce rendering constraints and monitor changes.

## 5\. Methods, results and evidence

Method codes: A = automated DOM, component, browser or scanner check; M = manual expert check with the relevant input mode or assistive technology; U = moderated user research. A+M means both are required. Automated checks of live-region nodes do not establish what a screen reader says. User research does not replace criterion-level checks.

For each case record: case and method requirement IDs; build; variant; fixture; environment; date; tester; steps taken; actual result; expected-result comparison; result; evidence location; defect ID; severity; owner; and retest result. Use Pass, Fail, Blocked, Not run or Not applicable. Record a criterion exception separately with its justification; do not silently weaken the expected outcome.

For screen reader cases retain the meaningful spoken sequence and whether information was absent, duplicated, interrupted or delayed. Exact voice phrasing may differ between products; assess whether the required name, role, state and content are conveyed. For visual cases retain viewport and preference settings with screenshots or measurements. Redact personal content and credentials. Apply the organisation's approved access and retention policy to recordings and transcripts; agree that policy before collecting real participant data.

The mappings below are related WCAG criteria, not claims that each case alone proves those criteria. "Delivery" identifies requirements beyond a direct criterion mapping. Where a test has several assertions, record each separately and pass the case only when every applicable assertion passes. Split assertions into local subcases when different owners or defects need independent tracking.

## 6\. Discovery, container and focus tests

### T01 — Find and identify the service

_Requirement M03. Method A+M. Related criteria: 2.4.6, 2.5.3, 4.1.2; AI disclosure is Delivery._

**Setup:** fresh host page, chat closed.

**Steps:** locate the launcher visually, by keyboard and through screen reader controls; inspect its name; read introductory information.

**Expected:** the launcher is reachable, its name includes visible wording and describes its purpose, and the user can establish that the service is automated and what help it offers.

**Evidence:** control name, location and reading sequence.

### T02 — No unsolicited interruption

_Requirement M03. Method A+M. Related criteria: 3.2.1 where applicable; no unsolicited opening or speech is Delivery._

**Setup:** page loaded with focus on a host task.

**Steps:** wait for chat initialization and any invitation; dismiss the invitation and continue.

**Expected:** initialization does not move focus, start audio or open a modal. Any invitation is dismissible, does not cover necessary controls and does not repeatedly return after dismissal within its defined scope.

**Evidence:** focus trace, speech observations and invitation behaviour.

### T03 — Embedded panel opening and exit

_Requirement M04. Method A+M. Related criteria: 2.1.1, 2.1.2, 2.4.3, 4.1.2._

**Setup:** embedded variant closed.

**Steps:** activate launcher; inspect expanded state; traverse the panel with Tab and Shift+Tab; leave it and use the host page.

**Expected:** state and accessible panel name are correct; initial focus follows the specification; no modal semantics or inert host are introduced; keyboard exit works in both directions with a logical order.

**Evidence:** focus sequence and accessibility-tree observations.

### T04 — Modal entry and containment

_Requirement M04. Method A+M. Related criteria: 2.1.1, 2.1.2, 2.4.3, 4.1.2; modal interaction contract is Delivery._

**Setup:** modal variant closed.

**Steps:** open it; traverse forward and backward; attempt pointer and screen reader access to the background.

**Expected:** a meaningful dialog name is conveyed, focus enters the specified element, sequential navigation remains inside, and background interaction and reading are unavailable while modal. All dialog content remains reachable.

**Evidence:** initial announcement, boundary behaviour and focus trace.

### T05 — Close and restore focus

_Requirement M04. Method A+M. Related criteria: 2.1.1, 2.1.2, 2.4.3; Escape policy is Delivery._

**Setup:** open chat with focus inside and a draft.

**Steps:** close using the visible button; repeat using Escape for modal; test removal of the original launcher before closure.

**Expected:** focus returns to the invoker or specified stable replacement; hidden controls cannot receive focus; host interaction is restored. Draft loss does not occur silently. Any confirmation is accessible and cancellable.

**Evidence:** restored focus and draft state.

### T06 — Breakpoint and iframe boundaries

_Requirement M04. Method A+M. Related criteria: 2.1.2, 2.4.3, 4.1.2; context continuity is Delivery._

**Setup:** open conversation with draft; embedded iframe or responsive mode change if shipped.

**Steps:** cross the breakpoint; enter and leave iframe content; close from the inner and outer controls.

**Expected:** iframe has a meaningful title; modality, focus and background state remain consistent; no trap or lost conversation appears. Parent and child do not create conflicting focus loops. Mark each absent subfeature Not applicable.

**Evidence:** before/after state and boundary trace.

### T07 — Host navigation and competing overlays

_Requirements M04, M13. Method A+M. Related criteria: 2.4.3, 2.4.11; restoration is Delivery._

**Setup:** chat open on a page with site navigation, cookie preferences or another overlay.

**Steps:** trigger supported overlays; follow a route; use browser Back; reopen chat.

**Expected:** only the active modal owns focus containment, focus never lands in hidden content, host navigation remains coherent and state follows the declared retention policy. Chat does not obscure focused host controls entirely.

**Evidence:** sequence and retained state.

## 7\. Input and operation tests

### T08 — Composer name and instructions

_Requirement M05. Method A+M. Related criteria: 1.3.1, 2.4.6, 3.3.2, 4.1.2._

**Setup:** ready composer.

**Steps:** inspect and focus the field with each input mode; review its name, instructions and limits.

**Expected:** a persistent visible label identifies the field; assistive technology receives the same purpose; placeholder text is not the sole label; submission and attachment instructions are available before they are needed.

**Evidence:** name/description and rendered instructions.

### T09 — Send, new lines and text composition

_Requirement M05. Method A+M. Related criteria: 2.1.1, 3.2.2; editing conventions are Delivery._

**Setup:** composer ready.

**Steps:** type a multiline message, paste text, dictate, use the documented submit shortcut and Send button; where supported, accept an IME composition candidate with Enter.

**Expected:** newline and submit behaviour match the instruction, ordinary editing works, and accepting a composition candidate does not send prematurely. Each deliberate send creates one message.

**Evidence:** submitted text and event count.

### T10 — Suggested prompts

_Requirement M05. Method A+M. Related criteria: 2.1.1, 2.5.3, 3.2.2, 4.1.2._

**Setup:** suggestions available.

**Steps:** navigate, identify and activate a suggestion; repeat by voice control and touch.

**Expected:** real, named controls operate by all supported methods; users can predict whether activation fills or sends; generated drafts remain editable when review is the declared behaviour. Focus remains at a useful stable location if suggestions disappear.

**Evidence:** names, action and focus outcome.

### T11 — Keyboard operation and shortcut conflicts

_Requirements M05, M06. Method A+M. Related criteria: 2.1.1, 2.1.2, 2.1.4, 2.4.3._

**Setup:** conversation with all controls and interactive content.

**Steps:** complete the task without a mouse; test Tab, Shift+Tab, activation keys and documented composite commands; type shortcut characters in fields.

**Expected:** every action is reachable and escapable, no positive tabindex disrupts the intended sequence, editing/browser/AT shortcuts remain usable, and character shortcuts have the required disable, remap or focus restriction.

**Evidence:** navigation script and any conflict.

### T12 — Voice control, switch access and label matching

_Requirement M05. Method M+U. Related criteria: 2.1.1, 2.5.3; manageable effort is Delivery._

**Setup:** supported voice-control and switch-access environments.

**Steps:** open, compose, send, review, retry and close using those tools.

**Expected:** visible names can be used to target controls; scanning reaches all actions without a trap; no essential action depends on a hidden label, mouse hover or simultaneous movement. Record repeated activations and fatigue separately from technical pass/fail.

**Evidence:** task record and barrier observations.

### T13 — Pointer, touch and gesture alternatives

_Requirement M05. Method A+M. Related criteria: 2.5.1, 2.5.2, 2.5.4, 2.5.7, 2.5.8._

**Setup:** touch and pointer views.

**Steps:** measure targets; press then move away before release; try any drag, path gesture or motion action using a simple alternative.

**Expected:** targets meet 24 by 24 CSS pixels or a documented permitted exception, accidental activation can be cancelled as applicable, and complex gestures, dragging and motion have the required alternatives. Assess 44 by 44 separately as a design target.

**Evidence:** dimensions and exception rationale.

## 8\. Transcript and announcement tests

### T14 — Message structure and chronology

_Requirement M06. Method A+M. Related criteria: 1.3.1, 1.3.2, 2.4.6, 4.1.2._

**Setup:** mixed user, bot and human messages.

**Steps:** read visually and with screen reader browse navigation; inspect headings and controls.

**Expected:** sender, content and meaningful delivery state are distinguishable without relying on colour or alignment; chronology is consistent; decorative avatars do not add repetitive noise; structural relationships survive nonvisual reading.

**Evidence:** reading sequence and message structure.

### T15 — Efficient history and composer navigation

_Requirement M06. Method M. Related criteria: 2.1.1, 2.1.2, 2.4.3; efficiency is Delivery._

**Setup:** long transcript with several interactive cards.

**Steps:** reach history, navigate earlier turns, enter and leave a card, return to the composer and find the latest turn.

**Expected:** documented routes work without an exhausting Tab journey; composite keys apply only within the relevant widget; users can leave card interaction and the transcript. Do not require vendor shortcuts on a different implementation.

**Evidence:** commands and number of navigation actions.

### T16 — Preserve reading position on arrival

_Requirements M06, M07. Method A+M. Related criteria: 2.4.3; reading and scroll preservation are Delivery._

**Setup:** user reviewing an old message, with a focused link or screen reader reading anchor there.

**Steps:** inject a new answer and continue reading.

**Expected:** focus, reading location and scroll position remain stable; a new-message action is available; activating it deliberately reaches the specified new content and provides a route back to composing.

**Evidence:** before/after focus, viewport and spoken context.

### T17 — Long history and virtualisation

_Requirement M06. Method A+M. Related criteria: 1.3.2, 2.1.1, 2.4.3, 4.1.2._

**Setup:** at least 100 turns with links and controls.

**Steps:** read near a rendering boundary; load older messages; receive new ones; return to the prior turn.

**Expected:** no reviewed message disappears, identifiers remain stable, history is not silently skipped or reordered, and controls retain their relationships. Loading history does not replay all old messages as new announcements.

**Evidence:** boundary sequence and reading trace.

### T18 — Announcement ownership and duplication

_Requirement M07. Method A+M. Related criterion: 4.1.3; single ownership is Delivery._

**Setup:** host, SDK and custom status mechanisms active.

**Steps:** trigger open, send, generate, complete, error and reconnect individually; inspect live regions and listen.

**Expected:** each event has the documented owner and useful announcement; the same answer is not announced by both transcript and wrapper; no full-history replay occurs. Merely finding one live-region node is insufficient.

**Evidence:** event-to-owner record and actual speech.

### T19 — Progress and response completion

_Requirement M07. Method A+M. Related criteria: 4.1.2, 4.1.3; bounded verbosity is Delivery._

**Setup:** delayed response and determinate upload fixture if present.

**Steps:** send; inspect progress; wait for completion and repeat with failure.

**Expected:** waiting is perceivable visually and nonvisually; a percentage is used only when meaningful; progress does not announce continuously; completion or failure replaces the waiting state and remains findable. Focus does not move.

**Evidence:** visible states and spoken sequence.

### T20 — Streaming, rapid answers and bursts

_Requirement M07. Method A+M. Related criterion: 4.1.3; speech scheduling is Delivery._

**Setup:** short, long and fast-streaming responses, including several arriving close together.

**Steps:** send while composing another draft and while reviewing old content.

**Expected:** no token-by-token speech or repeated partial answer; the agreed chunk or completion policy preserves access to all information without stealing focus. Rapid responses are not missed because a live region was mounted too late.

**Evidence:** timing and speech observations in each environment.

### T21 — Stop and regenerate

_Requirements M06, M07. Method A+M. Related criteria: 2.1.1, 4.1.2, 4.1.3; partial-answer labelling is Delivery._

**Setup:** generation in progress.

**Steps:** activate Stop; review partial content; retry or regenerate.

**Expected:** generation state ends, partial text is identified as incomplete, the control transition does not strand focus, and regeneration clearly relates to its prompt. Old content is not silently overwritten under the reader. Record any already-queued speech separately.

**Evidence:** state, retained text and focus sequence.

### T22 — Errors, alerts and announcement priority

_Requirements M07, M10. Method M. Related criteria: 3.3.1, 4.1.3; interruption policy is Delivery._

**Setup:** user typing or reading.

**Steps:** trigger a routine recoverable error and a genuinely urgent test warning separately.

**Expected:** routine feedback does not continually interrupt speech or typing; urgent information is perceivable with an actionable route; every message remains available after its announcement. Duplicate alert and status output is absent.

**Evidence:** speech sequence, urgency rationale and recovery route.

## 9\. Visual presentation and adaptation tests

### T23 — Text contrast and meaningful non-text contrast

_Requirement M08. Method A+M. Related criteria: 1.4.3, 1.4.11._

**Setup:** all themes and normal, hover, focus, selected, error and loading states.

**Steps:** measure relevant foreground/background pairs, including icons and boundaries.

**Expected:** ordinary text reaches 4.5:1; qualifying large text reaches 3:1; required graphical and component information reaches applicable 3:1 contrast. Record genuine exceptions such as inactive controls; do not use them to excuse essential explanatory text.

**Evidence:** measured pairs and screenshots.

### T24 — Colour-independent meaning

_Requirement M08. Method M. Related criteria: 1.3.3, 1.4.1._

**Setup:** success, error, selection and mixed-sender messages.

**Steps:** inspect without relying on hue; read instructions nonvisually.

**Expected:** labels, symbols with meaningful equivalents, or other cues identify the state and action. "Select the green option" or alignment alone does not carry essential meaning.

**Evidence:** equivalent cues for each state.

### T25 — Visible and unobscured focus

_Requirement M08. Method M. Related criteria: 2.4.7, 2.4.11, 1.4.11 where applicable._

**Setup:** every interactive control in each layout and theme.

**Steps:** traverse with keyboard while sticky headers, composer, notifications and software keyboard are present.

**Expected:** focus is clearly visible and never entirely hidden by author-created content; the stronger project target is fully visible focus. Assess AAA Focus Appearance separately if adopted; do not report it as AA.

**Evidence:** screenshots of boundary and overlay cases.

### T26 — Text resize

_Requirement M08. Method M. Related criterion: 1.4.4._

**Setup:** open chat and rich response.

**Steps:** enlarge text to 200%, including a browser text-only method where available; operate all controls.

**Expected:** no information or functionality is lost, labels and errors remain readable, and composer or message containers do not clip content. Record applicable criterion exceptions separately.

**Evidence:** setting, screenshots and completed interaction.

### T27 — Reflow and zoom

_Requirement M08. Method M. Related criterion: 1.4.10._

**Setup:** long answer with links, code and a table.

**Steps:** use a 1280-CSS-pixel-wide starting viewport at 400% browser zoom, or equivalent 320-CSS-pixel content width; inspect and operate chat.

**Expected:** ordinary vertically scrolling content needs no two-dimensional scrolling and no functionality is lost. Any necessary two-dimensional content is scoped and documented, not used to exempt the whole panel.

**Evidence:** actual viewport and exception boundaries.

### T28 — Text spacing overrides

_Requirement M08. Method A+M. Related criterion: 1.4.12._

**Setup:** supported markup-based text.

**Steps:** simultaneously apply line height 1.5 times font size, paragraph spacing 2 times, letter spacing 0.12 times and word spacing 0.16 times, changing no other style property.

**Expected:** content and controls remain readable and usable without loss; errors, buttons and fixed areas do not clip. Apply the criterion's language/script exception where appropriate.

**Evidence:** applied settings and affected components.

### T29 — Forced colours and user themes

_Requirement M08. Method M. Related criteria: 1.4.1, 1.4.3, 1.4.11, 2.4.7; adaptation is Delivery._

**Setup:** OS contrast theme, supported light/dark themes and contrast preferences.

**Steps:** switch before load and during chat; operate every control.

**Expected:** borders, focus, state indicators, text and meaningful icons remain perceivable; brand styling does not suppress system colours indiscriminately. Author-provided themes satisfy applicable contrast requirements.

**Evidence:** theme settings and screenshots.

### T30 — Motion, automatic updates and flashing

_Requirement M08. Method A+M. Related criteria: 2.2.2, 2.3.1; reduced-motion adaptation is Delivery._

**Setup:** loading, transitions, animated media and reduced-motion preference.

**Steps:** inspect normal and reduced modes; assess moving or auto-updating content for required controls; review flashing with appropriate analysis.

**Expected:** pause/stop/hide requirements are met where applicable; flashing is within the criterion's limits; reduced mode removes nonessential movement while preserving status. Never expose participants to suspected harmful flashing to validate it.

**Evidence:** state captures and analysis.

### T31 — Mobile viewport, keyboard and orientation

_Requirement M08. Method M. Related criteria: 1.3.4, 1.4.10, 2.4.11; mobile usability is Delivery._

**Setup:** physical phone, enlarged text and open chat.

**Steps:** rotate; focus composer to show software keyboard; type several lines; reach Send, Stop and Close; pinch zoom.

**Expected:** essential controls and content remain reachable, required orientation is not imposed without a valid reason, zoom is available, and keyboard appearance does not strand focus or conceal recovery controls.

**Evidence:** device recordings and viewport state.

## 10\. Content and component tests

### T32 — Understandable prompts and AI limits

_Requirement M09. Method M+U. Delivery requirement; related criteria: 2.4.6, 3.3.2._

**Setup:** first-use, complex and uncertain-answer fixtures.

**Steps:** ask users what the chatbot can do, whether a human is responding, what information is needed and what happens next.

**Expected:** the explanation is accurate; key actions are understood; uncertainty is not presented as certainty; users can request clarification or simpler wording. Do not pass on a readability score alone.

**Evidence:** comprehension responses and content defects.

### T33 — Links, headings and language

_Requirements M06, M09. Method A+M. Related criteria: 1.3.1, 2.4.4, 2.4.6, 3.1.1, 3.1.2._

**Setup:** long answer with citations and language changes.

**Steps:** navigate by headings and links; activate sources; inspect document and passage language.

**Expected:** structure conveys organisation; link purpose is understandable in context; citations reach the intended source; language metadata supports appropriate pronunciation where required. Raw formatting syntax is not the intended reading experience.

**Evidence:** structure, destinations and spoken language.

### T34 — Disclosures and hover content

_Requirement M09. Method A+M. Related criteria: 1.4.13, 2.1.1, 4.1.2._

**Setup:** expandable source detail and tooltip if present.

**Steps:** open and close by keyboard, pointer and touch; move pointer onto hover content; dismiss without moving focus; inspect exported content.

**Expected:** disclosure state is conveyed and revealed content is reachable; tooltip content is supplementary, noninteractive, dismissible, hoverable and persistent as applicable. Essential instructions are not hidden only in a tooltip.

**Evidence:** state and interaction observations.

### T35 — Cards and nested controls

_Requirement M11. Method A+M. Related criteria: 1.3.1, 2.1.1, 2.1.2, 3.3.2, 4.1.2._

**Setup:** each supported card type, including a form and choice card.

**Steps:** identify grouping; enter, complete, submit and leave; revisit after selection.

**Expected:** names, grouping and state are meaningful; navigation and exit work; selected answers remain readable when actions become inactive; custom rendering preserves the SDK's accessible equivalent.

**Evidence:** each card type and chosen-answer representation.

### T36 — Images, charts and tables

_Requirement M11. Method A+M. Related criteria: 1.1.1, 1.3.1, 1.4.5 where applicable._

**Setup:** meaningful and decorative images, chart and data table.

**Steps:** read without images and by screen reader; compare alternatives with the task information.

**Expected:** alternatives convey relevant meaning and function, decorative images add no noise, charts expose needed findings and values, and table headers identify relationships. Presence of an alt attribute alone is not a pass.

**Evidence:** content comparison and reading sequence.

### T37 — Generated markup and unsupported formats

_Requirement M11. Method A+M. Related criteria: 1.3.1, 2.1.1, 4.1.2; safe rendering is Delivery._

**Setup:** controlled malformed Markdown, unsafe HTML, missing labels, unexpected embeds and unsupported card types.

**Steps:** render each fixture and attempt navigation.

**Expected:** unsafe markup does not execute; supported content uses tested structure; unsupported content produces a useful accessible fallback, not an empty or broken control. Verify both safety and retained meaning.

**Evidence:** renderer output and fallback content.

### T38 — Upload lifecycle

_Requirement M11. Method A+M. Related criteria: 2.1.1, 3.3.1, 3.3.2, 3.3.3, 4.1.3._

**Setup:** upload enabled; valid, oversized and disallowed files; network failure.

**Steps:** inspect restrictions, choose a file without dragging, upload, cancel, remove and retry.

**Expected:** restrictions precede submission, file and progress state are identifiable, cancellation works, errors explain recovery, and the message draft survives. A picker is available as an alternative to drag-and-drop.

**Evidence:** lifecycle and announcements.

### T39 — Downloads and transcript export

_Requirement M11. Method M. Related criteria depend on content; at minimum assess 1.3.1 and 2.4.4 for the web controls. Artifact accessibility is Delivery with its own baseline._

**Setup:** every supported export format.

**Steps:** download and open in the intended reader; navigate headings, tables and links; inspect transcript sequence.

**Expected:** meaningful file names, sender and message order, complete content including needed disclosed detail, and appropriate artifact structure. Record format-specific accessibility evidence separately.

**Evidence:** exported files and reader checks.

# 11\. Recovery, session and transaction tests

### T40 — Validation and correction

_Requirement M10. Method A+M. Related criteria: 3.3.1, 3.3.2, 3.3.3, 4.1.3._

**Setup:** empty, over-limit and invalid card input.

**Steps:** submit; locate the error; correct and resubmit.

**Expected:** specific errors identify affected fields and practical correction; associations are programmatic; input remains available; corrected states update; exploration and ordinary typing do not trigger an excessive alert stream.

**Evidence:** wording, associations and successful correction.

### T41 — Delivery failure and duplicate prevention

_Requirement M10. Method A+M. Delivery requirement; related criterion: 4.1.3._

**Setup:** lost acknowledgement after the server receives a message.

**Steps:** send, interrupt connectivity, retry and reconnect.

**Expected:** the interface distinguishes uncertain from confirmed failure; server reconciliation prevents duplicate consequential execution; pending/sent/failed states are truthful; retained input can be recovered. If status cannot be established, the user is told how to check.

**Evidence:** client and backend identifiers with synthetic content.

### T42 — Outage and reconnect

_Requirements M10, M13. Method A+M. Related criteria: 2.1.1, 4.1.3; resilience is Delivery._

**Setup:** open chat and unsent draft.

**Steps:** go offline; send; restore connection; repeat with a service error and prolonged delay.

**Expected:** no endless unexplained spinner; draft and recoverable context persist according to policy; retries remain operable; reconnection is communicated without stealing focus; alternative support remains accessible.

**Evidence:** state sequence and recovery outcome.

### T43 — Session warning and extension

_Requirement M10. Method A+M. Related criterion: 2.2.1._

**Setup:** actual configured time limit and server timer.

**Steps:** inspect the selected compliance route; for extension, wait for warning and extend at least ten times, including by screen reader and keyboard.

**Expected:** at least 20 seconds are available to act on the warning for that route; extension actually resets the relevant timer. Other permitted routes or exceptions require evidence against their conditions.

**Evidence:** timestamps and server state.

### T44 — Expiry, reauthentication and draft policy

_Requirements M10, M13. Method A+M. Related criteria: 3.3.8 where applicable; state recovery is Delivery._

**Setup:** draft and active task near expiry.

**Steps:** let the session expire; attempt a send; sign in again; resume.

**Expected:** expiry and its consequences are clear, no message is presented as sent when rejected, retained state follows the declared privacy policy, and recovery does not strand the user. Any discarded sensitive content has an explained reason.

**Evidence:** before/after state and recovery path.

### T45 — Accessible authentication and redundant entry

_Requirements M10, M13. Method A+M. Related criteria: 1.3.5, 3.3.7, 3.3.8._

**Setup:** sign-in and identity-confirmation journey.

**Steps:** use password manager, paste and any one-time-code mechanism; revisit already-provided information in the same process.

**Expected:** cognitive-function tests have the required alternative or assistance unless a valid exception applies; paste and autofill are not obstructed; input purposes are identified where required; redundant entry is avoided or satisfies an exception.

**Evidence:** each authentication path and applicable exceptions.

### T46 — Consequential actions

_Requirement M10. Method A+M. Related criterion: 3.3.4 where applicable; broader confirmation policy is Delivery._

**Setup:** synthetic booking, payment or data-change action.

**Steps:** enter wrong details, review, correct, cancel and then confirm; simulate uncertain completion.

**Expected:** the applicable reversal, checking or confirmation mechanism works; the presented action matches execution; outcome is clear; retry does not create duplicates. No real irreversible transaction is needed for the test.

**Evidence:** review screen, corrected values and transaction state.

### T47 — Close, end, clear and new conversation

_Requirements M02, M10. Method A+M. Related criteria: 2.4.6, 3.3.4 if deletion is in scope; state distinction is Delivery._

**Setup:** history and draft present.

**Steps:** collapse and reopen; end; start a new conversation; clear saved history.

**Expected:** labels distinguish each action, consequences are explained before destructive action, required safeguards work, and history retention matches policy. Closing does not silently delete or falsely promise deletion.

**Evidence:** state transition and storage outcome.

## 12\. Voice, media, handoff and privacy tests

### T48 — Voice input and permission recovery

_Requirement M12. Method A+M. Delivery requirement; related criteria: 2.1.1, 4.1.2, 4.1.3._

**Setup:** voice feature enabled.

**Steps:** deny microphone permission; recover; record; stop; correct a recognition error; continue by text.

**Expected:** recording state and controls are perceivable, denial has a usable recovery path, recognised text can be corrected before consequential submission, and the same task is available without speech.

**Evidence:** permission and mode-switch sequence.

### T49 — Audio output and media alternatives

_Requirements M11, M12. Method M. Related criteria: 1.2.1–1.2.5 as applicable, 1.4.2, 2.1.1._

**Setup:** speech output and each supported media type.

**Steps:** complete the task with audio muted; inspect captions, transcript or audio description as applicable; operate playback and stop controls.

**Expected:** equivalent task information is available without hearing; visual-only media information has the required alternative; controls work without a pointer; audio does not start unexpectedly under the delivery policy. Record each applicable media criterion separately.

**Evidence:** alternatives and control results.

### T50 — Human handoff and unavailable service

_Requirement M12. Method A+M+U. Delivery requirement; related criteria: 3.2.6, 3.3.2, 4.1.3._

**Setup:** available, queued, unavailable and failed-handoff states.

**Steps:** request human support; review and correct summary; choose what is transferred; follow through to the receiving service.

**Expected:** real availability and next steps are clear, consent choices work, the communication route remains usable, and no mandatory phone call replaces the only accessible text route.

**Evidence:** end-to-end handoff and fallback completion.

### T51 — Privacy, consent and deletion

_Requirement M13. Method A+M. Delivery requirement, with separate privacy-policy assessment._

**Setup:** synthetic sensitive draft, transcript and attachment.

**Steps:** inspect notices; opt out of optional analytics; close, sign out and use deletion controls; inspect permitted diagnostic events.

**Expected:** behaviour matches declared retention and consent, optional refusal does not remove core access, shared-device exposure is addressed, and ordinary analytics do not include raw sensitive content or inferred disability.

**Evidence:** redacted event examples and data-lifecycle checks.

### T52 — Chat unavailable and progressive fallback

_Requirement M13. Method A+M. Delivery requirement; related criteria: 2.1.1, 2.4.4, 4.1.3 where applicable._

**Setup:** block chat script, third-party connection or storage separately.

**Steps:** load the host page and seek help.

**Expected:** the core host task remains usable; a useful unavailable message and accessible support route exist; no dead launcher, keyboard trap or permanent blocking overlay remains. Record what genuinely requires JavaScript rather than asserting complete chat functionality without it.

**Evidence:** each failure mode and alternate journey.

## 13\. Assurance and regression tests

### T53 — Automated state coverage

_Requirement M14. Method A with manual triage. Relevant criteria depend on scanner rule and state._

**Setup:** controlled fixture suite.

**Steps:** scan closed, open, loading, streaming, completed, error, reconnect and expiry states; include cards and overlays; inspect incomplete results.

**Expected:** applicable detectable failures are addressed, incomplete checks have reviewers, and rules, tool versions and tested states are retained. Focus and state assertions run separately. A zero-violation result is not a conformance statement.

**Evidence:** CI output and triage record.

### T54 — Full-page and complete-process review

_Requirements M01, M14. Method M supported by A. Baseline: all applicable WCAG 2.2 A/AA criteria._

**Setup:** representative host pages and complete service tasks.

**Steps:** review the criterion ledger in section 16, inspect every applicable criterion and link evidence to cases or additional tests.

**Expected:** every criterion has an applicability decision and evidence; page-level barriers and downstream stages are assessed; no widget-only result is represented as a full-page or full-process pass.

**Evidence:** signed applicability ledger and scope.

### T55 — SDK, model and host-change regression

_Requirements M14, M15. Method A+M. Delivery requirement._

**Setup:** proposed change to SDK, tokens, host layout, output schema, model configuration or content renderer.

**Steps:** compare affected requirements; rerun the core journey and impacted feature cases; inspect announcements on real AT.

**Expected:** changed behaviours have current evidence and no unresolved regression in essential tasks; source and build versions are retained. A previous vendor certificate does not replace integration testing.

**Evidence:** impact assessment and regression matrix.

### T56 — Release controls and rollback

_Requirement M15. Method M. Delivery requirement._

**Setup:** release candidate with results and a simulated critical regression.

**Steps:** apply exit criteria; trace ownership of open defects; rehearse feature disablement or rollback.

**Expected:** accountable approval references evidence, blockers prevent release, rollback restores a tested route, and users retain an accessible way to obtain support. Risk acceptance never relabels a failed criterion.

**Evidence:** release record and rehearsal result.

### T57 — Accessible feedback and continuous review

_Requirement M16. Method A+M+U. Delivery requirement; survey controls have their own applicable WCAG criteria._

**Setup:** feedback routes inside and outside chat.

**Steps:** submit feedback without completing chat, using keyboard and AT; decline optional demographic questions; review the triage workflow.

**Expected:** excluded users can report barriers, participation is optional, self-reported needs are not inferred from behaviour, and feedback has an owner and response process.

**Evidence:** completed submissions and review record.

## 14\. Moderated user-research brief

Research lead: assign before recruitment. Recruit disabled participants with relevant combinations of vision, hearing, speech, motor, cognitive and literacy needs, including people who use screen readers, magnification, voice control or switches. Include sighted participants and people with different digital confidence. Use participants' familiar devices where possible, compensate time, offer breaks and accessible consent, and permit a support person if requested. Do not use simulated disability or synthetic personas as substitutes.

Agree a recruitment matrix and sample rationale against task risk and audience diversity. Do not declare coverage from an arbitrary headcount. Report unrepresented needs. Start with formative rounds, fix observed barriers and retest with affected participants. Stop a session when it is distressing or unsafe; do not require repeated exposure to a known blocker.

Give realistic goals without naming the controls that solve them. Record unaided completion, prompted completion, inability to complete, errors, recoveries, perceived effort, loss of place and trust. Task time is diagnostic, not a universal speed requirement. Avoid comparing disabled participants against a single "normal" speed threshold.

### U01 — Discover help and understand the service

Related cases T01–T04, T32. Task: find help on the host page and decide whether chat is suitable for a realistic question. Expected outcome: the participant finds the service, understands its automated nature and starts or chooses an alternative without facilitator navigation instructions. Capture what caused hesitation or an incorrect expectation.

### U02 — Ask, understand and act

Related cases T08–T14, T32–T37. Task: ask a question with several details, interpret the response and choose the next step. Expected outcome: the participant can express the request, recognise the answer's meaning and limits, inspect a source where offered and take the intended action. Ask them to explain the answer in their own words rather than merely rating clarity.

### U03 — Review while a new message arrives

Related cases T15–T22. Task: find an earlier fact while another answer is generated, then return to the new answer. Expected outcome: the participant keeps their place, detects availability, reaches the new content deliberately and resumes composing. Record announcement overload, navigation effort and any need to restart reading.

### U04 — Recover from a mistake or interruption

Related cases T40–T47. Task: correct a deliberate input error, recover from a network interruption and resume after closing the panel. Expected outcome: the participant understands the problem, can recover without re-entering avoidably lost information and knows whether an action completed. Do not let the facilitator perform the recovery invisibly.

### U05 — Use preferred modes and presentation

Related cases T12, T23–T31, T48–T49. Task: complete a relevant journey with the participant's normal zoom, theme, input and output preferences. Expected outcome: settings remain effective and do not remove controls or require an unwanted mode change. Record fatigue, reach, precision, speech privacy and sensory load as well as completion.

### U06 — Obtain further help and report a barrier

Related cases T50, T52, T57. Task: resolve a question the bot cannot answer and report a difficulty. Expected outcome: the participant finds a usable alternative, understands any queue or delay, controls information transfer and can report the barrier without completing the inaccessible task. If no human service exists, test the actual alternative rather than inventing one.

Use optional questions after each relevant task: "Were you able to finish?", "What made this difficult?", "Did you lose your place or feel rushed?", "Did you use another route?" and "What would make this easier?" Include Not applicable and Prefer not to say where relevant. Provide a route outside the chat and avoid collecting unnecessary diagnoses or sensitive conversation content.

Assess outcomes across use without vision, limited vision, colour-independent use, hearing alternatives, speech alternatives, manipulation, reach, photosensitivity, cognitive support and privacy as relevant. Report concrete barriers, affected tasks and proposed fixes. These themes support research; they are not a conformity checklist or evidence that a legal regime applies.

## 15\. Defect severity, completion and release decision

Use severity based on task impact. Critical: essential service is unavailable to an interaction mode, inescapable trap, serious harmful flashing, or unrecoverable consequential action. High: important information or action is inaccessible, major focus loss, or recovery fails. Medium: repeated confusion, excessive effort or a limited workaround is required. Low: limited friction without loss of essential meaning or action. A workaround does not automatically lower severity; examine burden, privacy and independence.

Proposed exit criteria: all applicable cases executed in their agreed environments; all applicable criterion decisions supported; no unresolved Critical or High barriers; no unresolved baseline failures within a claimed conforming scope; manual announcement and focus checks completed; generated artifacts assessed where shipped; and user-research blockers addressed and retested. Medium and Low delivery findings require a named owner, remediation date and explicit release decision. Unknown results remain unknown.

Report coverage and pass rate separately. Coverage = executed applicable case-environment combinations divided by planned applicable combinations. Pass rate = passed combinations divided by executed combinations with a Pass or Fail result. Report Blocked, Not run and Not applicable counts alongside both so exclusions are visible. Criterion coverage is a separate measure from case coverage.

The release report contains: build and scope; supported environments; methods; coverage; criterion outcomes; task and research findings; defects and affected users; exceptions and limitations; remediation owners; approval; and rollback trigger. Preserve the evidence needed to reproduce each material finding. No product has been tested by producing this brief.

## 16\. WCAG 2.2 A/AA applicability ledger

Create one row per criterion below, with applicability, rationale, environment, evidence, result and owner. These are coverage prompts, not substitute test procedures. The related cases are starting points; add criterion-specific checks wherever their evidence is insufficient. The ledger includes 55 A/AA criteria. SC 4.1.1 is removed in WCAG 2.2; assess it separately if an older contractual baseline requires it.

| **Criteria to assess individually**                                                                                                                                                                   | **Starting cases or additional scope**                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 1.1.1 Non-text Content                                                                                                                                                                                | T36; CAPTCHA alternatives if present                                                                 |
| 1.2.1 Audio-only and Video-only (Prerecorded); 1.2.2 Captions (Prerecorded); 1.2.3 Audio Description or Media Alternative (Prerecorded); 1.2.4 Captions (Live); 1.2.5 Audio Description (Prerecorded) | T49; classify each media item and applicable exceptions                                              |
| 1.3.1 Info and Relationships; 1.3.2 Meaningful Sequence; 1.3.3 Sensory Characteristics; 1.3.4 Orientation; 1.3.5 Identify Input Purpose                                                               | T08, T14, T24, T31, T33, T35, T36, T45                                                               |
| 1.4.1 Use of Color; 1.4.2 Audio Control; 1.4.3 Contrast (Minimum); 1.4.4 Resize Text; 1.4.5 Images of Text                                                                                            | T23, T24, T26, T36, T49                                                                              |
| 1.4.10 Reflow; 1.4.11 Non-text Contrast; 1.4.12 Text Spacing; 1.4.13 Content on Hover or Focus                                                                                                        | T23, T25, T27–T29, T34                                                                               |
| 2.1.1 Keyboard; 2.1.2 No Keyboard Trap; 2.1.4 Character Key Shortcuts                                                                                                                                 | T03–T13, T15, T35                                                                                    |
| 2.2.1 Timing Adjustable; 2.2.2 Pause, Stop, Hide; 2.3.1 Three Flashes or Below Threshold                                                                                                              | T30, T43; check host content too                                                                     |
| 2.4.1 Bypass Blocks; 2.4.2 Page Titled                                                                                                                                                                | T54: inspect repeated host blocks, bypass routes and meaningful page/route titles                    |
| 2.4.3 Focus Order; 2.4.4 Link Purpose (In Context); 2.4.5 Multiple Ways; 2.4.6 Headings and Labels                                                                                                    | T01–T17, T33, T39; T54 checks multiple ways to locate pages within a set, with applicable exceptions |
| 2.4.7 Focus Visible; 2.4.11 Focus Not Obscured (Minimum)                                                                                                                                              | T07, T25, T29, T31                                                                                   |
| 2.5.1 Pointer Gestures; 2.5.2 Pointer Cancellation; 2.5.3 Label in Name; 2.5.4 Motion Actuation; 2.5.7 Dragging Movements; 2.5.8 Target Size (Minimum)                                                | T01, T10, T12, T13, T38                                                                              |
| 3.1.1 Language of Page; 3.1.2 Language of Parts                                                                                                                                                       | T33; inspect host and generated content                                                              |
| 3.2.1 On Focus; 3.2.2 On Input; 3.2.3 Consistent Navigation; 3.2.4 Consistent Identification; 3.2.6 Consistent Help                                                                                   | T02, T09, T10, T50; T54 compares repeated navigation, controls and help across pages                 |
| 3.3.1 Error Identification; 3.3.2 Labels or Instructions; 3.3.3 Error Suggestion; 3.3.4 Error Prevention (Legal, Financial, Data); 3.3.7 Redundant Entry; 3.3.8 Accessible Authentication (Minimum)   | T08, T38, T40, T44–T47                                                                               |
| 4.1.2 Name, Role, Value; 4.1.3 Status Messages                                                                                                                                                        | T01–T22, T34, T35, T38, T40–T50                                                                      |

## 17\. Requirement-to-test traceability

| **Methodology requirement** | **Test coverage**                        |
| --------------------------- | ---------------------------------------- |
| M01 Scope and evidence      | T54; commissioning and ledger            |
| M02 Interaction state model | T19–T22, T40–T47                         |
| M03 Discovery               | T01–T02, U01                             |
| M04 Container and focus     | T03–T07                                  |
| M05 Input                   | T08–T13, U02, U05                        |
| M06 Transcript              | T14–T17, T21, T33, U03                   |
| M07 Announcements           | T16, T18–T22, U03                        |
| M08 Adaptation              | T23–T31, U05                             |
| M09 Understanding           | T32–T34, U01–U02                         |
| M10 Recovery and time       | T22, T40–T47, U04                        |
| M11 Generated content       | T35–T39, T49                             |
| M12 Voice and handoff       | T48–T50, U05–U06                         |
| M13 Privacy and resilience  | T07, T42, T44–T45, T51–T52               |
| M14 Verification            | T53–T55 and all manual/research evidence |
| M15 Release                 | T55–T56 and exit criteria                |
| M16 Continuous improvement  | T57, U01–U06 and regression review       |

## 18\. Reference basis and maintenance

Use with Double FW's Inclusive Chatbot Interfaces Reference version 1.1 and Accessible Branded Chatbot Generation Prompt Template version 1.2, dated 24 September 2026. Criterion terminology follows W3C WCAG 2.2. The related W3C Understanding documents for reflow, contrast, target size, text spacing, timing and accessible authentication inform the measurement cases. WAI-ARIA Authoring Practices, H102, ARIA23 and status-message guidance inform container and notification checks. Bot Framework Web Chat accessibility documentation applies only where that SDK is installed. Record actual versions of axe-core and other test tools in execution evidence.

Review the brief whenever service scope, baseline, supported environments, SDK, model output structures or host integration changes. Version 1.0 establishes 57 test cases, six moderated research scenarios and traceability to 16 methodology requirements. The product owner and QA lead must assign the next review date when adopting the brief.
