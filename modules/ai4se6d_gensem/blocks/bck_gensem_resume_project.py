"""Slide — Welcome of day 5: refresh the kit, reopen the mini-project, /gse-resume (edition 2)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Resume styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "resume_project_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "resume_project_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "resume_project_foot")
bs = BlockStyles

_START = (
    "~/ai4se/ai4se-kit/tutor update     # in the tutor window\n"
    "PROJECT=~/ai4se/my-project         # your project's folder\n"
    'cd "$PROJECT"\n'
    "opencode\n"
    "/gse-resume                        # in opencode"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(72):
            st_write(bs.heading, "Back to Your Project", tag=t.div, toc_lvl="+1", label="Welcome — resume the mini-project")
            st_write(bs.body, "Yesterday you framed it and started it in Lightweight mode. Pick it up where you stopped.",
                     tag=t.div)
            with st_zoom(130):
                st_code(s.none, code=_START, language="bash", line_numbers=False)
            st_write(bs.body, "Project outside ", (bs.cmd, "~/ai4se"), "? Once: ",
                     (bs.cmd, "~/ai4se/ai4se-kit/tutor add ~/path/to/your-project"), " — so your tutor window can read it.", tag=t.div)
            st_write(bs.foot, "/gse-resume should say: Lightweight mode, card validated, next step the plan.", tag=t.div)
