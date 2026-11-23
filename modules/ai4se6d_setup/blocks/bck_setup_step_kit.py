"""Slide — Installation step 4: install the course kit (tutor, syllabus, GSE-One docs, default model)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Installation step slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    step = Style.create(s.project.titles.caption + s.center_txt, "setup_step_caption")
    body = s.project.titles.body
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 130  # st_code font_size is not applied by Pygments: zoom instead
# One command, split with "\" so no line wraps on screen.
_KIT = (
    "git clone https://github.com/nicolasguelfi/ai4se-kit ~/ai4se/ai4se-kit \\\n"
    "  && sh ~/ai4se/ai4se-kit/setup-learner.sh"
)

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Step 4 of the installation: everyone pastes the clone + "
     "setup-learner.sh command; it must end with no red line (mid-point 13:50: step 4 or beyond)."),
    ("The message",
     "One command installs the course kit in ~/ai4se: it clones the ai4se-kit repository and runs "
     "setup-learner.sh."),
    ("What you get",
     "tutor — an AI helper prepared by the trainer (step 8); the course syllabus and the GSE-One v0.93.2 docs; "
     "the default model for the workshops."),
    ("Your key stays yours",
     "The kit sets a default model, never your key: the key was connected in step 3."),
    ("Another folder",
     "The kit can live elsewhere: its folder then replaces ~/ai4se in every command. Never in a synchronised "
     "folder (Dropbox, iCloud, OneDrive)."),
    ("The check",
     "The script ends with « Done. Next steps: ». Then open a second terminal: it becomes your tutor window."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 4 of 8 · ~5 min", tag=t.div)
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "4 · The Course Kit", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — 4 · The Course Kit", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_KIT, language="bash", line_numbers=False)
        st_space("v", "1vh")
        with st_zoom(90):
            st_write(bs.body, (bs.label, "It installs, in "), (bs.cmd, "~/ai4se"), (bs.label, ":"))
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered,
                         text_align="left", item_gap=0.6) as l:
                with l.item():
                    st_write(bs.body, (bs.cmd, "tutor"), " — an AI helper prepared by the trainer (step 8)")
                with l.item():
                    st_write(bs.body, "the course syllabus and the GSE-One v0.93.2 docs")
                with l.item():
                    st_write(bs.body, "the default model for the workshops (never your key)")
            # Kit 2026-11-22.4: the folder holding the kit is the course folder (ss2-ul-gse, NG).
        st_space("v", "1vh")
        with st_zoom(80):
            st_write(
                bs.body, (bs.label, "Another folder? "), "Clone the kit elsewhere: its folder replaces ",
                (bs.cmd, "~/ai4se"), " in every command. Never in Dropbox / iCloud / OneDrive.",
            )
        st_space("v", "1vh")
        with st_zoom(90):
            with st_block(bs.done_box):
                st_write(
                    bs.body, (bs.done_label, "Done when: "), "it ends with ", (bs.cmd, "Done. Next steps:"),
                    " — then open a second terminal, your tutor window.",
                )
