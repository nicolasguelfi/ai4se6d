"""Slide — What you will be able to do by 10:45."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Objectives styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    number = Style.create(s.project.titles.body + s.bold + s.project.colors.highlight, "ocobj_number")
bs = BlockStyles

_ITEMS = [
    ("Make a project ", (bs.keyword, "readable"), " for the agent"),
    ("Write project rules in ", (bs.keyword, "AGENTS.md")),
    ("Feed the right context with ", (bs.keyword, "@file")),
    ((bs.keyword, "Plan"), " with the plan agent, then ", (bs.keyword, "build")),
    ("Follow the agent’s ", (bs.keyword, "todo list")),
    ("Add live docs with ", (bs.keyword, "MCP + Context7")),
]

_NOTES = [
    ("The message",
     "Six abilities by the break at 10:45, in the order of the session."),
    ("Readable project and rules",
     "A clear structure the agent can navigate, and the project rules written once in AGENTS.md instead of "
     "repeated in every prompt."),
    ("Context",
     "@file puts the right files in front of the agent — not the whole repository."),
    ("Plan, build, todo",
     "The plan agent proposes without editing; the build agent then edits. The todo list shows where the agent is."),
    ("Live docs",
     "MCP connects the agent to tools; Context7 gives it the current documentation of a library."),
    ("Ask the room",
     "« Which of the six did you miss most yesterday? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "By 10:45 You Can", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — By 10:45 You Can", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # one numbered row per objective, alternating fills — motif L2 + fonds f1 (margins 5 %, numbering column)
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2, 3))
        with st_zoom(123), st_grid(cols=cols, gap="3.4vh 0.5vw", cell_styles=cells) as g:
            for n, item in enumerate(_ITEMS, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *item, tag=t.div)
                with g.cell():
                    pass  # right margin
