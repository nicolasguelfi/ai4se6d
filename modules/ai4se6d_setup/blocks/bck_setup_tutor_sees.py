"""Slide — What your tutor sees: its folders, the course material, never your secrets; read-only."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Tutor scope slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    sees = Style.create(s.bold + s.project.colors.success, "setup_tsees_yes")
    never = Style.create(s.bold + s.project.colors.critical, "setup_tsees_no")
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_tsees_caption")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Explain what the tutor window can and cannot read, right after "
     "learners opened it in step 8."),
    ("The message",
     "The tutor sees the course, not your secrets — and it only reads."),
    ("Its folders",
     "The list is in ~/.config/ai4se/tutor-paths. Default: ~/ai4se, all the course repos. Add a folder of yours "
     "with « tutor add »."),
    ("Its material",
     "The course syllabus and the GSE-One v0.93.3 docs: it cites a syllabus sheet or a GSE-One section."),
    ("Never",
     "Your secrets: .env files, keys, ~/.ssh, the opencode credentials."),
    ("Read-only",
     "It never changes your files: to change code, you work in your own opencode session."),
    ("Ask the room",
     "« It cites its sources: what do you do when the source does not say what the tutor says? » — it can be wrong."),
]

# (label, label style, text parts) — one row each, alternating fills (NG, 2026-11-23)
_ROWS = [
    ("Sees:", bs.sees, ("the folders in ", (bs.cmd, "~/.config/ai4se/tutor-paths"))),
    ("Default:", bs.label, ((bs.cmd, "~/ai4se"), " — all the course repos")),
    ("Add:", bs.label, ((bs.cmd, "~/ai4se/ai4se-kit/tutor add ~/work/repo"),)),
    ("Sees:", bs.sees, ("the course syllabus and the GSE-One v0.93.3 docs",)),
    ("Never:", bs.never, ("your secrets — ", (bs.cmd, ".env"), ", keys, ", (bs.cmd, "~/.ssh"),
                          ", opencode credentials")),
    ("Read-only:", bs.label, ("it never changes your files",)),
    ("Cites its sources:", bs.label, ("a syllabus sheet or a GSE-One section",)),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "What Your Tutor Sees", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — What Your Tutor Sees", entries=_NOTES,
                                 position="left", width="50vw")
        cols = "5% 22% 68% 5%"
        cells = s.project.containers.rows(len(_ROWS), cols, filled=(2, 3))
        with st_zoom(84), st_grid(cols=cols, gap="1.2vh 0.5vw", cell_styles=cells) as g:
            for label, style, parts in _ROWS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, (style, label), tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "2vh")
        with st_zoom(120):
            st_write(bs.caption, "An AI prepared by the trainer — not the trainer. It can be wrong.", tag=t.div)
