"""Slide — How We Work This Week: practice first, your tutor window, GitHub feedback, daily buffer, hands-up quiz.

Edition 2 (board peda1: P5 tutor agent, P7 feedback issues, P8 hands-up quiz, P14 standard exercise sheet).
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from streamtex.styles import StyleGrid as sg
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


_page_fill = s.project.containers.page_fill_top

_row_label = Style.create(
    s.project.containers.cell_accent_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout,
    "hww_row_label",
)
_row_text = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout,
    "hww_row_text",
)


class BlockStyles:
    """Slide: How we work — two-column rule sheet."""
    heading = s.project.titles.section_title + s.center_txt
    label = Style.create(
        s.project.colors.accent + s.bold + s.text.sizes.pt28,
        "hww_label",
    )
    text = Style.create(s.text.sizes.pt24, "hww_text")
    key = Style.create(s.text.sizes.pt24 + s.bold + s.project.colors.highlight, "hww_key")
    code = Style.create(
        s.text.sizes.pt24 + s.text.fonts.font_monospace + s.project.colors.primary,
        "hww_code",
    )


bs = BlockStyles

_ROWS = sg.create("A1:A5", _row_label) + sg.create("B1:B5", _row_text)

_NOTES = [
    ("Tutor window", "Show it once live during installation (afternoon): a second terminal running "
                     "~/ai4se/ai4se-kit/tutor. Insist: it is an AI, it can be wrong, it cites its sources, "
                     "and it tells them when to call you."),
    ("Issues", "Typos, unclear slides, GSE-One bugs: one issue each, label ai4se-ed2. Fixed during the course."),
]


def build():
    with st_block(_page_fill):
        with st_grid(cols="92% 8%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell():
                st_write(bs.heading, "How We Work This Week", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — how we work", entries=_NOTES, position="left", width="45vw")

        with st_grid(cols="22% 78%", gap="10px", cell_styles=_ROWS) as g:
            with g.cell():
                st_write(bs.label, "Practice first")
            with g.cell():
                st_write(bs.text, "Short demo (≤ 10 min), then you do it. Every exercise says when you are ",
                         (bs.key, "done"), " — something you can see, e.g. ",
                         (bs.code, "npm run test:run"), " shows 3 passing tests.")
            with g.cell():
                st_write(bs.label, "Lost? Your tutor window")
            with g.cell():
                st_write(bs.text, "A second terminal running ", (bs.code, "~/ai4se/ai4se-kit/tutor"), ": an ",
                         (bs.key, "AI assistant"), ", not the trainer. It reads the course and your folders, "
                         "never changes them, cites its sources and tells you when to call me. "
                         "Then the recovery tag, then raise your hand.")
            with g.cell():
                st_write(bs.label, "Feedback any time")
            with g.cell():
                st_write(bs.text, "Open a GitHub issue on ", (bs.code, "nicolasguelfi/gensem"),
                         " with the label ", (bs.code, "ai4se-ed2"), ". It is ",
                         (bs.key, "public"), ": nothing confidential — no key, no client code.")
            with g.cell():
                st_write(bs.label, "Daily buffer")
            with g.cell():
                st_write(bs.text, "The last slot of each day is kept free: catch up, ask, finish the exercise.")
            with g.cell():
                st_write(bs.label, "Hands-up quiz")
            with g.cell():
                st_write(bs.text, "A few questions at the end of each day. No grades — it tells us what to revisit.")
