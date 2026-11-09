"""Slide — Installation step 2: connect your model key with opencode auth login."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Installation step slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    step = Style.create(s.project.titles.caption + s.center_txt, "setup_step_caption")
    body = s.project.titles.body
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    critical = Style.create(s.bold + s.project.colors.critical, "setup_critical")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 220  # st_code font_size is not applied by Pygments: zoom instead


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 2 of 7 · ~10 min", tag=t.div)
        st_write(bs.heading, "2 · Your Model Key", tag=t.div, toc_lvl="1")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code="opencode auth login", language="bash", line_numbers=False)
        with st_zoom(85):
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(bs.body, "Choose the ", (bs.label, "provider on your key sheet"))
                with l.item():
                    st_write(bs.body, "Paste your key when asked")
            st_write(bs.body, (bs.critical, "Never"), " in a committed file, a prompt, a screenshot, an issue.")
            with st_block(bs.done_box):
                st_write(bs.body, (bs.done_label, "Done when: "), (bs.cmd, "opencode auth list"), " shows it.")
