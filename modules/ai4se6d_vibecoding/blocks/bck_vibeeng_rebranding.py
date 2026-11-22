"""Slide — From Coding to Engineering (skippable)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """Rebranding slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    accent = s.bold + s.project.colors.accent
    highlight = s.bold + s.project.colors.highlight
    source = s.project.citation + s.large
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: recipes of the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"), "ve_rebranding_text_cell")

_PROMPT = (
    f"{_PREFIX} A loose fluid shape in teal morphing into a precise structured "
    "geometric form in electric blue. An amber arrow shows the transformation "
    f"direction. {_SUFFIX}"
)

_NOTES = [
    ("The message",
     "The same tools can be used in two ways: vibe coding (you do not read the code) or engineering (you own every decision)."),
    ("Kent Beck",
     "Kent Beck (« Augmented Coding », 2025) draws the line: vibe coding is not reading the AI's code; augmented coding is owning every decision with AI assistance."),
    ("Karpathy",
     "The author of « vibe coding » now speaks of « agentic engineering »: AI agents execute, humans steer."),
    ("The metaphor",
     "The kitchen upgrades its tools, but the chef still designs and serves the menu: the responsibility does not move to the oven."),
    ("Link to the course",
     "The next slides give the six principles of VibeEngineering, applied with opencode and GSE-One from day 2."),
    ("Ask the room",
     "« In your team, who owns a line of code that an AI wrote? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):
                    st_write(bs.heading, "From Coding to Engineering", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — From Coding to Engineering", entries=_NOTES,
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
                        name="ve_rebranding",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(95):   # text cell fills the slide (NG, 2026-11-23)
                        with st_zoom(110):
                            st_write(
                                bs.body,
                                (bs.keyword, "Kent Beck"),
                                " drew the line: ",
                                (bs.accent, '"vibe coding"'),
                                " is when you don't read the code. ",
                                "Engineering is when you ",
                                (bs.keyword, "own"),
                                " every decision.",
                            )
                            st_space("v", 1)
                            st_write(
                                bs.body,
                                "Karpathy's term has been evolving toward ",
                                (bs.highlight, '"agentic engineering"'),
                                " — AI agents executing, humans steering.",
                            )
                            st_space("v", 1)
                            st_write(
                                bs.body,
                                (s.project.colors.muted, "The kitchen upgrades its tools — "
                                "but the chef still designs and serves the menu."),
                            )
                            st_space("v", 1)
                            # REF: beck2025-augmented-coding
                            st_write(bs.source, cite("beck2025-augmented-coding"))
