# Inclusive Games Design

The purpose of this repository is to help teams and AI assistants design, build, test and iterate games that are more accessible, inclusive and enjoyable for a wider range of players.

This project contains a reusable design policy in `AGENTS.md` that can be used as a guidance document for AI-assisted game development. It helps teams ask the right questions about mechanics, sensory demands, communication, representation, testing and player agency before shipping features.

## What is included

- `AGENTS.md` — the core inclusive game design policy and operational guidance
- This README — practical guidance for using the resource in a real game project

## Why this matters

Good accessibility is not just a compliance task. It is a design problem about how players participate, understand, respond, recover and belong. Many barriers in games are not inherent to the genre or experience — they are caused by assumptions about controls, timing, information, reading, audio, social communication and representation.

This resource helps distinguish:

- essential challenge from incidental barriers
- intended experience from accidental difficulty
- player agency from forced exclusion
- meaningful accessibility options from cosmetic adjustments

## How to use this resource when creating games with AI

### 1. Put the policy at the root of the game repository

Copy or reference `AGENTS.md` in the root of the game project you are building. If your AI tool supports a repository-level instruction file, this is the ideal place to set it as a default design policy.

Recommended approach:

- keep `AGENTS.md` in the repository root
- make it part of the project’s source control
- review it with the design, QA and product owners before release

### 2. Treat it as a design lens, not a checklist only

Ask the AI to evaluate each feature using the questions below:

- What is the intended experience and emotional outcome?
- What gameplay demand is essential to that experience?
- What demands are merely friction or exclusion?
- What alternative ways can players participate without removing the core challenge?
- Which sensory, motor, cognitive, reading or communication barriers are introduced?
- What evidence supports the design choice?
- What remains untested or uncertain?

This creates a stronger process than simply asking the AI for “accessibility improvements.”

### 3. Use AI to map player journeys

Ask the AI to review the full journey of a player and document it in stages such as:

- first launch
- settings and onboarding
- learning the controls
- playing the core loop
- failing and recovering
- saving and returning
- communication and support

For each stage, the AI should identify:

- relevant controls and inputs
- audio and visual information
- timing and pacing demands
- reading and language demands
- social or communication demands
- environmental and fatigue considerations

### 4. Ask AI to separate challenge from barrier

A strong prompt is:

“I am creating a [genre] game for [platforms and audience]. Review the mechanic below and separate the essential challenge from incidental demands. Identify likely barriers for players with different input, sensory, cognitive, communication and reading needs. Propose reversible alternatives, explain their impact on the intended experience, and state what evidence is still missing.”

This is much more useful than asking for a generic accessibility pass.

### 5. Use AI to review specific features and mechanics

For each major mechanic, ask the AI to produce a design brief that includes:

- intended experience
- required action and challenge
- barriers or exclusion risk
- alternative input or presentation options
- impact on gameplay and agency
- test plan and evidence gaps

Examples:

- “Review this rhythm game mechanic and identify how audio, timing and visual feedback affect diverse players.”
- “Assess this stealth encounter for subtitle, sound cue and information access needs.”
- “Compare controller remapping, hold-to-repeat, and input timing options for this action system.”
- “Evaluate how this character or narrative portrayal affects agency and representation.”

### 6. Require evidence, not assumptions

The policy emphasises that conclusions must be grounded in traceable evidence. When using AI, ask it to distinguish between:

- known behaviour from tested gameplay
- inferred risk from likely barriers
- missing evidence that must be validated by humans
- design limits that require explicit review

This reduces the risk of the AI inventing “accessibility” without proof.

### 7. Keep a human decision loop

AI can help generate options, compare trade-offs and surface risks, but the final decision still belongs to the responsible human owner. The policy is designed to support human review, not replace it.

The project owner should confirm:

- who owns design decisions
- who reviews evidence
- who decides whether a remaining exclusion is acceptable
- how design limits are recorded and revisited

### 8. Test with real players and diverse contexts

The repository policies stress that accessibility work should be validated with relevant disabled players, not just simulated or automated checks. AI can help plan the research, but it should not replace actual testing.

Ask the AI to help with:

- test scenarios and player journeys
- consent-safe participant screening criteria
- evidence capture templates
- reporting of what was observed versus what was inferred
- prioritisation of remaining issues after testing

## Suggested AI workflow for a game project

A practical workflow for using this repository in a game team could be:

1. Add `AGENTS.md` to the game repository root.
2. Define the core brief:
   - genre
   - platform
   - audience
   - target age range
   - input methods
   - solo/social modes
   - languages and localisation requirements
3. Ask the AI to create a design brief for the game concept.
4. Ask it to map each core mechanic against access demands.
5. Require alternatives for control schemes, communication, reading, audio, haptics and information clarity.
6. Prompt for a risk register and remaining uncertainty.
7. Review the output with designers, QA and inclusion stakeholders.
8. Test with players and update the design based on observed evidence.
9. Record design limits and human decisions before release.

## Example prompts

### Concept review

“Review this game concept for accessibility and inclusion. Identify the essential experience, likely barriers, and the adjustments that preserve the intended challenge without excluding players unnecessarily.”

### Mechanic review

“Assess the combat mechanic for input burden, timing demands, information clarity, sensory load, and recovery options. Suggest several alternative designs and explain how each affects the player experience.”

### Narrative and representation review

“Review the proposed narrative and character portrayal for authenticity, agency, harmful stereotypes, and ability-related representation. Suggest safer, more inclusive alternatives grounded in player experience.”

### UI and reading review

“Audit the HUD, tutorial flow and text-heavy interfaces for typography, language support, contrast, legibility, progressive disclosure, and cognitive load. Prioritise changes by impact and risk.”

### QA and release review

“Create a pre-release accessibility and inclusion review based on the game’s current build. Distinguish evidence-backed findings from assumptions, and list remaining unknowns and escalation items.”

## Good practices when using AI

- Ask for evidence and trade-offs, not just feature suggestions.
- Require the AI to say what is essential vs optional.
- Keep the design brief grounded in the actual audience and platform.
- Ask for multiple alternatives before choosing one.
- Validate final choices with tests and player feedback.
- Record a clear decision trail for design limits and escalations.

## Scope and boundaries

This repository is a game design policy, not a substitute for legal review, platform rules, contractual obligations or a formal accessibility audit. It is intended to support thoughtful design and better AI-assisted decision-making.

It does not claim to implement or guarantee compliance with any single external standard. Instead, it captures game-relevant principles and operational habits that help teams build more inclusive games.

## Repository status

This project is a proposed design and guidance resource. It is intended to be adopted, adapted and reviewed by the team using it.

## Contributing

If you are using this resource in a game project, consider adding:

- a project-specific scope and audience definition
- a list of core mechanics and access risks
- testing notes and evidence summaries
- design decisions and remaining exclusions
- owner assignments for accessibility and release decisions

## License

The repository currently carries the project metadata for the source material and should be reviewed before distribution under a declared licence. This README is intended as a practical project guide and should be aligned with the repository’s chosen legal terms before public release.

## Summary

This resource is best used as a living design policy for AI-assisted game development. It helps an AI reason about player access, challenge, narrative, communication and testing in a way that is grounded in experience and evidence rather than isolated accessibility “ticking boxes.”

If you are building games with AI, use this repository to shape the conversation around inclusion from the beginning, not as a final-stage patch.



























































































































































































































































































































































































































