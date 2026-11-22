"""Slide 31 — The Tools That Make It Real: billboard intro."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """IDE overview billboard styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body + s.center_txt
    emphasis = Style.create(
        s.Large + s.bold + s.italic + s.project.colors.accent + s.center_txt,
        "ide_overview_emphasis",
    )
bs = BlockStyles

_NOTES = [
    ("The message",
     "Part 4 of the session. VibeCoding and VibeEngineering are ways of working; a tool only makes them possible. "
     "The same practice runs on several agents."),
    ("The idea explained",
     "This week the tool is opencode: a terminal agent, open source, used with your capped course key."),
    ("The trap",
     "Confusing the practice with the product: menus and names change, the discipline (requirements, tests, review) "
     "stays."),
    ("Link to the course",
     "The next slides go from the autonomy levels to opencode, then the other agents, MCP, the editor and the rules "
     "for this week."),
    ("Ask the room",
     "« Which AI coding tools do you use today, and at which step of your work? »"),
]

def build():
    with st_block(s.project.containers.page_fill_center + s.center_txt):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(85):
                st_write(bs.heading, "The Tools That Make It Real", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Tools That Make It Real", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "8vh")
        with st_zoom(150):
            st_write(
                bs.emphasis,
                "VibeCoding and VibeEngineering are practices.",
            )
            st_space("v", 1)
            st_write(
                bs.body,
                "The TOOLS bring them to life — this week, yours is opencode.",
            )
        st_space("v", "8vh")
