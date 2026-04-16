"""Slide — /gse:reqs: define product functions and qualities."""
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t5cr_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t5cr_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t5cr_acc")
bs = BlockStyles


def build():
    st_marker("/gse:reqs")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:reqs \u2014 What Should It Do?", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:reqs \u2014 Requirements Engineering",
                entries=[
                    ("Step 0 \u2014 Elicitation", "Conversational capture of user intent in natural language. The agent identifies functional needs AND implicit quality expectations."),
                    ("FR \u2014 Functional", "User stories with testable acceptance criteria (Given/When/Then). Each FR gets a REQ- ID."),
                    ("NFR \u2014 Non-Functional", "Quality requirements (performance, security, usability, accessibility). Measurable targets."),
                    ("Quality checklist", "ISO 25010-inspired verification: 7 quality dimensions, 2\u20133 checklist items each. Gaps classified by priority."),
                    ("Output", "reqs.md with quality coverage matrix. Every REQ traces to TASK items."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            _steps = [
                ("\U0001f4ac", "Elicitation", "Conversational intent capture"),
                ("\u2699\ufe0f", "FR Definition", "User stories + Given/When/Then"),
                ("\U0001f4cf", "NFR Definition", "Quality targets + metrics"),
                ("\u2705", "Quality Check", "ISO 25010 coverage matrix"),
            ]
            with st_grid(cols="1fr 1fr 1fr 1fr", gap="12px") as g:
                for i, (icon, step, desc) in enumerate(_steps):
                    cell_style = _cell_acc if i % 2 == 0 else _cell
                    with g.cell():
                        with st_block(cell_style):
                            st_write(bs.body, f"{icon} ", (bs.keyword, step))
                            st_write(bs.body, desc)

            st_space("v", 1)
            st_write(bs.accent, "Every requirement is testable \u2014 acceptance criteria = validation test specs.")
