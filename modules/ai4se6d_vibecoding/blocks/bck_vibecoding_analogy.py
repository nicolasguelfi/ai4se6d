"""Slide — Historical analogy: LLM as the new compiler?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """VibeCoding analogy slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_warn = s.bold + s.project.colors.highlight
    emphasis = Style.create(
        s.Large + s.italic + s.project.colors.accent + s.center_txt,
        "vc_analogy_emphasis",
    )
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A vintage punch-card machine morphing into a modern AI brain. Left side "
    "shows rigid geometric assembly patterns in muted blue. Right side shows fluid neural "
    "pathways in teal and amber. A timeline arrow runs beneath from 1960s to 2020s. "
    f"Symbolizes the evolution from assembly to AI-generated code. {_SUFFIX}"
)

def build():
    # Sub-slide 1: Historical parallel
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "LLM = The New Compiler?", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="vc_analogy",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with st_zoom(130),g.cell():
                    st_write(
                        bs.body,
                        (s.project.colors.highlight + s.LARGE + s.bold, "1960s: "),
                        (bs.body, "High-level languages replaced assembly."),
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (s.project.colors.muted,
                         "The compiler became the trusted intermediary \u2014 "
                         "programmers stopped writing machine code."),
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (s.project.colors.highlight + s.LARGE + s.bold, "2025: "),
                        (bs.body, "LLMs generate code from natural language. "
                         "Are we seeing the same shift?"),
                    )

    st_slide_break()

    # Sub-slide 2: Critical difference
    with st_zoom(130),st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.subheading, "The Critical Difference", tag=t.div, toc_lvl="2")
            st_space("v", 1)
            st_write(
                bs.body,
                (bs.keyword, "Compilers are deterministic "),
                (bs.body, "\u2014 same input always produces the same output."),
            )
            st_space("v", 1)
            st_write(
                bs.body,
                (bs.keyword_warn, "LLMs are stochastic "),
                (bs.body, "\u2014 same prompt can produce different (and sometimes wrong) code."),
            )
            st_space("v", 2)
            st_write(
                bs.emphasis,
                "You can trust a compiler blindly. Can you trust an LLM?",
            )
