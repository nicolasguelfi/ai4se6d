"""Slide sequence — day 3 morning (09:00-12:30): cycles CCSET09 to CCSET12, theory + "How GSE-One solves it".

Timetable: docs/plans/2026-11-10-012-six-days-cycles-plan.html (validated by NG, 2026-11-10).
Edition-1 blocks no longer listed stay on disk (option A: disabled, not deleted).
"""
import blocks

BLOCKS_CONCEPTS = [
    # 09:00 — Welcome (15 min)
    blocks.bck_gensem_title,
    blocks.bck_gensem_today_concepts,
    blocks.bck_gensem_recall_by_hand,
    blocks.bck_gensem_push_calcapp,
    # 09:15 — CCSET09 Software engineering concepts, defining your GenSEM (theory 50 min)
    blocks.bck_gensem_concepts_section,
    blocks.bck_gensem_sdlc_gravity,
    blocks.bck_gensem_sdlc_orchestrator,
    blocks.bck_gensem_sdlc_phases,
    blocks.bck_gensem_sdlc_evidence,
    blocks.bck_gensem_evidence_rcts,
    blocks.bck_gensem_evidence_perception,
    blocks.bck_gensem_risks,
    blocks.bck_gensem_fw_landscape,
    blocks.bck_gensem_fw_synthesis,
    blocks.bck_gensem_sota_takeaway,
    blocks.bck_gensem_method_ingredients,
    # 10:05 — CCSET09 How GSE-One solves it (10 min, concept only)
    blocks.bck_gensem_sdlc_title,  # GSE-One promo video
    blocks.bck_gse_solution_method,
    blocks.bck_gensem_gate_grid,
    blocks.bck_gensem_orientation_page,
    # 10:15 — CCSET10 Requirements elicitation (theory 40 min + solution 5 min)
    blocks.bck_elicitation_title,
    blocks.bck_elicitation_cost,
    blocks.bck_elicitation_good_requirement,
    blocks.bck_elicitation_stakeholders,
    blocks.bck_elicitation_techniques,
    blocks.bck_elicitation_user_stories,
    blocks.bck_elicitation_acceptance,
    blocks.bck_elicitation_ambiguity,
    blocks.bck_elicitation_with_ai,
    blocks.bck_gensem_sdlc_re,
    blocks.bck_gse_solution_requirements,
    # 11:00 — Break (15 min)
    # 11:15 — CCSET11 Non-functional requirements (theory 40 min + solution 5 min)
    blocks.bck_nfr_title,
    blocks.bck_nfr_versus_functional,
    blocks.bck_nfr_quality_model,
    blocks.bck_nfr_measurable,
    blocks.bck_nfr_scenarios,
    blocks.bck_nfr_tradeoffs,
    blocks.bck_nfr_ai_blind_spots,
    blocks.bck_gse_solution_nfr,
    # 12:00 — CCSET12 Verification and validation (theory 25 min + solution 5 min)
    blocks.bck_vv_title,
    blocks.bck_vv_definitions,
    blocks.bck_vv_levels,
    blocks.bck_vv_pyramid,
    blocks.bck_vv_test_design,
    blocks.bck_vv_static_dynamic,
    blocks.bck_vv_oracle_ai,
    blocks.bck_gensem_sdlc_testing,
    blocks.bck_gse_solution_verification,
    # 12:30 — Lunch
]
