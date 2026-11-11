"""Slide — What your tutor sees: its folders, the course material, never your secrets; read-only."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


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


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "What Your Tutor Sees", tag=t.div, toc_lvl="1")
        with st_zoom(75):
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(bs.body, (bs.sees, "Sees: "), "the folders in ", (bs.cmd, "~/.config/ai4se/tutor-paths"))
                with l.item():
                    st_write(bs.body, (bs.label, "Default: "), (bs.cmd, "~/ai4se"), " — all the course repos")
                with l.item():
                    st_write(bs.body, (bs.label, "Add: "), (bs.cmd, "~/ai4se/ai4se-kit/tutor add ~/work/repo"))
                with l.item():
                    st_write(bs.body, (bs.sees, "Sees: "), "the course syllabus and the GSE-One v0.90.1 docs")
                with l.item():
                    st_write(bs.body, (bs.never, "Never: "), "your secrets — ", (bs.cmd, ".env"),
                             ", keys, ", (bs.cmd, "~/.ssh"), ", opencode credentials")
                with l.item():
                    st_write(bs.body, (bs.label, "Read-only: "), "it never changes your files")
                with l.item():
                    st_write(bs.body, (bs.label, "Cites its sources: "), "a syllabus sheet or a GSE-One section")
        st_space("v", 1)
        st_write(bs.caption, "An AI prepared by the trainer — not the trainer. It can be wrong.", tag=t.div)
