"""Slide sequence — day 3 afternoon (13:30-17:00): first use of GSE-One, exercises E11-E13 (P1, P3, P5)."""
import blocks

BLOCKS_DISCOVERY = [
    blocks.bck_gensem_afternoon_title,
    # 13:30 — E11 Discover GSE-One (50 min) + debrief (10 min)
    blocks.bck_gensem_install_calcapp,
    blocks.bck_gensem_sheet_discover_steps,
    blocks.bck_gensem_sheet_discover_check,
    # 14:30 — E12 Plan the sprint (recall 5 + 35 + debrief 5)
    blocks.bck_gensem_t3_cmd_plan,
    blocks.bck_gensem_sheet_plan_steps,
    blocks.bck_gensem_sheet_plan_check,
    # 15:15 — Break (15 min)
    # 15:30 — E13 Requirements and design (65 min) + debrief (10 min)
    blocks.bck_gensem_sheet_requirements_steps,
    blocks.bck_gensem_sheet_requirements_check,
    # 16:45 — Day close: push, /gse-pause, quiz
    blocks.bck_gensem_concepts_quiz,
    blocks.bck_gensem_concepts_quiz_answers,
]
