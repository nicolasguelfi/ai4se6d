"""Slide sequence (sequence_pm) — Day 2 afternoon, 11:30-17:30.

Owned by a single writer: add blocks here in presentation order.
"""
import blocks

BLOCKS_PM = [
    blocks.bck_build_title,  # Section — CalcApp v0.1 Part 1
    blocks.bck_build_why_tests,  # Why start with tests?
    blocks.bck_build_tdd_cycle,  # TDD in one picture — red, green, refactor
    blocks.bck_build_demo,  # Live demo — one full red-green-refactor cycle in opencode
    blocks.bck_build_golden_rule,  # The AI-TDD discipline and its golden rule
    blocks.bck_build_mutant,  # The mutant test trick
    blocks.bck_build_agents_md,  # Testing rules in AGENTS.md before coding
    blocks.bck_build_prompts,  # Two prompts per task — RED then GREEN
    blocks.bck_gse_solution_tests,  # CCSET07 — how GSE-One solves it
    blocks.bck_build_ex_steps,  # Exercise sheet — task 1 of your own plan (goal and steps)
    blocks.bck_build_ex_check,  # Exercise sheet — task 1: done when, mid-point, if stuck
    blocks.bck_build_fallback_item,  # Fallback prompt A — ExpenseItem
    blocks.bck_build_fallback_form,  # Fallback prompt B — ExpenseForm
    blocks.bck_build_rescue,  # Rescue — restart from tag j2-start
    blocks.bck_build_debrief,  # Debrief — Part 1
    blocks.bck_build_lunch,  # Lunch break
    blocks.bck_tasks_title,  # Section — CalcApp v0.1 Part 2
    blocks.bck_tasks_reorient,  # Post-lunch re-orientation checklist
    blocks.bck_tasks_catchup,  # Catch-up — restart from tag j2-part1
    blocks.bck_tasks_loop,  # The same loop for every task
    blocks.bck_tasks_routing,  # Task — routing and navigation (prompts)
    blocks.bck_tasks_routing_review,  # Review checklist — routing
    blocks.bck_tasks_data,  # Task — data layer (prompts)
    blocks.bck_tasks_data_review,  # Review checklist — data layer
    blocks.bck_tasks_ui,  # Task — minimal UI (10 minutes max)
    blocks.bck_tasks_ex_steps,  # Exercise sheet — next tasks of your plan (goal and steps)
    blocks.bck_tasks_ex_check,  # Exercise sheet — Part 2: done when, mid-point, if stuck
    blocks.bck_tasks_notfinished,  # If you did not finish Part 2
    blocks.bck_tasks_debrief,  # Debrief — Part 2
    blocks.bck_review_title,  # Section — AI-assisted code review
    blocks.bck_review_paradox,  # The speed paradox — AI writes bugs faster
    blocks.bck_review_scale,  # Review at scale — 60 million Copilot code reviews
    blocks.bck_review_jones,  # Formal inspection vs testing — defect removal efficiency
    blocks.bck_review_size,  # Optimal review size — 200 to 400 lines
    blocks.bck_review_catches,  # What AI review catches well and what it misses
    blocks.bck_review_prompts,  # Weak vs effective review prompts
    blocks.bck_review_triage,  # Triage findings — HIGH / MEDIUM / LOW
    blocks.bck_review_judgment,  # AI review output is input to your judgment — accept, defer, refuse
    blocks.bck_gse_solution_review,  # CCSET08 — how GSE-One solves it
    blocks.bck_review_break,  # Afternoon break
    blocks.bck_review_ex_steps,  # Exercise sheet — review today's diff (goal and steps)
    blocks.bck_review_ex_prompt,  # The review prompt for the plan agent
    blocks.bck_review_ex_fix,  # Fix one finding, test first
    blocks.bck_review_ex_check,  # Exercise sheet — review: done when, mid-point, if stuck
    blocks.bck_review_readme_rule,  # Living documentation — the 80/20 rule
    blocks.bck_review_readme_ex,  # Exercise — README 80/20
    blocks.bck_review_ex_debrief,  # Debrief — review practice
    blocks.bck_ship_release,  # Exercise — ship v0.1 (merge and tag)
    blocks.bck_ship_checklist,  # v0.1 — what you just built
    blocks.bck_bridge_loop,  # Today's manual loop next to the GSE-One commands
    blocks.bck_bridge_debrief,  # Debrief — the whole day
    blocks.bck_bridge_quiz,  # Hands-up quiz — 5 questions
    blocks.bck_bridge_quiz_answers,  # Hands-up quiz — answers
    blocks.bck_bridge_tomorrow,  # Preview of Day 3
    blocks.bck_close_buffer,  # Buffer — catch up, questions, tutor window
]
