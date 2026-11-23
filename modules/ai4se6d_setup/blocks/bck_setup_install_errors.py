"""Slide — Common installation errors and their fix."""
# @guideline: maximize-viewport
# @pattern: ptn_comparison_table
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Installation errors table styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    cell_text = s.project.titles.table_cell
    symptom = s.project.titles.table_label
bs = BlockStyles

# Outer 5 % margins; header row, then alternating rows — motif L2 + fonds f1 (NG, 2026-11-23)
_COLS = "5% 40% 50% 5%"
_HEADERS = ("You see…", "Do this")
_ERRORS = [
    ("“command not found”", "Open a new terminal (PATH not reloaded)"),
    ("Downloads hang (SSL, timeout)", "Proxy: try another network, or hand up"),
    ("“401”, “invalid API key”", "Wrong key or provider: redo step 3"),
    ("git asks for a password", "Not logged in: redo step 6"),
    ("GSE-One before opencode 2", "Install opencode 2, then redo step 5"),
    ("node missing, or older than v20", "Redo step 2, then open a new terminal"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Go through the six symptoms and their fixes; learners come back "
     "to this slide whenever a step fails."),
    ("The message",
     "Six common symptoms, each with its fix: read the left column, do the right one."),
    ("The most frequent",
     "« command not found » right after an install: the open terminal has the old PATH. Open a new terminal."),
    ("Network",
     "Downloads that hang (SSL, timeout) usually come from a proxy: try another network, or raise your hand."),
    ("Redo a step",
     "A wrong key (« 401 ») → step 3; git asking for a password → step 6; GSE-One installed before opencode 2 → "
     "step 5 again; node missing or older than v20 → step 2."),
    ("Ask the room",
     "« Which error did you meet that is not on this list? » — tell the trainer."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Common Errors", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Common Errors", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(95):
            header = [s.none, s.project.containers.table_header_cell, s.project.containers.table_header_cell, s.none]
            with st_grid(cols=_COLS, gap="0.5vw", cell_styles=header) as g:
                with g.cell():
                    pass  # left margin
                for title in _HEADERS:
                    with g.cell():
                        st_write(bs.header_text, title)
                with g.cell():
                    pass  # right margin
            st_space("v", "3vh")
            cells = s.project.containers.rows(len(_ERRORS), _COLS, filled=(2, 3))
            with st_grid(cols=_COLS, gap="4.5vh 0.5vw", cell_styles=cells) as g:
                for symptom, fix in _ERRORS:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.symptom, symptom, tag=t.div)
                    with g.cell():
                        st_write(bs.cell_text, fix, tag=t.div)
                    with g.cell():
                        pass  # right margin
