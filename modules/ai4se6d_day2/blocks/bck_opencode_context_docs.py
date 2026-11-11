"""Slide — Context7: live docs instead of stale memory."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


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


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Context7 — Live Docs", tag=t.div, toc_lvl="+1")
        st_write(
            bs.body, (bs.label, "Problem: "), "the model learned old APIs; React Router 7 moves fast.",
            tag=t.div,
        )
        st_write(bs.body, "In the project folder, one command (no hand-written JSON):", tag=t.div)
        st_code(s.none, code=_CMD, language="bash", line_numbers=False, font_size="22pt")
        st_write(bs.body, "It writes ", (bs.label, "opencode.json"), " at the project root:", tag=t.div)
        st_code(s.none, code=_CONFIG, language="json", line_numbers=False, font_size="20pt")
        st_write(
            bs.body, "Check: restart opencode, the sidebar shows ", (bs.keyword, "context7 Connected"),
            " · In a prompt: ", (bs.keyword, "use context7"), tag=t.div,
        )
