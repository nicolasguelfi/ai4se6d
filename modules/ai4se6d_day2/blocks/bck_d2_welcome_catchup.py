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
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_catchup_cmd")
bs = BlockStyles

_RECOVER = """\
git clone https://github.com/nicolasguelfi/calcapp-starter ~/ai4se/calcapp-restart
cd ~/ai4se/calcapp-restart && git checkout -b mywork <tag> && npm ci"""

_TAGS = [
    ("j2-start", "start of the day (09:15)"),
    ("j2-part1", "end of the morning build (13:15)"),
    ("j2-v0.1", "v0.1 ready for delivery (16:15)"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Late or Lost? Catch Up", tag=t.div, toc_lvl="+1")
        st_write(
            bs.td, (bs.tl, "Ask: "),
            "1. your tutor window  →  2. a recovery tag  →  3. raise your hand", tag=t.div,
        )
        st_write(
            bs.td, (bs.cmd, "~/ai4se/ai4se-kit/tutor update"), " — get today's course notes", tag=t.div,
        )
        st_code(s.none, code=_RECOVER, language="bash", line_numbers=False, font_size="24pt")
        with st_grid(cols="auto 1fr", gap="6px 32px") as g:
            for tag, when in _TAGS:
                with g.cell():
                    st_write(bs.tl, tag)
                with g.cell():
                    st_write(bs.td, when)
        st_write(bs.td + s.project.colors.muted, "No ~/ai4se/calcapp yet? Clone there instead. Otherwise your work in it stays safe.", tag=t.div)
