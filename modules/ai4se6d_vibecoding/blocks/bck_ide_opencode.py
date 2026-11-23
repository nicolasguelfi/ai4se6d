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
# Terminal 1 — your work session
$ cd ~/ai4se/my-project       # always start in a dedicated project folder
$ opencode                    # the agent works in this folder
> /init                       # reads the code, writes AGENTS.md
[Shift+Tab] -> plan           # plan agent: explores, does not edit your files
[Shift+Tab] -> build          # now it may edit and run commands
> explain @src/export.js      # @file adds a file to the context
> /gse-status                 # GSE-One commands start with /gse-

# Terminal 2 — open a NEW terminal window, outside opencode
$ ~/ai4se/ai4se-kit/tutor     # the course tutor (read-only)"""

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
     "Two agents come built in, with no configuration: build (the default at start-up: edits files, runs commands) "
     "and plan (explores and proposes, does not edit your project files). Shift+Tab switches from one to the other. "
     "AGENTS.md holds the project rules, /init drafts it. Permissions and MCP servers are set in opencode.json."),
    ("The trap",
     "Staying in build all the time: the agent then edits before you have agreed on what it should do."),
    ("Link to the course",
     "GSE-One runs inside opencode: its commands start with /gse-. Day 2 starts from AGENTS.md."),
    ("Ask the room",
     "« Why would a team want the project rules in a file, rather than in each person's prompt? »"),
    ("Technical recap — terminal agent",
     "A program you start by typing « opencode » in a terminal window, inside a project folder. You talk to it in "
     "plain text; it reads the files of that folder and, when allowed, changes them and runs commands. Open source "
     "(MIT licence): free to use, the code is public."),
    ("Technical recap — model provider, capped key",
     "opencode is not itself an AI model: it sends your requests to a model chosen in its settings (OpenAI, "
     "Anthropic, DeepSeek… through a provider). This week every learner has a course key with a spending cap."),
    ("Technical recap — agents plan and build",
     "In opencode an « agent » is a working mode with its own permissions. Two come with every installation, "
     "nothing to configure: build, active when opencode starts, may edit files and run commands; plan explores the "
     "code and proposes, without editing your project files (it may write its own plan notes, and any command it "
     "wants to run still asks for permission)."),
    ("Technical recap — Shift+Tab",
     "The keyboard shortcut that switches to the next agent: press Shift and Tab together in opencode; the active "
     "agent's name is shown at the bottom of the window. Press it again to come back."),
    ("Technical recap — AGENTS.md and /init",
     "AGENTS.md is a plain text file at the root of the project, read by the agent at the start of every session: "
     "the project rules (language, structure, commands, conventions). /init is an opencode command (typed in the "
     "chat, it starts with a slash) that reads the code and writes a first draft of AGENTS.md."),
    ("Technical recap — permissions, MCP, opencode.json",
     "Permissions say what the agent may do without asking (edit files, run shell commands): allow, ask or deny. "
     "MCP (Model Context Protocol) servers give the agent extra tools, e.g. a browser. Both are written in "
     "opencode.json, the configuration file of the project."),
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
    ("Technical recap — $ and >",
     "Lines starting with $ are typed in the terminal (the shell); lines starting with > are typed in opencode's "
     "chat. [Shift+Tab] is a key press, not text."),
    ("Technical recap — cd, folder",
     "cd ~/ai4se/my-project moves the terminal into the project folder; opencode then works only on that folder. "
     "~ is your home folder."),
    ("Technical recap — /init, /gse-status",
     "Commands typed in the chat start with a slash. /init writes AGENTS.md; /gse-status is a GSE-One command "
     "(GSE-One adds its own /gse-… commands to opencode)."),
    ("Technical recap — @file",
     "Typing @ followed by a file path adds that file to what the agent reads for this request (its context), "
     "instead of letting it search the whole project."),
    ("Technical recap — tutor",
     "A small course program from the ai4se-kit folder, run in a second terminal: it reads your project and "
     "answers questions, without changing anything (read-only)."),
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
    ("Technical recap — JSON",
     "opencode.json is written in JSON: names in quotes, a colon, then a value; { } groups settings, [ ] holds a "
     "list."),
    ("Technical recap — model",
     "\"<provider>/<reference model>\" names the AI model, e.g. a provider followed by a model name; the course kit "
     "fills it in for you."),
    ("Technical recap — permissions",
     "Each rule says, for an action (edit = change a file, shell = run a command) on a resource (* = everything), "
     "what happens: allow (do it), ask (ask you first) or deny (never)."),
    ("Technical recap — MCP server",
     "An MCP (Model Context Protocol) server is a small program that offers the agent extra tools. Here « local » "
     "means it runs on your machine, started by the command npx -y @playwright/mcp, and lets the agent drive a "
     "web browser."),
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
