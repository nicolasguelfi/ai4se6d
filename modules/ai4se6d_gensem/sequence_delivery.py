"""Slide sequence — day 4 afternoon (13:15-17:00): CCSET14 delivery and capitalisation (E16), CCSET15 framing a project (E17, E18)."""
import blocks

BLOCKS_DELIVERY = [
    # 13:15 — CCSET14 (theory 12 + solution 3), E16 (60 min), debrief (15 min)
    blocks.bck_delivery_title,
    blocks.bck_delivery_merge_strategies,
    blocks.bck_delivery_release,
    blocks.bck_delivery_maintenance,
    blocks.bck_delivery_retrospective,
    blocks.bck_gse_solution_delivery,
    blocks.bck_gensem_sheet_delivery_steps,
    blocks.bck_gensem_sheet_delivery_check,
    # 14:45 — Break (15 min)
    # 15:00 — CCSET15 Framing a project (theory 15 + solution 5), E17 (25 min), E18 (45 min)
    blocks.bck_framing_title,
    blocks.bck_framing_challenge,
    blocks.bck_framing_scope,
    blocks.bck_framing_rules,
    blocks.bck_framing_ideas,
    blocks.bck_gse_solution_framing,
    blocks.bck_gensem_sheet_project_card_steps,
    blocks.bck_gensem_sheet_project_card_check,
    blocks.bck_gensem_sheet_project_start_steps,
    blocks.bck_gensem_sheet_project_start_check,
    # 16:30 — Push both repositories, debrief, quiz
    blocks.bck_gensem_practice_quiz,
    blocks.bck_gensem_practice_quiz_answers,
]
