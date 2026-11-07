---
title: "Inclusive Game Design: Design Policy Appendix"
version: "1.2.0"
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

This file is a lightweight policy appendix for AI agents and human teams designing, prototyping, reviewing, or iterating games. It is a guide, not a compliance system, release gate, or implementation specification. It applies to mechanics, interfaces, audiovisual design, narrative, onboarding, social play, testing, and post-release changes in a project that adopts it.

The goal is to help teams preserve the intended experience while reducing incidental barriers. Ask: what is essential to the challenge, and what is unnecessary friction or exclusion?

## Authority and limits

- Agents MAY analyse, compare options, identify barriers, suggest alternatives, and make reversible prototypes within the tools and scope available to the task.
- Agents MUST NOT claim to have tested a game, consulted players, approved a release, accepted a design limit, collected personal data, or changed external systems without explicit human authorization.
- Agents MUST distinguish observed evidence, inference, assumptions, and unknowns.
- Agents MUST NOT infer a person’s diagnosis, disability, or needs from behaviour alone.
- If policy or user instructions conflict, follow the higher-priority system or repository instructions and explain the issue instead of silently overriding it.
- If a human owner or escalation path is not known, say so. Do not invent a person, process, or approval.

## Scope

Use this policy when evaluating:

- gameplay goals and challenge design
- inputs, timing, movement, and recovery
- information delivery and cue redundancy
- captioning, narration, audio, visuals, text, and readability
- onboarding, settings, learning, and progression
- narrative portrayal, agency, and representation
- social communication, moderation, and support flows
- accessibility testing and outstanding risks

## Core design principles

### 1. Preserve challenge; reduce unnecessary barriers

Separate essential challenge from incidental demands. A mechanic may require timing, precision, memory, or strategy; it should not silently add avoidable barriers such as poor input support, unclear feedback, or exclusionary pacing.

### 2. Support multiple ways to participate

Consider remapping, alternative inputs, timing adjustments, simplified controls, practice modes, and recovery options. If an access option changes competitive information or performance, assess the actual effect instead of assuming all assistance is invalid.

### 3. Preserve meaning with redundant information paths

Do not rely on a single channel when essential information can be conveyed through another route. Consider captions, descriptions, visual cues, haptics, and readable summaries where appropriate. Avoid revealing hidden information unintentionally.

### 4. Support reading, learning, and comfort

Review text in context: size, legibility, layout, language support, and fallback behaviour. Consider clear instructions, replayable guidance, pacing, and recovery without unfair penalties. Address motion, flashes, vibration, and sensory load when relevant.

### 5. Treat representation and social participation as design concerns

Review how characters, performances, and systems portray disability and identity. Seek relevant lived-experience input when appropriate, without requiring diagnosis disclosure or assuming one person speaks for a group. For social play, consider communication alternatives, readable history, interruption, transparency, and usable help/report routes where relevant.

## Evidence and status

Use status labels only when they are useful and supported by the available evidence:

- pass: supported for the stated scope
- fail: evidence shows the requirement was not met
- unknown: missing or insufficient evidence
- not_applicable: a clear reason exists for exclusion

Important: "pass" does not mean the whole game is accessible. It only means the specific check was supported for its stated scope. A design exception does not convert a fail or unknown into a pass.

For any material finding, distinguish:

- observed facts
- inferences or likely risks
- missing information
- recommendations for next action

## Human review and escalation

Human authorization is required before:

- accepting a remaining design limit
- approving a release
- collecting participant data or involving people in research
- making consequential changes or trade-offs outside the project’s normal scope

Escalate unresolved issues when there is:

- an exclusion that materially affects gameplay access
- unsupported claims or conflicting policy
- hazardous or unsafe content or exposure
- missing owners or missing decision paths
- a decision that needs explicit human accountability

## Suggested assessment format

Use this when no project format is specified:

- Feature / context:
- Intended experience and essential challenge:
- Demands and potential barriers:
- Alternatives and trade-offs:
- Evidence and status:
- Unknowns and limitations:
- Recommendation / next test:
- Human decision or escalation needed:

## Source references

The following external references informed the design principles in this appendix. They are references for context, not executable policies and not proof of compliance:

- S1: Accessible Film, TV and Video Content Creation
- S2: Closed Caption Subtitles
- S3: Drama and Disability
- S4: Accessible Typography for UX and Brand Systems
- S5: POUR for Branding Systems and CX
- S6: Accessible Chatbots

If a source cannot be checked or is uncertain, say so plainly. Do not claim a source was verified when it was not.
