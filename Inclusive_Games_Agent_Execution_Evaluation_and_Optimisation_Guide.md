# Inclusive games: agent execution, evaluation and optimisation guide

**Prepared for Double FW Ltd · 7 November 2026 · Version 1.0**

**Purpose:** enable an LLM to configure a working process, develop reusable design skills, or define agent roles that apply the Double-FW Inclusive Games Design guidance in a separate video-game project. This is a standalone operating guide, not game code, a repository patch, or a claim that an agent system has been implemented.

## 1. Assessment of the existing repository

**Yes: an agent needs additional operational instructions.** The repository provides a strong design lens and a useful starting workflow. It does not yet supply the project-specific contracts needed to implement, verify and improve a game across platforms. Adding more accessibility principles alone would not close that gap.

Reviewed snapshot: [Double-FW/Inclusive-Games-Design](https://github.com/Double-FW/Inclusive-Games-Design/tree/6e92d8d81be68293b059378639de60b7c8bdaa47), commit `6e92d8d81be68293b059378639de60b7c8bdaa47`. The complete recursive tree contained four files: README.md, AGENTS.md, Accessible Games and other Dynamic Content.md, and LICENSE. The three guidance files were read; this review does not assess licensing terms or any playable build.

The README already describes player journeys, mechanic reviews, evidence, human decisions and iterative testing. AGENTS.md explicitly calls itself a proposed policy appendix rather than an implementation specification or release gate. The longer knowledge base provides detailed thematic instructions. Consequently, the following gaps are **missing operational detail**, not an absence of concern for these subjects.

| Existing source and coverage | Additional instruction needed | Result in an adopting game project |
| --- | --- | --- |
| README: core brief and player journeys | Capture actual engine, platform, devices, modes, environments and tool access; establish the first playable baseline | Project capability brief and scoped test matrix |
| AGENTS.md: essential challenge versus incidental barriers | Turn each mechanic into observable demands, alternatives and acceptance conditions | Traceable mechanic contracts |
| Knowledge base §§2.1–2.4: visual, motor, cognitive and hearing access | Specify complete feature behaviour, dependencies, localisation and test conditions | Implementable feature briefs |
| Knowledge base §§3–4: motion and animation | Resolve native-game applicability; distinguish comfort checks from specialist photosensitivity assessment | Platform-specific comfort and safety plan |
| Knowledge base §§5–7: dynamic UI, timing and multimodal cues | Define UI state, announcement priority, cue semantics and information parity | Testable interaction and information contracts |
| Knowledge base §8 and README testing guidance | Define acceptance thresholds, evidence levels, player research and setting combinations | Outcome assessment with explicit limitations |
| AGENTS.md: evidence statuses and human accountability | Define handoffs, decision ownership and what agents can do with available tools | Reviewable agent workflow |
| README: iteration and post-release changes | Specify issue triage, patch selection, persistence migration, regression and follow-up | Evidence-led optimisation backlog |
| AGENTS.md: representation and social participation | Define narrative review, accessible communication, reporting and mode-specific fairness checks | Inclusion review beyond menus and controls |

Source links: [README](https://github.com/Double-FW/Inclusive-Games-Design/blob/6e92d8d81be68293b059378639de60b7c8bdaa47/README.md), [AGENTS.md](https://github.com/Double-FW/Inclusive-Games-Design/blob/6e92d8d81be68293b059378639de60b7c8bdaa47/AGENTS.md), [knowledge base](https://github.com/Double-FW/Inclusive-Games-Design/blob/6e92d8d81be68293b059378639de60b7c8bdaa47/Accessible%20Games%20and%20other%20Dynamic%20Content.md).

### Interpretations that must be made explicit

- “Any platform” requires a portable process with platform adapters, not identical controls or APIs everywhere. Record unsupported capabilities and provide equivalent routes where possible.
- Keyboard-only testing is valuable on supported keyboard platforms. On a console, touch device or headset, also test the supported alternative input routes and complete navigation without unnecessary simultaneous actions. Do not silently waive an unmet source instruction: record the applicability decision and rationale.
- Respect OS/browser motion preferences where exposed. Where they are unavailable, offer an accessible in-game choice before motion-heavy content. A static web-content alternative cannot automatically substitute for real-time spatial gameplay.
- Pausing a multiplayer world is different from pausing a menu or offline game. Specify safe AFK behaviour, reconnection, input protection and recovery instead of promising a global pause that the game does not support.
- A text equivalent is not necessarily usable during fast play. Delivery timing, direction, priority and cognitive load determine whether an alternative conveys equivalent information.
- Preserve intended challenge, but do not use “essential” to rule out every player-selected assist. Record what the player values about the challenge; offer granular options and explain their effects.
- Do not overwrite an existing game project's AGENTS.md with this repository's policy. Integrate adopted guidance under that project's instruction hierarchy and authorised scope.

## 2. Operating mandate for the adopting LLM

Use the repository as an inclusion policy and this document as an execution method. Work only in the authorised target game project. Do not create workflows, code, agents, configuration or other engineering in the Double-FW guidance repository as a consequence of reading this document.

For each proposed change, connect:

**player goal → demand/barrier → design response → acceptance condition → evidence → remaining limitation → next action.**

Apply these rules throughout:

1. Record observed behaviour, source-backed facts, inferences and unknowns separately. A source-code review or model-generated playthrough is not a hardware test or disabled-player research.
2. Give each requirement, test, finding and patch a stable identifier. Link them rather than duplicating contradictory instructions.
3. Use functional needs and player preferences. Do not infer diagnoses from inputs, settings, mistakes or performance.
4. Keep mandatory access paths available without requiring diagnosis, online profiling or a failed attempt first.
5. Preserve player choice, recoverability and existing access settings. Do not automatically change difficulty or assist strength without an explicit, reversible player choice.
6. Treat a low-use feature as inconclusive: discoverability, inaccessible setup or a small relevant audience may explain low adoption.
7. Use existing project tools where suitable. Do not invent engine support, APIs, owners, test results or approval mechanisms.
8. Follow the adopted policy's human authorisation requirements for research, data collection, release approval and acceptance of remaining design limits. An existing authorisation applies to its stated scope; do not repeatedly seek it for routine work already covered.

## 3. Establish the project and its capabilities

Before implementation planning, produce a brief containing the following. Mark each field as known, assumed or unresolved; identify which unknowns block a decision.

| Area | Required information |
| --- | --- |
| Experience | Genre, core loop, intended emotions, age audience, essential challenges, narrative and social goals |
| Delivery | Target platforms and editions; engine/version; current build; offline, online, co-op and competitive modes |
| Input | Supported devices, remapping limits, adaptive controllers, switches, touch, pointer, keyboard, voice and tracking where relevant |
| Output | Displays and viewing distance; screen narration versus external screen reader support; audio, captions and haptic capabilities |
| Context | Handheld/TV/desktop, noisy/quiet conditions, fatigue, interruptions, cloud latency and device constraints |
| Content | Languages, right-to-left text, user-generated content, chat, cinematics, tutorials and downloadable content |
| Evidence | Existing tests, access complaints, player research, known exclusions, metrics and build provenance |
| Authority | Allowed files/actions, available test tools, research/data permission, actual decision owners and release process |

If no playable build or execution tools exist, complete the design contracts and test plan. Label implementation and runtime results unknown. Continue useful analysis without claiming implementation is complete.

### Platform adapters

For every shipped platform/mode combination, state capability, implementation route, test hardware, fallback, limitation and evidence status.

| Platform/context | Decisions and checks that need an adapter |
| --- | --- |
| PC/native | Gamepad/keyboard/pointer parity; focus when switching windows; display scaling; native UI accessibility integration; device disconnect/reconnect |
| Console/TV | Couch-distance readability; system-reserved controls; supported adaptive input; account/profile changes; suspend/resume; platform narration capabilities |
| Mobile/touch | Small displays, target spacing, gesture alternatives, orientation, external inputs, interruptions, safe areas and thermal/performance changes |
| Browser | Semantic DOM where available; accessible alternatives for canvas/WebGL UI; keyboard escape; browser zoom; exposed OS preferences; permission prompts |
| XR/spatial | Seated play, height/reach calibration, recentering, locomotion and turning choices, tracking loss, one-controller alternatives and alternatives to head/gaze precision |
| Cloud/streamed | Latency and jitter affecting timing; compressed caption readability; local versus streamed settings; disconnection recovery |
| Online/co-op | Per-player preferences; host/client authority; chat alternatives; invitations and reporting; assists' actual effect on competitive information |

Platform availability does not prove an assistive technology works with the engine UI. Test the exact integration. Consult current platform documentation when implementing an adapter.

## 4. Turn guidance into mechanic and feature contracts

Create one contract per meaningful mechanic or journey barrier. Include first launch, account access, settings, onboarding, core play, failure/recovery, save/return, social participation and support. Include alternate branches, bosses, timed sequences, credits and newly introduced mechanics.

Use this reusable record:

```yaml
id: GAME-ACCESS-001
journey_and_mechanic: "State the actual situation"
player_goal: "What the player should be able to accomplish"
intended_experience: "Challenge, emotion and agency to preserve"
source_guidance: "Repository file and section"
scope: "Build, platforms, devices, languages and modes"
demands: ["Perception", "input", "timing", "memory", "communication"]
barrier: "Demand that prevents or degrades participation"
design_response: "Concrete default design and optional adjustments"
setting_dependencies: []
information_parity: "What must be conveyed; what must remain hidden"
acceptance_conditions: []
tests_and_evidence: []
status: unknown
limitations: []
decision_owner: "Actual assigned owner, otherwise unassigned"
next_action: "Specific action needed to reduce uncertainty"
```

The YAML is a documentation template, not a new runtime schema or validation system. Replace its explanatory values before adoption.

### Worked contract: sustained input in an action game

**Goal:** traverse a climbing section while choosing a route and managing hazards. A sustained grip input is an incidental physical demand unless the design team can explain otherwise.

**Response:** offer hold and toggle grip, with a clear state indicator and an accessible way to release. Keep timing/route assistance independently configurable.

**Acceptance conditions:**

- With toggle enabled, one configured activation engages grip and the next releases it; no continuous hold is required during the scripted traversal test.
- Remapped prompts, tutorial instructions and state feedback reflect the active binding and mode.
- Pausing, losing focus or disconnecting the device cannot leave a stuck logical input on return; the expected recovery state is specified and verified.
- The player can change the option and leave settings using the same supported input route.
- Preferences survive a normal restart and the planned patch migration test.
- Relevant players evaluate effort, clarity and agency; report these separately from the technical pass.

**Tests:** action-state tests for transitions; integration checks in the actual traversal; hardware input and reconnect checks; authorised playtests with relevant functional needs. Until run, all results remain unknown.

## 5. Customisation and control design skills

Build skills around reusable reasoning and acceptance patterns. A skill should state its inputs, procedure, outputs, limits and verification method. It should produce a concrete design brief, not a generic list of options.

| Skill | Procedure and candidate features | Evidence required |
| --- | --- | --- |
| Input and fatigue design | Map actions across gameplay and menus; assess one-handed and sequential alternatives; consider remapping, toggle/hold, auto-repeat, sensitivity, dead zones, axis inversion, simplified chords and single-input modes | Reach every required action; test conflicts, prompts, device switching, fatigue and recovery |
| Visual information design | Identify essential objects/states; use shape/text alongside colour; consider text/HUD scaling, contrast, cursor visibility, camera zoom and clutter controls | Readability in actual scenes and viewing conditions; extreme settings and localisation |
| Nonvisual gameplay design | Map essential state and spatial decisions; design narration, navigation/traversal cues and optional assistance with explicit coverage | End-to-end tasks without required visual interpretation; distinguish menu narration from playable nonvisual access |
| Captions and sound design | Inventory dialogue and meaningful sounds; design speaker/direction cues and independent audio categories; prioritise narration and warnings | Muted-audio tasks, overlapping speakers, timing, localisation, cue masking and user comprehension |
| Learning and memory design | Analyse recall and planning demands; consider replayable tutorials, objective history, maps, journals, contextual reminders and optional hints | Return after interruption; find relevant information without forced spoilers or dependence on an inaccessible map |
| Pacing and challenge design | Separate enemy strength, damage, timing windows, speed, recovery, resource pressure and puzzle guidance | Chosen challenge remains meaningful; settings behave independently; no hidden assist escalation |
| Comfort and sensory design | Inventory camera shake, blur, flashes, vibration, particles, camera motion and content triggers; define independent reductions and safe setup | Scene-level checks, first-launch behaviour and specialist assessment where required; never claim universal safety |
| Social and narrative design | Assess voice-only requirements, captions/transcription, pings, text entry, mute/block/report, identity portrayal and agency | Complete representative social journeys; review accuracy, privacy, moderation and representation with relevant expertise |

Not every candidate is relevant to every game. Supply an applicability rationale, a dependency and an outcome test for each selected feature.

### Settings are part of the playable experience

Every setting specification must include:

- Plain-language label; purpose; default; valid range/steps; scope; dependencies; effects on progression or ranked modes; preview and immediate/restart behaviour.
- A reachable setup path before the setting is needed. First-launch narration must not depend on reading an unnarrated menu; sensory reduction must precede avoidable exposure.
- Presets as editable starting points. Show what changes, preserve individual overrides where intended, and provide undo and category-level reset.
- Independent options where needs conflict. Reducing camera motion must not remove essential alerts; reducing music must not silence a navigation cue.
- Persistence boundaries: account, device, save or session. Include guest/shared-device behaviour, cloud conflicts, offline use and local privacy.
- Safe remapping and display recovery. Detect unusable mappings; retain an accessible cancel/revert route that does not itself require a difficult chord or sustained hold.
- Optional personal profiles for different devices or fatigue states, with explicit player selection. Do not label profiles by inferred disability.
- Migration rules for patches: preserve supported values and bindings; explain unavoidable changes; retain a recoverable prior configuration where feasible.

Treat settings proliferation as a usability risk. Improve defaults and access-by-design first; use clear grouping, search where useful, contextual help and practical previews to make optional complexity manageable.

## 6. Learn from established game designs

The following are documented feature examples, not proof that an entire game is accessible or that the same feature will succeed elsewhere. The final column is a proposed transfer and test, not a claim about those games' internal implementation. Check the exact edition, platform and build before relying on feature availability.

| Game and documented pattern | Repository objective | Transferable design experiment and evaluation |
| --- | --- | --- |
| The Last of Us Part II: editable accessibility presets, remapping, narration, navigation/traversal assistance and audio cues [S1] | Multiple input routes; access to visual information; usable setup | Offer coordinated starting profiles with individual overrides. Test whether players can configure them, understand cues and finish the specified journey; do not infer full nonvisual access from narrated menus |
| Forza Motorsport: configurable Blind Driving Assists [S2] | Alternative information paths and player control | Separate cue and assist configuration so players can learn and tune it. Evaluate actionable track information, cue comprehension and agency under the chosen assist configuration |
| Prince of Persia: The Lost Crown: map-linked screenshot Memory Shards and custom parry timing [S3] | Memory support; granular timing adjustment | Prototype a revisit marker and separately adjustable timing window. Measure recall/reorientation and player-selected challenge. Add nonvisual descriptions to a proposed marker design rather than assuming a screenshot addresses blindness |
| Grounded: graded changes to spider appearance without changing gameplay/difficulty [S4] | Sensory choice and comfort | Offer configurable alternative presentation while preserving necessary state cues. Evaluate comfort and comprehension voluntarily; do not assume its name guarantees safety for every player |
| Celeste: later patches expanded rebinding, added toggle grab, changed screen-shake options and removed a conflicting hard-coded restart shortcut [S5] | Motor flexibility; motion control; iterative improvement | Review the whole control system when expanding remapping. Test existing shortcuts, menus and old preferences as well as new bindings; plan migration explicitly |

The useful lesson is to borrow the **design relationship**: configurable cue → interpretable state; memory support → reorientation; timing option → retained agency. Do not copy a menu without testing the outcome it is meant to support.

## 7. Evaluate success at four levels

### 7.1 Coverage and implementation

Maintain a traceability table: requirement ID, source section, platform/mode scope, implementation reference, acceptance test IDs, latest evidence, status and outstanding action.

Use the repository's statuses: `pass`, `fail`, `unknown`, `not_applicable`. Track planned/implemented/retested as separate delivery states. A feature can be implemented with unknown access outcomes. A documented exception never changes a fail into a pass.

Record evidence provenance: build/commit, device/OS, mode, language, settings, date, test procedure, tool or reviewer, observed result and limitations. Retain only authorised participant information.

### 7.2 Technical and integration verification

Use the strongest available method appropriate to the claim:

- Automated/unit checks: settings persistence, mapping validation, action state transitions, localisation completeness and known UI semantics where inspectable.
- Integration/manual checks: actual menu focus, prompts, captions, cue prioritisation, overlays, device recovery, interrupted sessions and representative gameplay.
- Hardware/assistive-technology checks: supported devices, native narration or screen readers, displays, headsets and real deployment conditions.
- Specialist assessment: photosensitivity and other questions that ordinary functional checks cannot settle.

A screenshot cannot prove dynamic focus or narration order. Automated UI checks cannot prove that a player understands a directional cue. Blindfolds, colour simulations and model personas can expose hypotheses; they do not substitute for lived experience.

Test initial launch as well as a configured save. An inaccessible login, settings menu or mandatory tutorial can invalidate otherwise accessible gameplay.

### 7.3 Player outcomes and experience

Involve disabled players during concept and prototype development to shape priorities, then use stable builds for outcome evaluation after routine technical barriers are addressed. Use accessible recruitment, informed consent, paid participation where arranged, voluntary functional-needs disclosure and comfortable stopping conditions. Do not expose people to known hazardous effects to prove a defect.

Define tasks and thresholds **before** evaluating a candidate. Agree them with the real project owner; no universal completion percentage establishes accessibility.

| Measure | Operational definition | Interpretation and guardrail |
| --- | --- | --- |
| Independent task completion | Completed without unplanned external help; player-selected built-in assists count as independent play | Report successful attempts/eligible attempts, settings and reasons for failure |
| Access setup | Time and assistance required to find, configure and recover required settings | Include people unable to finish setup; do not analyse only successful starters |
| Information equivalence | Required state, direction and response are available in the chosen route without unintended hidden information | Assess timeliness and comprehension, not only cue presence |
| Input effort | Forced holds, rapid repetitions, simultaneous actions, errors and self-reported effort/fatigue | Fewer actions alone do not prove a better experience |
| Learning and recovery | Ability to resume a task, identify objectives and recover from mistakes or interruptions | Test after a meaningful interruption and with newly introduced mechanics |
| Agency and enjoyment | Separate, consistently worded ratings and participant explanations of control, intended challenge and satisfaction | Never substitute raw engagement or time played for enjoyment |
| Comfort | Voluntary ratings and stop/avoidance reports in the tested conditions | A comfortable session does not certify medical safety |
| Social participation | Ability to join, communicate, understand team cues and use mute/report/help | Test the route used by the group, not only an isolated chat widget |

Report by relevant functional need, device, mode and selected configuration when consent and sample size permit. Support intersections such as limited vision plus hearing loss or motor fatigue plus narration use. Avoid publishing identifiable small groups.

Use counts and distributions alongside averages. Document recruitment gaps and confidence limits; a small study is formative evidence, not proof of population-wide equivalence. For version comparisons, account for learning, order and task differences. Do not claim a causal uplift from uncontrolled telemetry.

### 7.4 Decision and acceptance

Provide a scoped conclusion for each target journey:

1. Which acceptance conditions passed, failed or remain unknown?
2. Can the intended players complete the journey using their preferred supported routes?
3. What happened to agency, effort, comprehension, comfort and enjoyment?
4. Which modes, intersections, languages, devices or sections remain untested?
5. Which exclusions need an accountable decision or further work?

Do not produce a single “accessibility score” that hides a critical blocker. Recommend release readiness only within the evidence scope; the accountable human makes the release and remaining-limit decisions.

## 8. Test interacting settings and failure states

Use risk-based combinations rather than pretending all configurations can be exhaustively tested. Pairwise coverage can help with breadth; explicitly add higher-order combinations where failure would block access.

| Combination or transition | Failure to look for |
| --- | --- |
| Large text + long translation + captions + HUD scaling | Clipping, occlusion, unreachable controls and lost information |
| Remapping + toggle actions + simplified controls | Conflicting shortcuts, wrong prompts, inaccessible cancel/release |
| Reduced motion + high contrast + visual sound cues | Essential cues removed or cluttered; state confused with decoration |
| Narration + spatial audio + dialogue + warning | Queue delay, masking, stale announcements and missed decisions |
| No audio + captions + directional indicators | Missing sound events, ambiguous source/direction and unreadable timing |
| One-handed route + menu + timed interaction | Inaccessible transitions or required simultaneous input |
| Assist enabled + boss/cutscene/tutorial + save/reload | Progression blocked or setting ignored outside the core loop |
| Local co-op + separate profiles + online host | One player's preferences override another's; host-only capability |
| Patch + older save + custom bindings + cloud conflict | Preferences reset, invalid values or inaccessible recovery |

For each failure, preserve a repeatable test scenario in the target game's existing test system or documented procedure. Include performance and latency checks when extra narration, overlays or effects change timing.

## 9. Plan and evaluate optimisation patches

A patch is a hypothesis about a player outcome. It is not successful merely because new options ship.

### Triage

Classify each finding as a defect, missing access path, usability/discoverability problem, preference opportunity, unsupported assumption or accepted limit requiring revisit.

Prioritise, in order:

1. Safety concerns and complete access blockers, including regressions and inaccessible recovery.
2. Essential-information loss and repeated high-effort barriers.
3. Partial access, comprehension and settings-discovery problems.
4. New personalisation opportunities and convenience improvements.

Within a tier, consider severity, affected journey, evidence confidence, dependencies, feasible effort and reversibility. Investigate high-impact unknowns; do not downgrade rare needs simply because telemetry is sparse.

### Patch planning record

```text
Patch ID and linked finding/requirement/test IDs:
Affected players, journey, platforms, builds and modes:
Observed evidence and unresolved assumptions:
Outcome hypothesis:
Options considered and reason for selection:
Default behaviour and optional customisation:
Dependencies and implementation boundary in the target game:
Information/fairness, privacy and performance considerations:
Preference/save migration and recovery approach:
Acceptance conditions and planned regression combinations:
Before/after evaluation method and success thresholds:
Actual owner and any required decision:
Rollout, rollback and accessible player communication:
Post-patch review trigger and remaining work:
```

### Close the loop

Reproduce the issue; establish the baseline; propose alternatives; select a scoped change; implement within authorisation; run targeted and relevant regression tests; conduct authorised player evaluation; compare outcomes; report residual limits; obtain any required release decision; monitor authorised feedback after rollout.

Reopen the finding if the outcome fails even when all code-level tests pass. Trigger a fresh assessment after new mechanics, platform ports, input changes, engine upgrades, localisation, UI redesigns and relevant complaints.

Never run an experiment that withholds a known essential access route or safety fix. If comparing optional designs, keep working access paths available and allow an accessible exit. Collect only approved, necessary data; preference usage is not a diagnosis. Do not autonomously expand telemetry to discover disability categories.

## 10. Example optimisation hypothesis

**Hypothetical finding:** players returning to an exploration game cannot remember why a route was blocked. There is no evaluated game build in this review; the example contains no actual participant results.

**Baseline task:** after an interruption, locate a previously encountered blocked route and identify what is needed to revisit it. Record completion, unplanned help, reorientation time, errors and perceived control.

**Design candidates:** manual map notes; a map-linked image; an optional marker with accessible text and narration describing the obstacle and known requirement. Preserve discovery by recording only information the player has already learned. Treat automatic spoiler-revealing hints as a separate, explicit choice.

**Selected prototype:** a player-created marker, searchable in an accessible list, with optional image, plain-language note and jump-to-map location. This extends the Memory Shards pattern; it is not a claim about features present in Prince of Persia.

**Proposed acceptance:** create/read/edit/delete without a pointer-only action; use the chosen input route; read or hear the marker's information; retain it through restart/migration; preserve the source location; avoid exposing undiscovered objectives. The team must set study thresholds before comparison.

**Evaluation:** compare baseline and candidate with comparable tasks and account for learning effects. Include memory-related access needs, nonvisual use and relevant intersections. Check whether comprehension and independence improve without unwanted hand-holding or extra settings burden.

**Further patch decisions:** if the marker helps recall but is hard to find, improve discoverability before adding more features. If creation is too effortful, test an optional simplified capture flow. If image-only information excludes nonvisual use, fix the information path before declaring the feature complete.

## 11. Configure a process, skill or agent system

One LLM may perform the roles sequentially. Multiple agents are optional; this guide does not require spawning agents, extra infrastructure or code generation.

| Role | Inputs | Required output and handoff |
| --- | --- | --- |
| Coordinator | Brief, policy, authorisation and evidence inventory | Scoped plan, assigned work, unresolved decisions and consolidated traceability |
| Inclusive design | Mechanics, player goals and relevant examples | Barrier analysis, alternative designs and testable contracts for implementation |
| Platform/implementation | Approved contracts and actual project capabilities | Target-game implementation plan/change references, limitations and verification needs |
| Verification | Contracts, candidate build and platform matrix | Reproducible checks, scoped findings and evidence; no invented pass results |
| Player-research synthesis | Authorised research plan and supplied observations | Outcome analysis, uncertainty, intersections and design implications |
| Optimisation | Findings, outcomes and constraints | Prioritised patch hypotheses, regression plan and reassessment triggers |

A handoff must include IDs, scope, source versions, evidence locations, assumptions, unresolved dependencies, next action and acceptance criteria. Maintain one authoritative requirement/evidence record. A second model's agreement is a review opinion, not independent runtime evidence or lived-experience validation.

For a reusable skill, package one bounded procedure from §5 with a worked example, output contract and stopping conditions. For an agent definition, add actual tool permissions, inputs, outputs, decision limits and handoff recipient. Do not assign authority merely by giving a role a title.

### Ready-to-use instruction for an LLM

> Apply the Double-FW Inclusive Games Design repository and this execution guide to the authorised target game project. First identify the game brief, platform and tool capabilities, applicable project instructions, existing evidence and missing decisions. Do not modify the Double-FW guidance repository.
>
> Select an implementation form appropriate to the request: a documented process, reusable design skill, agent role definition, or authorised work in the separate game project. Do not create infrastructure merely because it might be useful.
>
> Map the complete player journey and core mechanics. Separate essential challenge from incidental demands. Produce traceable design contracts with functional needs, platform applicability, customisation behaviour, acceptance conditions and evidence methods. Use the established-game examples as testable inspiration, not universal solutions or proof of success.
>
> Evaluate implementation, integrated behaviour and player outcomes separately. Run only the checks that available tools and authorisation support. Mark unavailable tests and player evidence unknown. Include interacting settings, first launch, recovery, persistence and patch migration. Preserve the player's control over assists and preferences.
>
> Turn findings into a prioritised patch plan containing outcome hypotheses, alternatives, acceptance criteria, regressions, migration, rollback and follow-up evaluation. Distinguish proposed work from implemented work and verified outcomes. Escalate decisions requiring accountable human judgement under the adopted policy, using the actual owner where known.
>
> Return: project scope; repository-to-project mapping; design contracts; platform matrix; skill/process/agent definitions requested; evidence-based findings; success assessment with limitations; and prioritised optimisation patches. If information is missing, complete independent work and identify the precise blocked decision. Never invent a build, participant, API, owner, result or approval.

## 12. Definition of a useful result

The operating material is ready for adoption when another LLM can identify what to do next, in which project, with which authority, against which acceptance criteria and using what evidence. Each material recommendation must lead to a testable outcome or an explicit decision.

The game itself is not declared successful by that document's completion. Success requires supported player journeys, usable customisation, player-selected challenge, measured experience outcomes and candid reporting of remaining exclusions within the tested scope.

## Sources and evidence limits

Repository analysis is tied to the commit above. External sources were consulted on 7 November 2026. Feature summaries below are deliberately narrow. Publisher documentation supports the existence and intended behaviour of features; it does not establish effectiveness for every player or platform. Recommendations, templates, thresholds policy and workflow structure in this document are the proposed operational extension.

- **S1 — PlayStation / Naughty Dog:** [The Last of Us Part II accessibility options](https://www.playstation.com/en-ie/games/the-last-of-us-part-ii/accessibility/). Source for presets, individual adjustment, controls, narration and navigation/traversal features.
- **S2 — Forza Support:** [Forza Motorsport Accessibility Support](https://support.forza.net/hc/en-us/articles/20964254277267-Forza-Motorsport-Accessibility-Support). Source for configurable Blind Driving Assists.
- **S3 — Microsoft Game Dev, interview with Ubisoft senior game designer Rémi Boutin, 5 March 2025:** [How Ubisoft Made Prince of Persia: The Lost Crown Its Most Accessible Game Ever](https://developer.microsoft.com/en-us/games/articles/2025/03/prince-of-persia-the-lost-crown-accessibility/). Source for Memory Shards and adjustable parry timing. The developer describes playtesting and tracking; no player-outcome percentage is used here as an efficacy benchmark.
- **S4 — Obsidian, 25 July 2020:** [Grounded accessibility features](https://grounded.obsidian.net/news/grounded/accessibility-features). Historical primary-source example of graded spider presentation; not a current cross-edition inventory.
- **S5 — Extremely OK Games / Celeste:** [Official changelog](https://www.celestegame.com/changelog.html), particularly v1.4.0.0. Source for control, toggle-grab, screen-shake and shortcut changes. The same notes state bindings reset in that update; preserving/migrating bindings in this guide is a recommendation, not a description of that patch.
- **S6 — Microsoft:** [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines). Supplementary implementation/test reference covering input, information channels, captions, narration, timing, UI and other areas. These are best-practice guidelines, not a legal compliance checklist. Select and verify relevant individual guidelines when adopting detailed criteria; this document does not claim an exhaustive XAG audit.

No game was executed and no player research was conducted for this review. Runtime performance, platform integration, actual player outcomes and release readiness remain matters for the adopting project to establish.
