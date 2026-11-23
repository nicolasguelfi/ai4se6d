"""Slide — Context7: live docs instead of stale memory."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Context7 styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
bs = BlockStyles

_CMD = "opencode mcp add context7 --url https://mcp.context7.com/mcp"

_CONFIG = """\
{
  "mcp": { "servers": {
    "context7": { "type": "remote", "url": "https://mcp.context7.com/mcp" }
  } }
}"""

_NOTES = [
    ("The message",
     "The model learned APIs at training time; libraries such as React Router 7 move fast. Context7 is an MCP "
     "server that brings the current docs into the context."),
    ("Setup",
     "One command in the project folder: opencode mcp add context7 with its URL. It writes opencode.json at the "
     "project root — no hand-written JSON."),
    ("Check",
     "Restart opencode: the sidebar shows « context7 Connected ». Then ask for it in a prompt: « use context7 »."),
    ("The trap",
     "Trusting code that compiles in the model's memory of an old version. Ask for the live docs when the library "
     "is recent or fast-moving."),
    ("What comes next",
     "Try-it 3 uses it: plan a /budgets page with context7 for React Router 7."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(75):
                st_write(bs.heading, "Context7 — Live Docs", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Context7 — Live Docs", entries=_NOTES,
                                 position="left", width="50vw")
        with st_grid(cols="5% 90% 5%") as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                st_write(
                    bs.body, (bs.label, "Problem: "), "the model learned old APIs; React Router 7 moves fast.",
                    tag=t.div,
                )
                st_space("v", "1.5vh")
                st_write(bs.body, "In the project folder, one command (no hand-written JSON):", tag=t.div)
                st_code(s.none, code=_CMD, language="bash", line_numbers=False, font_size="24pt")
                st_space("v", "1.5vh")
                st_write(bs.body, "It writes ", (bs.label, "opencode.json"), " at the project root:", tag=t.div)
                st_code(s.none, code=_CONFIG, language="json", line_numbers=False, font_size="22pt")
                st_space("v", "1.5vh")
                st_write(
                    bs.body, "Check: restart opencode, the sidebar shows ", (bs.keyword, "context7 Connected"),
                    " · In a prompt: ", (bs.keyword, "use context7"), tag=t.div,
                )
            with g.cell():
                pass  # right margin
