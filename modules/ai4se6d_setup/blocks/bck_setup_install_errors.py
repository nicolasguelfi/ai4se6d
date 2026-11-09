"""Slide — Common installation errors and their fix."""
# @guideline: maximize-viewport
# @pattern: ptn_comparison_table
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Installation errors table styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    cell_text = s.project.titles.table_cell
    symptom = s.project.titles.table_label
bs = BlockStyles

_COLS = "42% 58%"
_HEADERS = ("You see…", "Do this")
_ERRORS = [
    ("“command not found”", "Open a new terminal (PATH not reloaded)"),
    ("Downloads hang (SSL, timeout)", "Proxy: try another network, or hand up"),
    ("“401”, “invalid API key”", "Wrong key or provider: redo step 2"),
    ("git asks for a password", "Not logged in: redo step 5"),
    ("GSE-One before opencode 2", "Install opencode 2, then redo step 4"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Common Errors", tag=t.div, toc_lvl="1")
            with st_zoom(90), st_grid(cols=_COLS, gap="8px", cell_styles=s.project.containers.table_header_cell) as g:
                for header in _HEADERS:
                    with g.cell():
                        st_write(bs.header_text, header)
            for symptom, fix in _ERRORS:
                with st_zoom(90), st_grid(cols=_COLS, gap="8px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell():
                        st_write(bs.symptom, symptom)
                    with g.cell():
                        st_write(bs.cell_text, fix)
