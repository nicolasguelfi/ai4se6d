"""Slide — Installation step 4: install the course kit (tutor, syllabus, GSE-One docs, default model)."""
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
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 130  # st_code font_size is not applied by Pygments: zoom instead
# One command, split with "\" so no line wraps on screen.
_KIT = (
    "git clone https://github.com/nicolasguelfi/ai4se-kit ~/ai4se/ai4se-kit \\\n"
    "  && sh ~/ai4se/ai4se-kit/setup-learner.sh"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 4 of 8 · ~5 min", tag=t.div)
        st_write(bs.heading, "4 · The Course Kit", tag=t.div, toc_lvl="1")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_KIT, language="bash", line_numbers=False)
        with st_zoom(85):
            st_write(bs.body, (bs.label, "It installs, in "), (bs.cmd, "~/ai4se"), (bs.label, ":"))
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(bs.body, (bs.cmd, "tutor"), " — an AI helper prepared by the trainer (step 8)")
                with l.item():
                    st_write(bs.body, "the course syllabus and the GSE-One v0.90.1 docs")
                with l.item():
                    st_write(bs.body, "the default model for the workshops (never your key)")
            with st_block(bs.done_box):
                st_write(bs.body, (bs.done_label, "Done when: "), "it ends with “Next: open your tutor window”.")
