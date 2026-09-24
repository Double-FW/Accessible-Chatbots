# Accessible Chatbots

Prompt templates and reference material for designing, implementing, testing and continuously improving inclusive chatbot experiences.

## Overview

This repository provides a practical framework for teams building branded conversational interfaces that are accessible, usable and legally defensible across a range of user needs and jurisdictions.

It is intended for use in product delivery, engineering implementation, accessibility review and ongoing optimisation. The materials are platform-agnostic and can be adapted for bespoke chat interfaces, Microsoft Copilot Studio, Bot Framework Web Chat or other chatbot providers.

## Repository contents

| File | Description |
| --- | --- |
| [`Accessible_Branded_Chatbot_Generation_Prompt_Template.md`](Accessible_Branded_Chatbot_Generation_Prompt_Template.md) | A reusable implementation prompt template to structure chatbot discovery, design, build and review work for inclusive delivery. |
| [`Inclusive_Chatbot_Interface_RAG_Reference.md`](Inclusive_Chatbot_Interface_RAG_Reference.md) | A companion retrieval reference covering inclusive interaction patterns, accessibility requirements, test strategies, rollout and optimisation guidance. |
| [`LICENSE`](LICENSE) | Licensing information for the repository. |

## Purpose

The repository supports teams in creating chatbot experiences that are accessible to users with:

- low or no vision
- limited hearing or communication needs
- cognitive or literacy barriers
- motor limitations or alternative input methods
- varying levels of digital confidence and context

It focuses on the full lifecycle of delivery, from initial architecture and accessibility baseline to test coverage, release planning and user research.

## What the template covers

The generation prompt template includes structured fields for:

- organisation and product scope
- target users, languages and tasks
- site or app context and page links
- frontend framework and tooling
- design system and branding
- chat platform, SDK and version
- RAG sources and assistant behaviour
- presentation variant and entry point
- features and supported environments
- analytics, privacy and feedback
- build, release and research workflows

It also instructs the implementing AI to produce reviewable outputs including:

- implementation code and configuration
- architecture and interaction specification
- focus and transcript navigation flows
- announcement ownership table
- baseline applicability matrix
- test catalogue and automated tests
- manual test script
- user research and survey plan
- release and optimisation plan

## What the reference covers

The companion reference provides guidance on:

- accessible launcher and chat entry-point design
- semantic structure, focus order and keyboard behaviour
- transcript navigation and live updates
- announcements, status messaging and error recovery
- readable content constraints and rich media accessibility
- content safety, privacy and human handoff
- legal baseline mapping for WCAG 2.2, Section 508, EN 301 549 and the European Accessibility Act
- testing approaches and continuous improvement planning

## Typical usage

1. Open the prompt template.
2. Replace each bracketed field with project-specific information.
3. Use the reference as retrieval material for the implementing AI or delivery team.
4. Execute the task in the host application, design system and chatbot platform context.
5. Review the resulting architecture, accessibility baseline, implementation choices and tests before release.
6. Re-run relevant checks whenever SDKs, design tokens, host pages or model outputs change.

## Accessibility baseline

This repository explicitly encourages teams to identify the governing source and version for each project. It supports distinctions between:

- WCAG 2.2 A/AA
- US Revised Section 508
- EN 301 549
- European Accessibility Act requirements

The applicable legal and accessibility baseline should be determined for each product and jurisdiction rather than assumed from a single standard.

## License

This repository is distributed under the terms of the included [LICENSE](LICENSE).

## Notes

This project is designed as a reusable delivery aid rather than a turnkey chatbot implementation. It is most effective when used with product-specific design requirements, local code and platform documentation.
