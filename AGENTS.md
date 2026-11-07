---
title: "Inclusive Game Design: Design Policy Appendix"
version: "1.3.0"
author: "Double FW Ltd"
date: "2026-11-07"
license: "NOASSERTION"
language: "en-GB"
repository: "https://github.com/Double-FW/Inclusive-Games-Design"
artifact_type: "design_policy_appendix"
use_case: "Guide AI and game teams in identifying barriers and improving inclusivity in game design."
status: "proposed"
target_repository: null
---

# Inclusive Game Design — design policy appendix

## Purpose

This file is lightweight policy guidance for AI agents and human teams designing, prototyping, reviewing, or iterating games. It is a guide, not a compliance system, release gate, or implementation specification. The goal is to preserve the intended experience while reducing incidental barriers: ask what is essential to the challenge and what is unnecessary friction or exclusion.

## Repository-specific instructions

- Treat this repository as design guidance, not as a claim that a game is already accessible.
- Separate observed facts, assumptions, inferences, and unknowns; prefer evidence-backed recommendations and clearly label uncertainty.
- Do not claim to have tested a game, consulted players, approved a release, accepted a design limit, collected personal data, or changed external systems without explicit human authorisation.
- Do not infer a person’s diagnosis, disability, or needs from behaviour alone.
- If instructions conflict, follow the higher-priority system, repository, or user instruction and explain the conflict rather than silently overriding it.
- If a human owner or escalation path is unknown, say so plainly; do not invent a person, process, or approval.
- Use the [Agent Routing Guide](Accessible_Game_Technology_Selection_and_Agent_Routing_Guide.md) to find relevant technology and specialist guidance. Select references for the actual game and feature; do not treat every listed resource as mandatory or as proof of implementation or compliance.

## Authority and limits

Agents MAY analyse, compare options, identify barriers, suggest alternatives, and make reversible prototypes within the task’s tools and scope. Agents MUST distinguish evidence from inference and uncertainty. Agents MUST NOT claim human authorisation or player research that did not occur. Consequential decisions—including accepting a remaining design limit, approving release, or collecting participant data—require explicit human authorisation.

## Scope

Use this policy when evaluating gameplay goals and challenge; inputs, timing, movement, and recovery; information delivery and cue redundancy; captions, narration, audio, visuals, text, and readability; onboarding, settings, learning, and progression; narrative portrayal, agency, and representation; social communication, moderation, and support; and accessibility evidence and outstanding risks.

## Core design principles

### 1. Preserve challenge; reduce unnecessary barriers

Separate essential challenge from incidental demands. A mechanic may require timing, precision, memory, or strategy; it should not silently add avoidable barriers such as poor input support, unclear feedback, or exclusionary pacing.

### 2. Support multiple ways to participate

Consider remapping, alternative inputs, timing adjustments, simplified controls, practice modes, and recovery options. If an access option changes competitive information or performance, assess the actual effect instead of assuming all assistance is invalid.

### 3. Preserve meaning with redundant information paths

Do not rely on a single channel when essential information can be conveyed through another route. Consider captions, audio description, visual cues, haptics, and readable summaries where appropriate. Avoid revealing hidden information unintentionally.

### 4. Support reading, learning, and comfort

Review text in context: size, legibility, layout, language support, and fallback behaviour. Consider clear instructions, replayable guidance, pacing, and recovery without unfair penalties. Address motion, flashes, vibration, and sensory load when relevant.

### 5. Treat representation and social participation as design concerns

Review how characters, performances, and systems portray disability and identity. Seek relevant lived-experience input when appropriate, without requiring diagnosis disclosure or assuming one person speaks for a group. For social play, consider communication alternatives, readable history, interruption, transparency, and usable help/report routes where relevant.

## Agent routing guide and practical references

Read the [Accessible Game Technology Selection and Agent Routing Guide](Accessible_Game_Technology_Selection_and_Agent_Routing_Guide.md) to route a task by game type, platform, player journey, and feature. The following specialist repositories are practical references for relevant design decisions. Their inclusion is a routing aid, not a blanket requirement or an assertion that their recommendations have been implemented, tested, or accepted in a particular game. Check each repository’s current README, agent instructions, and other applicable guidance before relying on it.

| Reference | Route when the task involves… |
| --- | --- |
| [Accessible Chatbots](https://github.com/Double-FW/Accessible-Chatbots) | Chat-style interfaces, conversational interactions, dialogue systems, or chatbot-like game features. |
| [Accessible Typography for UX and Brand Systems](https://github.com/Double-FW/Accessible-Typography-for-UX-and-Brand-Systems) | HUDs, menus, subtitles, dialogue, tutorials, text-heavy interfaces, and typography/readability decisions. |
| [VR/XR and AR Accessibility](https://github.com/Double-FW/VR_XR_and_AR_Accessibility) | Immersive, spatial, headset, augmented-reality, or mixed-reality interaction and comfort. |
| [Audio Descriptions](https://github.com/Double-FW/Audio-Descriptions) | Spoken description of visual events or information, including authored or linear sequences where relevant. |
| [Accessible Film, TV and Video Content Production Management](https://github.com/Double-FW/Accessible-Film-TV-and-Video-Content-Production-Management) | Cut scenes, trailers, and other produced/linear video, particularly access-service planning and production handoffs. |
| [Closed Caption Subtitles](https://github.com/Double-FW/Closed-Caption-Subtitles) | Dialogue, speaker identification, music, sound effects, and meaningful audio cues in gameplay, cut scenes, or trailers. |
| [POUR for Branding Systems and CX](https://github.com/Double-FW/POUR-for-Branding-Systems-and-CX) | Broader player-facing experience, communication, and branding decisions across interfaces and journeys. |
| [Data Ethics and Disability](https://github.com/Double-FW/Data_Ethics_and_Disability) | Research, analytics, personalisation, AI, telemetry, or handling of sensitive or disability-related data. |
| [Accessible Charts, Graphs and Maps](https://github.com/Double-FW/Accessible_Charts_Graphs_and_Maps) | Maps, minimaps, charts, graphs, diagrams, dashboards, or complex visual information. |
| [Drama and Disability](https://github.com/Double-FW/Drama-and-Disability) | Portrayal of disability and identity, characterisation, performance, narrative agency, and creative decisions. |

Use a reference only where it applies. Describe the relevance and evidence boundary; do not present a repository link as validation of the game or as a substitute for appropriate human review.

## Evidence and status

Use status labels only when useful and supported for a stated scope:

- `pass`: evidence supports the specific check for its stated scope.
- `fail`: evidence shows the requirement was not met.
- `unknown`: evidence is missing or insufficient.
- `not_applicable`: a clear reason justifies exclusion.

A `pass` does not mean the whole game is accessible. A design exception does not convert a fail or unknown into a pass. For each material finding, distinguish observed facts, inferences or likely risks, missing information, and recommended next action.

## Human review and escalation

Human authorisation is required before accepting a remaining design limit, approving a release, collecting participant data or involving people in research, or making consequential changes/trade-offs outside the task’s normal scope.

Escalate unresolved issues when an exclusion materially affects gameplay access; evidence is unsupported or policies conflict; content or exposure may be hazardous; owners or decision paths are missing; or a decision requires explicit human accountability. If the owner or escalation route is not known, state that it is unknown.

## Suggested assessment format

Use this when no project format is specified:

- Feature / context:
- Intended experience and essential challenge:
- Demands and potential barriers:
- Relevant routing references and why:
- Alternatives and trade-offs:
- Evidence and status:
- Unknowns and limitations:
- Recommendation / next test:
- Human decision or escalation needed:

## Working guidance for AI assistants

When reviewing a game feature or design proposal:

1. Identify the intended experience and essential challenge.
2. Separate core demands from incidental demands.
3. List likely access barriers across motor, sensory, cognitive, communication, reading, and social factors as relevant.
4. Route to specialist guidance only when the game type or feature makes it relevant.
5. Suggest viable alternatives that preserve the intended experience without removing the core challenge.
6. Distinguish observed evidence, risk, assumptions, and missing validation.
7. Recommend a proportionate next human review or test step.

A strong review is specific, testable, and honest about uncertainty. A weak review is generic, assumes access is universal, or presents preference as fact.

## Source references

The linked repositories above are practical starting points, not executable policies for every game and not evidence of compliance. Check the current source, scope, and version before making a claim based on any reference. If a source cannot be checked or its relevance is uncertain, say so plainly. Do not claim a source was reviewed or verified when it was not.
