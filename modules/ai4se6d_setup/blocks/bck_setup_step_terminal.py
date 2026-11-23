"""Slide — Installation step 0: open a terminal (macOS, Linux, Windows via WSL or the VM)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Installation step slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    step = Style.create(s.project.titles.caption + s.center_txt, "setup_step_caption")
    body = s.project.titles.body
    label = s.project.titles.label
    os_name = Style.create(s.project.titles.table_header, "setup_os_name_left")
    os_text = Style.create(s.project.titles.table_cell, "setup_os_text_left")
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

_NOTES = [
    ("The message",
     "Everything this afternoon happens in a terminal: every later step is a command to paste there."),
    ("Per system",
     "macOS: Spotlight (Cmd + Space), type Terminal. Linux: Ctrl + Alt + T. Windows: the Ubuntu (WSL) app or the "
     "VM described on your VM access sheet."),
    ("The trap",
     "PowerShell is not a bash shell: the commands of the next steps will not work there."),
    ("The check",
     "echo $SHELL must end in bash or zsh. Anything else: ask your neighbour before going on."),
    ("Ask the room",
     "« Who has never typed a command in a terminal? » — pair them with a neighbour who has."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 0 of 8 · ~5 min", tag=t.div)
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "0 · Open a Terminal", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — 0 · Open a Terminal", entries=_NOTES,
                                 position="left", width="50vw")

        # One row per system, alternating fills, outer 5 % margins (NG, 2026-11-23)
        cols = "5% 20% 70% 5%"
        cells = s.project.containers.rows(len(_OS), cols, filled=(2, 3))
        with st_zoom(130), st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
            for name, how in _OS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.os_name, name, tag=t.div)
                with g.cell():
                    st_write(bs.os_text, how, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "3vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code="echo $SHELL      # then type this", language="bash", line_numbers=False)
        st_space("v", "3vh")
        with st_zoom(120), st_block(bs.done_box):
            st_write(bs.body, (bs.done_label, "Done when: "), "it ends in ", (bs.cmd, "bash"), " or ", (bs.cmd, "zsh"), ".")
