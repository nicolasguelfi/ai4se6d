"""Slide — Demo vs Production gap (balanced layout)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """Demo vs prod slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword_ok = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    emphasis = Style.create(
        s.Large + s.italic + s.project.colors.primary,
        "vc_danger_demo_prod_emphasis",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: recipes of the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"), "vc_danger_demo_prod_text_cell")

_PROMPT = (
    f"{_PREFIX} Split screen: left side shows a perfect, shiny application interface "
    "in electric blue (demo). Right side shows the same interface crumbling with error "
    "symbols and warning triangles in amber (production reality). A teal curtain "
    f"separates the two halves. Represents the gap between demo and production. {_SUFFIX}"
)

_NOTES = [
    ("The message",
     "A working demo proves that the happy path runs once, on your machine. Production must run for everyone, every day."),
    ("What production adds",
     "Security, scalability, maintainability, monitoring, error handling, edge cases, compliance: none of these is visible in a demo, and none is requested by a « make it work » prompt."),
    ("The idea",
     "The gap between « it works » and « it is production-ready » is exactly the engineering work: it does not disappear with AI, it moves to specification, tests and review."),
    ("The trap",
     "Judging generated code by « it runs » (Trust in Output, principle 2) stops at the demo."),
    ("Ask the room",
     "« Your FreeSelfApp from this afternoon: which item of the list would it fail first? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):
                    st_write(bs.heading, "Demo vs. Production", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — Demo vs. Production", entries=_NOTES,
                                     position="left", width="50vw")

            with st_grid(
                cols="1.5fr 3.5fr",
                gap="3vw",
                cell_styles=[s.project.containers.grid_cell_centered, _text_cell],
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="vc_danger_demo_prod",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(125):   # text cell fills the slide (NG, 2026-11-23)
                        with st_zoom(110):
                            st_write(
                                bs.body,
                                (bs.keyword_ok, "The demo works."),
                            )
                            st_space("v", 1)
                            st_write(
                                bs.body,
                                (bs.keyword_warn, "Production requires: "),
                                "security, scalability, maintainability, monitoring, "
                                "error handling, edge cases, compliance.",
                            )
                            st_space("v", 2)
                            st_write(
                                bs.emphasis,
                                "The gap between \u201Cit works\u201D and "
                                "\u201Cit\u2019s production-ready\u201D "
                                "is where engineering lives.",
                            )
