"""Slide — The four areas of Git, drawn with StreamTeX grids and styled text.

NG, 2026-11-24: replaces the old PNG diagram (readable in dark mode, fills the slide, editable as code);
the git commands are the point of the slide, so they and the arrows are the largest elements.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


def _tone(rgb, hexa, key):
    """Card (tinted fill + coloured border), title, chip and commit-dot styles of one area colour."""
    card = Style.create(
        Style(f"background-color: rgba({rgb}, 0.13); border: 3px solid {hexa}; border-radius: 16px; "
              "padding: 2.5vh 0.8vw; min-height: 60vh; box-sizing: border-box;", f"gitareas_card_{key}")
        + s.container.layouts.vertical_center_layout + s.center_txt,
        f"gitareas_card_{key}_c",
    )
    title = Style.create(s.project.titles.table_label + s.bold + Style(f"color: {hexa};", f"gitareas_fg_{key}"),
                         f"gitareas_title_{key}")
    chip = Style(f"background-color: rgba({rgb}, 0.28); border-radius: 8px; padding: 2px 10px; margin: 3px 4px; "
                 "white-space: nowrap; display: inline-block;",
                 f"gitareas_chip_{key}")
    dot = Style(f"background-color: {hexa}; border-radius: 50%; padding: 4px 9px; margin: 0 3px; "
                "font-weight: bold; display: inline-block;", f"gitareas_dot_{key}")
    return card, title, chip, dot


# Same colours as the old diagram: blue, amber, green, purple
_WORK = _tone("122, 184, 245", "#7AB8F5", "work")
_STAGE = _tone("243, 156, 18", "#F39C12", "stage")
_LOCAL = _tone("39, 174, 96", "#27AE60", "local")
_REMOTE = _tone("155, 89, 182", "#B07CD8", "remote")


class BlockStyles:
    """Native four-areas diagram styles."""
    heading = s.project.titles.heading
    sub = Style.create(s.project.titles.caption + s.center_txt, "gitareas_sub")
    body = Style.create(s.project.titles.body + s.center_txt, "gitareas_body")
    icon = Style.create(s.project.titles.body + s.center_txt + Style("font-size: 2.2em; line-height: 1.2;", "gitareas_icon_size"),
                        "gitareas_icon")
    cmd = Style.create(s.text.fonts.font_monospace + s.bold + s.center_txt
                       + Style("font-size: 1.5em; white-space: nowrap;", "gitareas_cmd_size"), "gitareas_cmd")
    arrow = Style.create(s.project.titles.body + s.bold + s.center_txt + Style("font-size: 4.5em; line-height: 0.9;",
                                                                              "gitareas_arrow_size"),
                         "gitareas_arrow")
    caption = Style.create(s.project.titles.body + s.center_txt, "gitareas_caption")
    keyword = s.project.titles.keyword
    analogy_box = s.project.containers.callout
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Walk the four boxes left to right; learners do it in the Git exercise."),
    ("The message",
     "A change goes through areas before it is saved in the history: you choose what goes into the next snapshot."),
    ("Read the diagram",
     "Working directory = your files on disk. git add copies a change into the staging area (what is ready for "
     "the next commit). git commit saves that snapshot in the local repository (c1, c2, c3 = commits). git push "
     "sends commits to the remote repository on GitHub; git pull brings its new commits back."),
    ("The photography analogy",
     "Scene (your files) → pose the subjects you want in the picture (git add) → click the shutter (git commit) → "
     "upload to the cloud (git push)."),
    ("Why it matters with an agent",
     "The agent may change many files; staging lets you commit only the changes you have reviewed and approved."),
    ("The trap",
     "Thinking that a saved file is a committed file: until git commit, the change is not in the history."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git add (file)",
     "Copies the current state of the file into the staging area, e.g. git add App.tsx. git add . (dot = this folder "
     "and everything below) stages everything: avoid it after the agent worked."),
    ("Command — git commit",
     "Saves everything in the staging area as one commit in the local repository. Usually with -m \"message\"."),
    ("Command — git push / git pull",
     "git push sends your new commits to the remote (GitHub); git pull downloads the remote's new commits and "
     "merges them into your branch."),
]

# (tone, icon, title, subtitle, chips, dots)
_AREAS = [
    (_WORK, "📂", "Working Directory", "Your files on disk", ["App.tsx", "index.ts"], []),
    (_STAGE, "📋", "Staging Area", "Ready to commit", ["+ App.tsx"], []),
    (_LOCAL, "💾", "Local Repository", "Committed history", [], ["c1", "c2", "c3"]),
    (_REMOTE, "☁️", "Remote Repository", "GitHub", [], ["c1", "c2"]),
]


_CARD_ZOOM = 80     # cards + arrows; tuned by measure (content bottom <= 1000 px at 1920x1080)
_ANALOGY_ZOOM = 72
_CHIP_ZOOM = 85     # file names and commit dots inside the cards
_ICON_ZOOM = 200    # emoji above each area title
_ARROW_ZOOM = 440   # arrow glyphs between the areas
_CMD_ZOOM = 240     # git command under each arrow


def _card(tone, icon, title, subtitle, chips, dots):
    card, title_style, chip, dot = tone
    with st_block(card):
        with st_zoom(_ICON_ZOOM):
            st_write(bs.icon, icon, tag=t.div)
        st_write(title_style, title, tag=t.div)
        st_write(bs.sub, subtitle, tag=t.div)
        st_space("v", "1.5vh")
        with st_zoom(_CHIP_ZOOM):
            for c in chips:  # one file name per line: keeps the cards narrow
                st_write(bs.body, (chip, c), tag=t.div)
            if dots:
                st_write(bs.body, *[(dot, d) for d in dots], tag=t.div)


def _arrow(lines):
    """lines: [(arrow, command, tone_title_style)] stacked in one column."""
    for i, (glyph, cmd, colour) in enumerate(lines):
        if i:
            st_space("v", "1vh")
        with st_zoom(_ARROW_ZOOM):
            st_write(bs.arrow + colour, glyph, tag=t.div)
        with st_zoom(_CMD_ZOOM):
            st_write(bs.cmd + colour, cmd, tag=t.div)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Where Your Changes Live", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Where Your Changes Live", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(105):
            st_write(bs.sub, "How your code travels from your editor to GitHub", tag=t.div)
        st_space("v", "3vh")

        blue = Style("color: #7AB8F5;", "gitareas_c_blue")
        green = Style("color: #27AE60;", "gitareas_c_green")
        purple = Style("color: #B07CD8;", "gitareas_c_purple")
        arrows = [
            [("→", "git add", blue)],
            [("→", "git commit", green)],
            [("→", "git push", purple), ("←", "git pull", purple)],
        ]
        with st_zoom(_CARD_ZOOM):
            with st_grid(cols="1fr 0.95fr 1fr 0.95fr 1fr 0.95fr 1fr", gap="0 0.2vw",
                         cell_styles=s.project.containers.grid_cell_centered) as g:
                for i, area in enumerate(_AREAS):
                    with g.cell():
                        _card(*area)
                    if i < len(arrows):
                        with g.cell():
                            _arrow(arrows[i])
        st_space("v", "4vh")
        amber = Style("color: #F39C12;", "gitareas_c_amber")
        with st_zoom(_ANALOGY_ZOOM), st_block(bs.analogy_box):
            st_write(
                bs.caption, (s.bold, "Photography analogy: "),
                (blue, "📂 scene"), "  →  ", (amber, "📋 pose subjects"), "  →  ",
                (green, "💾 click shutter"), "  →  ", (purple, "☁️ upload to cloud"), tag=t.div,
            )
        st_space("v", "2vh")
        with st_zoom(_ANALOGY_ZOOM):
            st_write(
                bs.caption, (bs.keyword, "git add"), " chooses what goes into the next snapshot — ",
                (bs.keyword, "git commit"), " takes it.", tag=t.div,
            )
