"""Slide — P5: Human Review at Boundaries."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

<<<<<<< HEAD

_page_fill = s.project.containers.page_fill_top

_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "ve_p5_cell",
)


=======
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
class BlockStyles:
    """P5 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p5_number",
    )
bs = BlockStyles

<<<<<<< HEAD

=======
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
_PROMPT = (
    f"{_PREFIX} A flow of automated process in electric blue passing through "
    "human-shaped gate checkpoints in amber. Magnifying glass at each gate. "
    f"{_SUFFIX}"
)

<<<<<<< HEAD

def build():
    with st_block(_page_fill):
=======
def build():
    with st_block(s.project.containers.page_fill_top):
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
        with st_block(s.center_txt):
            st_write(bs.heading, "P5 — Human Review at Boundaries", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
<<<<<<< HEAD
                cell_styles=_cell,
=======
                cell_styles=s.project.containers.grid_cell_centered,
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ve_p5_review",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with st_zoom(130), g.cell():
                    st_write(bs.number, "5")
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "Review ",
                        (bs.keyword, "architectural decisions"),
                        ", ",
                        (bs.keyword, "security-critical code"),
                        ", and ",
                        (bs.keyword, "integration points"),
                        ".",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (s.project.colors.muted, "HACCP — control at critical points, "
                         "not on every gesture."),
                    )
