"""Act IV — opencode, the course tool: overview + a first session + its configuration file.

Replaces the former Cursor deep dive (edition 2: learners use opencode, not Cursor).
Facts checked against the opencode documentation (opencode.ai/docs: agents, models, MCP servers),
November 2026.
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """opencode slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    caption = Style.create(
        s.large + s.italic + s.project.colors.muted + s.center_txt,
        "ide_opencode_caption",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


_SESSION = """\
$ cd ~/ai4se/my-project       # always start in a dedicated project folder
$ opencode                    # the agent works in this folder

> /init                       # reads the code, writes AGENTS.md
[Tab] -> plan                 # read-only: propose a plan first
[Tab] -> build                # now it may edit and run commands
> explain @src/export.js      # @file adds a file to the context
> /gse-status                 # GSE-One commands start with /gse-
$ ~/ai4se/ai4se-kit/tutor     # 2nd terminal: the course tutor (read-only)"""

_CONFIG = """\
{
  "model": "<provider>/<reference model>",
  "permissions": [
    { "action": "edit", "resource": "*", "effect": "ask" },
    { "action": "shell", "resource": "*", "effect": "ask" }
  ],
  "mcp": { "servers": {
    "playwright": { "type": "local",
      "command": ["npx", "-y", "@playwright/mcp"] }
  } }
}"""


def build():
    # Slide 1 — opencode overview
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "opencode \u2014 Our Tool", tag=t.div, toc_lvl="1")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword, "Terminal agent"), " \u2014 open source (MIT)")
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Any model provider"), " \u2014 this week: your capped key")
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "plan"), " / ", (bs.keyword_accent, "build"), " agents \u2014 ", (bs.keyword_warn, "Tab"), " to switch")
                with l.item():
                    st_write(bs.body, (bs.keyword, "AGENTS.md"), " \u2014 project rules; ", (bs.keyword, "/init"), " drafts it")
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Permissions"), " + ", (bs.keyword, "MCP"), " \u2014 in opencode.json")

            st_write(bs.source, cite("opencode-sst2024"))

    st_slide_break()

    # Slide 2 — a first session
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.subheading, "A First opencode Session", tag=t.div, toc_lvl="2")
            with st_zoom(130):
                st_code(s.none, code=_SESSION, language="bash")
            st_write(
                bs.caption,
                "Plan first, build second, review the diff before you commit.",
                tag=t.div,
            )

    st_slide_break()

    # Slide 3 — the configuration file
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.subheading, "opencode.json", tag=t.div, toc_lvl="2")

            with st_grid(
                cols="2fr 1fr",
                gap="24px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell(), st_zoom(105):
                    st_code(s.none, code=_CONFIG, language="json")
                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Model"), " — set once")
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "Permissions"), " — ask first")
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "MCP"), " — extra tools")

            st_write(
                bs.caption,
                "Example only — the course kit sets your reference model; permissions stay at opencode defaults.",
                tag=t.div,
            )
