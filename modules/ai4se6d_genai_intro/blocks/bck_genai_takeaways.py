"""Slide 13 — Key Takeaways: four summary points + transition phrase."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


_page_fill = s.project.containers.page_fill_top


class BlockStyles:
    """Slide: Takeaways — maximize-viewport archetype: bullet list + transition."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.project.titles.body + s.bold + s.project.colors.primary
    transition = s.project.titles.body_accent + s.center_txt


bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Key Takeaways", tag=t.div, toc_lvl="1")

            st_space("v", "6vh")

            # One grid row per takeaway, alternating fills — motif « lignes-alternées » (L2 + fonds f1) of
            # streamtex-all-trainings, four columns (NG, 2026-11-22): margins 5 %, keyword 40 %, explanation 50 %.
            items = [
                ("GenAI creates", "it generates, not just classifies"),
                ("LLMs are probabilistic", "next-token prediction at scale"),
                ("Powerful but limited", "complement, don't replace expertise"),
                ("Use responsibly", "bias, privacy, transparency matter"),
            ]
            cols = "5% 40% 50% 5%"
            cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
            with st_zoom(90):   # the four rows and the "Next" line fit one screen
                with st_grid(cols=cols, gap="5vh 0.5vw", cell_styles=cells) as g:
                    for key, text in items:
                        with g.cell():
                            pass  # left margin
                        with g.cell():
                            st_write(bs.keyword, key, tag=t.div)
                        with g.cell():
                            st_write(bs.body, text, tag=t.div)
                        with g.cell():
                            pass  # right margin

                st_space("v", "6vh")
                st_write(
                    bs.transition,
                    "Next: VibeCoding — from intent to code",
                    tag=t.div,
                )
