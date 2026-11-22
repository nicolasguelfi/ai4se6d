"""Slide sequence (sequence_am) — the block list for this part of the book.

Owned by a single writer: add blocks here in presentation order.
Morning of day 2 (09:00-12:15), per docs/plans/2026-11-09-007-day2-plan-b.md.
"""
import blocks

BLOCKS_AM = [
    # 09:00 — Welcome (15 min)
    blocks.bck_calcapp_day_title,
    blocks.bck_welcome_recap,
    blocks.bck_welcome_discipline,
    blocks.bck_welcome_compare,
    blocks.bck_welcome_agenda,
    blocks.bck_welcome_chain,
    blocks.bck_welcome_catchup,
    # 09:15 — Git first (35 min: show 12, try 15, debrief 5)
    blocks.bck_git_title,
    blocks.bck_git_why,
    blocks.bck_git_concepts,
    blocks.bck_git_areas,
    blocks.bck_git_commands,
    blocks.bck_git_review,
    blocks.bck_git_checkpoint,
    blocks.bck_git_branches,
    blocks.bck_git_conventions,
    blocks.bck_gse_solution_git,  # CCSET04 — how GSE-One solves it
    blocks.bck_git_exercise,
    blocks.bck_git_sheet,
    blocks.bck_git_debrief,
    # 09:50 — Driving opencode (55 min: 3 demos, each followed by 5 min of try-it)
    blocks.bck_opencode_title,
    blocks.bck_opencode_objectives,
    blocks.bck_opencode_why,
    blocks.bck_opencode_structure,
    blocks.bck_opencode_structure_habits,
    blocks.bck_opencode_agents_md,
    blocks.bck_opencode_agents_calcapp,
    blocks.bck_opencode_try_rules,          # demo 1 + try it
    blocks.bck_opencode_context,
    blocks.bck_opencode_mentions,
    blocks.bck_opencode_hygiene,
    blocks.bck_opencode_try_context,        # demo 2 + try it
    blocks.bck_opencode_plan_build,
    blocks.bck_opencode_plan_workflow,
    blocks.bck_opencode_todo,
    blocks.bck_opencode_mcp,
    blocks.bck_opencode_context_docs,
    blocks.bck_opencode_try_plan,           # demo 3 + try it
    blocks.bck_gse_solution_context,  # CCSET05 — how GSE-One solves it
    blocks.bck_opencode_debrief,
    blocks.bck_opencode_takeaways,
    # 10:45 — Break (15 min)
    blocks.bck_plan_break,
    # 11:00 — Technical planning workshop (30 min: frame 5, practice 20, debrief 5)
    blocks.bck_plan_title,
    blocks.bck_plan_calcapp,
    blocks.bck_plan_scope,
    blocks.bck_plan_elicit,
    blocks.bck_plan_good,
    blocks.bck_plan_atomic,
    blocks.bck_plan_format,
    blocks.bck_gse_solution_plan,  # CCSET06 — how GSE-One solves it
    blocks.bck_plan_exercise,
    blocks.bck_plan_sheet,
    blocks.bck_plan_debrief,
    # 11:30 — CalcApp v0.1 part 1 starts in BLOCKS_PM
]
