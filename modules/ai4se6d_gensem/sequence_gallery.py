"""Slide sequence — day 6 afternoon (13:45-17:00): gallery demos (E24), lessons learned (E25), closing.

Timetable: docs/plans/2026-11-10-012-six-days-cycles-plan.html (validated by NG, 2026-11-10).
"""
import blocks

BLOCKS_GALLERY = [
    # 13:45 — Prepare your demo (E24); the trainer checks the final repositories (open point 11)
    blocks.bck_gallery_how,
    blocks.bck_gensem_sheet_gallery_demo_steps,
    blocks.bck_gallery_visitor_grid,
    blocks.bck_gensem_sheet_gallery_demo_check,
    # 14:00 — Gallery, rotation 1 · 14:45 — rotation 2 · 15:30 — Break
    # 15:45 — E25 Lessons learned in group (30 min) · 16:15 — Monday-morning plan (20 min)
    blocks.bck_gensem_sheet_lessons_steps,
    blocks.bck_gensem_sheet_lessons_check,
    blocks.bck_closing_monday_plan,
    # 16:35 — Final questionnaire (15 min) · 16:50 — Certificates, resources (10 min)
    blocks.bck_closing_questionnaire,
    blocks.bck_closing_resources,
]
