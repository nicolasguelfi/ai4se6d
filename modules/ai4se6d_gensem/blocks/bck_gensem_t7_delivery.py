"""T7 — DELIVER, COMPOUND (3 axes), INTEGRATE, Health Dashboard."""
# @guideline: minimalist-visual + maximize-viewport
# @reuse: bck_gensem_ce_compound, _compound_flywheel (v01)
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_pfc = s.project.containers.page_fill_center
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t7_body")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t7_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t7_hl")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t7_kw")
bs = BlockStyles


def build():
    st_slide_break(marker_label="Deliver, Compound, Integrate")

    # ── Slide: DELIVER ──────────────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:deliver — Ship It", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="DELIVER — Merge, Tag, Deploy, Clean",
                        entries=[
                            ("Merge strategy", "Adapted to your level: beginners see 'Clean summary' vs 'Full history'. Advanced see squash/merge/rebase."),
                            ("Safety", "Backup tag created before every merge. Semantic version tag on main. Release notes auto-generated."),
                            ("Cleanup", "Merged branches and worktrees are automatically cleaned up. Stale backup tags purged."),
                            ("Optional deploy", "Post-tag hook triggers automatic deployment. /gse:deploy handles Hetzner/Coolify: provisioning, hardening, DNS/SSL, app deployment in one flow."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "Merge → Tag → Deploy → Clean. Main stays stable.")
                st_space("v", 1)
                with st_grid(cols="repeat(auto-fit, minmax(200px, 1fr))", gap="12px", cell_styles=_cell) as g:
                    with g.cell():
                        st_write(bs.body, "\U0001f500 Merge")
                    with g.cell():
                        st_write(bs.body, "\U0001f3f7\ufe0f Tag")
                    with g.cell():
                        st_write(bs.body, "\U0001f680 Deploy")
                    with g.cell():
                        st_write(bs.body, "\U0001f9f9 Clean")

    st_slide_break(marker_label="/gse:compound — Knowledge Flywheel")

    # ── Slide: COMPOUND — the distinctive phase ────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:compound — Knowledge Flywheel", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="COMPOUND — The Discipline\u2019s Distinctive Phase",
                        entries=[
                            ("The problem", "Without capitalization, each sprint starts from zero. Learnings are lost between sessions."),
                            ("3 axes", "Axe 1 (Project): patterns, errors, best practices \u2192 compound.md. Axe 2 (Method): feedback on GSE-One. Axe 3 (Skills): learning notes + competency map."),
                            ("Flywheel effect", "Sprint 1 \u2192 10 rules. Sprint 3 \u2192 25 rules. Sprint 5 \u2192 50+ rules. First-attempt success rises from baseline to 80%+."),
                            ("Discipline principle", "Knowledge capitalization is what distinguishes Generative SE from VibeEngineering. GSE-One\u2019s COMPOUND is one implementation \u2014 this principle transfers to any GenSE methodology."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.highlight, "The phase no one does — that changes everything.")
                st_space("v", 1)
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.keyword + s.center_txt, "Axe 1: Project")
                            st_write(bs.body, "Patterns, errors, best practices")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.keyword + s.center_txt, "Axe 2: Method")
                            st_write(bs.body, "Feedback on GSE-One itself")
                    with g.cell():
                        with st_block(_cell_act):
                            st_write(bs.keyword + s.center_txt, "Axe 3: Skills")
                            st_write(bs.body, "Learning notes + competency map")

    st_slide_break(marker_label="/gse:integrate + /gse:health")

    # ── Slide: INTEGRATE + Health ───────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "/gse:integrate + /gse:health", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="INTEGRATE Routes Solutions, HEALTH Monitors Progress",
                        entries=[
                            ("INTEGRATE", "Routes capitalized solutions to operational destinations: Axe 1 → project config, Axe 2 → GitHub issue, Axe 3 → learning notes."),
                            ("HEALTH", "8-dimension dashboard: Requirements Coverage, Test Pass Rate, Design Debt, Review Findings, Complexity Budget, Traceability, Git Hygiene, AI Integrity."),
                            ("Trend tracking", "Health score is tracked across sprints — you can see if quality improves or degrades over time."),
                            ("Actionable alerts", "'Requirements coverage below 60%' → the agent suggests what to fix."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.accent, "Solutions become operational. Health monitors progress.")
                st_space("v", 1)
                with st_grid(cols="repeat(auto-fit, minmax(200px, 1fr))", gap="12px", cell_styles=_cell) as g:
                    for dim in ["REQ Coverage", "Test Pass", "Design Debt", "Findings",
                                "Budget", "Traceability", "Git Hygiene", "AI Integrity"]:
                        with g.cell():
                            st_write(bs.body, dim)
