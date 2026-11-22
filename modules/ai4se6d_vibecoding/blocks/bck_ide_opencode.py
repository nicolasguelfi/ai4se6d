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
from shared_widgets import st_hover_tooltip


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

# Text cell: vertically centred, left-aligned (NG, 2026-11-23)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "ide_opencode_text_cell")


_SESSION = """\
$ cd ~/ai4se/my-project       # always start in a dedicated project folder
$ opencode                    # the agent works in this folder

> /init                       # reads the code, writes AGENTS.md
[Shift+Tab] -> plan           # read-only: propose a plan first
[Shift+Tab] -> build          # now it may edit and run commands
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


# One screen per slide: the box is a full screen (the book zoom is 90 %), so the next slide's title does not show
# at the bottom (NG, 2026-11-23)
_one_screen = Style("min-height:104vh;", "ide_opencode_one_screen")

_NOTES_OVERVIEW = [
    ("The message",
     "opencode is the agent of the week: it runs in the terminal, in the project folder, and works with any model "
     "provider. This week it uses your capped course key."),
    ("The idea explained",
     "Two agents: plan (read-only, proposes) and build (edits files, runs commands); Shift+Tab switches. AGENTS.md "
     "holds the project rules, /init drafts it. Permissions and MCP servers are set in opencode.json."),
    ("The trap",
     "Staying in build all the time: the agent then edits before you have agreed on what it should do."),
    ("Link to the course",
     "GSE-One runs inside opencode: its commands start with /gse-. Day 2 starts from AGENTS.md."),
    ("Ask the room",
     "« Why would a team want the project rules in a file, rather than in each person's prompt? »"),
]

_NOTES_SESSION = [
    ("The message",
     "The gestures of a first session, in order: start in a dedicated folder, /init, plan, then build."),
    ("Line by line",
     "/init reads the code and writes AGENTS.md; Shift+Tab switches plan / build; @file adds a file to the context; "
     "/gse-status is a GSE-One command; a second terminal runs the course tutor, read-only."),
    ("The trap",
     "Launching opencode in your home folder: the agent works in the folder where it starts."),
    ("The rule",
     "Plan first, build second, review the diff before you commit."),
    ("Ask the room",
     "« Which of these lines protects you from an unwanted edit? » (plan, then the diff review)"),
]

_NOTES_CONFIG = [
    ("The message",
     "opencode.json is the agent's configuration: the model, the permissions, the MCP servers."),
    ("The three parts",
     "Model: set once. Permissions: here edit and shell are set to « ask », so the agent asks before acting. "
     "MCP: extra tools, for example a Playwright server to drive a browser."),
    ("The trap",
     "This file is an example: the course kit sets your reference model, and the permissions stay at opencode "
     "defaults."),
    ("Link to the course",
     "MCP comes back a few slides later (Model Context Protocol)."),
    ("Ask the room",
     "« Which actions would you set to ask, and which to allow, on a real project? »"),
]


def _header(style, title, lvl, notes, zoom):
    """Title and « i » on the same line (header grid 95% / 5%), title smaller (NG, 2026-11-23)."""
    with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
        with h.cell(), st_zoom(zoom):
            st_write(style, title, tag=t.div, toc_lvl=lvl)
        with h.cell():
            st_hover_tooltip(title=f"Trainer notes — {title}", entries=notes, position="left", width="50vw")


def build():
    # Slide 1 — opencode overview
    with st_block(s.project.containers.page_fill_top + _one_screen):
        _header(bs.heading, "opencode \u2014 Our Tool", "1", _NOTES_OVERVIEW, 85)
        st_space("v", "2vh")

        # one row per feature, alternating fills (motif L2 + fonds f1), margins 5 %
        items = [
            ((bs.keyword, "Terminal agent"), " \u2014 open source (MIT)"),
            ((bs.keyword_warn, "Any model provider"), " \u2014 this week: your capped key"),
            ((bs.keyword_accent, "plan"), " / ", (bs.keyword_accent, "build"), " agents \u2014 ",
             (bs.keyword_warn, "Shift+Tab"), " to switch"),
            ((bs.keyword, "AGENTS.md"), " \u2014 project rules; ", (bs.keyword, "/init"), " drafts it"),
            ((bs.keyword_warn, "Permissions"), " + ", (bs.keyword, "MCP"), " \u2014 in opencode.json"),
        ]
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2,))
        with st_zoom(112), st_grid(cols=cols, gap="3vh 1vw", cell_styles=cells) as g:
            for parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin

        st_space("v", "2vh")
        st_write(bs.source, cite("opencode-sst2024"))

    st_slide_break()

    # Slide 2 — a first session
    with st_block(s.project.containers.page_fill_top + _one_screen):
        _header(bs.subheading, "A First opencode Session", "2", _NOTES_SESSION, 85)
        st_space("v", "2vh")
        with st_zoom(150):
            st_code(s.none, code=_SESSION, language="bash")
        st_space("v", "2vh")
        with st_zoom(130):
            st_write(
                bs.caption,
                "Plan first, build second, review the diff before you commit.",
                tag=t.div,
            )

    st_slide_break()

    # Slide 3 — the configuration file
    with st_block(s.project.containers.page_fill_top):
        _header(bs.subheading, "opencode.json", "2", _NOTES_CONFIG, 85)
        st_space("v", "2vh")

        with st_grid(
            cols="2fr 1fr",
            gap="3vw",
            cell_styles=[s.project.containers.grid_cell_centered, _text_cell],
        ) as g:
            with g.cell(), st_zoom(135):
                st_code(s.none, code=_CONFIG, language="json")
            with g.cell(), st_zoom(125):
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered,
                             text_align="left", item_gap=0.6) as l:
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Model"), " — set once")
                    with l.item():
                        st_write(bs.body, (bs.keyword_warn, "Permissions"), " — ask first")
                    with l.item():
                        st_write(bs.body, (bs.keyword_accent, "MCP"), " — extra tools")

        st_space("v", "2vh")
        with st_zoom(120):
            st_write(
                bs.caption,
                "Example only — the course kit sets your reference model; permissions stay at opencode defaults.",
                tag=t.div,
            )
