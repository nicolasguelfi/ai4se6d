"""Slide sequence — day 4 morning (09:00-12:15): CCSET12 in practice (E14), CCSET13 measuring quality (E15).

Provisional: the CCSET13 theory slides are added in production lot 3 (docs/plans/2026-11-10-013-production-days1-4.md).
"""
import blocks

BLOCKS_QUALITY = [
    # 09:00 — Welcome, /gse-resume
    blocks.bck_gensem_t2_cmd_pause_resume,
    # 09:15 — CCSET12 recall + commands (10 min), E14 (80 + 30 min), debrief (15 min)
    blocks.bck_gensem_t6_cmd_tests,
    blocks.bck_gensem_t6_cmd_produce,
    blocks.bck_gensem_t6_cmd_review,
    blocks.bck_gensem_sheet_testing_steps,
    blocks.bck_gensem_sheet_testing_check,
    # 11:45 — CCSET13 Measuring quality (theory 10 + solution 3 + E15 12 + debrief 5)
    blocks.bck_gensem_t7_cmd_health,
    blocks.bck_gensem_sheet_quality_steps,
    blocks.bck_gensem_sheet_quality_check,
]
