"""Slide — Installation step 6: run check-learner.sh until everything is green."""
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
    critical = Style.create(s.bold + s.project.colors.critical, "setup_critical")
    green = Style.create(s.bold + s.project.colors.success, "setup_green")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 190  # st_code font_size is not applied by Pygments: zoom instead
_CHECK = "curl -fsSL https://raw.githubusercontent.com/nicolasguelfi/ai4se-kit/main/check-learner.sh | sh"


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 6 of 7 · ~10 min", tag=t.div)
        st_write(bs.heading, "6 · Check Everything", tag=t.div, toc_lvl="1")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_CHECK, language="bash", line_numbers=False)
        with st_zoom(85):
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(bs.body, (bs.critical, "Red line? "), "Redo that step, run the check again.")
                with l.item():
                    st_write(bs.body, (bs.green, "All green? "), "Show your neighbour.")
            with st_block(bs.done_box):
                st_write(bs.body, (bs.done_label, "Done when: "), "every line is green.")
