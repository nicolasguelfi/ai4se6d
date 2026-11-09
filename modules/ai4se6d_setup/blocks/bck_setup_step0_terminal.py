"""Slide — Installation step 0: open a terminal (macOS, Linux, Windows via WSL or the VM)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Installation step slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    step = Style.create(s.project.titles.caption + s.center_txt, "setup_step_caption")
    body = s.project.titles.body
    label = s.project.titles.label
    os_name = Style.create(s.project.titles.table_header + s.center_txt, "setup_os_name")
    os_text = Style.create(s.project.titles.table_cell + s.center_txt, "setup_os_text")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 190  # st_code font_size is not applied by Pygments: zoom instead
_OS = [
    ("macOS", "Cmd + Space → type Terminal → Enter"),
    ("Linux", "Ctrl + Alt + T"),
    ("Windows", "Ubuntu (WSL) app or the VM (see your VM access sheet). Not PowerShell."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 0 of 7 · ~5 min", tag=t.div)
        st_write(bs.heading, "0 · Open a Terminal", tag=t.div, toc_lvl="1")
        with st_grid(
            cols="repeat(auto-fit, minmax(300px, 1fr))",
            gap="16px",
            cell_styles=s.project.containers.table_normal_cell,
        ) as g:
            for name, how in _OS:
                with g.cell():
                    st_write(bs.os_name, name, tag=t.div)
                    st_write(bs.os_text, how, tag=t.div)
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code="echo $SHELL      # then type this", language="bash", line_numbers=False)
        with st_zoom(85), st_block(bs.done_box):
            st_write(bs.body, (bs.done_label, "Done when: "), "it ends in ", (bs.cmd, "bash"), " or ", (bs.cmd, "zsh"), ".")
