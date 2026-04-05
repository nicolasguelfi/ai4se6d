# Proposal: `/stx-ce:go --task` — Ad-Hoc Task Mode

## Problem

The CE cycle (COLLECT → ASSESS → PLAN → PRODUCE → REVIEW → FIX → COMPOUND) is designed for structured, sequential document production. But real-world usage requires **punctual, free-form tasks** that:

- Don't correspond to a single CE phase
- May cross-cut several phases (a bit of analysis, a bit of production, a bit of review)
- Should update lifecycle artifacts so the main cycle can resume coherently
- Don't require re-running the full pipeline

### Examples of tasks that don't fit today

| Task | CE phases involved | Problem |
|------|--------------------|---------|
| "Compare source LaTeX lines 524-600 with produced blocks and list gaps" | COLLECT + REVIEW (partial) | No `compare` command; collect inventories but doesn't compare with production |
| "Review only bck_vibeeng_principles on citation accuracy" | REVIEW (scoped) | Review has no `--target` flag and no custom criteria |
| "Add a new block bck_vibeeng_workflow based on source line 612" | PRODUCE (one item) + PLAN (update) | Produce expects a full plan; adding one block requires plan amendment |
| "Update the plan to add a section on AI ethics" | PLAN (amendment) | Plan is a one-shot generation, no amendment mode |
| "Capitalize what we learned about the kitchen metaphor" | COMPOUND (targeted) | Compound scans everything; can't target a specific learning |
| "Check if the Bain study citation is correct" | REVIEW (micro) | No micro-review capability |

---

## Proposed Solution: `--task` flag on `/stx-ce:go`

### Syntax

```
/stx-ce:go --task "<free-text description of the task>"
```

### Behavior

The `--task` flag activates **Task Mode** — a lightweight, intelligent execution mode that:

1. **Analyzes** the task description to determine which CE capabilities are needed
2. **Plans** a micro-execution using available agents and tools
3. **Executes** the task, reusing CE agents as building blocks
4. **Updates** lifecycle artifacts as side-effects
5. **Reports** what was done and what changed

### Execution Flow

```
┌─────────────────────────────────────────────────┐
│  1. PARSE — Understand the task                 │
│     - Extract: scope, intent, targets, sources  │
│     - Classify into task archetype(s)           │
│     - Identify required CE capabilities         │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  2. CONTEXT — Load relevant CE artifacts        │
│     - Latest plan (if exists)                   │
│     - Latest review (if exists)                 │
│     - Producer profile (if exists)              │
│     - Source files (if referenced)              │
│     - Target blocks (if specified)              │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  3. EXECUTE — Run the task using CE agents      │
│     - Use existing agents as building blocks    │
│     - Combine capabilities as needed            │
│     - Apply design guideline if active          │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  4. RECONCILE — Update lifecycle artifacts      │
│     - Amend plan if blocks added/removed        │
│     - Append to review if findings produced     │
│     - Write to solutions if learnings captured  │
│     - Update producer profile if relevant       │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  5. REPORT — Summarize what was done            │
│     - Actions taken                             │
│     - Artifacts modified/created                │
│     - Impact on cycle state                     │
│     - Suggested next steps                      │
└─────────────────────────────────────────────────┘
```

---

## Task Archetypes

The task analyzer classifies the user's request into one or more archetypes. Each archetype has a default execution strategy that can be combined.

### Archetype 1: COMPARE (source ↔ production coverage)

**Triggers**: "compare", "what's covered", "what's missing", "coverage", "gaps between source and"

**Execution**:
1. Read the source document (file path, line range, or URL)
2. Extract themes/sections/concepts from source
3. Read the target blocks (all, or filtered by pattern)
4. For each source theme: search produced blocks for semantic coverage
5. Produce a **coverage matrix**:

```markdown
| Source Theme | Lines | Status | Block(s) | Fidelity |
|-------------|-------|--------|----------|----------|
| VibeCoding definition | 524-526 | COVERED | bck_vibecoding_definition | Exact |
| Conductor metaphor | 538 | REPLACED | bck_vibecoding_paradigm | Adapted (cook→customer) |
| FlowGen experiment | 582 | COVERED | bck_vibeeng_evidence | Summarized |
| Package hallucination detail | 844-846 | PARTIAL | bck_vibecoding_danger_halluc | Key stat only |
| Tool comparison table | 1855-1864 | COVERED | bck_ide_comparison | Table-roadmap |
| MCP registry details | 1765-1770 | MISSING | — | Not produced |
```

6. Produce a **gap report** with recommendations

**Artifact**: `docs/reviews/YYYY-MM-DD-coverage-task.md`

**Reconciliation**: If gaps are significant, propose plan amendments (new blocks to add).

---

### Archetype 2: TARGETED REVIEW (custom scope + custom criteria)

**Triggers**: "review", "check", "verify", "audit" + block name or criteria

**Execution**:
1. Identify scope: specific block(s), pattern, sequence, or full project
2. Identify criteria: one of the 5 built-in perspectives, OR a custom criterion from the user's description
3. For built-in perspective: reuse the corresponding review agent
4. For custom criterion: create an ad-hoc review agent with the user's criteria as mandate
5. Execute review on the scoped target
6. Produce findings with standard severity levels

**Artifact**: Findings appended to latest review file under "Task Review" section, or new `docs/reviews/YYYY-MM-DD-task-review.md`

**Reconciliation**: New findings feed into the next `/stx-ce:fix` cycle.

**Examples**:
```
/stx-ce:go --task "Review bck_vibecoding_danger_* blocks on citation accuracy"
/stx-ce:go --task "Check that all stat-hero slides have proper cite() references"
/stx-ce:go --task "Verify the kitchen metaphor is used exactly 5 times, no more"
```

---

### Archetype 3: TARGETED PRODUCTION (add/modify one or few blocks)

**Triggers**: "add", "create", "produce", "write", "implement" + block description

**Execution**:
1. Load current plan (if exists)
2. Determine what to produce (new block, modification, split, merge)
3. Produce using `/stx-designer:block-new` or `/stx-designer:update`
4. Apply design guideline if active
5. Run `/stx-designer:audit --target` on the produced block
6. Fix any findings

**Artifact**: New/modified block files

**Reconciliation**:
- **Plan amendment**: Add the new block to the plan document (appended section "Plan Amendments")
- **book.py update**: Insert the block at the correct position
- Plan status updated to reflect the addition

**Examples**:
```
/stx-ce:go --task "Add a block bck_vibeeng_workflow showing the full VibeEngineering workflow diagram"
/stx-ce:go --task "Split bck_ide_cursor into two blocks: overview and architecture"
```

---

### Archetype 4: PLAN AMENDMENT (update plan without re-generating)

**Triggers**: "update plan", "add to plan", "remove from plan", "reorder", "amend plan"

**Execution**:
1. Load current plan
2. Apply the requested change (add section, remove block, reorder, update description)
3. Write amended plan (same file, new section "Amendments" with timestamp)
4. Do NOT regenerate — preserve all existing plan content

**Artifact**: Updated plan file with amendment log

**Reconciliation**: The amended plan becomes the reference for subsequent `/stx-ce:produce` runs.

**Examples**:
```
/stx-ce:go --task "Add a section on AI ethics after the IDE ecosystem in the plan"
/stx-ce:go --task "Remove bck_vibeeng_rebranding from the plan — it's redundant"
/stx-ce:go --task "Move bck_vibeeng_evidence before the spectrum in the plan"
```

---

### Archetype 5: TARGETED COMPOUND (capitalize one specific learning)

**Triggers**: "capitalize", "save learning", "document pattern", "extract pattern"

**Execution**:
1. Identify what to capitalize (pattern, technique, anti-pattern, workaround)
2. Check for duplicates in `docs/solutions/`
3. Write or update the solution file
4. Update producer profile if relevant
5. Update design-guideline patterns if relevant

**Artifact**: `docs/solutions/<category>/YYYY-MM-DD-<topic>.md`

**Reconciliation**: Solution available for future cycles via `learnings-researcher` agent.

**Examples**:
```
/stx-ce:go --task "Capitalize the kitchen metaphor as a pattern for all modules"
/stx-ce:go --task "Document the stat-hero pattern we refined during this production"
```

---

### Archetype 6: SOURCE ANALYSIS (deep-dive into a source without production)

**Triggers**: "analyze source", "extract from source", "list topics in", "what does the source say about"

**Execution**:
1. Read the source document (path + optional line range)
2. Extract structure, themes, key concepts, statistics, citations
3. Produce a structured analysis report
4. Optionally compare with existing plan/blocks

**Artifact**: `docs/collect/YYYY-MM-DD-task-analysis.md`

**Reconciliation**: Analysis available for subsequent plan amendments or production.

**Examples**:
```
/stx-ce:go --task "Analyze source lines 1083-1870 and list all IDE tools mentioned with their key stats"
/stx-ce:go --task "Extract all statistics with citations from the source document"
```

---

## Composite Tasks

A single `--task` can combine multiple archetypes. The analyzer decomposes and sequences them:

```
/stx-ce:go --task "Compare source lines 524-600 with bck_vibecoding_* blocks,
                    identify gaps, produce missing blocks, and update the plan"
```

Decomposition:
1. COMPARE (source 524-600 vs bck_vibecoding_*)
2. TARGETED PRODUCTION (create blocks for gaps)
3. PLAN AMENDMENT (add new blocks to plan)

Each step feeds into the next. The report covers all steps.

---

## Artifact Reconciliation Rules

The critical design principle: **after a task, the lifecycle is coherent**.

| Task produces... | Reconciliation action |
|------------------|-----------------------|
| New block(s) | Append to plan "Amendments" section; update book.py |
| Review findings | Append to latest review or create task-review file |
| Plan changes | Write amendment log with timestamp in plan file |
| Solutions/patterns | Write to `docs/solutions/`; update design-guideline if pattern |
| Source analysis | Write to `docs/collect/` for future reference |
| Nothing (read-only) | No reconciliation needed; report only |

### Plan Amendment Format

```markdown
## Amendments

### 2026-04-04 — Task: "Add block on AI ethics"

- **Added**: `bck_ethics_overview` after Block 38 (bck_ide_cursor_choice)
- **Reason**: Source coverage gap identified — lines 402-410 not covered
- **Impact**: Total blocks 41 → 42, total slides +2
- **book.py**: Updated, block inserted at position 39
```

### Review Task Findings Format

```markdown
## Task Review — 2026-04-04

**Task**: "Verify citation accuracy on danger slides"
**Scope**: bck_vibecoding_danger_*
**Criteria**: Every statistic must have cite() + # REF: comment

| Block | Finding | Severity |
|-------|---------|----------|
| bck_vibecoding_danger_vuln | cite("tihanyi2024formai") verified ✓ | OK |
| bck_vibecoding_danger_halluc | cite("spracklen2024packages") verified ✓ | OK |
| bck_vibecoding_danger_paradox | cite("gitlab2024devsecops") — URL returns 404 | MAJOR |
```

---

## Implementation Approach

### Option 1: Extend `ce-go.md` (recommended)

Add `--task` as a new flag in the existing skill file. When `--task` is set, bypass the standard 7-step pipeline and enter Task Mode instead.

**Changes to `ce-go.md`**:
```
### Parse Arguments and Flags

- `--task "<description>"`: Enter Task Mode. Bypass the standard pipeline.
  Analyze the task, classify into archetypes, execute, reconcile, report.
  All other flags are ignored when --task is set.
```

**New section in `ce-go.md`**:
```
### Task Mode

When `--task` is set:

1. Load CE context (plan, review, profile, guideline)
2. Analyze task description → classify into archetype(s)
3. For each archetype, execute using available CE agents and designer commands
4. Reconcile: update plan/review/solutions as side-effects
5. Report: actions taken, artifacts modified, suggested next steps
6. Pipeline mode rules apply: minimal prompting, auto-context, error handling
```

### Option 2: New skill file `ce-task.md` (alternative)

Create a dedicated skill file. Simpler to maintain but requires a new slash command registration.

### Recommendation: Option 1

Extending `ce-go.md` keeps the interface unified — one command (`/stx-ce:go`) with two modes:
- **Cycle mode** (default): the standard 7-step pipeline
- **Task mode** (`--task`): ad-hoc execution with lifecycle reconciliation

---

## Interaction with Existing Flags

| Flag | In Cycle Mode | In Task Mode |
|------|--------------|--------------|
| `--task "<desc>"` | — | Activates Task Mode |
| `--quick` | Skip COLLECT+ASSESS | Ignored |
| `--from-plan <path>` | Resume from plan | Uses this plan as context |
| `--interactive` | Force interactive planning | Ignored (tasks are inherently interactive) |
| `--review-only` | Only review | Ignored (use archetype 2 instead) |
| `--no-deploy` | Skip deployment | Ignored (tasks don't deploy) |
| `--import <path>` | Force pathway A | Ignored |
| `--improve` | Force pathway B | Ignored |

---

## Summary

| Aspect | Standard Cycle | Task Mode |
|--------|---------------|-----------|
| **Trigger** | `/stx-ce:go` (no --task) | `/stx-ce:go --task "..."` |
| **Flow** | Fixed 7-step pipeline | Dynamic, archetype-driven |
| **Scope** | Full project | Targeted (blocks, sections, sources) |
| **Duration** | Long (hours) | Short (minutes to ~1 hour) |
| **Gates** | 3 mandatory gates | None (report at end) |
| **Artifacts** | Full set (7 phases) | Only what the task requires |
| **Reconciliation** | N/A (artifacts are the output) | Updates plan/review/solutions |
| **Resumability** | Resume from any phase | One-shot (no resume needed) |
