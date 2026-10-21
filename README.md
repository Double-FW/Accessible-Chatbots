# Accessible Chatbots

Prompt templates, retrieval guidance, and reference material for designing, implementing, testing, and continuously improving inclusive chatbot experiences.

## Overview

This repository is a practical knowledge base for teams building accessible conversational interfaces. It supports product delivery, engineering implementation, accessibility review, and ongoing optimisation for chatbot experiences that are usable across a wide range of user needs, devices, and jurisdictions.

The materials are platform-agnostic and intended to be adapted to project-specific design systems, chat SDKs, and host applications. They are designed to support inclusive, reviewable, and defensible delivery decisions rather than to provide a turnkey chatbot implementation.

## Repository contents

| File | Description |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | Repository governance, task rules, source map, retrieval expectations, and delivery instructions for maintainers and contributors. |
| [`Accessible_Branded_Chatbot_Generation_Prompt_Template.md`](Accessible_Branded_Chatbot_Generation_Prompt_Template.md) | A project-input template and implementation brief for generating or reviewing a branded chatbot experience. |
| [`Accessible_Chatbot_Delivery_Methodologies.md`](Accessible_Chatbot_Delivery_Methodologies.md) | Delivery requirements, ownership, governance, and methodology guidance for accessible chatbot work. |
| [`Accessible_Chatbot_Testing_Brief.md`](Accessible_Chatbot_Testing_Brief.md) | Testing strategy, evidence expectations, and QA guidance for accessible chatbot delivery and release. |
| [`Inclusive_Chatbot_Interface_Reference.md`](Inclusive_Chatbot_Interface_Reference.md) | Interaction rationale, interface guidance, and accessibility considerations for chatbot experiences. |
| [`chatbot_RAG.md`](chatbot_RAG.md) | Compact retrieval-augmented generation (RAG) knowledge base covering core rules and chunked guidance. |
| [`Reusable generation prompt.md`](Reusable%20generation%20prompt.md) | Standalone reusable prompt for generating or reviewing chatbot design and implementation work. |
| [`LICENSE`](LICENSE) | Licensing information for the repository. |

## Purpose

The repository supports teams in creating chatbot experiences that are accessible to users with:

- low or no vision
- limited hearing or communication needs
- cognitive or literacy barriers
- motor limitations or alternative input methods
- varying levels of digital confidence and context
- situational barriers such as distraction, noise, or poor connectivity

It focuses on the full lifecycle of delivery: discovery, baseline and legal applicability, design, implementation, testing, release decisions, and ongoing improvement.

## Core themes

The repository addresses key accessibility and usability areas for conversational interfaces, including:

- discoverability and entry-point design
- semantic structure and focus management
- transcript and history navigation
- live announcements and status messaging
- keyboard, touch, and alternative input support
- error recovery and handling uncertainty
- streaming, state transitions, and async updates
- content readability, trust, and clarity
- file, voice, and rich-media considerations
- human handoff and alternative support
- verification, evidence, and release gates

## Typical usage

1. Review the governing guidance in [`AGENTS.md`](AGENTS.md).
2. Use [`chatbot_RAG.md`](chatbot_RAG.md) as the primary compact retrieval source.
3. Choose the relevant template or reference document for the project context.
4. Fill in the generation prompt template with the project-specific inputs.
5. Apply the accessible design and testing guidance in implementation, review, and release decisions.
6. Revisit the relevant checks whenever SDKs, models, renderer behaviour, or host pages change.

## Accessibility baseline

This repository adopts a baseline-first approach to accessibility, with explicit attention to applicability and evidence. It is intended to support decisions grounded in standards such as WCAG 2.2, alongside relevant jurisdictional and sector requirements where applicable.

The repository distinguishes between:

- baseline requirements
- additional delivery requirements
- research and validation activities

It is not a substitute for legal advice or a final conformance statement for any specific product or service.

## Notes

This project is designed as a reusable delivery aid rather than a turnkey chatbot implementation. It is most effective when used alongside product-specific requirements, local code, platform constraints, and accountable human review.

## License

This repository is distributed under the terms of the included [LICENSE](LICENSE).
