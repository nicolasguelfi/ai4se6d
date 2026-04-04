# Production Plan — Module ai4se6d_vibecoding (Complete Edition)

## Metadata

| Field | Value |
|-------|-------|
| Project name | ai4se6d_vibecoding |
| Document type | presentation |
| Design guideline | `maximize-viewport` |
| Template | presentation |
| Source document | `ul-ai-4-se/sota-ai-4-se-EN.tex` |
| Context | Day 1, Session 1 — Part 2 (after ai4se6d_genai_intro) |
| Training | "VibeEngineering: The Future of Software Development with Generative AI" |
| First delivery | April 9, 2026 — DLH Luxembourg |
| Date of this plan | 2026-04-03 |
| Central metaphor | The Starred Kitchen (see `docs/metaphor-starred-kitchen.md`) |
| Total slides | ~65 |
| Total blocks | 32 |
| Exercises | 2 (18 min total) |
| Audience interactions | 3 |
| AI images needed | ~30 |
| Estimated duration (all slides) | ~70 min (skippable sections allow 45-60 min delivery) |

---

## Design Guideline: maximize-viewport

### Active Rules

| Rule | Specification |
|------|---------------|
| Philosophy | Every pixel serves the content — no artificial void |
| P1 | Content expands to fill the viewport (font size is the primary lever) |
| P2 | One clear visual hierarchy per slide (dominant element 1.5x larger) |
| P3 | Images fill their allocated zone completely (object-fit: cover) |
| P4 | All content centered by default (`st_block(s.center_txt)`) |
| P5 | Spacing serves rhythm, not fill |
| Min font | 24pt (absolute minimum for projection) |
| Viewport | 16:9, dark theme (#1A1A2E), paginated, hidden slide breaks |

### Named Patterns Used

| Pattern | Description | Blocks Using It |
|---------|-------------|----------------|
| **stat-hero** | Giant statistic (GIANT/Giant) + supporting text + source | danger slides, reality check, evidence |
| **spectrum-bar** | Horizontal gradient bar with labels at extremes | review habits, spectrum overview |
| **exercise-flow** | 3-phase: briefing → timer → debrief | exercises 2 & 3 |
| **table-roadmap** | Responsive grid with bordered colored cells | spectrum levels, IDE comparison, recap roadmap |

### Slide Type Templates

| Type | Layout | Font Sizes |
|------|--------|------------|
| **Billboard** | Centered in 85vh, single phrase | Giant (128pt) or GIANT (196pt) |
| **Balanced** | 2-col grid: image 40% + text 60% | Title Huge (80pt), body Large (48pt) |
| **Stat-hero** | Centered number + subtitle + source | Number GIANT (196pt), subtitle Large (48pt) |
| **Content list** | Title + ordered/unordered list, fills viewport | Title Huge (80pt), items Large (48pt) |
| **Image-dominant** | Image 70-80% + title/caption | Title Huge (80pt), caption large (32pt) |
| **Table** | Full-width table-roadmap pattern | All cells Large (48pt) |

### Graphic Line — AI Image Generation

| Rule | Specification |
|------|---------------|
| Background | Pure dark (#1A1A2E) |
| Colors | Primary #7AB8F5, Accent #2EC4B6, Highlight #F39C12, White |
| Style | Flat vector / soft gradients — NO photorealism |
| Text in images | NEVER |
| Balanced slides | Portrait 2:3 (`ai_size="1024x1536"`) |
| Image-dominant | Landscape 16:9 (`ai_size="1536x1024"`) |

**Master Prompt Prefix** (prepend to ALL image prompts):
> "Minimalist digital illustration on a pure dark background (#1A1A2E). Flat vector style with soft gradients. Limited color palette: electric blue (#7AB8F5), teal (#2EC4B6), amber (#F39C12), white (#FFFFFF). Clean geometric shapes, no text, no watermarks, no photorealism. Ample negative space. Professional and modern aesthetic, suitable for tech conference projection."

**Master Prompt Suffix — Balanced slides**:
> "No text, no letters, no words, no labels, no watermarks. 2:3 portrait aspect ratio. Dark background #1A1A2E."

**Master Prompt Suffix — Image-dominant slides**:
> "No text, no letters, no words, no labels, no watermarks. 16:9 aspect ratio. Dark background #1A1A2E."

---

## Central Metaphor: The Starred Kitchen

This module **formally introduces** the kitchen metaphor that runs across all 6 training days (see `docs/metaphor-starred-kitchen.md` for the full reference).

The metaphor is woven into the narrative at 5 key moments — never forced, never over-explained:

| Moment | Where | What | How |
|--------|-------|------|-----|
| **Seeding** | Act I, slide 10 | Paradigm shift | "You're no longer cooking — you're ordering at a restaurant" (1 sentence) |
| **Exercise framing** | Exercise 2 intro | Exercise context | "Cook at home, any way you like" (exercise subtitle) |
| **Pivot** | Act II, danger intro | Emotional turn | "Now imagine cooking the same way for a gala dinner at a starred hotel" (billboard) |
| **Principles framing** | Act III, VibeEng intro | Discipline = chef | "The 6 principles are what separates a home cook from a starred chef" (1 sentence) |
| **Closing** | Key message | Training arc | "Same ingredients, same kitchen. The difference: the discipline of the chef." |

All other slides use the metaphor vocabulary **only when it maps naturally** (mise en place for context engineering, brigade for multi-agent, etc.) — never with explicit explanation.

---

## Narrative Arc

```
OPENING — Ice-breaker & Self-Assessment
  ├── Title
  ├── AI Usage Habits (audience interaction)
  └── Code Review Habits (audience interaction)

ACT I — VIBECODING: THE CONCEPT
  ├── Origins (Karpathy, timeline, dictionary)
  ├── Paradigm Shift (from cook to customer) ← metaphor seeded
  ├── 4 Principles (intent, trust, conversation, low barrier)
  └── Historical Analogy (compilers, trust transfer, critical difference)

INTERLUDE — EXERCISE 2: PURE VIBECODING (10 min)
  "Cook at home, any way you like" ← metaphor framing

ACT II — THE REALITY CHECK
  ├── Billboard: "It Works... But at What Cost?"
  ├── 5 Dangers (vulnerabilities, hallucinated deps, tech debt, AI paradox, demo vs prod)
  ├── Pivot: "Would you cook like this for a gala?" ← metaphor pivot
  ├── Industry Data (Anthropic, Bain)
  ├── Legitimate Use Cases
  └── Bridge: "Speed AND Quality?"

ACT III — VIBEENGINEERING: THE DISCIPLINE
  ├── Transition (audience interaction)
  ├── Rebranding: Coding → Engineering
  ├── 6 Principles as chef's discipline ← metaphor framing
  │     (menu = requirements, tasting = TDD, recipe = architecture,
  │      courses = iteration, HACCP = review, mise en place = context)
  ├── 4-Level Spectrum (home → friends → bistro → starred hotel)
  └── Evidence (FlowGen study)

INTERLUDE — EXERCISE 3: REDO WITH DISCIPLINE (8 min)
  "Same dish, but for the gala" ← metaphor callback

ACT IV — THE TOOL ECOSYSTEM
  ├── The Autonomy Spectrum (5 levels)
  ├── The Agentic Turn (2024-2026)
  ├── Cursor = your professional kitchen, brigade = agents ← light reference
  ├── Claude Code
  ├── Windsurf + GitHub Copilot
  ├── Comparison Matrix
  ├── MCP = certified suppliers ← light reference
  └── Why Cursor for This Training

CLOSING
  ├── Recap: GenAI
  ├── Recap: VibeCoding → VibeEngineering
  ├── Road Ahead (6-day preview)
  ├── Key Message: "Same kitchen, same ingredients. Different discipline." ← metaphor closing
  ├── Questions?
  └── Glossary
```

---

## Slide-by-Slide Content Plan

### Legend

- **Source ref** = line numbers in `sota-ai-4-se-EN.tex`
- **Layout** = slide type from design guideline
- **Image prompt** = MASTER PREFIX + specific + MASTER SUFFIX
- **Pattern** = named pattern from design guideline
- **Skippable** = can be dropped without breaking narrative flow

---

## OPENING — Ice-breaker & Self-Assessment

---

### Block 1 — `bck_title` (1 slide)

#### Slide 1 — Title

| Field | Value |
|-------|-------|
| **Title** | Discovering VibeCoding & VibeEngineering |
| **Content** | Subtitle: "Session 1 — Part 2 · AI for Software Engineering". Training context, DLH Luxembourg. |
| **Layout** | Image-dominant: hero image fills slide, title overlaid in Huge (80pt), subtitle in Large (48pt) |
| **Source ref** | Training program |
| **Image prompt** | MASTER PREFIX + "Split composition: left side shows casual, chaotic code fragments scattered loosely in teal (representing VibeCoding). Right side shows the same code fragments organized into a precise geometric structure in electric blue with amber accent lines (representing VibeEngineering). A subtle gradient divides the two halves." + MASTER SUFFIX (landscape) |
| **Status** | DONE |

---

### Block 2 — `bck_intro_review_habits` (4 slides)

#### Slide 2 — How much of your code is AI-generated?

| Field | Value |
|-------|-------|
| **Title** | How Much of Your Code Is AI-Generated? |
| **Layout** | Billboard: single question centered, Giant (128pt), accent color |
| **Source ref** | — (audience interaction) |
| **Image prompt** | — (text only) |
| **Status** | DONE |

#### Slide 3 — AI Usage Spectrum

| Field | Value |
|-------|-------|
| **Title** | Where Do You Stand? |
| **Content** | Spectrum-bar gradient 0% → 100%. Labels: "I write everything myself" ↔ "AI generates most of my code". |
| **Layout** | Pattern: **spectrum-bar** |
| **Source ref** | — (audience interaction) |
| **Image prompt** | — (pattern, no image) |
| **Status** | DONE |

#### Slide 4 — Do you review AI-generated code?

| Field | Value |
|-------|-------|
| **Title** | Do You Review AI-Generated Code? |
| **Layout** | Billboard: single question centered, Giant (128pt) |
| **Source ref** | — (audience interaction) |
| **Image prompt** | — (text only) |
| **Status** | DONE |

#### Slide 5 — Review Spectrum

| Field | Value |
|-------|-------|
| **Title** | The Review Spectrum |
| **Content** | Spectrum-bar gradient Never → Always. Note: "Your answer will evolve by the end of this training." |
| **Layout** | Pattern: **spectrum-bar** |
| **Source ref** | Lines 528-533 |
| **Image prompt** | — (pattern, no image) |
| **Status** | DONE |

---

## ACT I — VIBECODING: THE CONCEPT

---

### Block 3 — `bck_vibecoding_origin` (3 slides)

#### Slide 6 — Karpathy 2023: The New Programming Language

| Field | Value |
|-------|-------|
| **Title** | Andrej Karpathy, 2023 |
| **Content** | Quote: "The hottest new programming language is English." First signal that natural language would replace traditional coding for many tasks. |
| **Layout** | Balanced: image left (40%), quote right (60%) in italic Large (48pt), attribution in caption large (32pt) |
| **Source ref** | Lines 524-525 |
| **Image prompt** | MASTER PREFIX + "A glowing keyboard with letters floating upward and transforming into natural language words in electric blue. The keys dissolve into conversational phrases. Amber highlights on key letters." + MASTER SUFFIX (portrait) |
| **Status** | DONE |

#### Slide 7 — Karpathy 2025: VibeCoding Is Born

| Field | Value |
|-------|-------|
| **Title** | February 2025: VibeCoding |
| **Content** | Quote: "You just see stuff, say stuff, run stuff, and copy-paste stuff, and it mostly works." Karpathy names the practice that millions were already doing. |
| **Layout** | Balanced: image left (40%), quote + context right (60%) |
| **Source ref** | Lines 524-525 |
| **Image prompt** | MASTER PREFIX + "A casual, flowing river of code fragments in electric blue, moving effortlessly from left to right with no structure or organization. Teal sparkles suggest ease and speed. The flow feels natural, almost lazy." + MASTER SUFFIX (portrait) |
| **Status** | DONE |

#### Slide 8 — Collins Dictionary Word of the Year

| Field | Value |
|-------|-------|
| **Title** | Word of the Year 2025 |
| **Content** | "VibeCoding" — Collins English Dictionary. From tweet to mainstream vocabulary in months. The term captured a cultural shift in how developers relate to code. |
| **Layout** | Balanced: managed image (dictionary visual) + text |
| **Source ref** | Lines 524-525 |
| **Image prompt** | — (managed image: vc_origin) |
| **Status** | IN PROGRESS (image versions v1-v8 exist, needs final selection) |

---

### Block 4 — `bck_vibecoding_definition` (1 slide) — NEW

#### Slide 9 — Formal Definition

| Field | Value |
|-------|-------|
| **Title** | VibeCoding — Definition |
| **Content** | "A practice where developers describe tasks to LLMs, accept generated code without closely reviewing its internal structure, and rely on results and follow-up prompts to guide changes." Key phrase highlighted: "without closely reviewing." |
| **Layout** | Content: definition centered in Large (48pt), key phrase in Huge (80pt) highlight color |
| **Source ref** | Lines 525-526 |
| **Image prompt** | — (text only, definition slide) |
| **Skippable** | No |

---

### Block 5 — `bck_vibecoding_paradigm` (2 slides) — NEW

> **Metaphor moment: SEEDING** — This is where the kitchen metaphor is introduced, in one natural sentence. No heavy explanation.

#### Slide 10 — From Cook to Customer

| Field | Value |
|-------|-------|
| **Title** | From Cook to Customer |
| **Content** | Traditional SE: you are the **cook** — you choose the ingredients, follow the recipe, control every step. VibeCoding: you become the **customer at a restaurant** — you describe what you want, the kitchen prepares it, you taste the result. You don't need to know the recipe. The implementation stays behind the kitchen door. |
| **Layout** | Balanced: image left (40%), two contrasting roles right (60%) with keyword+body pairs |
| **Source ref** | Line 538 |
| **Image prompt** | MASTER PREFIX + "Split composition: left side shows a figure cooking at a stove, hands busy, surrounded by ingredients in teal. Right side shows a figure seated at an elegant restaurant table, a finished plate arriving, in electric blue and amber. A bold arrow from left to right." + MASTER SUFFIX (portrait) |
| **Skippable** | No |
| **Metaphor note** | First mention of the kitchen metaphor. Delivered as a natural analogy, not as "our metaphor for today is...". The audience absorbs it without noticing it's been planted. |

#### Slide 11 — What Changes, What Stays

| Field | Value |
|-------|-------|
| **Title** | What Changes, What Stays |
| **Content** | What changes: you stop writing every line. You express intent. What stays: you're still responsible for the result. A customer who gets food poisoning doesn't blame themselves — but a professional who serves it does. The question: which one are you? |
| **Layout** | Content: two columns (Changes / Stays) filling viewport, provocative closing question in highlight |
| **Source ref** | Line 538 |
| **Image prompt** | — (text only, provocative) |
| **Skippable** | Yes (reinforces paradigm shift, not critical) |

---

### Block 6 — `bck_vibecoding_intent` (1 slide) — NEW

#### Slide 12 — Principle 1: Intent over Implementation

| Field | Value |
|-------|-------|
| **Title** | 1. Intent over Implementation |
| **Content** | "The developer describes WHAT they want, not HOW to build it." You specify the goal. The AI determines the implementation. The shift: from writing code to expressing intent. |
| **Layout** | Balanced: image left (40%), principle heading in Huge (80pt) + explanation in Large (48pt) right (60%) |
| **Source ref** | Line 528 |
| **Image prompt** | MASTER PREFIX + "A thought bubble in amber floating above, connected by a beam of light down to a code block in electric blue below. The thought bubble is large and prominent, the code block smaller and subordinate." + MASTER SUFFIX (portrait) |
| **Skippable** | No |

---

### Block 7 — `bck_vibecoding_trust` (1 slide) — NEW

#### Slide 13 — Principle 2: Trust in Output

| Field | Value |
|-------|-------|
| **Title** | 2. Trust in Output |
| **Content** | "The developer accepts generated code based on whether the application WORKS, not on whether the code is correct, efficient, or maintainable." If it runs and passes tests = good enough. The code itself is not read. |
| **Layout** | Balanced: image left (40%), principle heading in Huge (80pt) + explanation in Large (48pt) right (60%) |
| **Source ref** | Line 529 |
| **Image prompt** | MASTER PREFIX + "A glowing checkmark in amber hovering over a code window in electric blue. The code lines are blurred and abstract (unread). The checkmark is crisp and confident." + MASTER SUFFIX (portrait) |
| **Skippable** | No |

---

### Block 8 — `bck_vibecoding_conversation` (1 slide) — NEW

#### Slide 14 — Principle 3: Conversational Iteration

| Field | Value |
|-------|-------|
| **Title** | 3. Conversational Iteration |
| **Content** | "Errors are addressed by describing the problem back to the LLM rather than by reading and debugging the code directly." Bug? Describe the symptom. The AI fixes it. No need to understand the implementation. |
| **Layout** | Balanced: image left (40%), principle heading in Huge (80pt) + explanation in Large (48pt) right (60%) |
| **Source ref** | Line 530 |
| **Image prompt** | MASTER PREFIX + "A spiral conversation pattern: alternating speech bubbles in electric blue (human) and teal (AI), spiraling inward toward a solution point in amber at the center. Each iteration is closer to the center." + MASTER SUFFIX (portrait) |
| **Skippable** | No |

---

### Block 9 — `bck_vibecoding_low_barrier` (1 slide) — NEW

#### Slide 15 — Principle 4: Low Barrier to Entry

| Field | Value |
|-------|-------|
| **Title** | 4. Low Barrier to Entry |
| **Content** | "Non-programmers can produce functional prototypes, blurring the traditional boundary between developers and non-developers." Anyone with an idea can build a working prototype. The democratization of software creation. |
| **Layout** | Balanced: image left (40%), principle heading in Huge (80pt) + explanation in Large (48pt) right (60%) |
| **Source ref** | Line 531 |
| **Image prompt** | MASTER PREFIX + "A wide-open gate made of simple geometric lines in electric blue, with diverse abstract human silhouettes of varying sizes walking through. No walls on either side. Amber glow at the threshold." + MASTER SUFFIX (portrait) |
| **Skippable** | Yes (can be mentioned verbally) |

---

### Block 10 — `bck_vibecoding_analogy` (2 slides)

#### Slide 16 — The Historical Parallel

| Field | Value |
|-------|-------|
| **Title** | Assembly → High-Level Languages (1960s) |
| **Content** | "When high-level languages replaced assembly, programmers lost direct control over machine instructions — and gained enormous productivity. The compiler became a trusted intermediary." History repeats: VibeCoding proposes an analogous trust transfer from the developer to the LLM. |
| **Layout** | Balanced: image left (40%), historical parallel right (60%) |
| **Source ref** | Line 540 |
| **Image prompt** | MASTER PREFIX + "A split timeline: top half shows punch cards transforming into a high-level code editor (1960s transition) in teal. Bottom half shows manual code transforming into AI-generated code (2020s transition) in electric blue. Amber parallel lines connect both transitions." + MASTER SUFFIX (portrait) |
| **Status** | DONE |

#### Slide 17 — LLM = The New Compiler?

| Field | Value |
|-------|-------|
| **Title** | LLM = The New Compiler? |
| **Content** | The critical difference: **Compilers** are deterministic and provably correct. **LLMs** are stochastic and can hallucinate. Can we really transfer the same level of trust? This question defines the rest of our session. |
| **Layout** | Content: question centered in Huge (80pt), two contrasting columns below (Compiler: deterministic, correct, verifiable vs. LLM: stochastic, hallucinates, probabilistic) |
| **Source ref** | Lines 386-391, 540 |
| **Image prompt** | — (text only, provocative question) |
| **Status** | DONE |

---

### Block 11 — `bck_exercise_vibecoding` (3 slides) — Pattern: exercise-flow

> **Metaphor moment: EXERCISE FRAMING** — Light subtitle callback, no explanation needed.

#### Slide 18 — Exercise: Pure VibeCoding

| Field | Value |
|-------|-------|
| **Title** | Exercise 2: Pure VibeCoding |
| **Content** | Subtitle: *"Cook at home — any way you like."* Instructions (ordered list): 1. Open Cursor (or your AI tool). 2. Describe a small utility in natural language (timer, todo list, unit converter, or your own idea). 3. Accept ALL generated code without reading it. 4. Only test if it works. 5. DO NOT look at the code. Duration: 10 minutes. |
| **Layout** | Content list: title + subtitle in italic + ordered list filling viewport |
| **Source ref** | — (pedagogical, illustrates VibeCoding principles) |
| **Image prompt** | MASTER PREFIX + "A home kitchen scene in flat vector: a casual figure tossing ingredients into a pan without measuring, without a recipe. Teal and electric blue tones, amber sparks from the stove. The mood is carefree and improvisational." + MASTER SUFFIX (portrait) |
| **Status** | DONE (image to update) |

#### Slide 19 — Timer

| Field | Value |
|-------|-------|
| **Title** | — |
| **Content** | "10:00" in GIANT (196pt) centered. Subtitle: "Build something. Don't read the code." |
| **Layout** | Billboard: timer display |
| **Status** | DONE |

#### Slide 20 — Debrief

| Field | Value |
|-------|-------|
| **Title** | Debrief |
| **Content** | 5 discussion questions: Does it work? Do you trust the code? Would you ship this to production? How does it feel to NOT read the code? What could go wrong? |
| **Layout** | Content list: 5 questions filling viewport |
| **Status** | DONE |

---

## ACT II — THE REALITY CHECK

---

### Block 12 — `bck_vibecoding_danger_intro` (1 slide) — NEW

> **Metaphor moment: PIVOT** — The emotional turning point. The audience shifts from home cooking to imagining professional stakes.

#### Slide 21 — It Works... But at What Cost?

| Field | Value |
|-------|-------|
| **Title** | It Works... But at What Cost? |
| **Content** | "Your dish looked good. But the kitchen just got inspected..." Then: "Unconstrained vibe coding produces prototypes that work in demos but harbour security vulnerabilities, hallucinated dependencies, and accumulated technical debt." |
| **Layout** | Billboard: opening line in Giant (128pt) accent, quote below in Large (48pt) |
| **Source ref** | Line 542 |
| **Image prompt** | — (text only, dramatic) |
| **Skippable** | No (sets up the danger sequence) |
| **Metaphor note** | One sentence bridges the exercise ("your dish") to the dangers. The rest of the danger slides are pure SE content — no more kitchen references until the bridge slide. |

---

### Block 13 — `bck_vibecoding_danger_vuln` (1 slide) — NEW

#### Slide 22 — 12-65% Vulnerabilities

| Field | Value |
|-------|-------|
| **Title** | Security Vulnerabilities |
| **Content** | "12% to 65%" in GIANT amber. "of AI-generated code contains vulnerabilities, depending on language, model, and prompting strategy." Tihanyi et al.: at least 62.07% of generated C programs contain vulnerabilities (zero-shot). Your exercise code likely has security flaws. |
| **Layout** | Pattern: **stat-hero** |
| **Source ref** | Lines 840-841 |
| **Image prompt** | MASTER PREFIX + "A shield icon in electric blue with deep cracks running through it, revealing amber danger glow beneath. Percentage numbers float around the shield in teal." + MASTER SUFFIX (portrait) |
| **Skippable** | No (strongest argument) |

---

### Block 14 — `bck_vibecoding_danger_halluc` (1 slide) — NEW

#### Slide 23 — Hallucinated Dependencies

| Field | Value |
|-------|-------|
| **Title** | Phantom Packages |
| **Content** | "5.2% — 21.7%" in GIANT amber. "of package references generated by LLMs point to non-existent packages." Creates supply-chain attack vectors: adversaries upload malicious code under hallucinated package names. |
| **Layout** | Pattern: **stat-hero** |
| **Source ref** | Lines 842-844 |
| **Image prompt** | MASTER PREFIX + "A package box icon in electric blue with a ghost-like phantom duplicate next to it in faint teal, both feeding into a supply chain arrow. The phantom package has an amber warning glow." + MASTER SUFFIX (portrait) |
| **Skippable** | Yes (can be mentioned verbally during vuln slide) |

---

### Block 15 — `bck_vibecoding_danger_debt` (1 slide) — NEW

#### Slide 24 — Technical Debt Iceberg

| Field | Value |
|-------|-------|
| **Title** | The Iceberg |
| **Content** | Fowler: "Organizations chasing short-term productivity gains may face 'long-term catastrophe' from accumulated technical debt in AI-generated code." What you SEE: working prototype. What's HIDDEN: unmaintainable code, missing error handling, no tests, brittle architecture. |
| **Layout** | Balanced: image left (40%, iceberg visual), Fowler quote + hidden/visible contrast right (60%) |
| **Source ref** | Lines 850-852 |
| **Image prompt** | MASTER PREFIX + "An iceberg: small tip visible above a waterline in electric blue, massive hidden mass below in teal. Amber cracks run through the submerged portion. The visible part is clean and shiny, the hidden part is chaotic." + MASTER SUFFIX (portrait) |
| **Skippable** | Yes (can be mentioned verbally) |

---

### Block 16 — `bck_vibecoding_danger_paradox` (1 slide) — NEW

#### Slide 25 — The AI Paradox

| Field | Value |
|-------|-------|
| **Title** | The AI Paradox |
| **Content** | "7 hours" in GIANT amber. "lost per team member weekly to AI-related inefficiencies." (GitLab DevSecOps Report) Faster coding creates new bottlenecks: code review of AI output, debugging hallucinations, fixing integration issues, managing non-determinism. Speed here, slowdown there. |
| **Layout** | Pattern: **stat-hero** |
| **Source ref** | Line 619 |
| **Image prompt** | MASTER PREFIX + "Two clocks side by side: left clock runs forward smoothly in electric blue (time saved). Right clock is broken and spinning backwards in amber (time lost). A teal balance between them tips toward the right." + MASTER SUFFIX (portrait) |
| **Skippable** | Yes |

---

### Block 17 — `bck_vibecoding_danger_demo_prod` (1 slide) — NEW

#### Slide 26 — Demo vs. Production

| Field | Value |
|-------|-------|
| **Title** | Demo vs. Production |
| **Content** | The demo works. Production requires: security, scalability, maintainability, monitoring, error handling, edge cases, compliance. The gap between "it works" and "it's production-ready" is where engineering lives. |
| **Layout** | Balanced: image left (40%), two contrasting columns right (60%) — Demo (green checks) vs. Production (requirements list) |
| **Source ref** | Lines 542, 852 |
| **Image prompt** | MASTER PREFIX + "Split screen: left side shows a perfect, shiny application interface in electric blue (demo). Right side shows the same interface crumbling with error symbols and warning triangles in amber (production reality). A teal curtain separates them." + MASTER SUFFIX (portrait) |
| **Skippable** | Yes (recap of previous points) |

---

### Block 18 — `bck_vibecoding_reality` (3 slides)

#### Slide 27 — The Anthropic Finding

| Field | Value |
|-------|-------|
| **Title** | What Can Actually Be Delegated? |
| **Content** | "60%" in GIANT blue / "0-20%" in GIANT amber. "Developers can integrate AI into 60% of their work but can fully delegate only 0-20% of tasks." Most work still needs human judgment, review, and direction. AI augments — it doesn't replace. |
| **Layout** | Pattern: **stat-hero** (dual stat) |
| **Source ref** | Line 586 |
| **Image prompt** | — (stat only) |
| **Status** | DONE (in current bck_vibecoding_reality) |

#### Slide 28 — Process Matters More Than Tools

| Field | Value |
|-------|-------|
| **Title** | Process > Tools |
| **Content** | "10%" vs "25-30%" in GIANT. "Organizations adopting AI tools without corresponding process transformation report only 10% productivity gains, compared to 25-30% for those undertaking end-to-end process redesign." (Bain Consulting). Tools alone are not enough. |
| **Layout** | Pattern: **stat-hero** (comparative) |
| **Source ref** | Lines 198, 1897 |
| **Image prompt** | — (stat only) |
| **Status** | DONE (in current bck_vibecoding_reality) |

#### Slide 29 — Naive VibeCoding Has Its Place

| Field | Value |
|-------|-------|
| **Title** | It Has Its Place |
| **Content** | Cooking at home is fine — for home. Appropriate: personal prototypes, throwaway demos, learning experiments, exploring ideas. But tomorrow your restaurant hosts a gala dinner for 200 guests. Individual dietary requirements. Press in attendance. **Would you cook the same way?** |
| **Layout** | Content: two columns (At home / At the hotel) filling viewport, closing question in highlight |
| **Source ref** | Lines 566-567 |
| **Image prompt** | — (text only) |
| **Skippable** | Yes (can be mentioned during bridge) |
| **Metaphor note** | The gala dinner image lands the stakes without explaining the metaphor. Participants make the connection themselves. |

---

### Block 19 — `bck_vibecoding_bridge` (1 slide) — NEW

#### Slide 30 — Speed AND Quality?

| Field | Value |
|-------|-------|
| **Title** | Speed AND Quality? |
| **Content** | Can we keep the speed and flow of VibeCoding while adding the discipline of software engineering? "AND" in amber GIANT. |
| **Layout** | Billboard: question centered, "AND" in GIANT (196pt) amber, rest in Huge (80pt) |
| **Source ref** | Lines 547-549 |
| **Image prompt** | — (text only, bridge to VibeEngineering) |
| **Skippable** | No (critical narrative bridge) |

---

## ACT III — VIBEENGINEERING: THE DISCIPLINE

---

### Block 20 — `bck_vibeeng_transition` (2 slides)

#### Slide 31 — What Practices Remain Essential?

| Field | Value |
|-------|-------|
| **Title** | What Practices Remain Essential? |
| **Content** | Billboard question: "Even with AI generating code, which software engineering practices do you think are non-negotiable?" Expected answers from audience: testing, code review, requirements, architecture... |
| **Layout** | Billboard: question centered, Giant (128pt), audience interaction |
| **Source ref** | — (interaction, bridges to VibeEngineering) |
| **Image prompt** | — (text only) |
| **Status** | DONE |

#### Slide 32 — That's VibeEngineering

| Field | Value |
|-------|-------|
| **Title** | Exactly — That's VibeEngineering |
| **Content** | Everything you just mentioned — requirements, tests, architecture, review — is exactly what separates the home cook from the starred chef. Let's formalize this. |
| **Layout** | Billboard: affirmation centered, Giant (128pt), accent highlight |
| **Source ref** | Lines 547-549 |
| **Image prompt** | — (text only) |
| **Status** | DONE (content to update) |
| **Metaphor note** | Single sentence callback. No elaboration — participants already have the mental model. |

---

### Block 21 — `bck_vibeeng_rebranding` (1 slide) — NEW

#### Slide 33 — From "Coding" to "Engineering"

| Field | Value |
|-------|-------|
| **Title** | From "Coding" to "Engineering" |
| **Content** | "A term that deliberately replaces 'coding' with 'engineering' to signal the reintroduction of systematic discipline." Kent Beck: critical distinction between casual vibe coding and disciplined "augmented coding." By early 2026, Karpathy himself moved to "agentic engineering." |
| **Layout** | Balanced: image left (40%), quotes + evolution right (60%) |
| **Source ref** | Lines 547-549 |
| **Image prompt** | MASTER PREFIX + "A loose, fluid shape in teal on the left morphs into a precise, structured geometric form in electric blue on the right. An amber arrow shows the transformation direction. The contrast between chaos and order." + MASTER SUFFIX (portrait) |
| **Skippable** | Yes (context already established in transition) |

---

### Block 22 — `bck_vibeeng_p_requirements` (1 slide) — NEW

> **Metaphor moment: PRINCIPLES FRAMING** — Each principle carries a one-word kitchen echo in parentheses. Subtle, not explained.

#### Slide 34 — Principle 1: Requirements Before Prompts

| Field | Value |
|-------|-------|
| **Title** | P1 — Requirements Before Prompts |
| **Content** | "Functional and non-functional requirements are explicitly defined before engaging the AI agent." Don't start prompting until you know WHAT you're building and WHY. The client's order — allergies, preferences, occasion — before the kitchen starts. |
| **Layout** | Balanced: image left (40%), principle heading Huge (80pt) + explanation Large (48pt) right (60%) |
| **Source ref** | Line 553 |
| **Image prompt** | MASTER PREFIX + "A solid foundation block in amber at the base, with a requirements checklist outline above it in electric blue. A faint chat prompt bubble waits above, unable to proceed without the foundation." + MASTER SUFFIX (portrait) |
| **Skippable** | No |

---

### Block 23 — `bck_vibeeng_p_tdd` (1 slide) — NEW

#### Slide 35 — Principle 2: Test-Driven Generation

| Field | Value |
|-------|-------|
| **Title** | P2 — Test-Driven Generation |
| **Content** | "Tests are written (or generated and validated) BEFORE implementation code." Tests define the contract. AI generates code that must pass. The test suite is your verification layer. Taste at every step, not just when the plate is served. |
| **Layout** | Balanced: image left (40%), principle heading + rationale right (60%) |
| **Source ref** | Line 554 |
| **Image prompt** | MASTER PREFIX + "A test tube or verification checkmark icon in amber standing tall on the left, casting a protective shadow over code blocks in electric blue on the right. The tests came first and guard the code." + MASTER SUFFIX (portrait) |
| **Skippable** | No |

---

### Block 24 — `bck_vibeeng_p_architecture` (1 slide) — NEW

#### Slide 36 — Principle 3: Architectural Intent

| Field | Value |
|-------|-------|
| **Title** | P3 — Architectural Intent |
| **Content** | "System architecture and design patterns are specified in project rules and context files." .cursorrules, CLAUDE.md, AGENTS.md — these files constrain the AI's decisions. The architecture is human-defined, the implementation is AI-generated. Your recipe book — the kitchen follows it. |
| **Layout** | Balanced: image left (40%), principle heading + concrete examples right (60%) |
| **Source ref** | Line 555 |
| **Image prompt** | MASTER PREFIX + "A blueprint wireframe of a building structure in electric blue with clean architectural lines. Project rule cards float nearby in teal. An amber compass in the corner indicates direction and constraints." + MASTER SUFFIX (portrait) |
| **Skippable** | No |

---

### Block 25 — `bck_vibeeng_p_iteration` (1 slide) — NEW

#### Slide 37 — Principle 4: Iterative Refinement

| Field | Value |
|-------|-------|
| **Title** | P4 — Iterative Refinement |
| **Content** | "Development proceeds through planned iterations, each with defined scope, acceptance criteria, and review gates." Not "generate everything at once." Incremental progress with validation at each step. |
| **Layout** | Balanced: image left (40%), principle heading + rationale right (60%) |
| **Source ref** | Line 556 |
| **Image prompt** | MASTER PREFIX + "A spiral staircase viewed from above, with each step clearly defined in electric blue. Gate checkpoints between iterations glow in amber. The spiral converges toward a goal point in teal at the center." + MASTER SUFFIX (portrait) |
| **Skippable** | Yes (can be covered briefly) |

---

### Block 26 — `bck_vibeeng_p_review` (1 slide) — NEW

#### Slide 38 — Principle 5: Human Review at Boundaries

| Field | Value |
|-------|-------|
| **Title** | P5 — Human Review at Boundaries |
| **Content** | "Architectural decisions, security-critical code, and integration points undergo systematic human review." You don't review every line. You review at critical boundaries. Trust the AI for implementation, verify at integration points. HACCP — control at critical points, not on every gesture. |
| **Layout** | Balanced: image left (40%), principle heading + rationale right (60%) |
| **Source ref** | Line 557 |
| **Image prompt** | MASTER PREFIX + "A flow of automated process in electric blue passing through human-shaped gate checkpoints in amber. At each gate, a magnifying glass examines the flow. Between gates, the flow runs freely." + MASTER SUFFIX (portrait) |
| **Skippable** | No |

---

### Block 27 — `bck_vibeeng_p_context` (1 slide) — NEW

#### Slide 39 — Principle 6: Context Engineering

| Field | Value |
|-------|-------|
| **Title** | P6 — Context Engineering |
| **Content** | "The practice of designing, building, and maintaining the optimal information environment for AI agents." Project rules, documentation, MCP servers, memory systems, tool configurations — the context IS the engineering. The better the context, the better the AI output. Your mise en place — everything prepared before the first flame. |
| **Layout** | Balanced: image left (40%), principle heading + explanation right (60%) |
| **Source ref** | Lines 1841-1864 (context engineering as primary differentiator) |
| **Image prompt** | MASTER PREFIX + "A central hub circle in amber surrounded by orbiting information spheres of different sizes in electric blue and teal — documents, rules, tools, memories. Lines connect everything to the hub. The arrangement is deliberate and designed." + MASTER SUFFIX (portrait) |
| **Skippable** | Yes (advanced concept, can defer to later sessions) |

---

### Block 28 — `bck_vibeeng_spectrum` (5 slides) — EXPANDED

#### Slide 40 — The Full Spectrum

| Field | Value |
|-------|-------|
| **Title** | The Spectrum |
| **Content** | VibeCoding and VibeEngineering are not opposites — they're a spectrum. 4 levels of increasing discipline. Choose the right level for your context and stakes. |
| **Layout** | Pattern: **spectrum-bar** (gradient from teal/loose to amber/structured). Labels: "Home kitchen" ↔ "Starred hotel restaurant" |
| **Source ref** | Lines 564-580 |
| **Image prompt** | — (pattern, no image) |
| **Status** | Partially done (current bck_vibeeng_spectrum has table) |

#### Slide 41 — Level 1: Naive VibeCoding

| Field | Value |
|-------|-------|
| **Title** | Level 1 — Naive VibeCoding |
| **Content** | "No requirements, no tests, no review. 'Just make it work.'" What you did in Exercise 2. Maximum speed, minimum guarantees. **Best for:** personal prototypes, learning, throwaway demos. **Never for:** production or shared code. *(Cooking at home — if it's edible, it's done.)* |
| **Layout** | Content: level name in Huge (80pt), characteristics + use cases in Large (48pt), filling viewport |
| **Source ref** | Line 567 |
| **Image prompt** | — (text only) |
| **Skippable** | Yes (can show spectrum overview only) |

#### Slide 42 — Level 2: Guided VibeCoding

| Field | Value |
|-------|-------|
| **Title** | Level 2 — Guided VibeCoding |
| **Content** | "Informal requirements; output evaluated manually; minimal project rules." Some direction, but no formal process. You check the output, but without systematic criteria. **Best for:** internal tools, proof-of-concept, personal productivity. *(Dinner for friends — some care, low stakes.)* |
| **Layout** | Content: same pattern as Level 1 |
| **Source ref** | Line 570 |
| **Image prompt** | — (text only) |
| **Skippable** | Yes |

#### Slide 43 — Level 3: Structured VibeCoding

| Field | Value |
|-------|-------|
| **Title** | Level 3 — Structured VibeCoding |
| **Content** | "Written requirements; some tests; project rules configured; code review of critical paths." Real discipline starts here. Tests exist. Architecture is documented. Critical code is reviewed. **Best for:** team projects, early-stage products. *(Bistro — paying customers, online reviews, hygiene standards.)* |
| **Layout** | Content: same pattern as Level 1 |
| **Source ref** | Line 573 |
| **Image prompt** | — (text only) |
| **Skippable** | Yes |

#### Slide 44 — Level 4: VibeEngineering

| Field | Value |
|-------|-------|
| **Title** | Level 4 — VibeEngineering |
| **Content** | "Full requirements engineering; TDD/BDD; architecture constraints; CI/CD integration; systematic review gates." The full discipline. This is where this training takes you over 6 days. **Best for:** production software, enterprise, regulated environments. *(Starred hotel restaurant — stars to lose, regulations, client expectations, financial stakes.)* |
| **Layout** | Balanced: image left (40%), level description + highlight right (60%) |
| **Source ref** | Line 576 |
| **Image prompt** | MASTER PREFIX + "A complete engineering workstation: a central screen in electric blue showing structured code, surrounded by orbiting elements — test results in amber, CI/CD pipeline in teal, review checklist in white. All connected in a harmonious, disciplined system." + MASTER SUFFIX (portrait) |
| **Skippable** | No |

---

### Block 29 — `bck_vibeeng_evidence` (1 slide) — NEW

#### Slide 45 — The Evidence

| Field | Value |
|-------|-------|
| **Title** | The Evidence |
| **Content** | "15%" in GIANT amber. "fewer code smells when incorporating design and code review activities into AI-assisted development." (FlowGen experiment) Moving rightward on the spectrum yields measurable quality improvements. Discipline pays off. |
| **Layout** | Pattern: **stat-hero** |
| **Source ref** | Line 582 |
| **Image prompt** | — (stat only) |
| **Skippable** | Yes (supporting evidence, not critical) |

---

### Block 30 — `bck_exercise_vibeeng` (3 slides) — Pattern: exercise-flow

#### Slide 46 — Exercise: Redo with Discipline

| Field | Value |
|-------|-------|
| **Title** | Exercise 3: Redo with Discipline |
| **Content** | Subtitle: *"Same dish, but for the gala."* Instructions: Take the SAME tool from Exercise 2. This time: (1) Write 3 functional requirements first. (2) Ask the AI to generate tests BEFORE implementation. (3) Then ask for implementation that passes those tests. (4) Review the test results. Compare the experience. Duration: 8 minutes. |
| **Layout** | Content list: title + subtitle in italic + ordered steps filling viewport |
| **Source ref** | Lines 553-557 (VibeEngineering principles applied) |
| **Image prompt** | MASTER PREFIX + "A professional kitchen station: clean steel surface, ingredients organized in labeled containers (mise en place), a recipe card pinned above, a chef's hand tasting from a spoon. Electric blue and teal tones, amber accent on the recipe card. The mood is precise and controlled." + MASTER SUFFIX (portrait) |
| **Status** | DONE (image to update) |

#### Slide 47 — Timer

| Field | Value |
|-------|-------|
| **Title** | — |
| **Content** | "8:00" in GIANT (196pt) centered. Subtitle: "Requirements → Tests → Implementation." |
| **Layout** | Billboard: timer display |
| **Status** | DONE |

#### Slide 48 — Compare Both Approaches

| Field | Value |
|-------|-------|
| **Title** | Compare Both Approaches |
| **Content** | 4 discussion questions: How did the quality change? Did the tests catch issues? Do you feel more confident? Was the tradeoff worth it? Closing: "This is the difference between Level 1 and Level 4." |
| **Layout** | Content list: 4 questions filling viewport |
| **Status** | DONE |

---

## ACT IV — THE TOOL ECOSYSTEM

---

### Block 31 — `bck_ide_overview` (1 slide) — NEW

#### Slide 49 — Agentic IDE Tools

| Field | Value |
|-------|-------|
| **Title** | The Tools That Make It Real |
| **Content** | VibeCoding and VibeEngineering are practices. The TOOLS bring them to life. Each with different trade-offs on the autonomy spectrum. |
| **Layout** | Billboard: title in Giant (128pt), subtitle in Large (48pt) |
| **Source ref** | Lines 1083-1870 |
| **Image prompt** | MASTER PREFIX + "A code editor window in electric blue with multiple AI agent avatars (small geometric shapes) floating inside it, each performing different tasks simultaneously. Amber highlights on active agents." + MASTER SUFFIX (landscape) |
| **Skippable** | Yes (can jump directly to autonomy spectrum) |

---

### Block 32 — `bck_ide_autonomy` (2 slides)

#### Slide 50 — The Autonomy Spectrum

| Field | Value |
|-------|-------|
| **Title** | The Autonomy Spectrum |
| **Content** | 5 levels: 1. **Passive assistance** — respond when invoked (inline completion on demand). 2. **Proactive copiloting** — suggest unprompted, developer retains authority. 3. **Task-level delegation** — NL spec, model plans+executes (Cursor Composer). 4. **Autonomous agents** — minimal oversight, plan-execute-test-iterate (Claude Code, SWE-agent). 5. **Multi-agent orchestration** — specialized agents collaborate. |
| **Layout** | Content list: 5 levels as ascending list filling viewport, each with keyword in bold highlight + description |
| **Source ref** | Lines 455-461 |
| **Image prompt** | MASTER PREFIX + "Five ascending steps or platforms from left to right, each higher than the previous. A human silhouette on the leftmost step, gradually transforming into a more abstract AI agent shape on the rightmost. Colors progress from teal to electric blue to amber." + MASTER SUFFIX (portrait) |
| **Status** | DONE (in current bck_ide_ecosystem) |

#### Slide 51 — The Agentic Turn (2024-2026)

| Field | Value |
|-------|-------|
| **Title** | The Agentic Turn |
| **Content** | All major platforms racing up the autonomy spectrum. Cursor: 8 parallel agents on isolated worktrees. Claude Code: 5 built-in sub-agents + Agent Teams. GitHub Copilot: async Coding Agent in GitHub Actions. Every vendor moving toward autonomous agents. The shift from "assistant" to "agent" is the defining trend. |
| **Layout** | Balanced: image left (40%), 4 key examples right (60%) |
| **Source ref** | Lines 1093, 1189, 1287, 1855-1864 |
| **Image prompt** | MASTER PREFIX + "A steep upward curve (hockey stick shape) in electric blue, with the inflection point highlighted by an amber burst. Below the curve, small tool icons. Above the curve, larger autonomous agent icons rising." + MASTER SUFFIX (portrait) |
| **Skippable** | Yes |

---

### Block 33 — `bck_ide_cursor` (2 slides) — EXPANDED

#### Slide 52 — Cursor: Your Primary Tool

| Field | Value |
|-------|-------|
| **Title** | Cursor |
| **Content** | AI-native IDE (VS Code fork). $29.3B valuation, 1M+ daily active users, 17x YoY growth. Key capabilities: Tab Completion, Chat, Composer/Agent Mode (up to 8 parallel agents on isolated git worktrees — your brigade). Rules System, Skills, Sub-agents, Hooks (20+ lifecycle events). Plugin Marketplace (Feb 2026). |
| **Layout** | Balanced: image left (40%), key stats + feature list right (60%) |
| **Source ref** | Lines 1087-1175 |
| **Image prompt** | MASTER PREFIX + "A cursor arrow icon in amber centered inside a fully-featured IDE window outline in electric blue. The cursor radiates interaction lines to every part of the IDE. Energy flows outward." + MASTER SUFFIX (portrait) |
| **Status** | DONE (in current bck_ide_ecosystem) |

#### Slide 53 — Cursor: Agent Architecture

| Field | Value |
|-------|-------|
| **Title** | Cursor Agent Architecture |
| **Content** | Agent Mode: 8 parallel agents on isolated git worktrees. Each agent: plans → executes → tests → iterates. Background/Cloud Agents for long-running tasks. Mission Control for monitoring. Rules cascade: workspace → project → .cursorrules. Pricing: Free / Pro $20 / Business $40. |
| **Layout** | Content: architecture overview with key details |
| **Source ref** | Lines 1093-1175 |
| **Image prompt** | — (text/diagram slide) |
| **Skippable** | Yes (detail for advanced audiences) |

---

### Block 34 — `bck_ide_claude_code` (2 slides) — EXPANDED

#### Slide 54 — Claude Code

| Field | Value |
|-------|-------|
| **Title** | Claude Code |
| **Content** | Terminal-based, CLI-first, highest autonomy. No inline completion — deliberate design choice. 5 built-in sub-agents + experimental Agent Teams. 17 hook event types. 9,000+ community plugins. Agent SDK (Python, TypeScript). CLAUDE.md rules (6-level hierarchy). |
| **Layout** | Balanced: image left (40%), key features right (60%) |
| **Source ref** | Lines 1179-1274 |
| **Image prompt** | MASTER PREFIX + "A terminal window in electric blue with autonomous process flows running inside — branching decision trees, parallel execution threads in teal, completion indicators in amber. Pure CLI aesthetic." + MASTER SUFFIX (portrait) |
| **Status** | DONE (in current bck_ide_ecosystem) |

#### Slide 55 — Claude Code: Unique Capabilities

| Field | Value |
|-------|-------|
| **Title** | Claude Code: Unique Strengths |
| **Content** | Persistent Memory system. Model Tools: WebSearch, WebFetch, Python execution, PDF analysis, extended thinking. Permission System with sandboxing. IDE Integration: VS Code, JetBrains, Desktop, Web, Chrome, Slack. Task Management system. Pricing: Pro $20 / Max $100-200 / Team $30. |
| **Layout** | Content: feature categories filling viewport |
| **Source ref** | Lines 1200-1274 |
| **Image prompt** | — (text slide) |
| **Skippable** | Yes (detail for advanced audiences) |

---

### Block 35 — `bck_ide_others` (2 slides)

#### Slide 56 — Windsurf

| Field | Value |
|-------|-------|
| **Title** | Windsurf |
| **Content** | Formerly Codeium, 800,000+ active developers. Flagship: Cascade (agentic mode with deep codebase awareness). Memories (persistent context), Rules. SOC 2 Type II, FedRAMP High, Zero Data Retention. Security-first posture — strongest for regulated industries. Being acquired by Cognition AI (Devin) for ~$3B. |
| **Layout** | Balanced: image left (40%), features right (60%) |
| **Source ref** | Lines 1555-1616 |
| **Image prompt** | MASTER PREFIX + "A surfboard on a digital wave: the wave represents structured workflow in electric blue, the surfboard is the tool in teal riding the wave smoothly, with amber spray at the crest." + MASTER SUFFIX (portrait) |
| **Status** | DONE (in current bck_ide_ecosystem) |

#### Slide 57 — GitHub Copilot

| Field | Value |
|-------|-------|
| **Title** | GitHub Copilot |
| **Content** | Most widely adopted: 20M+ developers, 90% Fortune 100. Pioneer since 2022. Agent Mode + async Coding Agent (GitHub Actions). Agent HQ for organizations. .github/copilot-instructions.md. Extensions migrated to MCP (Sept 2025). IP indemnity on Business/Enterprise. |
| **Layout** | Balanced: image left (40%), features right (60%) |
| **Source ref** | Lines 1276-1315 |
| **Image prompt** | MASTER PREFIX + "A pilot's wing emblem in electric blue with a code bracket at the center. Subtle teal shadow of millions of users below. Amber highlight on the agent mode badge." + MASTER SUFFIX (portrait) |
| **Status** | DONE (in current bck_ide_ecosystem) |

---

### Block 36 — `bck_ide_comparison` (1 slide)

#### Slide 58 — Comparison Matrix

| Field | Value |
|-------|-------|
| **Title** | Comparison |
| **Content** | Table-roadmap pattern. Columns: Tool / Autonomy / IDE Integration / Best For. Cursor: Medium / Very High / Interactive dev agent. Claude Code: Very High / Low (CLI) / Autonomous coding. Windsurf: High / Very High / Security-first. Copilot: Low-Medium / Very High / Largest ecosystem. |
| **Layout** | Pattern: **table-roadmap** (4 columns, 4 data rows + header) |
| **Source ref** | Lines 1855-1864 |
| **Image prompt** | — (table, no image) |
| **Status** | DONE (in current bck_ide_ecosystem) |

---

### Block 37 — `bck_ide_mcp` (1 slide) — NEW

#### Slide 59 — Model Context Protocol (MCP)

| Field | Value |
|-------|-------|
| **Title** | Model Context Protocol |
| **Content** | Open protocol connecting AI agents to external tools, data sources, and services. Registry: 16,670+ servers. Covers: version control, testing, databases, cloud, observability, design, communication. Your certified suppliers — vetted, traceable, always available. |
| **Layout** | Balanced: image left (40%), key facts right (60%) |
| **Source ref** | Lines 1025, 1765 |
| **Image prompt** | MASTER PREFIX + "A central hub circle in amber with six spokes extending to peripheral circles in electric blue and teal. Each peripheral circle has a different simple icon (database, file, API, cloud). Represents MCP as universal integration." + MASTER SUFFIX (portrait) |
| **Skippable** | Yes (can be deferred to Session 2) |

---

### Block 38 — `bck_ide_cursor_choice` (1 slide)

#### Slide 60 — Why Cursor for This Training

| Field | Value |
|-------|-------|
| **Title** | You Will Master Cursor |
| **Content** | Best compromise: deep IDE integration + powerful agent mode. 8 parallel agents for maximum throughput. Full hooks and rules system. Plugin marketplace. Perfect for learning VibeEngineering workflows interactively. You'll explore it in depth from this afternoon through all 6 days. |
| **Layout** | Content: statement in Huge (80pt) + 5 reasons in Large (48pt) |
| **Source ref** | Training program, Lines 1855-1856 |
| **Image prompt** | — (text only, declarative) |
| **Skippable** | No |

---

## CLOSING

---

### Block 39 — `bck_recap` (4 slides)

#### Slide 61 — Recap: Generative AI

| Field | Value |
|-------|-------|
| **Title** | Recap: Generative AI |
| **Content** | 4 takeaways: GenAI = next-token prediction at massive scale. Powerful: code, text, reasoning, multimodal. Limited: hallucinations, no understanding, bias, cost. 84% of devs use it — the question is HOW. |
| **Layout** | Content list: 4 key takeaways filling viewport |
| **Source ref** | Summary of Part 1 (ai4se6d_genai_intro) |
| **Status** | DONE |

#### Slide 62 — Recap: VibeCoding → VibeEngineering

| Field | Value |
|-------|-------|
| **Title** | Recap: VibeCoding → VibeEngineering |
| **Content** | 4 takeaways: VibeCoding: intent-driven, fast, accessible. Naive VibeCoding: dangerous for production (12-65% vulnerabilities). VibeEngineering: 6 principles — requirements + tests + architecture + iteration + review + context. Choose the right level for your context. |
| **Layout** | Content list: 4 key takeaways filling viewport |
| **Source ref** | Summary of Part 2 |
| **Status** | DONE |

#### Slide 63 — The Road Ahead

| Field | Value |
|-------|-------|
| **Title** | The Road Ahead |
| **Content** | Day 1 PM: Tools ecosystem + FreeSelfApp workshop (naive prototype). Day 2: Mastering Cursor. Day 3: Git + SE Requirements. Day 4: Iterative Improvement (CalcApp). Day 5: Mini-project synthesis. Day 6: Ethics + Governance + Presentations. |
| **Layout** | Pattern: **table-roadmap** (6 rows, Day column highlighted for Day 1) |
| **Source ref** | Training program |
| **Status** | DONE |

#### Slide 64 — Same Kitchen, Different Discipline

> **Metaphor moment: CLOSING** — The metaphor lands one last time, completing the arc from slide 10.

| Field | Value |
|-------|-------|
| **Title** | Same Kitchen, Different Discipline |
| **Content** | Same ingredients. Same utensils. Same kitchen. The difference: **the discipline of the chef.** This training is your culinary school. In 6 days, you go from the customer's seat to the chef's pass. |
| **Layout** | Billboard: key message in Giant (128pt), "discipline of the chef" in amber |
| **Source ref** | Lines 547-549 |
| **Image prompt** | MASTER PREFIX + "Two identical professional kitchens side by side in electric blue. Left kitchen has ingredients scattered chaotically, no mise en place, a mess (teal). Right kitchen is immaculate: ingredients organized in labeled containers, recipes pinned up, every tool in its place (amber glow). Same kitchen, different discipline." + MASTER SUFFIX (landscape) |
| **Status** | DONE (content + image to update) |

---

### Block 40 — `bck_closing` (1 slide) — NEW

#### Slide 65 — Questions?

| Field | Value |
|-------|-------|
| **Title** | Questions? |
| **Content** | Open floor for questions, comments, and discussion before the afternoon session. |
| **Layout** | Image-dominant: full visual, inviting |
| **Image prompt** | MASTER PREFIX + "A large question mark made of small glowing dots in electric blue, surrounded by subtle audience silhouettes in teal. Amber glow at the dot of the question mark. Inviting and open." + MASTER SUFFIX (landscape) |
| **Skippable** | No |

---

### Block 41 — `bck_glossary` (1 slide)

#### Slide (reference, not counted in flow)

| Field | Value |
|-------|-------|
| **Title** | Glossary |
| **Content** | 19+ key terms: GenAI, LLM, GPT, NLU, RLHF, Transformer, Token, Embedding, Attention, VibeCoding, VibeEngineering, Context Engineering, TDD, BDD, CI/CD, MCP, NFR, V&V, Hallucination. |
| **Layout** | Continuous scrollable list (not paginated within) |
| **Source ref** | All sections |
| **Status** | DONE |

---

## Book Order

```python
st_book([
    # Opening
    blocks.bck_title,                        #  1 slide
    blocks.bck_intro_review_habits,          #  4 slides

    # ACT I — VibeCoding: The Concept
    blocks.bck_vibecoding_origin,            #  3 slides
    blocks.bck_vibecoding_definition,        #  1 slide  (NEW)
    blocks.bck_vibecoding_paradigm,          #  2 slides (NEW)
    blocks.bck_vibecoding_intent,            #  1 slide  (NEW)
    blocks.bck_vibecoding_trust,             #  1 slide  (NEW)
    blocks.bck_vibecoding_conversation,      #  1 slide  (NEW)
    blocks.bck_vibecoding_low_barrier,       #  1 slide  (NEW)
    blocks.bck_vibecoding_analogy,           #  2 slides

    # Exercise 2 — Pure VibeCoding
    blocks.bck_exercise_vibecoding,          #  3 slides

    # ACT II — The Reality Check
    blocks.bck_vibecoding_danger_intro,      #  1 slide  (NEW)
    blocks.bck_vibecoding_danger_vuln,       #  1 slide  (NEW)
    blocks.bck_vibecoding_danger_halluc,     #  1 slide  (NEW)
    blocks.bck_vibecoding_danger_debt,       #  1 slide  (NEW)
    blocks.bck_vibecoding_danger_paradox,    #  1 slide  (NEW)
    blocks.bck_vibecoding_danger_demo_prod,  #  1 slide  (NEW)
    blocks.bck_vibecoding_reality,           #  3 slides
    blocks.bck_vibecoding_bridge,            #  1 slide  (NEW)

    # ACT III — VibeEngineering: The Discipline
    blocks.bck_vibeeng_transition,           #  2 slides
    blocks.bck_vibeeng_rebranding,           #  1 slide  (NEW)
    blocks.bck_vibeeng_p_requirements,       #  1 slide  (NEW)
    blocks.bck_vibeeng_p_tdd,               #  1 slide  (NEW)
    blocks.bck_vibeeng_p_architecture,       #  1 slide  (NEW)
    blocks.bck_vibeeng_p_iteration,          #  1 slide  (NEW)
    blocks.bck_vibeeng_p_review,             #  1 slide  (NEW)
    blocks.bck_vibeeng_p_context,            #  1 slide  (NEW)
    blocks.bck_vibeeng_spectrum,             #  5 slides (EXPANDED)
    blocks.bck_vibeeng_evidence,             #  1 slide  (NEW)

    # Exercise 3 — Redo with Discipline
    blocks.bck_exercise_vibeeng,             #  3 slides

    # ACT IV — The Tool Ecosystem
    blocks.bck_ide_overview,                 #  1 slide  (NEW)
    blocks.bck_ide_autonomy,                 #  2 slides (NEW split)
    blocks.bck_ide_cursor,                   #  2 slides (EXPANDED)
    blocks.bck_ide_claude_code,              #  2 slides (EXPANDED)
    blocks.bck_ide_others,                   #  2 slides (NEW split)
    blocks.bck_ide_comparison,               #  1 slide
    blocks.bck_ide_mcp,                      #  1 slide  (NEW)
    blocks.bck_ide_cursor_choice,            #  1 slide  (NEW)

    # Closing
    blocks.bck_recap,                        #  4 slides
    blocks.bck_closing,                      #  1 slide  (NEW)
    blocks.bck_glossary,                     #  1 slide
], ...)
```

---

## Migration from Current Implementation

### Blocks to KEEP as-is (8 blocks)

| Current Block | Plan Block | Notes |
|---------------|------------|-------|
| `bck_title` | `bck_title` | No change |
| `bck_intro_review_habits` | `bck_intro_review_habits` | No change |
| `bck_vibecoding_origin` | `bck_vibecoding_origin` | Finalize image selection |
| `bck_vibecoding_analogy` | `bck_vibecoding_analogy` | No change |
| `bck_exercise_vibecoding` | `bck_exercise_vibecoding` | No change |
| `bck_vibeeng_transition` | `bck_vibeeng_transition` | No change |
| `bck_exercise_vibeeng` | `bck_exercise_vibeeng` | No change |
| `bck_glossary` | `bck_glossary` | No change |

### Blocks to REFACTOR (4 blocks → content redistributed)

| Current Block | Action | Content Goes To |
|---------------|--------|-----------------|
| `bck_vibecoding_principles` | REMOVE | Split into `bck_vibecoding_intent`, `bck_vibecoding_trust`, `bck_vibecoding_conversation`, `bck_vibecoding_low_barrier` |
| `bck_vibecoding_dangers` | REMOVE | Split into `bck_vibecoding_danger_intro`, `_vuln`, `_halluc`, `_debt`, `_paradox`, `_demo_prod` |
| `bck_vibeeng_principles` | REMOVE | Split into `bck_vibeeng_p_requirements`, `_tdd`, `_architecture`, `_iteration`, `_review`, `_context` |
| `bck_vibeeng_spectrum` | EXPAND | Add 4 individual level slides (currently table-only) |

### Blocks to SPLIT (3 blocks → new blocks)

| Current Block | New Blocks |
|---------------|------------|
| `bck_vibecoding_reality` | KEEP `bck_vibecoding_reality` (3 slides) + NEW `bck_vibecoding_bridge` (1 slide extracted) |
| `bck_ide_ecosystem` | Split into `bck_ide_overview`, `bck_ide_autonomy`, `bck_ide_cursor`, `bck_ide_claude_code`, `bck_ide_others`, `bck_ide_comparison`, `bck_ide_mcp`, `bck_ide_cursor_choice` |
| `bck_recap` | KEEP `bck_recap` (4 slides) + NEW `bck_closing` (1 slide extracted) |

### NEW blocks to CREATE (22 blocks)

| Block | Content | Type |
|-------|---------|------|
| `bck_vibecoding_definition` | Formal definition | Content |
| `bck_vibecoding_paradigm` | Author→Director + Conductor | Balanced + Image-dominant |
| `bck_vibecoding_intent` | Principle 1 | Balanced |
| `bck_vibecoding_trust` | Principle 2 | Balanced |
| `bck_vibecoding_conversation` | Principle 3 | Balanced |
| `bck_vibecoding_low_barrier` | Principle 4 | Balanced |
| `bck_vibecoding_danger_intro` | Billboard | Billboard |
| `bck_vibecoding_danger_vuln` | 12-65% stat | Stat-hero |
| `bck_vibecoding_danger_halluc` | 5.2-21.7% stat | Stat-hero |
| `bck_vibecoding_danger_debt` | Iceberg | Balanced |
| `bck_vibecoding_danger_paradox` | 7h/week stat | Stat-hero |
| `bck_vibecoding_danger_demo_prod` | Demo vs Prod | Balanced |
| `bck_vibecoding_bridge` | Speed AND Quality? | Billboard |
| `bck_vibeeng_rebranding` | Coding→Engineering | Balanced |
| `bck_vibeeng_p_requirements` | Principle 1 | Balanced |
| `bck_vibeeng_p_tdd` | Principle 2 | Balanced |
| `bck_vibeeng_p_architecture` | Principle 3 | Balanced |
| `bck_vibeeng_p_iteration` | Principle 4 | Balanced |
| `bck_vibeeng_p_review` | Principle 5 | Balanced |
| `bck_vibeeng_p_context` | Principle 6 | Balanced |
| `bck_vibeeng_evidence` | FlowGen 15% | Stat-hero |
| `bck_ide_overview` | Section billboard | Billboard |
| `bck_ide_autonomy` | 5 levels + agentic turn | Content + Balanced |
| `bck_ide_cursor` | 2-slide Cursor | Balanced |
| `bck_ide_claude_code` | 2-slide Claude Code | Balanced |
| `bck_ide_others` | Windsurf + Copilot | Balanced |
| `bck_ide_comparison` | Matrix | Table-roadmap |
| `bck_ide_mcp` | MCP protocol | Balanced |
| `bck_ide_cursor_choice` | Why Cursor | Content |
| `bck_closing` | Questions | Image-dominant |

---

## Skippable Sections Map

For time-constrained delivery, the following blocks can be skipped (marked in plan):

| Priority | Blocks to Skip | Slides Saved | Remaining Duration |
|----------|---------------|--------------|-------------------|
| All slides | — | 0 | ~70 min |
| **Quick (55 min)** | `bck_vibecoding_low_barrier`, `bck_vibecoding_paradigm` slide 2 (conductor), `bck_vibecoding_danger_halluc`, `bck_vibecoding_danger_debt`, `bck_vibecoding_danger_paradox`, `bck_vibecoding_danger_demo_prod`, `bck_vibecoding_reality` slide 3 (naive ok), `bck_vibeeng_rebranding`, `bck_vibeeng_p_iteration`, `bck_vibeeng_p_context`, spectrum levels 1-3, `bck_vibeeng_evidence`, `bck_ide_overview`, `bck_ide_autonomy` slide 2 (agentic turn), `bck_ide_cursor` slide 2, `bck_ide_claude_code` slide 2, `bck_ide_mcp` | ~17 slides | ~53 min |
| **Express (45 min)** | Above + `bck_vibecoding_paradigm`, 2 danger slides, `bck_ide_others` | ~22 slides | ~43 min |

---

## AI Image Summary

| Category | Count |
|----------|-------|
| Balanced slides (portrait 2:3) | ~22 |
| Image-dominant slides (landscape 16:9) | ~4 |
| Managed images (existing) | ~3 |
| Text-only / pattern slides | ~36 |
| **Total AI images needed** | **~26** |

---

## Source Line Reference Index

| Source Lines | Content | Blocks Using |
|-------------|---------|-------------|
| 455-461 | Autonomy spectrum (5 levels) | `bck_ide_autonomy` |
| 524-533 | VibeCoding definition, principles | `bck_vibecoding_origin`, `_definition`, `_intent`, `_trust`, `_conversation`, `_low_barrier` |
| 535-542 | Philosophy + dangers | `bck_vibecoding_paradigm`, `_danger_intro` |
| 547-559 | VibeEngineering definition + principles | `bck_vibeeng_transition`, `_rebranding`, `_p_*` |
| 564-580 | Spectrum levels | `bck_vibeeng_spectrum` |
| 582 | FlowGen evidence | `bck_vibeeng_evidence` |
| 586 | Anthropic finding (60%/0-20%) | `bck_vibecoding_reality` |
| 619 | AI paradox (7h/week) | `bck_vibecoding_danger_paradox` |
| 840-852 | Vulnerabilities, hallucinations, tech debt | `bck_vibecoding_danger_vuln`, `_halluc`, `_debt` |
| 1025, 1765 | MCP | `bck_ide_mcp` |
| 1083-1175 | Cursor | `bck_ide_cursor` |
| 1179-1274 | Claude Code | `bck_ide_claude_code` |
| 1276-1315 | GitHub Copilot | `bck_ide_others` |
| 1555-1616 | Windsurf | `bck_ide_others` |
| 1841-1871 | Tool synthesis + agentic turn | `bck_ide_comparison`, `bck_ide_autonomy` |
| 1897 | Bain study (10% vs 25-30%) | `bck_vibecoding_reality` |

---

## Production Sequence

| Step | Action | Blocks | Effort |
|------|--------|--------|--------|
| 1 | Create new block stubs (22 blocks) | NEW blocks | 1h |
| 2 | Generate AI images (~26 images) | Multiple | 2-3h |
| 3 | Split `bck_vibecoding_principles` → 4 principle blocks | 4 blocks | 30 min |
| 4 | Split `bck_vibecoding_dangers` → 6 danger blocks | 6 blocks | 45 min |
| 5 | Create `bck_vibecoding_definition` + `bck_vibecoding_paradigm` | 2 blocks | 30 min |
| 6 | Create `bck_vibecoding_bridge` | 1 block | 10 min |
| 7 | Split `bck_vibeeng_principles` → 6 principle blocks | 6 blocks | 45 min |
| 8 | Expand `bck_vibeeng_spectrum` (add 4 level slides) | 1 block | 30 min |
| 9 | Create `bck_vibeeng_rebranding` + `bck_vibeeng_evidence` | 2 blocks | 20 min |
| 10 | Split `bck_ide_ecosystem` → 8 IDE blocks | 8 blocks | 1h |
| 11 | Create `bck_closing` | 1 block | 10 min |
| 12 | Update `book.py` (new import order) | — | 15 min |
| 13 | Update `blocks/__init__.py` (registry) | — | 10 min |
| 14 | Full run-through + visual QA | All | 1h |
| 15 | Export HTML + PDF | — | 15 min |

---

## Summary

| Metric | Previous Implementation | This Plan |
|--------|------------------------|-----------|
| Block files | 15 | 41 |
| Total slides | ~34 | ~65 |
| Exercises | 2 (18 min) | 2 (18 min) |
| Audience interactions | 2 | 3 |
| AI images | ~3 | ~26 |
| Source coverage | ~95% | 100% |
| Skippable blocks | 0 (all or nothing) | 17 (fine-grained control) |
| Design guideline compliance | Partial | Full (maximize-viewport) |
| Named patterns used | 2 | 4 (stat-hero, spectrum-bar, exercise-flow, table-roadmap) |

---

## Next Steps

1. **GATE**: User validates this plan before production starts
2. Create block stubs for all 22 new blocks
3. Generate AI images (batch)
4. Produce blocks following the production sequence
5. Update `book.py` and `blocks/__init__.py`
6. Full QA run-through
7. Sync with LaTeX source for any last-minute updates
