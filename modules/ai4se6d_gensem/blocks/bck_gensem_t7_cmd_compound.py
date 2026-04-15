"""Slide — /gse:compound: capitalize learnings across 3 axes."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t7ccm_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t7ccm_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t7ccm_acc")
bs = BlockStyles


def build():
    st_marker("/gse:compound")
    with st_block(_pf):
        with st_block(s.center_txt):
            st_write(bs.heading, "/gse:compound \u2014 What Did We Learn?", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:compound \u2014 3-Axis Capitalization",
                entries=[
                    ("Axe 1 \u2014 Project", "Patterns, errors, best practices observed during the sprint \u2192 compound.md. What worked, what didn\u2019t, what to repeat."),
                    ("Axe 2 \u2014 Methodology", "What worked/didn\u2019t in GSE-One itself \u2192 propose issue on GSE-One repo. Filtered: only actionable feedback observed in 2+ sprints or confirmed by user."),
                    ("Axe 3 \u2014 Competencies", "Feed P14 learning notes. Aggregate contextual tips into topic-based notes. Update the competency map."),
                    ("Deeper than retro", "Goes beyond a standard agile retrospective \u2014 includes knowledge transfer and methodology feedback."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="1fr 1fr 1fr", gap="16px") as g:
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.keyword + s.center_txt, "Axe 1 \u2014 Project")
                        st_space("v", 0.5)
                        st_write(bs.body, "Patterns & best practices")
                        st_write(bs.body, "Errors to avoid")
                        st_write(bs.body, "\u2192 compound.md")
                with g.cell():
                    with st_block(_cell):
                        st_write(bs.keyword + s.center_txt, "Axe 2 \u2014 Methodology")
                        st_space("v", 0.5)
                        st_write(bs.body, "GSE-One feedback")
                        st_write(bs.body, "Filtered: 2+ sprints")
                        st_write(bs.body, "\u2192 issue on repo")
                with g.cell():
                    with st_block(_cell_act):
                        st_write(bs.keyword + s.center_txt, "Axe 3 \u2014 Competencies")
                        st_space("v", 0.5)
                        st_write(bs.body, "Learning notes (P14)")
                        st_write(bs.body, "Competency map update")
                        st_write(bs.body, "\u2192 docs/learning/")

            st_space("v", 1)
            st_write(bs.accent, "Deeper than a retrospective \u2014 knowledge transfer + methodology feedback.")
