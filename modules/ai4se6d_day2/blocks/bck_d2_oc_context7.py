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

_CONFIG = """\
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "context7": {
      "type": "remote",
      "url": "https://mcp.context7.com/mcp"
    }
  }
}"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Context7 — Live Docs", tag=t.div, toc_lvl="+1")
        st_write(
            bs.body, (bs.label, "Problem: "), "the model learned old APIs; React Router 7 moves fast.",
            tag=t.div,
        )
        st_write(bs.body, "Add to ", (bs.label, "opencode.json"), " at the project root:", tag=t.div)
        st_code(s.none, code=_CONFIG, language="json", line_numbers=False, font_size="22pt")
        st_write(
            bs.body, "Check: ", (bs.keyword, "opencode mcp list"),
            " · In a prompt: ", (bs.keyword, "use context7"), tag=t.div,
        )
