"""Act IV — Why opencode for this course (replaces the former "You Will Master Cursor" slide)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Course-tool rationale slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    number = Style.create(s.project.titles.body + s.bold + s.project.colors.highlight + s.center_txt,
                          "ide_opencode_choice_number")
    note = Style.create(
        s.large + s.italic + s.project.colors.muted + s.center_txt,
        "ide_opencode_choice_note",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

_NOTES = [
    ("The message",
     "opencode is the course tool for five reasons: it is open source, it works with any model provider, its "
     "concepts transfer to the other agents, it lives in the terminal, and GSE-One runs on it."),
    ("Any provider",
     "One capped key for the course: the same tool works with whichever model the key gives access to — no seat "
     "licence, no vendor account per participant."),
    ("Concepts transfer",
     "AGENTS.md, plan / build agents, permissions, MCP: the same ideas exist in Cursor, Claude Code and the others "
     "under other names (previous slides). Learning them once in opencode is enough."),
    ("Terminal-first",
     "The agent works where the project lives — files, git, npm, tests — so what it does is visible and reproducible."),
    ("The editor next to it",
     "Keep an editor open beside opencode to READ the code; VSCodium is recommended, with its AI switched off "
     "(next slides)."),
    ("Ask the room",
     "« Which of these five reasons matters most for your team at work? »"),
]

# (number, keyword, keyword style, rest)
_REASONS = [
    ("1", "Open source", bs.keyword_warn, " — no seat licence, readable"),
    ("2", "Any provider", bs.keyword, " — one capped key for the course"),
    ("3", "Concepts transfer", bs.keyword_accent, " — to Cursor, Claude Code…"),
    ("4", "Terminal-first", bs.keyword, " — files, git, npm, tests"),
    ("5", "GSE-One", bs.keyword_warn, " — runs on 5 agents: the method goes with you"),
]

def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Why opencode?", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Why opencode?", entries=_NOTES, position="left", width="50vw")
        st_space("v", "2vh")

        # alternating rows (motif L2 + fonds f1): margins 5 %, numbering column, text column
        cols = "5% 6% 84% 5%"
        cells = s.project.containers.rows(len(_REASONS), cols, filled=(2, 3))
        with st_zoom(120), st_grid(cols=cols, gap="1vh 0.4vw", cell_styles=cells) as g:
            for num, key, key_style, rest in _REASONS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.number, num, tag=t.div)
                with g.cell():
                    st_write(bs.body, (key_style, key), rest, tag=t.div)
                with g.cell():
                    pass  # right margin

        st_space("v", "4vh")
        with st_zoom(120):
            st_write(
                bs.note,
                "Keep an editor open next to opencode to read code — VSCodium recommended, its AI off.",
                tag=t.div,
            )
        st_write(bs.source, cite("opencode-sst2024"))
