"""Slide — /gse:hug: establish the user engineering profile."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t2ch_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t2ch_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t2ch_acc")
bs = BlockStyles

_DIMENSIONS = [
    ("\U0001f4bb", "IT Expertise"),
    ("\U0001f52c", "Scientific Expertise"),
    ("\U0001f9e9", "Abstraction Capability"),
    ("\U0001f310", "Language (chat + artifacts)"),
    ("\U0001f4cf", "Preferred Verbosity"),
    ("\U0001f3af", "Domain Background"),
    ("\U0001f91d", "Decision Involvement"),
    ("\U0001f4e6", "Project Domain"),
    ("\U0001f465", "Team Context"),
    ("\U0001f4d6", "Learning Goals"),
    ("\U0001f4a1", "Contextual Tips"),
    ("\U0001f600", "Emoji Preference"),
    ("\U0001f464", "User Name"),
]


def build():
    st_marker("/gse:hug")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:hug \u2014 Know Your Developer", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:hug \u2014 User Profile (13 Dimensions)",
                entries=[
                    ("Purpose", "Establish or update the full engineering context profile. This profile calibrates EVERYTHING: decision tiers (P7), communication depth (P9), guardrail thresholds (P11), learning proposals (P14)."),
                    ("Smart interview", "The agent infers as many dimensions as possible from context (language from first message, domain from package manifest, expertise from vocabulary). Only 4\u20135 explicit questions needed."),
                    ("Git init", "Also verifies the project is a git repository (initializes with foundational commit if needed) and creates the .gse/ directory."),
                    ("Updatable", "Run /gse:hug anytime to update your profile. Preferences evolve as you learn \u2014 expertise domains are also updated silently by observation (P14)."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(80):
            _left = _DIMENSIONS[:7]
            _right = _DIMENSIONS[7:]
            with st_grid(cols="1fr 1fr", gap="16px") as g:
                with g.cell():
                    with st_grid(cols="1fr", gap="10px", cell_styles=_cell) as inner:
                        for icon, label in _left:
                            with inner.cell():
                                st_write(bs.body, f"{icon} ", (bs.keyword, label))
                with g.cell():
                    with st_grid(cols="1fr", gap="10px", cell_styles=_cell_acc) as inner:
                        for icon, label in _right:
                            with inner.cell():
                                st_write(bs.body, f"{icon} ", (bs.keyword, label))

            st_space("v", 1)
            st_write(bs.accent, "4\u20135 questions only \u2014 the agent infers the rest from context.")
