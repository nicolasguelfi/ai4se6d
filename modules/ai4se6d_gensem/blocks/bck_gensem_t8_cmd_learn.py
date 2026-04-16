"""Slide — /gse:learn: continuous learning with 3 modes."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt
_hdr_cell = s.project.containers.table_header_cell
_normal_cell = s.project.containers.table_normal_cell


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t8cl_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t8cl_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t8cl_acc")
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
bs = BlockStyles


def build():
    st_slide_break(marker_label="/gse:learn")

    # ── Slide 1: 3 Modes ──────────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:learn \u2014 The Agent Teaches You", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:learn \u2014 3 Learning Modes",
                entries=[
                    ("Contextual mode", "2\u20133 sentence tips during activities. Automatic, non-intrusive. Concepts not repeated if already explained (tracked in competency map)."),
                    ("Proactive mode", "At natural transitions (end of sprint, before complex activity), the agent proposes a session: 'You encountered 3 security decisions \u2014 want a 5-min overview?'"),
                    ("Reactive mode", "You ask: /gse:learn git branching. Quick (5 min) or Deep (15 min + exercise)."),
                    ("Learning notes", "Saved to docs/learning/ in your language. Include: key concepts, how it applies to your project, quick reference card."),
                    ("Competency map", "Tracked in .gse/profile.yaml: concepts explained, sessions completed, skill gaps, learning goals progress."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="1fr 1fr 1fr", gap="16px") as g:
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.keyword + s.center_txt, "Quick")
                        st_write(bs.body, "~5 min")
                        st_write(bs.body, "Key concepts + project application")
                with g.cell():
                    with st_block(_cell):
                        st_write(bs.keyword + s.center_txt, "Deep")
                        st_write(bs.body, "~15 min")
                        st_write(bs.body, "Concepts + examples + practice exercise")
                with g.cell():
                    with st_block(_cell_act):
                        st_write(bs.keyword + s.center_txt, "Roadmap")
                        st_write(bs.body, "~2 min")
                        st_write(bs.body, "Competency map: learned, gaps, next")

    st_slide_break(marker_label="/gse:learn Options")

    # ── Slide 2: Options & Competency Map ──────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:learn \u2014 Options & Competency Map", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:learn Options",
                entries=[
                    ("--roadmap", "Show your competency map: what you've learned, what gaps remain, what the agent recommends next."),
                    ("--notes", "List all learning notes by topic."),
                    ("--notes <topic>", "Show the note on a specific topic (e.g., /gse:learn --notes git)."),
                    ("--notes --recent", "Show notes from the current sprint only."),
                    ("Proactive limits", "Max 1 proposal per activity phase. 'Not now' honored without pressure. 'Not interested' suppresses the topic permanently."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="40% 60%", gap="8px", cell_styles=_hdr_cell) as g:
                with g.cell():
                    st_write(bs.table_hdr, "Option")
                with g.cell():
                    st_write(bs.table_hdr, "Description")

            for opt, desc in [
                ("/gse:learn <topic>", "Quick learning session on a topic"),
                ("/gse:learn --roadmap", "Show competency map & recommendations"),
                ("/gse:learn --notes", "List all learning notes by topic"),
                ("/gse:learn --notes <topic>", "Show a specific learning note"),
                ("/gse:learn --notes --recent", "Notes from current sprint only"),
            ]:
                with st_grid(cols="40% 60%", gap="8px", cell_styles=_normal_cell) as g:
                    with g.cell():
                        st_write(bs.table_lbl, opt)
                    with g.cell():
                        st_write(bs.table_txt, desc)

            st_space("v", 1)
            st_write(bs.accent, "LRN- artifacts accumulate \u2014 your personal course, in your language.")
