"""Slide — Late or lost? Recovery tags of the CalcApp starter."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Catch-up slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label
bs = BlockStyles

_RECOVER = """\
git clone https://github.com/nicolasguelfi/calcapp-starter calcapp
cd calcapp && git checkout -b mywork <tag> && npm ci"""

_TAGS = [
    ("j2-start", "start of the day (09:15)"),
    ("j2-part1", "end of the morning build (13:15)"),
    ("j2-v0.1", "v0.1 ready for delivery (16:15)"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Late or Lost? Catch Up", tag=t.div, toc_lvl="+1")
        st_space("v", 0.5)
        st_write(
            bs.body, (bs.label, "Ask in this order: "),
            "1. @tutor  →  2. a recovery tag  →  3. raise your hand", tag=t.div,
        )
        st_code(s.none, code=_RECOVER, language="bash", line_numbers=False, font_size="24pt")
        with st_grid(cols="auto 1fr", gap="6px 32px") as g:
            for tag, when in _TAGS:
                with g.cell():
                    st_write(bs.tl, tag)
                with g.cell():
                    st_write(bs.td, when)
        st_write(bs.td + s.project.colors.muted, "Folder calcapp already exists? Clone into calcapp2: your work stays safe.", tag=t.div)
