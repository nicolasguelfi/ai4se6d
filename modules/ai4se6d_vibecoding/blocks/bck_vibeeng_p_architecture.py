"""Slide — P3: Architectural Intent."""
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
    "ve_p3_cell",
)


=======
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
class BlockStyles:
    """P3 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    accent = s.bold + s.project.colors.accent
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p3_number",
    )
bs = BlockStyles

<<<<<<< HEAD

=======
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
_PROMPT = (
    f"{_PREFIX} A blueprint wireframe of a building in electric blue with project "
    "rule cards floating nearby in teal. An amber compass indicates direction. "
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
            st_write(bs.heading, "P3 — Architectural Intent", tag=t.div, toc_lvl="1")

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
                        name="ve_p3_architecture",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with st_zoom(130), g.cell():
                    st_write(bs.number, "3")
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (bs.accent, ".cursorrules"),
                        ", ",
                        (bs.accent, "CLAUDE.md"),
                        ", ",
                        (bs.accent, "AGENTS.md"),
                        " constrain AI decisions.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "The architecture is ",
                        (bs.keyword, "declared"),
                        ", not discovered after the fact.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (s.project.colors.muted, "Your recipe book — the kitchen "
                         "follows it."),
                    )
