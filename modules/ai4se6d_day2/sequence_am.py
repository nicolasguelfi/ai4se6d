"""Slide sequence (sequence_am) — the block list for this part of the book.

Owned by a single writer: add blocks here in presentation order.
Morning of day 2 (09:00-12:15), per docs/plans/2026-11-09-007-day2-plan-b.md.
"""
import blocks

BLOCKS_AM = [
    # 09:00 — Welcome (15 min)
    blocks.bck_d2_title,
    blocks.bck_d2_welcome_recap,
    blocks.bck_d2_welcome_discipline,
    blocks.bck_d2_welcome_compare,
    blocks.bck_d2_welcome_agenda,
    blocks.bck_d2_welcome_chain,
    blocks.bck_d2_welcome_catchup,
    # 09:15 — Git first (35 min: show 12, try 15, debrief 5)
    blocks.bck_d2_git_title,
    blocks.bck_d2_git_why,
    blocks.bck_d2_git_concepts,
    blocks.bck_d2_git_areas,
    blocks.bck_d2_git_commands,
    blocks.bck_d2_git_review,
    blocks.bck_d2_git_checkpoint,
    blocks.bck_d2_git_branches,
    blocks.bck_d2_git_conventions,
    blocks.bck_d2_git_exercise,
    blocks.bck_d2_git_sheet,
    blocks.bck_d2_git_debrief,
    # 09:50 — Driving opencode (55 min: 3 demos, each followed by 5 min of try-it)
    blocks.bck_d2_oc_title,
    blocks.bck_d2_oc_objectives,
    blocks.bck_d2_oc_why,
    blocks.bck_d2_oc_structure,
    blocks.bck_d2_oc_structure_habits,
    blocks.bck_d2_oc_agents_md,
    blocks.bck_d2_oc_agents_calcapp,
    blocks.bck_d2_oc_try_rules,          # demo 1 + try it
    blocks.bck_d2_oc_context,
    blocks.bck_d2_oc_mentions,
    blocks.bck_d2_oc_hygiene,
    blocks.bck_d2_oc_try_context,        # demo 2 + try it
    blocks.bck_d2_oc_plan_build,
    blocks.bck_d2_oc_plan_workflow,
    blocks.bck_d2_oc_todo,
    blocks.bck_d2_oc_mcp,
    blocks.bck_d2_oc_context7,
    blocks.bck_d2_oc_try_plan,           # demo 3 + try it
    blocks.bck_d2_oc_debrief,
    blocks.bck_d2_oc_takeaways,
    # 10:45 — Break (15 min)
    blocks.bck_d2_plan_break,
    # 11:00 — Technical planning workshop (30 min: frame 5, practice 20, debrief 5)
    blocks.bck_d2_plan_title,
    blocks.bck_d2_plan_calcapp,
    blocks.bck_d2_plan_scope,
    blocks.bck_d2_plan_elicit,
    blocks.bck_d2_plan_good,
    blocks.bck_d2_plan_atomic,
    blocks.bck_d2_plan_format,
    blocks.bck_d2_plan_exercise,
    blocks.bck_d2_plan_sheet,
    blocks.bck_d2_plan_debrief,
    # 11:30 — CalcApp v0.1 part 1 starts in BLOCKS_PM
]
