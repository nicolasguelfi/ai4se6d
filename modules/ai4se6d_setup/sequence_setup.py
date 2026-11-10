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
    # ── FreeSelfApp workshop (14:30 + 15:30, 2 × 45 min) ──
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
    blocks.bck_setup_workshop_continue,
    # ── Debrief (16:15, 30 min) ──
    blocks.bck_setup_debrief_compare,
    blocks.bck_setup_debrief_questions,
    blocks.bck_setup_debrief_cycles,  # link to the morning cycles 01-03
    blocks.bck_setup_quiz,
    blocks.bck_setup_quiz_answers,
    blocks.bck_setup_tomorrow_preview,
]
