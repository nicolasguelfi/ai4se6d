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
    ("Trainer action",
     "Read and comment — nothing to type. Present opencode (build / plan, AGENTS.md, opencode.json); learners install it at 13:15 and use it from 14:30 (FreeSelfApp)."),
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
    ("Cheat sheet",
     "Mini guide + cheat sheet for opencode 2 in the course kit: syllabus/opencode-guide.md (same shape as the IDE "
     "guide, ide-guide.md)."),
]

_NOTES_SESSION = [
    ("Trainer action",
     "Read and comment — nothing to type. Learners install opencode only at 13:15 and practise these gestures at 14:30 (FreeSelfApp); /gse-status comes on day 3."),
    ("The message",
     "The gestures of a first session, in order: start in a dedicated folder, /init, plan, then build."),
    ("Line by line",
     "/init reads the code and writes AGENTS.md; Shift+Tab switches plan / build; @file adds a file to the context; "
     "/gse-status is a GSE-One command; a second terminal runs the course tutor, read-only."),
    ("The trap",
     "Launching opencode in your home folder: the agent works in the folder where it starts."),
    ("The rule",
     "Plan first, build second, check the changes before you commit: which files changed, do the tests pass, "
     "then read what is risky. Day 2 turns this into a method."),
    ("Ask the room",
     "« Which of these lines protects you from an unwanted edit? » (plan, then the diff review)"),
    ("Technical recap — $ and >",
     "Lines starting with $ are typed in the terminal (the shell); lines starting with > are typed in opencode's "
     "chat. [Shift+Tab] is a key press, not text. Do not type the $ or the > themselves: they only show where the "
     "line goes (the terminal shows its own $ prompt, opencode its own input box)."),
    ("Technical recap — # comments",
     "Everything after # on a line is a comment for you, not part of the command: do not type it. In the terminal "
     "the shell ignores it anyway; in opencode's chat it would be sent to the agent as text. « # Terminal 1 » and "
     "« # Terminal 2 » just label the two windows."),
    ("Technical recap — cd, folder",
     "cd ~/ai4se/my-project moves the terminal into the project folder; opencode then works only on that folder. "
     "cd = change directory; ~ is your home folder (/home/student in the course VM); / separates folder names, so "
     "this is the folder my-project inside ai4se inside your home. The folder must exist (otherwise « No such file "
     "or directory »): create it first with mkdir -p ~/ai4se/my-project (-p = also create the missing parent "
     "folders, no error if it already exists)."),
    ("Command — opencode",
     "Starts opencode in the current folder (the one cd moved to): the terminal turns into opencode's window, with "
     "an input box at the bottom and the active agent's name (build at start-up). The project is that folder; "
     "opencode also reads its AGENTS.md if there is one. To leave: type /exit or press Ctrl+C."),
    ("Technical recap — /init, /gse-status",
     "Commands typed in the chat start with a slash. /init writes AGENTS.md; /gse-status is a GSE-One command "
     "(GSE-One adds its own /gse-… commands to opencode)."),
    ("Prompt — /init",
     "An opencode command, not a request in plain words: the agent reads the project (its files, its structure, "
     "its build and test commands) and writes a first draft of AGENTS.md at the root of the folder. Read the draft "
     "and correct it: it is a guess from the code. If AGENTS.md already exists, /init improves it rather than "
     "starting from nothing."),
    ("Key — Shift+Tab (plan, then build)",
     "Press Shift and Tab together: opencode switches to the next agent and shows its name at the bottom. "
     "First press: build → plan (explores, reads, proposes; does not edit your project files). Second press: "
     "plan → build (may edit files and run commands). The arrow on the slide (->) means « switches to », it is not "
     "typed."),
    ("Prompt — explain @src/export.js",
     "A request in plain words: « explain » asks the agent to describe what the code does, without changing it. "
     "@ then a path attaches that file: typing @ opens a list of the project's files, keep typing (src/exp…) to "
     "narrow it, then choose the file. src/export.js = the file export.js in the src folder (src = « source », "
     "where the code lives). Useful in plan, to read before changing."),
    ("Prompt — /gse-status",
     "A command added by GSE-One (all its commands start with /gse-): it answers « where are we? » — the "
     "project's state in the GSE-One method and what comes next. It only reports, it changes nothing. Used from "
     "day 3; before GSE-One is installed, opencode does not know it."),
    ("Command — ~/ai4se/ai4se-kit/tutor",
     "Typed in a SECOND terminal window, not in opencode: it runs the file named tutor in the course kit folder "
     "(~/ai4se/ai4se-kit). Giving its full path runs it from any folder; no cd needed. It opens the course tutor, "
     "an AI prepared by the trainer in its own opencode session. With the word update after it "
     "(tutor update), it first downloads the latest course notes."),
    ("Technical recap — tutor",
     "A small course program from the ai4se-kit folder, run in a second terminal: it reads the course folders "
     "(~/ai4se by default, i.e. the course repos and your projects there) and answers questions, without changing "
     "anything (read-only). It never reads your secrets (.env files, keys, ~/.ssh)."),
    ("Also asked — !, /new, /compact",
     "Not on the slide, often asked. ! at the start of an empty prompt runs a shell command (e.g. !git status) and "
     "puts its output into the conversation. /new starts a fresh session (empty conversation, same project). "
     "/compact summarises the conversation so far, to free room in the agent's context."),
    ("Cheat sheet",
     "Mini guide + cheat sheet for opencode 2 in the course kit: syllabus/opencode-guide.md (same shape as the IDE "
     "guide, ide-guide.md)."),
]

_NOTES_CONFIG = [
    ("Trainer action",
     "Read and comment — nothing to type. The file is an example only: the course kit sets the model and permissions stay at opencode defaults, so learners never edit it."),
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
     "The value names the AI model as (provider)/(model): the provider first (the company or service that runs it), "
     "a slash, then the model's name, e.g. anthropic/claude-sonnet-5-5. On the slide the two parts in angle "
     "brackets are placeholders, not text to type; the course kit fills them in for you."),
    ("Technical recap — permissions",
     "Each rule says, for an action (edit = change a file, shell = run a command) on a resource (* = everything), "
     "what happens: allow (do it), ask (ask you first) or deny (never)."),
    ("Key — \"permissions\": [ … ]",
     "A list (the square brackets) of rules, read from top to bottom; when several rules match, the LAST one wins. "
     "Each rule is one { } with three keys: \"action\" = what the agent wants to do, \"resource\" = on what "
     "(a file path, or the command line for shell), \"effect\" = allow, ask or deny. With no rule at all, opencode "
     "2's default lets the agent act without asking (except reading .env secret files, where it asks); the plan "
     "agent adds its own rule that forbids editing project files."),
    ("Key — \"action\": \"edit\" / \"shell\"",
     "edit = create, change or delete a file. shell = run a command in the terminal (npm test, git commit…); "
     "opencode 1 called it bash. Other actions exist (read, webfetch…), not shown here."),
    ("Symbol — \"resource\": \"*\"",
     "* is a wildcard: it matches any text, including folder separators, so here « every file » or « every "
     "command ». A narrower pattern is possible, e.g. \"git status *\" for shell, or \"docs/*\" for edit."),
    ("Key — \"effect\": \"ask\"",
     "ask = opencode stops and asks you before each edit or command (allow once, always, or refuse). The other "
     "values: allow = act without asking, deny = always refuse."),
    ("Key — \"mcp\": { \"servers\": { … } }",
     "The MCP section: \"servers\" lists the MCP servers by name. \"playwright\" is just the name chosen for this "
     "one; its tools appear to the agent under that name."),
    ("Key — \"type\": \"local\"",
     "local = opencode starts the server itself, on your machine, with the command given next. The other value, "
     "remote, connects to a server on the internet through a \"url\" instead of a command."),
    ("Command — \"command\": [\"npx\", \"-y\", \"@playwright/mcp\"]",
     "The command that starts the server, written as a list: the program first, then each argument in its own "
     "quotes. Same as typing npx -y @playwright/mcp in a terminal. npx = runs a package from the npm registry "
     "(downloading it the first time) without installing it in your project; -y = answer « yes » to npx's "
     "question « OK to download? » so it does not wait; @playwright/mcp = the package's name (@playwright = the "
     "Playwright team's account on npm, mcp = the package). Node.js must be installed."),
    ("Technical recap — MCP server",
     "An MCP (Model Context Protocol) server is a small program that offers the agent extra tools. Here « local » "
     "means it runs on your machine, started by the command npx -y @playwright/mcp, and lets the agent drive a "
     "web browser."),
    ("Technical recap — where the file lives",
     "opencode.json sits at the root of the project folder (settings for that project); a global one in "
     "~/.config/opencode/ applies to all your projects, and the project file wins. The file may also be called "
     "opencode.jsonc (JSON with comments)."),
    ("Cheat sheet",
     "Mini guide + cheat sheet for opencode 2 in the course kit: syllabus/opencode-guide.md (same shape as the IDE "
     "guide, ide-guide.md)."),
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
                "Plan first, build second, check the changes before you commit.",
                tag=t.div,
            )

    st_slide_break()

    # Slide 3 — the configuration file
    with st_block(s.project.containers.page_fill_top):
        _header(bs.subheading, "opencode.json", "2", _NOTES_CONFIG, 85)
        st_space("v", "2vh")

        with st_grid(
            cols="3fr 2fr",
            gap="3vw",
            cell_styles=[s.project.containers.grid_cell_centered, _text_cell],
        ) as g:
            with g.cell(), st_zoom(135):
                st_code(s.none, code=_CONFIG, language="json")
            with g.cell(), st_zoom(110):
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
