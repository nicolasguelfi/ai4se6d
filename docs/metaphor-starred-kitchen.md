# Metaphor Reference — The Starred Kitchen

## Purpose

This document defines the **central metaphor** used across all modules of the "VibeEngineering: The Future of Software Development with Generative AI" training. It maps the journey from naive AI-assisted coding to disciplined generative software engineering onto the world of professional gastronomy — from cooking at home to running a Michelin-starred hotel restaurant.

This metaphor is **shared across all 6 training days** and all modules. Each module may reference it lightly, but should never over-explain it. Once introduced in the vibecoding module (Day 1), it becomes a background vocabulary that participants recognize and build upon.

---

## Why This Metaphor

- **Universal** — everyone has cooked; everyone has eaten at a restaurant
- **Continuous spectrum** — from home cooking to starred restaurant, no binary jumps
- **Multi-agent native** — the brigade de cuisine is a natural multi-agent system
- **Covers all SE dimensions** — requirements, architecture, testing, review, deployment, scaling, compliance, maintainability, compound engineering
- **Proportional stakes** — not "people die" (too dramatic for enterprise SE), but lost stars, lost clients, financial damage, regulatory shutdown (exactly the stakes of production software)
- **Aspirational** — nobody wants to stay a customer; everyone wants to be the chef

---

## The Spectrum

| Discipline Level | Kitchen Context | SE Context | Stakes |
|-----------------|----------------|------------|--------|
| **Naive VibeCoding** | Cooking at home | Personal prototype | None — if it's edible, it's done |
| **Guided VibeCoding** | Dinner for friends | Internal tool | Personal reputation, low consequences |
| **Structured VibeCoding** | Bistro / brasserie | Team product | Paying customers, online reviews, basic hygiene standards |
| **VibeEngineering** | Starred hotel restaurant | Production / enterprise / regulated | Michelin stars, regulation, client preferences, financial consequences, sustainability |
| **Generative SE** | Culinary director of a hotel group | Multi-project engineering leadership | Multiple restaurants, cookbooks, training programs, brand, scaling |

---

## Role Mapping

| Kitchen Role | SE Role | Description |
|-------------|---------|-------------|
| **Customer** | End user / VibeCoder | Describes what they want, trusts the result, doesn't know the recipe |
| **Home cook** | Junior VibeCoder | Improvises, no formal training, personal stakes only |
| **Bistro cook** | Structured developer | Follows some standards, serves paying customers |
| **Chef de cuisine** | VibeEngineer / Tech lead | Designs the menu, writes recipes, leads the brigade, reviews at critical points |
| **Sous-chef** | Senior agent / sub-agent | Assists the chef, manages sections, takes over when needed |
| **Chef de partie** | Specialized agent | Expert in one domain (sauces, pastry = tests, UI, API) |
| **Commis** | Parallel agent | Handles simpler tasks under supervision |
| **Sommelier** | MCP server / external API | Specialized knowledge source, consulted for pairings |
| **Supplier** | MCP server / data provider | Provides raw materials (verified, traceable) |
| **Nutritionist** | Requirements engineer | Prescribes what the client needs (not what they want) |
| **Health inspector** | Auditor / compliance reviewer | Verifies standards are met, can shut down the kitchen |
| **Food critic** | End user / QA / reviewer | Evaluates the final result, writes public reviews |
| **Culinary director** | Generative Software Engineer | Designs concepts across restaurants, writes cookbooks, trains teams, scales |

---

## Vocabulary Mapping

### Preparation & Planning

| Kitchen | SE / VibeEngineering |
|---------|---------------------|
| Menu / carte | Product backlog |
| Client order | User story, requirement |
| Client preferences / allergies | Non-functional requirements (NFR) |
| Recipe | Architecture, project rules (.cursorrules, CLAUDE.md) |
| Mise en place | Context engineering — everything prepared, organized, labeled before work starts |
| Tasting menu design | Sprint planning, iteration scope |
| Seasonal menu adaptation | Requirement evolution, source document sync |

### Execution & Production

| Kitchen | SE / VibeEngineering |
|---------|---------------------|
| Brigade de cuisine | Multi-agent orchestration |
| Kitchen (the workspace) | IDE (Cursor, VS Code) |
| Professional utensils | Plugins, generative tools (linter, test runner, doc generator) |
| Certified suppliers | MCP servers (verified data sources, APIs) |
| Cooking (the act) | Code generation by AI agents |
| Tasting at each step | TDD, continuous testing |
| Plating / dressage | UI/UX, final deliverable presentation |
| Service (dinner service) | Release, deployment |
| Le coup de feu (rush hour) | Sprint deadline, peak load, incident response |

### Quality & Compliance

| Kitchen | SE / VibeEngineering |
|---------|---------------------|
| HACCP standards | Review gates, V&V, security audits |
| Lot traceability | Git history, audit trail, provenance |
| Cross-contamination | SQL injection, XSS, corrupted dependencies |
| Health inspection | Security audit, compliance check |
| Administrative shutdown | Regulatory shutdown, critical vulnerability disclosure |
| Michelin stars | SLA, certifications, product quality rating |
| Losing a star | Production incident, trust erosion, market loss |
| TripAdvisor review | Bug report, public user feedback |
| Food recall | Hotfix, rollback, incident response |

### Growth & Capitalization

| Kitchen | SE / VibeEngineering |
|---------|---------------------|
| House cookbook | Compound engineering — capitalized patterns and recipes |
| Training an apprentice | Onboarding, documentation, knowledge transfer |
| Inventing a new dish | Innovation, R&D, creative problem solving |
| Opening a second restaurant | Multi-environment deployment, scaling |
| Hotel chain | CI/CD pipeline, enterprise deployment |
| Franchise standards | Shared project rules, organizational standards |
| Culinary school | Training program (this training!) |

### Maintainability & Sustainability

| Kitchen | SE / VibeEngineering |
|---------|---------------------|
| Same quality every night | Production reliability, consistency |
| Staff rotation / shifts | Team changes, developer turnover |
| Seasonal ingredient changes | Dependency updates, API evolution |
| Kitchen that no other chef can work in | Unmaintainable code, technical debt |
| Menu that only one chef can execute | Bus factor = 1 |
| Documented recipe vs. "chef's instinct" | Documented architecture vs. tribal knowledge |

---

## Module Integration Guide

### How to use this metaphor across modules

**Rule 1 — Introduce once, reference lightly thereafter.**
The metaphor is formally introduced in **ai4se6d_vibecoding** (Day 1, Part 2). All subsequent modules can reference it with a word or phrase ("remember the kitchen", "this is your mise en place") without re-explaining.

**Rule 2 — Never force it.**
If a concept maps naturally to the kitchen, use it. If it doesn't, skip the metaphor for that slide. Not every SE concept needs a culinary equivalent.

**Rule 3 — Let participants build on it.**
After the introduction, participants will start making their own connections ("so this is like changing suppliers mid-service?"). Encourage this — it means the metaphor is working.

**Rule 4 — Escalate stakes across days.**
Day 1 = home cooking → bistro. Day 2-3 = brasserie → restaurant. Day 4-6 = starred hotel restaurant → hotel group. The stakes grow as the training progresses.

### Per-module mapping

| Module | Day | Kitchen Context | Key Metaphor Moments |
|--------|-----|----------------|---------------------|
| **ai4se6d_genai_intro** | 1 AM | Discovering the ingredients and utensils | "Today you discovered the ingredients (GenAI, LLMs) and the utensils (tools). Now let's cook." |
| **ai4se6d_vibecoding** | 1 AM/PM | From customer to chef — the full introduction | Formal introduction of the metaphor. Spectrum from home to starred restaurant. |
| *(cursor mastery)* | 2 | Setting up your professional kitchen | Cursor = your professional kitchen. Rules = recipes. Agents = brigade. Context = mise en place. |
| *(git + requirements)* | 3 | Writing the menu, sourcing suppliers | Requirements = menu with client preferences. Git = lot traceability. NFR = allergies and dietary constraints. |
| *(iterative improvement)* | 4 | Running a dinner service | Iterations = courses (starter, main, dessert, each validated). Refactoring = reorganizing the kitchen for efficiency. |
| *(mini-project)* | 5 | The gala dinner | Full service for a demanding event. All disciplines combined. |
| *(ethics + governance)* | 6 | The Michelin guide and health inspections | Ethics = responsible sourcing. Governance = HACCP compliance. Sustainability = kitchen's environmental footprint. |

---

## Key Narrative Moments

### The Pivot (ai4se6d_vibecoding, Act II)

After Exercise 2 (naive VibeCoding = cooking at home), the dangers are revealed. The pivot:

> "Your dish looked good. But imagine tomorrow your restaurant hosts a gala dinner for 200 guests. Individual dietary requirements. Press in attendance. **Would you cook the same way you just did?**"

This is the emotional turning point where the audience understands WHY discipline matters.

### The Closing (ai4se6d_vibecoding)

> "Same ingredients, same utensils, same kitchen. The difference: **the discipline of the chef.**"

### The Training Arc

> "This training is your culinary school. In 6 days, you go from the customer's seat to the chef's pass. Same AI tools as everyone else — but you'll know how to run the kitchen."

---

## Anti-patterns (when NOT to use the metaphor)

- **Don't use it for deeply technical explanations** (Transformer architecture, tokenization, embeddings). The metaphor is for methodology and workflow, not for AI internals.
- **Don't force every concept into the kitchen.** If it takes more than one sentence to explain the mapping, drop it.
- **Don't repeat the full mapping.** After the introduction, a single word ("mise en place", "your brigade") is enough. Participants get it.
- **Don't use it condescendingly.** The audience are professional developers. The metaphor clarifies, it doesn't simplify. Treat it as a shared vocabulary, not a dumbed-down explanation.
- **Don't mix with other metaphors** (aviation, orchestra, etc.) in the same slide. One metaphor, consistently applied.
