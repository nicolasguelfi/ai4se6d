"""Section title — Driving opencode (09:50, 55 min)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Section title styles."""
    section = Style.create(s.project.titles.section_title + s.center_txt, "sec_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "sec_subtitle")
    info = Style.create(s.project.titles.caption + s.center_txt, "sec_info")
bs = BlockStyles

_NOTES = [
    ("The message",
     "The agent knows nothing about the project when a session starts. Give it what a new colleague would need: "
     "a readable project, written rules, the right context."),
    ("Timing",
     "55 minutes: three short demos, each followed by 5 minutes of try-it."),
    ("What comes",
     "A readable project structure, AGENTS.md rules, context with @file, the plan and build agents, checking the agent's « done », "
     "live docs through MCP and Context7."),
    ("Link to Git",
     "Everything the agent does from now on goes through the Git reflex just practised: status, diff, then commit."),
    ("Ask the room",
     "« What would you tell a new colleague on their first morning on CalcApp? »"),
    ("Cheat sheet",
     "Mini guide + cheat sheet for opencode 2 in the course kit: syllabus/opencode-guide.md (same shape as the IDE "
     "guide, ide-guide.md)."),
]


def build():
    with st_block(s.project.containers.page_fill_center):
        # the « i » at the top right, on the first line (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell():
                st_write(bs.info, "09:50 — 55 min · 3 short demos, each followed by 5 min of try-it", tag=t.div)
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Driving opencode", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "18vh")
        with st_zoom(130):
            st_write(bs.section, "Driving opencode", tag=t.div, toc_lvl="1")
            st_space("v", "3vh")
            st_write(bs.subtitle, "Give the agent what a new colleague would need", tag=t.div)
