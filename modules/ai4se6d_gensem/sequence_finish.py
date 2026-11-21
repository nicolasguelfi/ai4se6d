"""Slide sequence — day 6 morning (09:00-12:45): finish the sprint (README = its last task, from 11:00),
deliver, tag demo and freeze (E22), audit (E23).

Timetable: docs/plans/2026-11-10-012-six-days-cycles-plan.html (validated by NG, 2026-11-10).
"""
import blocks

BLOCKS_FINISH = [
    # 09:00 — Welcome: tutor update, /gse-resume (15 min)
    blocks.bck_gensem_today_finish,
    # 09:15 — Finish the sprint (E20) (75 min, break 10:30, 45 min)
    blocks.bck_project_finish_line,
    # 11:00 — the last task of the sprint: empty shells, README project card (sheet E22, step 1)
    blocks.bck_project_readme_card,
    # 11:30 — E22 Deliver, tag demo (11:30), then freeze = demo rehearsal (12:00) (45 min)
    blocks.bck_gensem_sheet_deliver_freeze_steps,
    blocks.bck_gensem_sheet_deliver_freeze_check,
    # 12:15 — E23 Audit your project: cycle CCSET03 applied (30 min)
    blocks.bck_ethics_recall,
    blocks.bck_gensem_sheet_project_audit_steps,
    blocks.bck_ethics_readme_section,
    blocks.bck_gensem_sheet_project_audit_check,
    # 12:45 — Lunch
]
