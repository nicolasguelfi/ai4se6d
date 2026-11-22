"""Slide 10 — What GenAI Can Do: five capabilities with accent keywords."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s


# Override: non-standard justify-content:top
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:top;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_capabilities",
)


class BlockStyles:
    """Slide: Capabilities — maximize-viewport archetype: bullet list with accent keywords."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent


bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "What GenAI Can Do", tag=t.div, toc_lvl="1")
            st_space("v", "6vh")

            # One grid row per item, alternating fills — motif « lignes-alternées » (L2 + fonds f1) of
            # streamtex-all-trainings (NG, 2026-11-22). Columns 1 and 3 are margins; only column 2 is filled.
            items = [
                ("Generate code", " — from natural language descriptions"),
                ("Write & summarize", " — documents, emails, reports"),
                ("Analyze data", " — patterns, trends, anomalies"),
                ("Create images", " — from text prompts (image models)"),
                ("Reason & plan", " — multi-step problem solving"),
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
