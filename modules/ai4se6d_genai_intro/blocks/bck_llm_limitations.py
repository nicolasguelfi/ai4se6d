"""Slide 11 — What GenAI Cannot Do: five limitations with amber keywords."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


_page_fill = s.project.containers.page_fill_top


class BlockStyles:
    """Slide: Limitations — maximize-viewport archetype: bullet list with warning keywords."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.highlight


bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "What GenAI Cannot Do", tag=t.div, toc_lvl="1")

            st_space("v", "6vh")

            # One grid row per item, alternating fills — motif « lignes-alternées » (L2 + fonds f1) of
            # streamtex-all-trainings (NG, 2026-11-22). Columns 1 and 3 are margins; only column 2 is filled.
            items = [
                ("Guarantee truth", " — hallucinations are real"),
                ("Replace judgment", " — no domain expertise"),
                ("Access real-time data", " — training cutoff date"),
                ("Understand deeply", " — pattern matching, not comprehension"),
                ("Be deterministic", " — same prompt, different outputs"),
            ]
            cols = "5% 90% 5%"
            cells = s.project.containers.rows(len(items), cols, filled=(2,))
            with st_zoom(115), st_grid(cols=cols, gap="3.5vh 1vw", cell_styles=cells) as g:   # one row per line, fits one screen
                for key, text in items:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body, (bs.keyword, key), text, tag=t.div)
                    with g.cell():
                        pass  # right margin
