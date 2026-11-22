"""Slide — 6 Principles of VibeEngineering."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip


# Viewport-filling container
_page_fill = s.project.containers.page_fill_top

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "vibeeng_principles_cell",
)


class BlockStyles:
    """VibeEngineering principles slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = Style.create(s.bold + s.project.colors.primary + s.Large, "vibeeng_pr_keyword")
    keyword_accent = Style.create(s.bold + s.project.colors.accent + s.Large, "vibeeng_pr_keyword_accent")
    number = Style.create(s.bold + s.project.colors.highlight + s.Large, "vibeeng_pr_number")
bs = BlockStyles

# The six principles, in order; the last one in the accent colour (as before)
_ITEMS = [
    ("Requirements Before Prompts", bs.keyword),
    ("Test-Driven Generation", bs.keyword),
    ("Architectural Intent", bs.keyword),
    ("Iterative Refinement", bs.keyword),
    ("Human Review at Boundaries", bs.keyword),
    ("Context Engineering", bs.keyword_accent),
]

_NOTES = [
    ("The message",
     "VibeEngineering keeps the speed of AI generation and puts back the engineering discipline around it: six "
     "principles, one slide each next."),
    ("The six in one sentence each",
     "P1 requirements written before the prompt; P2 tests written before the code, as its contract; P3 design "
     "decisions taken by humans and passed to the agent through context files; P4 planned iterations with acceptance "
     "criteria and review gates; P5 human review where mistakes cost most; P6 curate what the agent sees."),
    ("Not new",
     "Each principle is classic software engineering (requirements, TDD, architecture, iterations, review). What "
     "changes is who writes the code: the discipline moves to what you give the agent and what you check."),
    ("Why P6 stands out",
     "Context Engineering is the one specific to AI agents: project rules, memory, MCP servers."),
    ("Link to the course",
     "Tomorrow on CalcApp you apply them; from day 3 GSE-One turns them into the steps of one lifecycle."),
    ("Ask the room",
     "« Which of the six did you skip this afternoon in FreeSelfApp? »"),
]


_PROMPT = (
    f"{_PREFIX} A sturdy bridge made of five glowing pillars connecting two platforms. "
    "Left platform is chaotic with scattered code fragments. Right platform is orderly "
    "with structured blueprints. Each pillar glows in alternating electric blue and teal. "
    "Amber light flows across the bridge top. Symbolizes engineering discipline "
    f"as the bridge from chaos to quality. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "6 Principles of VibeEngineering", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — 6 Principles of VibeEngineering", entries=_NOTES,
                                 position="left", width="50vw")

        with st_grid(cols="1.5fr 3.5fr", gap="3vw", cell_styles=_cell) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="80%",
                    editable=IS_EDITABLE,
                    name="vibeeng_principles",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1024x1536",
                )

            with g.cell():
                # one grid row per principle, alternating fills, a number column (motif L2 + fonds f1)
                cols = "8% 92%"
                cells = s.project.containers.rows(len(_ITEMS), cols, filled=(1, 2))
                with st_zoom(95), st_grid(cols=cols, gap="5.5vh 0.4vw", cell_styles=cells) as r:   # rows spread over the slide
                    for i, (name, style) in enumerate(_ITEMS, start=1):
                        with r.cell():
                            st_write(bs.number, str(i), tag=t.div)
                        with r.cell():
                            st_write(bs.body, (style, name), tag=t.div)
