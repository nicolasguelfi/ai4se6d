"""Slide — What each form of git restore brings back, on the app.ts example (NG, 2026-11-26).

Follows « Three Versions of Every File »: same example (disk total = 99, prepared total = 10, last commit
total = 0), same colours (blue = disk, amber = prepared, green = last commit).
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Restore-table slide styles."""
    heading = s.project.titles.heading
    sub = Style.create(s.project.titles.caption + s.center_txt, "gitrestore_sub")
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label
    # table_cell first: it carries the font size; monospace after it so the font family wins
    cmd = Style.create(s.project.titles.table_cell + s.text.fonts.font_monospace + s.bold + s.project.colors.accent
                       + Style("white-space: nowrap;", "gitrestore_nowrap"), "gitrestore_cmd")
    val = Style.create(s.project.titles.table_cell + s.text.fonts.font_monospace + s.center_txt
                       + Style("white-space: nowrap;", "gitrestore_nowrap"), "gitrestore_val")
    keyword = s.project.titles.keyword
bs = BlockStyles

_BLUE, _AMBER, _GREEN = s.project.tone_blue, s.project.tone_amber, s.project.tone_green
_RED = s.project.tone_red

# (first column, disk, prepared, last commit, what you lose)
_ROWS = [
    ("Before the command", "total = 99", "total = 10", "total = 0", "—"),
    ("git restore --staged .", "total = 99", "total = 0", "total = 0", "nothing"),
    ("git restore .", "total = 10", "total = 10", "total = 0", "total = 99"),
    ("git restore --staged --worktree .", "total = 0", "total = 0", "total = 0", "total = 10 and 99"),
]

_TABLE_ZOOM = 70  # tuned by measure (content bottom <= 1000 px at 1920x1080)

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Go row by row; ask the room what each command loses before showing it."),
    ("The message",
     "--staged acts on what you prepared with git add; --worktree acts on the file you see in the editor. Only "
     "--worktree (or plain git restore) loses work."),
    ("Row by row",
     "git restore --staged . undoes git add: the prepared version goes back to the last commit, your file keeps "
     "total = 99, nothing is lost. git restore . puts the prepared version back on your disk: total = 10, you lose "
     "99. git restore --staged --worktree . puts everything back as in the last commit: total = 0, you lose 10 and "
     "99, with no undo."),
    ("The trap",
     "Files never added with git add (untracked) are not touched by any of the three: git status still lists them. "
     "Delete them by hand, or git clean -n to list them and git clean -f to delete them."),
    ("Link to « Checkpoint Commits »",
     "The checkpoint pattern uses the last row: commit first, let the agent work, and if you are not happy, "
     "git restore --staged --worktree . brings the checkpoint back."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git restore --staged .",
     "--staged = the prepared version (staging area, « index ») takes the content of the last commit. The dot = "
     "this folder and everything below. Your files on disk are not changed: the opposite of git add ."),
    ("Command — git restore .",
     "Without option, git restore acts on the files on disk (--worktree is the default) and takes their content "
     "from the prepared version. Changes made since the last git add are lost."),
    ("Command — git restore --staged --worktree .",
     "Both: the prepared version and the files on disk take the content of the last commit. Every change since the "
     "last commit is lost, prepared or not. No undo."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "What git restore Brings Back", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — What git restore Brings Back", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(110):
            st_write(bs.sub, "Same file app.ts: on disk total = 99, prepared total = 10, last commit total = 0",
                     tag=t.div)
        st_space("v", "2vh")
        cols = "36% 14% 14% 14% 22%"
        header = s.project.containers.table_header_cell
        with st_zoom(_TABLE_ZOOM):
            with st_grid(cols=cols, gap="0.8vh 0.4vw", cell_styles=header) as g:
                for label, tone in [("", None), ("📂 On disk", _BLUE), ("📋 Prepared", _AMBER),
                                    ("💾 Commit", _GREEN), ("You lose", _RED)]:
                    with g.cell():
                        st_write(tone.title if tone else bs.tl, label)
            cells = s.project.containers.rows(len(_ROWS), cols, filled=(1, 2, 3, 4, 5))
            with st_grid(cols=cols, gap="1.6vh 0.4vw", cell_styles=cells) as g:
                for i, (first, disk, prep, last, lost) in enumerate(_ROWS):
                    with g.cell():
                        st_write(bs.tl if i == 0 else bs.cmd, first)
                    for value in (disk, prep, last):
                        with g.cell():
                            st_write(bs.val, value)
                    with g.cell():
                        st_write(bs.val + (_RED.fg if lost.startswith("total") else s.none), lost)
        st_space("v", "3vh")
        with st_zoom(95):
            st_write(bs.td, (bs.keyword, "--staged"), " acts on what you prepared with git add; ",
                     (bs.keyword, "--worktree"), " acts on the file you see in the editor.", tag=t.div)
            st_space("v", "1vh")
            st_write(bs.td + s.project.colors.muted,
                     "Files never added with git add are touched by none of them.", tag=t.div)
