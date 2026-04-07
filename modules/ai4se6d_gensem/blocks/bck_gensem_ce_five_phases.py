"""Slide — The Five-Phase Workflow of Compound Engineering."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX

class BlockStyles:
    """Five-phase workflow slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    phase_name = s.bold + s.project.colors.primary + s.Large
    command = s.project.colors.accent + s.Large
    body = s.project.titles.body
bs = BlockStyles

PIPELINE_PROMPT = (
    f"{_PREFIX} Five hexagonal nodes arranged in a horizontal chain, connected by "
    "flowing curved lines. Each hexagon slightly larger than the previous. Colors "
    "transition from electric blue on the left through teal in the center to amber "
    f"on the right. Glowing edges, geometric, sense of progression. {_SUFFIX}"
)

_PHASES = [
    ("Brainstorm", "/ce:brainstorm", "Requirements exploration and clarification"),
    ("Plan", "/ce:plan", "Implementation blueprint with task decomposition"),
    ("Work", "/ce:work", "Execute with safeguards against plan"),
    ("Review", "/ce:review", "Multi-perspective quality review"),
    ("Compound", "/ce:compound", "Codify knowledge for future cycles"),
]

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Five-Phase Workflow", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        st_image(
            s.none,
            width="80%",
            editable=IS_EDITABLE,
            name="hero_ce_five_phases",
            prompt=PIPELINE_PROMPT,
            provider="openai",
            ai_size="1536x1024",
        )

        st_space("v", 1)

        with st_grid(
            cols="repeat(auto-fit, minmax(150px, 1fr))",
            gap="12px",
            cell_styles=s.project.containers.cell_primary_bg
            + s.project.containers.cell_pad_md
            + s.project.containers.grid_cell_centered,
        ) as g:
            for name, command, description in _PHASES:
                with g.cell():
                    st_write(bs.phase_name, name, tag=t.div)
                    st_write(bs.command, command, tag=t.div)
                    st_space("v", 0.3)
                    st_write(bs.body, description)
