"""Slide sequence — day 5 afternoon (13:15-17:00): sprint, waves 3-4, milestone, debrief.

Timetable: docs/plans/2026-11-10-012-six-days-cycles-plan.html (validated by NG, 2026-11-10).
"""
import blocks

BLOCKS_SPRINT = [
    # 13:15 — Sprint (E20); deployment waves 3 (13:15) and 4 (14:00) (E19)
    blocks.bck_project_afternoon,
    # 15:00 — Break (15 min)
    # 15:15 — Sprint; the trainer validates plans and requirements on the fly (open point 14)
    blocks.bck_project_milestone,
    # 16:30 — Debrief: milestone, deployment (cycle 16); 16:45 push, /gse-pause
    blocks.bck_project_day_debrief,
]
