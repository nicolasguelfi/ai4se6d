"""Slide sequence (sequence_setup) — the block list for this part of the book.

Owned by a single writer: add blocks here in presentation order.
Day 1 afternoon (13:15-17:00): installation, FreeSelfApp workshop, debrief.
"""
import blocks

BLOCKS = [
    blocks.bck_setup_title,
    blocks.bck_setup_agenda,
    # ── Installation in the room (13:15, 75 min) ──
    blocks.bck_setup_install_sheet,
    blocks.bck_setup_step_terminal,
    blocks.bck_setup_step_tools,         # 0b git and curl (NG « ok », 2026-11-26)
    blocks.bck_setup_step_opencode,
    blocks.bck_setup_step_node,
    blocks.bck_setup_step_key,
    blocks.bck_setup_step_kit,
    blocks.bck_setup_step_gse,
    blocks.bck_setup_step_github,
    blocks.bck_setup_step_git_identity,
    blocks.bck_setup_step_check,
    blocks.bck_setup_step_tutor,
    blocks.bck_setup_tutor_sees,
    blocks.bck_setup_stuck,
    blocks.bck_setup_install_errors,
    # ── FreeSelfApp workshop (14:30, 45 min: 3 iterations + the presentation) ──
    blocks.bck_setup_workshop_intro,
    blocks.bck_setup_core_loop,
    blocks.bck_setup_live_demo,
    blocks.bck_setup_challenge,
    blocks.bck_setup_ideas,
    blocks.bck_setup_first_prompts,
    blocks.bck_setup_go_build,
    blocks.bck_setup_workshop_sheet,
    blocks.bck_setup_take_notes,
    blocks.bck_setup_build_stuck,
    blocks.bck_setup_workshop_continue,  # 14:45 iteration 2 — the client wants more
    blocks.bck_setup_present_prep,       # 14:55 iteration 3 — the presentation
    # ── Break (15:15, 15 min): late installs are helped here ──
    # ── Presentations (15:30, 60 min): 9 × 6 min on Google Meet — NG, 2026-11-24 ──
    blocks.bck_setup_presentations,
    # ── Questions on any project (16:30, 20 min) ──
    blocks.bck_setup_debrief_questions,
    # ── Wrap-up (16:50, 10 min) — bck_setup_debrief_compare left out (no time) ──
    blocks.bck_setup_debrief_cycles,  # link to the morning cycles 01-03
    blocks.bck_setup_quiz,
    blocks.bck_setup_quiz_answers,
    blocks.bck_setup_tomorrow_preview,
]
