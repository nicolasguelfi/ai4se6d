"""Slide — VibeCoding Principle 4: Low Barrier to Entry."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Principle 4 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_low_barrier_number",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "vc_low_barrier_text_cell")

_NOTES = [
    ("The message",
     "Fourth principle: you no longer need to know how to program to get a working prototype. An idea and the "
     "words to describe it are enough."),
    ("The idea explained",
     "The boundary between developers and non-developers blurs: product owners, designers, domain experts can build "
     "their own tools."),
    ("The good side",
     "It is a real gain: faster prototypes, ideas tested before they are specified, more people able to automate "
     "their work. This afternoon you will feel it yourselves."),
    ("The trap",
     "Building a prototype is not building a product. The person who cannot read the code cannot judge its "
     "security, its quality or its maintenance cost."),
    ("Ask the room",
     "« Who in your organisation would build their own app tomorrow if it took one afternoon? Who maintains it "
     "after? »"),
]

_PROMPT = (
    f"{_PREFIX} A wide-open gate made of simple geometric lines in electric blue, "
    "with diverse abstract human silhouettes of varying sizes walking through. "
    "No walls on either side. Amber glow at the threshold. Represents the "
    f"democratization of software creation. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Low Barrier to Entry", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Low Barrier to Entry", entries=_NOTES,
                                 position="left", width="50vw")

        with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                     cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="80%",
                    editable=IS_EDITABLE,
                    name="vc_low_barrier",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1024x1536",
                )

            with g.cell():
                st_write(bs.number, "4")
                st_space("v", 1)
                with st_zoom(100):
                    st_write(
                        bs.body,
                        (bs.keyword, "Anyone with an idea "),
                        "can build a working prototype.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "Non-programmers can produce functional prototypes, "
                        "blurring the traditional boundary between developers "
                        "and non-developers.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (s.project.colors.accent + s.LARGE + s.bold,
                        "Software creation made easier."),
                    )
