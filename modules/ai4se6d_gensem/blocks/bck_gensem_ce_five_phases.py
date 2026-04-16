"""Slide — The 4-Phase GSE-One Lifecycle (LC00-LC03)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """GSE-One lifecycle slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    phase_name = s.bold + s.project.colors.primary + s.Large
    command = s.project.colors.accent + s.Large
    body = s.project.titles.body
bs = BlockStyles

PIPELINE_PROMPT = (
    f"{_PREFIX} Four hexagonal nodes arranged in a horizontal chain, connected by "
    "flowing curved lines. Each hexagon slightly larger than the previous. Colors "
    "transition from electric blue on the left through teal in the center to amber "
    f"on the right. Glowing edges, geometric, sense of progression. {_SUFFIX}"
)

_PHASES = [
    ("LC00 — Onboarding", "/gse:hug", "User profiling and project initialization"),
    ("LC01 — Discovery & Planning", "/gse:collect  /gse:assess  /gse:plan", "Understand context, identify gaps, plan the sprint"),
    ("LC02 — Development", "/gse:reqs  /gse:design  /gse:preview  /gse:tests  /gse:produce  /gse:review  /gse:fix  /gse:deliver", "Specify, design, test, build, review, and ship"),
    ("LC03 — Capitalization", "/gse:compound  /gse:integrate", "Codify learnings, route improvements"),
]

def build():
    st_marker("4-Phase Lifecycle")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "The 4-Phase GSE-One Lifecycle", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="GSE-One Lifecycle — LC00 to LC03",
                        entries=[
                            ("LC00 Onboarding", "/gse:hug captures your profile (11 dimensions) to adapt the agent to your level."),
                            ("LC01 Discovery", "/gse:collect scans sources, /gse:assess identifies gaps, /gse:plan creates a sprint with complexity budget."),
                            ("LC02 Development", "REQS > DESIGN > PREVIEW > TESTS > PRODUCE > REVIEW > FIX > DELIVER — the full development cycle."),
                            ("LC03 Capitalization", "/gse:compound codifies learnings, /gse:integrate routes them to operational destinations."),
                            ("Cross-cutting", "/gse:status, /gse:health, /gse:backlog, /gse:task, /gse:learn, /gse:pause, /gse:resume, /gse:deploy — available at any phase."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

        with st_grid(cols="40% 1fr", gap="16px", cell_styles=s.project.containers.grid_cell_centered) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="100%",
                    editable=IS_EDITABLE,
                    name="hero_ce_five_phases",
                    prompt=PIPELINE_PROMPT,
                    provider="openai",
                    ai_size="1536x1024",
                )
            with st_zoom(70):
                with g.cell():
                    with st_grid(
                        cols="1fr",
                        gap="12px",
                        cell_styles=s.project.containers.cell_primary_bg
                        + s.project.containers.cell_pad_md
                        + s.project.containers.cell_pad_md,
                    ) as inner:
                        for name, commands, description in _PHASES:
                            with inner.cell():
                                st_write(bs.phase_name, name)
                                st_write(bs.command, commands)
                                st_space("v", 0.3)
                                st_write(bs.body, description)
