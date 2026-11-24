"""Slide — Late or lost? Recovery tags of the CalcApp starter."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Catch-up slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "catchup_cmd")
bs = BlockStyles

_CODE_ZOOM = 110  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)

_RECOVER = """\
git clone https://github.com/nicolasguelfi/calcapp-starter ~/ai4se/calcapp-restart   # clones into ~/ai4se, from any folder
TAG=j2-start               # the tag your half-day sheet names
cd ~/ai4se/calcapp-restart && git checkout -b mywork "$TAG" && npm ci"""

_TAGS = [
    ("j2-start", "start of the day (09:15)"),
    ("j2-part1", "end of the morning build (13:15)"),
    ("j2-v0.1", "v0.1 ready for delivery (16:15)"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type now. The clone-from-a-tag commands are for whoever falls behind later; "
     "nobody runs them unless lost."),
    ("The message",
     "Nobody stays behind for the whole day: the CalcApp starter has a recovery tag at each checkpoint."),
    ("Who to ask, in order",
     "1. the tutor window, 2. a recovery tag, 3. raise your hand. Running ~/ai4se/ai4se-kit/tutor update first "
     "gets today's course notes."),
    ("How a tag works",
     "Clone the starter into ~/ai4se/calcapp-restart, then git checkout -b mywork \"$TAG\" (TAG set to the tag your sheet names, e.g. j2-start) and npm ci: you continue "
     "from that point on your own branch."),
    ("The three tags",
     "j2-start (09:15, start of the day), j2-part1 (13:15, end of the morning build), j2-v0.1 (16:15, v0.1 ready "
     "for delivery)."),
    ("Reassure",
     "Cloning in a new folder leaves the work in ~/ai4se/calcapp safe. No ~/ai4se/calcapp yet? Clone there instead."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — ~/ai4se/ai4se-kit/tutor update",
     "Runs the course kit's tutor script with « update »: it downloads the latest version of the kit (course notes, "
     "sheets) with git pull, then checks GSE-One. Close and reopen the tutor window afterwards."),
    ("Command — git clone (address) (folder)",
     "git clone copies a project from GitHub onto your machine, with its whole history and its tags. First argument: "
     "the address of the project (here the CalcApp starter). Second argument: the folder to create "
     "(~/ai4se/calcapp-restart); it must not exist yet. Because the folder is given in full, the command works from "
     "any folder. Without it, git would create « calcapp-starter » in the current folder."),
    ("Command — TAG=j2-start",
     "Not a git command: it stores the text « j2-start » in a variable named TAG, for this terminal only (until you "
     "close it). Later, \"$TAG\" is replaced by that text; the quotes keep it as one word. Your half-day sheet tells "
     "you which tag to use."),
    ("Command — cd ~/ai4se/calcapp-restart",
     "cd = change directory: the terminal now works inside that folder. ~ is your home folder (/home/student in the "
     "course VM)."),
    ("Symbol — &&",
     "Runs the next command only if the previous one succeeded. If cd fails, nothing else runs."),
    ("Command — git checkout -b mywork \"$TAG\"",
     "A tag is a fixed label on one commit (a checkpoint of the course). git checkout -b mywork \"$TAG\" creates a "
     "new branch named mywork that starts at that commit, and switches to it: -b = create the branch, mywork = its "
     "name, \"$TAG\" = where it starts. Newer equivalent: git switch -c mywork \"$TAG\"."),
    ("Command — npm ci",
     "Installs the project's libraries (into node_modules/) exactly at the versions written in package-lock.json. "
     "ci = « clean install »: it first deletes any old node_modules, so everybody gets the same setup. Needed once per "
     "fresh clone, before npm run test:run or npm run dev."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Late or Lost? Catch Up", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Late or Lost? Catch Up", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(117):
            st_write(
                bs.td, (bs.tl, "Ask: "),
                "1. your tutor window  →  2. a recovery tag  →  3. raise your hand", tag=t.div,
            )
            st_write(
                bs.td, (bs.cmd, "~/ai4se/ai4se-kit/tutor update"), " — get today's course notes", tag=t.div,
            )
            st_space("v", "2vh")
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_RECOVER, language="bash", line_numbers=False, font_size="24pt")

            st_space("v", "2vh")
            # one row per tag, alternating fills — motif L2 + fonds f1 (margins 5 %)
            cols = "5% 22% 68% 5%"
            cells = s.project.containers.rows(len(_TAGS), cols, filled=(2, 3))
            with st_grid(cols=cols, gap="1.2vh 0.4vw", cell_styles=cells) as g:
                for tag, when in _TAGS:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.tl, tag)
                    with g.cell():
                        st_write(bs.td, when)
                    with g.cell():
                        pass  # right margin
            st_space("v", "2vh")
            st_write(bs.td + s.project.colors.muted, "No ~/ai4se/calcapp yet? Clone there instead. Otherwise your work in it stays safe.", tag=t.div)
