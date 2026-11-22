"""Slide — P4: Iterative Refinement (skippable)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """P4 slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p4_number",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "ve_p_iteration_text_cell")

_NOTES = [
    ('The message',
     'Work in planned iterations, each with a defined scope, acceptance criteria and a review gate.'),
    ('The idea explained',
     'Not « generate everything at once »: each cycle delivers a validated increment, small enough to review, and the next cycle builds on something known to work.'),
    ('The analogy',
     'A tasting menu: each course refined before the next is plated.'),
    ('The trap',
     'One giant prompt for the whole application: too much code to review, and errors are found late.'),
    ('Link to the course',
     'The days of this training follow the same cycles; GSE-One plans them as sprints.'),
    ('Ask the room',
     '« What is the smallest increment of your project that you could validate today? »'),
]

_PROMPT = (
    f"{_PREFIX} A spiral staircase viewed from above, each step clearly defined in "
    "electric blue. Gate checkpoints between iterations glow in amber. "
    f"{_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):
                    st_write(bs.heading, "P4 — Iterative Refinement", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — P4 — Iterative Refinement", entries=_NOTES,
                                     position="left", width="50vw")

            with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                         cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ve_p4_iteration",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(70):   # the number smaller: more room for the text
                        st_write(bs.number, "4")
                    with st_zoom(105):
                        st_write(
                            bs.body,
                            (bs.keyword, "Planned iterations"),
                            " with defined scope, ",
                            (bs.keyword, "acceptance criteria"),
                            ", and review gates.",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            "Not ",
                            (s.project.colors.muted, '"generate everything at once"'),
                            " — each cycle delivers a ",
                            (bs.keyword, "validated increment"),
                            ".",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            (s.project.colors.muted, "A tasting menu — each course refined "
                            "before the next is plated."),
                        )
