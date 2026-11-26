"""Slide — Three versions of every file: on disk, prepared (git add), last commit (NG, 2026-11-26).

Sets up the app.ts example (total = 0 / 10 / 99) that the next slide, « What git restore Brings Back »,
uses to show what each form of git restore keeps and loses. Same colours as « Where Your Changes Live »:
blue = disk, amber = prepared (staging area), green = history.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Three-versions slide styles."""
    heading = s.project.titles.heading
    sub = Style.create(s.project.titles.caption + s.center_txt, "gitthree_sub")
    body = s.project.titles.body
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label
    icon = Style.create(s.project.titles.body + s.center_txt
                        + Style("font-size: 2.2em; line-height: 1.2;", "gitthree_icon_size"), "gitthree_icon")
    desc = Style.create(s.project.titles.body + s.center_txt, "gitthree_desc")
    value = Style.create(s.text.fonts.font_monospace + s.bold + s.center_txt
                         + Style("font-size: 1.4em;", "gitthree_value_size"), "gitthree_value")
    code = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "gitthree_code")
bs = BlockStyles

_BLUE, _AMBER, _GREEN = s.project.tone_blue, s.project.tone_amber, s.project.tone_green

# (tone, icon, title, description, value at the end of the example)
_VERSIONS = [
    (_BLUE, "📂", "1 · On your disk", "the file you open and edit", "total = 99"),
    (_AMBER, "📋", "2 · Prepared", "what git add set aside for the next commit", "total = 10"),
    (_GREEN, "💾", "3 · Last commit", "what is saved in the history", "total = 0"),
]

_CARD_ZOOM = 90
_ICON_ZOOM = 180
_STORY_ZOOM = 100
_VALUE_ZOOM = 200  # the value of each version, read from the back of the room

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Tell the app.ts story step by step; the next slide uses it."),
    ("The message",
     "Git keeps three versions of each file: the one on your disk, the one you prepared with git add, and the one "
     "of the last commit. They can all be different at the same time."),
    ("Link to « Where Your Changes Live »",
     "Same boxes, same colours: disk = working directory (blue), prepared = staging area (amber), last commit = "
     "local repository (green). « Index » is the technical name of the staging area; « worktree » is the files on "
     "your disk."),
    ("The example",
     "The last commit says total = 0. You change it to total = 10, then git add app.ts: the prepared version is now "
     "total = 10. You change it again to total = 99 without git add: the disk says 99, the prepared version 10, the "
     "last commit 0."),
    ("Why it matters with an agent",
     "The agent often runs git add itself: what is prepared is not always what you reviewed. git status shows both: "
     "green = prepared, red = changed on disk but not prepared."),
    ("Ask the room",
     "« If I commit now, which value goes into the history? » Answer: total = 10 — the prepared one, not the one "
     "on the disk."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git add app.ts",
     "Copies the current content of app.ts from your disk into the prepared version (the staging area). Later "
     "changes on the disk are not prepared until you run git add again."),
]


def _card(tone, icon, title, desc, value):
    with st_block(tone.card):
        with st_zoom(_ICON_ZOOM):
            st_write(bs.icon, icon, tag=t.div)
        st_write(tone.title, title, tag=t.div)
        st_write(bs.desc, desc, tag=t.div)
        st_space("v", "1.5vh")
        with st_zoom(_VALUE_ZOOM):
            st_write(bs.value, (tone.chip, value), tag=t.div)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Three Versions of Every File", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Three Versions of Every File", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(110):
            st_write(bs.sub, "Example: the file app.ts, after the three steps below", tag=t.div)
        st_space("v", "1vh")
        with st_zoom(_CARD_ZOOM):
            with st_grid(cols="1fr 1fr 1fr", gap="0 1.5vw",
                         cell_styles=s.project.containers.grid_cell_centered) as g:
                for version in _VERSIONS:
                    with g.cell():
                        _card(*version)
        st_space("v", "2vh")
        story = [
            ("1.", ("Your last commit contains the line ", (bs.code, "total = 0"), ".")),
            ("2.", ("You change it to ", (bs.code, "total = 10"), ", then run ", (bs.code, "git add app.ts"),
                    ": the prepared version is now ", (bs.code, "total = 10"), ".")),
            ("3.", ("You change it again to ", (bs.code, "total = 99"), ", without running git add again.")),
        ]
        cols = "5% 4% 86% 5%"
        cells = s.project.containers.rows(len(story), cols, filled=(2, 3))
        with st_zoom(_STORY_ZOOM):
            with st_grid(cols=cols, gap="0.6vh 0", cell_styles=cells) as g:
                for num, parts in story:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.tl, num)
                    with g.cell():
                        st_write(bs.td, *parts)
                    with g.cell():
                        pass  # right margin
