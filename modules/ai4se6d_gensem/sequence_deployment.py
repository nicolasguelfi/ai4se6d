"""Slide sequence — day 5 morning (09:00-12:15): CCSET16 deployment, then the mini-project sprint (E20, E21, E19).

Timetable: docs/plans/2026-11-10-012-six-days-cycles-plan.html (validated by NG, 2026-11-10).
Production tracker: docs/plans/2026-11-20-014-production-days5-6.md.
"""
import blocks

BLOCKS_DEPLOYMENT = [
    # 09:00 — Welcome: tutor update, /gse-resume on the mini-project (15 min)
    blocks.bck_gensem_today_project,
    blocks.bck_gensem_resume_project,
    # 09:15 — CCSET16 Deployment (theory 20 min)
    blocks.bck_deploy_title,
    blocks.bck_deploy_code_to_service,
    blocks.bck_deploy_container_image,
    blocks.bck_deploy_server,
    blocks.bck_deploy_configuration,
    blocks.bck_deploy_logs,
    blocks.bck_deploy_rollback,
    # 09:35 — CCSET16 How GSE-One solves it + course set-up (10 min)
    blocks.bck_gse_solution_deployment,
    blocks.bck_deploy_course_mode,  # PLACEHOLDER until the deployment server is chosen
    # 09:45 — Mini-project sprint (E20): the plan, then the requirements on two models (E21) (60 min)
    blocks.bck_project_lightweight_loop,
    blocks.bck_gensem_sheet_sprint_steps,
    blocks.bck_gensem_sheet_sprint_check,
    blocks.bck_gensem_sheet_model_comparison_steps,
    blocks.bck_project_model_grid,
    blocks.bck_gensem_sheet_model_comparison_check,
    # 10:45 — Break (15 min)
    # 11:00 — Sprint (E20); deployment waves 1 (11:00) and 2 (11:40) (E19)
    blocks.bck_gensem_sheet_deploy_calcapp_steps,  # PLACEHOLDER steps
    blocks.bck_gensem_sheet_deploy_calcapp_check,
    # 12:15 — Lunch
]
