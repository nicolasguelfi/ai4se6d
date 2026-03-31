---
title: Hierarchical Naming Convention for Blocks, Images, and Identifiers
date: 2026-03-30
category: structure
document_type: presentation
problem_type: pattern
pathway: B: IMPROVE
scope: collection
origin: AI4SE-NG (migrated 2026-03-31)
tags: [naming, blocks, images, style-ids, alphabetical-grouping, maintainability]
---

# Hierarchical Naming Convention for Blocks, Images, and Identifiers

## Context

| Field | Value |
|-------|-------|
| Document | AI4SE-NG |
| Audience | Software engineering trainees |
| Objective | Establish a naming convention that enables natural alphabetical grouping and context-free reuse |
| Pathway | B: IMPROVE |

The project initially used numeric prefixes (`bck_b1_`, `bck_p1_`) to group blocks by section.
This created maintenance problems: reordering sections required renaming files, and blocks
could not be reused in a different context without carrying a meaningless number.

## Problem

**Symptoms:**
- Block filenames like `bck_b1_transformers.py` carry a "Block 1" prefix that has no semantic meaning
- Alphabetical file listing groups by number (`b1_*`) rather than by topic
- Reusing a block in another project or section requires renaming to avoid confusion
- Style IDs like `p1_title` embed a section number that breaks if sections are reordered

**Root cause:**
Using ordinal numbers (b1, b2, p1, p2) as group identifiers instead of semantic category names.

## Solution

**Rule: `bck_<category>_<topic>.py`** — the most general concept comes first (category),
the most specific comes last (topic). This creates natural alphabetical clusters.

### Naming principles

1. **Never use numbers** in filenames, style IDs, or image names (except content-inherent
   numbers like dates or version numbers in text)
2. **Category first, topic second** — enables alphabetical grouping:
   `bck_llm_capabilities`, `bck_llm_comparison`, `bck_llm_tokens` all cluster together
3. **Self-sufficient names** — each name must be understandable without its group context:
   `bck_training` is ambiguous (training of what?), `bck_llm_training` is clear
4. **Short group prefixes only when stable** — use a category prefix only when the
   element will never appear in another group with a different name

### Applied renaming (AI4SE-NG)

| Before (numeric) | After (hierarchical) | Category |
|---|---|---|
| `bck_p1_title` | `bck_intro_title` | `intro_` |
| `bck_p1_roadmap` | `bck_intro_roadmap` | `intro_` |
| `bck_b1_what_is_ai` | `bck_ai_definition` | `ai_` |
| `bck_b1_ai_vs_genai` | `bck_ai_vs_genai` | `ai_` |
| `bck_b1_ethics` | `bck_ai_ethics` | `ai_` |
| `bck_b1_genai_revolution` | `bck_genai_revolution` | `genai_` |
| `bck_b1_landscape` | `bck_genai_landscape` | `genai_` |
| `bck_b1_takeaways` | `bck_genai_takeaways` | `genai_` |
| `bck_b1_how_llms_work` | `bck_llm_how_work` | `llm_` |
| `bck_b1_llm_comparison` | `bck_llm_comparison` | `llm_` |
| `bck_b1_transformers` | `bck_llm_transformers` | `llm_` |
| `bck_b1_tokens` | `bck_llm_tokens` | `llm_` |
| `bck_b1_training` | `bck_llm_training` | `llm_` |
| `bck_b1_capabilities` | `bck_llm_capabilities` | `llm_` |
| `bck_b1_limitations` | `bck_llm_limitations` | `llm_` |

### Style IDs follow the same rule

```python
# Before
Style.create(s.Huge + s.bold, "p1_title")

# After
Style.create(s.Huge + s.bold, "intro_title")
```

### The rule applies to all identifiers

- **Block files**: `bck_<category>_<topic>.py`
- **Style IDs**: `<category>_<role>` (e.g., `intro_title`, `llm_card_border`)
- **Image names**: `<category>_<subject>` (e.g., `genai_landscape.png`, not `b1_landscape.png`)
- **CSS class prefixes**: same hierarchy

**Key decisions:**
- Category comes first for alphabetical grouping (not `bck_how_work_llm`)
- Vague standalone names get a category prefix (`training` -> `llm_training`)
- Already-specific names drop the old numeric prefix (`ai_vs_genai` needs no group)

## Prevention

- Never introduce numbers in identifiers unless they represent inherent content (dates, versions)
- When creating a new block, choose the category first, then the topic
- Run `ls blocks/ | sort` to verify alphabetical clustering after adding blocks
- Define the category taxonomy in project documentation before starting production

## References

| Type | Reference |
|------|-----------|
| Block | All 15 renamed blocks in AI4SE-NG |
| Project | AI4SE-NG |
| Documentation | coding_standards.md, section 8 |
| Related solutions | — |
