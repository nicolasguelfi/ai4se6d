"""T8 — Plugin architecture, cross-tool, learning system, specializations, frameworks, project prep."""
# @guideline: minimalist-visual + maximize-viewport
# @reuse: bck_gensem_plugin_architecture, _cursor, _sync, _ce_toolsupport, _specialization, _roadmap (v01)
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t8_body")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t8_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t8_hl")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t8_kw")
bs = BlockStyles


def build():
    st_slide_break(marker_label="GSE-One Advanced")

    # ── Slide: Cross-tool portability ───────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "GSE-One Everywhere", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Mono-Plugin Architecture",
                        entries=[
                            ("52 files", "46 shared (skills, agents, templates) + 3 Claude Code specific + 3 Cursor specific."),
                            ("Parity", "The orchestrator body is identical across Claude Code and Cursor — verified by the generator."),
                            ("Installation", "gse install --target cursor OR gse install --target claude-code. One command."),
                            ("Sync", "gse sync keeps rules consistent across tools when working on the same project."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px", cell_styles=_cell) as g:
                    with g.cell():
                        st_write(bs.body, (bs.keyword, "Claude Code "), (bs.body, "— agent + hooks"))
                    with g.cell():
                        st_write(bs.body, (bs.keyword, "Cursor "), (bs.body, "— .mdc rules + hooks"))
                    with g.cell():
                        st_write(bs.body, (bs.keyword, "Copilot "), (bs.body, "— compatible"))
                    with g.cell():
                        st_write(bs.body, (bs.keyword, "10+ tools "), (bs.body, "— Windsurf, Kiro, OpenCode..."))

    st_slide_break(marker_label="Learning & Specializations")

    # ── Slide: Learning system + specializations ────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Learning & Specializations", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Continuous Learning in GSE-One",
                        entries=[
                            ("Contextual mode", "2-3 sentence explanations during activities \u2014 the agent teaches as you work."),
                            ("Proactive mode", "End of sprint: 'You encountered 3 security decisions \u2014 want a 5-min overview?'"),
                            ("/gse:learn", "Quick (1 concept), Deep (session), Roadmap (learning plan). Accessible anytime."),
                            ("5 specializations", "Development, Research, Training, Audit, Consulting \u2014 each calibrates agents differently."),
                            ("Discipline principle", "You\u2019ve learned one methodology. The 15 universal concepts (C1-C15) and these principles transfer to any Generative SE tool or method."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                with st_grid(cols="repeat(auto-fit, minmax(200px, 1fr))", gap="12px", cell_styles=_cell_acc) as g:
                    with g.cell():
                        st_write(bs.body, "\U0001f4bb Development")
                    with g.cell():
                        st_write(bs.body, "\U0001f52c Research")
                    with g.cell():
                        st_write(bs.body, "\U0001f393 Training")
                    with g.cell():
                        st_write(bs.body, "\U0001f50d Audit")
                    with g.cell():
                        st_write(bs.body, "\U0001f4bc Consulting")

    st_slide_break(marker_label="Ready for Your Project")

    # ── Slide: Preparation for professional project ─────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Ready for Your Project", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Transition to Professional Project",
                        entries=[
                            ("What you mastered", "LC00 (HUG) → LC01 (COLLECT/ASSESS/PLAN) → LC02 (REQS→DELIVER) → LC03 (COMPOUND/INTEGRATE)."),
                            ("Tips", "Start Lightweight, budget 8-10pts for 3h, don't skip COMPOUND, use /gse:learn for unknown domains."),
                            ("/gse:go vs commands", "/gse:go for guided flow (GPS), individual commands for fine control (map). Choose based on your confidence."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                with st_grid(cols="repeat(auto-fit, minmax(280px, 1fr))", gap="16px") as g:
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.keyword + s.center_txt, "Start Lightweight")
                            st_write(bs.body, "Escalate to Full if needed")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.highlight + s.center_txt, "Don't Skip COMPOUND")
                            st_write(bs.body, "Each cycle makes the next better")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.keyword + s.center_txt, "Health = Copilot")
                            st_write(bs.body, "Monitor your 8 dimensions")

            st_space("v", 2)
            st_image(
                s.none, width="12%",
                uri="images/managed/GSE/images/logo-gse-geni-with-shield.webp",
            )
            st_write(bs.highlight, "You are ready.")
