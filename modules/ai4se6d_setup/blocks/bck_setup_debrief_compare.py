"""Slide — Debrief: what I would have done by hand / what the AI did (one example each)."""
# @guideline: maximize-viewport
# @pattern: ptn_comparison_table
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Debrief comparison styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    example = Style.create(s.project.titles.table_cell + s.italic + s.project.colors.muted, "setup_debrief_example")
    empty = Style.create(s.project.titles.table_cell + s.project.colors.muted, "setup_debrief_empty")
    body = Style.create(s.project.titles.body + s.center_txt, "setup_debrief_body")
    keyword = s.bold + s.project.colors.highlight
bs = BlockStyles

_COLS = "5% 44.5% 44.5% 5%"  # a two-column table between outer 5 % margins
_CELL_H = Style("min-height:15vh;", "setup_debrief_cell_h")

_NOTES = [
    ("The message",
     "Debrief round: each participant gives ONE example, 30 seconds — what they would have done by hand, and "
     "what the AI did instead."),
    ("The example on the slide",
     "« Search how to save data in the browser » by hand vs. « used localStorage — I never checked how »: the "
     "app works, but a decision was taken without the participant."),
    ("What to listen for",
     "Decisions the participants did not see (storage, libraries, structure) and things they could not explain. "
     "Write a few on the board."),
    ("Link to the rest",
     "Next slide: three questions (surprise, breakage, would you give it to a client?), then the link to this "
     "morning's cycles."),
    ("Keep it moving",
     "30 seconds each: start with volunteers, then go round the room."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "By Hand vs. AI", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — By Hand vs. AI", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        hdr = [s.none, s.project.containers.table_header_cell, s.project.containers.table_header_cell, s.none]
        body = [s.none, s.project.containers.table_normal_cell + _CELL_H,
                s.project.containers.table_normal_cell + _CELL_H, s.none]
        with st_zoom(140):
            with st_grid(cols=_COLS, gap="12px", cell_styles=hdr) as g:
                with g.cell():
                    pass
                with g.cell():
                    st_write(bs.header_text, "What I would have done by hand")
                with g.cell():
                    st_write(bs.header_text, "What the AI did")
                with g.cell():
                    pass
            with st_grid(cols=_COLS, gap="12px", cell_styles=body * 2) as g:
                for left, right, style in [("e.g. search how to save data in the browser",
                                            "e.g. used localStorage — I never checked how", bs.example),
                                           ("…", "…", bs.empty)]:
                    with g.cell():
                        pass
                    with g.cell():
                        st_write(style, left)
                    with g.cell():
                        st_write(style, right)
                    with g.cell():
                        pass
        st_space("v", "6vh")
        with st_zoom(110):
            st_write(bs.body, (bs.keyword, "Each of you: one example"), " — 30 seconds.", tag=t.div)
