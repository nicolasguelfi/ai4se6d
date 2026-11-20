"""Slide — CCSET16: how GSE-One deploys (concept only, edition 2).

Facts from gensem src/activities/deploy.md: Dockerfile and .dockerignore generated only when absent
(Phase 6 Step 3, template by project type, shown for approval); phases tracked in .gse/deploy.json
(phases_completed, skipped on re-run); live-version check after deploy (healthy != correct version).
"""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET16 · Deployment",
        label="GSE-One solution — deployment",
        problem="Going live takes many steps a beginner does not know, and a half-done deployment is hard to resume.",
        solution=[
            ((CMD, "/gse-deploy"), " guides the whole path in one flow, from the server to the live address."),
            "It writes a Dockerfile only if your project has none, picked by project type and shown to you first: "
            "CalcApp's own Dockerfile is kept.",
            ("Its state is a file, ", (CMD, ".gse/deploy.json"), ": the steps already done are skipped on a re-run, "
             "so an interrupted deployment resumes."),
            "After deploying, it checks that the app answers — and that the live version is the one you pushed.",
        ],
        foot="Concept only — the course set-up for exercise E19 comes next.",
    )
