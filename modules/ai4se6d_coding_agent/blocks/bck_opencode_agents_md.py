"""Slide — Project rules = AGENTS.md (opencode)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """AGENTS.md styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "ocagents_closing")
bs = BlockStyles

_NOTES = [
    ("The message",
     "AGENTS.md is where the project's rules live for opencode: a Markdown file at the project root, read at "
     "every start, and again when it changes."),
    ("How to get one",
     "/init drafts one from your project; you then edit it. Commit it so everyone in the team works with the same "
     "rules."),
    ("Two levels",
     "Personal rules go in ~/.config/opencode/AGENTS.md; extra rule files can be listed under « instructions » "
     "in opencode.json."),
    ("The trap",
     "Expecting a special syntax. It is plain Markdown: write it as you would brief a colleague."),
    ("What comes next",
     "The AGENTS.md shipped with the CalcApp starter, then a try-it: one rule of yours changes the agent's answer."),
    ("Ask the room",
     "« What is the first rule you would write for your own project? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — /init",
     "Typed in the opencode prompt box, in the project: the agent looks at the project and drafts (or updates) "
     "AGENTS.md. Read and edit the draft: it is a first version, not the truth."),
    ("Path — ~/.config/opencode/AGENTS.md",
     "Your personal rules, for every project on this machine. ~ = your home folder; .config starts with a dot, so "
     "it is hidden (ls -a shows it). Loaded before the project's AGENTS.md."),
    ("Key — instructions in opencode.json",
     "A list of extra rule files read after AGENTS.md, e.g. \"instructions\": [\"docs/style.md\"]. Each entry is a "
     "path, a pattern such as docs/*.md, a ~/ path or a web address."),
    ("Command — commit it",
     "git add AGENTS.md && git commit -m \"docs: add project rules\": the file goes into the history, so everyone "
     "who clones the project gets the same rules."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Project Rules = AGENTS.md", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Project Rules = AGENTS.md", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # One row per fact, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ("At the project root, read at start and when it changes",),
            ((bs.keyword, "/init"), " drafts one from your project"),
            ((bs.keyword, "Commit it"), ": same rules for everyone"),
            ("Personal: ", (bs.keyword, "~/.config/opencode/AGENTS.md")),
            ("Extra files: ", (bs.keyword, "instructions"), " in opencode.json"),
        ]
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2,))
        with st_zoom(122), st_grid(cols=cols, gap="2.2vh 0.5vw", cell_styles=cells) as g:
            for parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "4vh")
        with st_zoom(130):
            st_write(bs.closing, "Plain Markdown. No special syntax.", tag=t.div)
