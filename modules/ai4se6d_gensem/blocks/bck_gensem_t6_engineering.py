"""T6 — LC02b: PRODUCE (worktree), TESTS (pyramid, 3 coverages), REVIEW (5 agents), FIX."""
# @guideline: minimalist-visual + maximize-viewport
# @reuse: bck_gensem_ce_review_nversion, _work_review, _brainstorm_antipattern (v01)
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_pfc = s.project.containers.page_fill_center
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t6_body")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t6_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t6_hl")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t6_kw")
    critical = Style.create(s.Large + s.bold + s.project.colors.critical + s.center_txt, "t6_crit")
bs = BlockStyles


def build():
    st_slide_break(marker_label="LC02b: Produce, Test, Review")

    # ── Slide: PRODUCE ──────────────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:produce — Code Within the Plan", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="PRODUCE — Constrained by the Plan",
                        entries=[
                            ("How it works", "The agent creates a feature branch + worktree, then generates code strictly following the approved plan."),
                            ("Constraint", "Any deviation from the plan requires an explicit plan revision. No 'while we're at it' additions."),
                            ("Budget visible", "The complexity budget gauge updates in real-time. Warning at 80%, Gate at 100%."),
                            ("Output", "Committed code with conventional messages: gse(sprint-01/feat/budget): description."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "The agent codes WITHIN the plan. Deviation = plan revision.")
                st_space("v", 1)
                st_write(bs.body, "No scope creep. No 'while we're at it'. Budget-constrained.")

    st_slide_break(marker_label="/gse:tests — Test Pyramid & Coverage")

    # ── Slide: TESTS — pyramid + 3 coverages ───────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:tests — Test Pyramid & Coverage", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Testing in GSE-One",
                        entries=[
                            ("Test pyramid", "Calibrated by domain: web frontend = 20% unit, 20% integration, 40% E2E, 20% acceptance."),
                            ("3 coverage dimensions", "Code coverage (% lines), Requirements coverage (% REQ with tests), Risk coverage (% high-risk modules tested)."),
                            ("Requirements > Code", "Having 80% code coverage but 0% requirements coverage is useless. REQ coverage tells you if you're testing what matters."),
                            ("CalcApp", "Vitest auto-detected. Pyramid calibrated for web frontend. TST- IDs trace back to REQ-."),
                            ("Visual testing", "For web/mobile projects, GSE-One captures screenshots after each production and uses multimodal AI analysis to detect visual regressions, layout issues, and accessibility problems."),
                            ("Discipline principle", "Multi-perspective review is a disciplinary requirement of Generative SE \u2014 AgileGen uses a memory pool, V-Bounce has a QA agent, GSE-One uses /gse:review with 5 agents."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.keyword + s.center_txt, "Code Coverage")
                            st_write(bs.body, "% lines tested")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.highlight + s.center_txt, "REQ Coverage")
                            st_write(bs.body, "% requirements with tests")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.critical + s.center_txt, "Risk Coverage")
                            st_write(bs.body, "% high-risk modules tested")

    st_slide_break(marker_label="Test Pyramid by Domain")

    # ── Slide: Test Pyramid by Domain ───────────────────────────────
    _hdr_cell = s.project.containers.table_header_cell
    _norm_cell = s.project.containers.table_normal_cell
    _act_cell = s.project.containers.table_active_cell

    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Test Pyramid by Domain", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Why Different Pyramids?",
                        entries=[
                            ("Web frontend", "E2E and acceptance tests dominate because UI behavior is the primary quality concern."),
                            ("API backend", "Unit tests dominate because business logic is the primary concern; E2E is minimal."),
                            ("CLI tool", "Unit tests dominate because input/output parsing is the core logic."),
                            ("CalcApp = Web", "As a web frontend app, CalcApp uses the 20/20/40/20 pyramid — more E2E than unit tests."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

            _table_hdr = s.project.titles.table_header
            _table_txt = s.project.titles.table_cell
            _table_lbl = s.project.titles.table_label
            _table_lbl_act = s.project.titles.table_label_active

            with st_grid(cols="repeat(auto-fit, minmax(120px, 1fr))", gap="6px", cell_styles=_hdr_cell) as g:
                for h in ["Domain", "Unit", "Integration", "E2E", "Acceptance"]:
                    with g.cell():
                        st_write(_table_hdr + s.center_txt, h)

            _pyramids = [
                ("Web Frontend", "20%", "20%", "40%", "20%", True),
                ("API Backend", "50%", "30%", "5%", "15%", False),
                ("CLI Tool", "60%", "20%", "10%", "10%", False),
                ("Mobile", "25%", "20%", "35%", "20%", False),
                ("Scientific", "40%", "20%", "0%", "40%", False),
                ("Library", "70%", "20%", "0%", "10%", False),
            ]
            for domain, unit, integ, e2e, accept, active in _pyramids:
                cell_s = _act_cell if active else _norm_cell
                lbl_s = _table_lbl_act if active else _table_lbl
                with st_grid(cols="repeat(auto-fit, minmax(120px, 1fr))", gap="6px", cell_styles=cell_s) as g:
                    with g.cell():
                        st_write(lbl_s + s.center_txt, domain)
                    for v in (unit, integ, e2e, accept):
                        with g.cell():
                            st_write(_table_txt + s.center_txt, v)

    st_slide_break(marker_label="/gse:review — 5 Perspectives")

    # ── Slide: REVIEW — 5 agents ────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:review — 5 Perspectives", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Multi-Agent Review (N-Version Verification)",
                        entries=[
                            ("Analogy", "Like having 3 expert reviewers on every PR — but it takes 2 minutes, not 2 days."),
                            ("5 perspectives", "Correctness (code-reviewer), Security (auditor), Architecture (architect), UX (advocate), Self-critique (devil-advocate P16)."),
                            ("Findings", "Each finding gets an RVW- ID, severity (HIGH/MEDIUM/LOW), and a proposed fix. HIGH findings block delivery."),
                            ("Health update", "The health score updates after review. Findings impact the Design Debt dimension."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "5 agents review your code simultaneously. 2 minutes.")
                st_space("v", 1)
                with st_grid(cols="repeat(auto-fit, minmax(200px, 1fr))", gap="12px", cell_styles=_cell) as g:
                    with g.cell():
                        st_write(bs.body, "\U0001f4dd Correctness")
                    with g.cell():
                        st_write(bs.body, "\U0001f6e1\ufe0f Security")
                    with g.cell():
                        st_write(bs.body, "\U0001f3d7\ufe0f Architecture")
                    with g.cell():
                        st_write(bs.body, "\U0001f464 UX")
                    with g.cell():
                        st_write(bs.body, "\U0001f608 Devil's Advocate")

    st_slide_break(marker_label="/gse:fix — Iterate Until Quality")

    # ── Slide: FIX → iterate ────────────────────────────────────────
    with st_block(_pfc):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:fix — Iterate Until Quality", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="FIX — The Quality Loop",
                        entries=[
                            ("How it works", "Creates a fix branch targeting specific RVW- findings. Each fix commit references the finding ID."),
                            ("Iteration", "REVIEW → FIX can loop until quality is acceptable: 0 HIGH findings + health score above threshold."),
                            ("Discipline", "The fix ONLY addresses the finding. No extra changes. Scope stays constrained."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "REVIEW → FIX → REVIEW → FIX → ... until quality.")
                st_space("v", 1)
                st_write(bs.body, "0 HIGH findings + acceptable health score = ready to deliver.")
