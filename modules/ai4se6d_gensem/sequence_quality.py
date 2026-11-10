"""Slide sequence — day 4 morning (09:00-12:15): CCSET12 in practice (E14), CCSET13 measuring quality (E15).

Timetable: docs/plans/2026-11-10-012-six-days-cycles-plan.html (validated by NG, 2026-11-10).
"""
import blocks

BLOCKS_QUALITY = [
    # 09:00 — Welcome, /gse-resume, quality kit (15 min)
    blocks.bck_gensem_today_practice,
    blocks.bck_gensem_t2_cmd_pause_resume,
    blocks.bck_gensem_quality_kit,
    # 09:15 — CCSET12 in practice: recall + commands (10 min), E14 (80 min, break, 30 min), debrief (15 min)
    blocks.bck_vv_practice_title,
    blocks.bck_gensem_command_form,
    blocks.bck_gensem_t6_cmd_tests,
    blocks.bck_gensem_t6_cmd_produce,
    blocks.bck_gensem_t6_cmd_review,
    blocks.bck_gensem_sheet_testing_steps,
    blocks.bck_gensem_sheet_testing_check,
    # 11:45 — CCSET13 Measuring quality (theory 10 + solution 3 + E15 12 + debrief 5)
    blocks.bck_quality_title,
    blocks.bck_quality_signals,
    blocks.bck_quality_coverage_limits,
    blocks.bck_quality_continuous_integration,
    blocks.bck_gse_solution_quality,
    blocks.bck_gensem_sheet_quality_steps,
    blocks.bck_gensem_sheet_quality_check,
]
