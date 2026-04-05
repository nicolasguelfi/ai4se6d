"""Slide — Paradigm shift: from cook to customer (kitchen metaphor seeding)."""
# @guideline: maximize-viewport
from streamtex import *
<<<<<<< HEAD
from streamtex.styles import Style as ns
=======
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

<<<<<<< HEAD

# Viewport-filling containers
_page_fill = s.project.containers.page_fill_top

# Override: vertically centered but NOT horizontally centered (no align-items:center),
# with wider gap — intentional for paradigm shift layout.
_page_fill_center = ns(
    "display:flex;flex-direction:column;justify-content:center;"
    "min-height:85vh;gap:2rem;",
    "page_fill_vc_paradigm_center",
)

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "vc_paradigm_cell",
)

=======
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
# Table cell for Changes/Stays
_table_cell = Style.create(
    s.project.containers.cell_primary_bg
    + s.project.containers.cell_pad_md
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "vc_paradigm_table_cell",
)

<<<<<<< HEAD

=======
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
class BlockStyles:
    """Paradigm shift slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    emphasis = Style.create(
        s.Large + s.italic + s.project.colors.highlight + s.center_txt,
        "vc_paradigm_emphasis",
    )
bs = BlockStyles

<<<<<<< HEAD

=======
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
_PROMPT = (
    f"{_PREFIX} Split composition: left side shows a figure cooking at a stove, "
    "hands busy, surrounded by ingredients in teal tones. Right side shows a figure "
    "seated at an elegant restaurant table, a beautifully plated dish arriving, "
    "in electric blue and amber tones. A bold geometric arrow connects left to right. "
    f"Symbolizes the shift from doing the work to delegating it. {_SUFFIX}"
)

<<<<<<< HEAD

def build():
    # Sub-slide 1: From Cook to Customer
    with st_block(_page_fill):
=======
def build():
    # Sub-slide 1: From Cook to Customer
    with st_block(s.project.containers.page_fill_top):
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
        with st_block(s.center_txt):
            st_write(bs.heading, "From Cook to Customer", tag=t.div, toc_lvl="1")

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
                        name="vc_paradigm",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(
                        bs.body,
                        (bs.keyword, "Traditional SE: "),
                        "You are the cook \u2014 you choose ingredients, "
                        "follow the recipe, control every step.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (bs.keyword_accent, "VibeCoding: "),
                        "You become the customer \u2014 you describe what you want, "
                        "the kitchen prepares it, you taste the result.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "The implementation stays behind the kitchen door.",
                    )

    st_slide_break()

    # Sub-slide 2: What Changes, What Stays
<<<<<<< HEAD
    with st_zoom(130),st_block(_page_fill_center):
=======
    with st_zoom(130),st_block(s.project.containers.page_fill_center_noalign):
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
        with st_block(s.center_txt):
            st_write(bs.subheading, "What Changes, What Stays", tag=t.div, toc_lvl="2")
            st_space("v", 3)

            with st_grid(
                cols="1fr 3fr",
                gap="12px",
                cell_styles=_table_cell,
            ) as g:
                with g.cell():
                    #st_write(bs.body, (bs.keyword, "Changes:"))
                    st_write(bs.body+bs.keyword, "Changes: ")
                with g.cell():
                    st_write(bs.body, "you stop writing every line.<br>You express intent.")
                with g.cell():
                    st_write(bs.body+bs.keyword_accent, "Stays:")
                with g.cell():
                    st_write(bs.body, "you\u2019re still responsible for the result.")
            st_space("v", 2)
            st_write(
                bs.emphasis,
                "A customer who gets food poisoning doesn\u2019t blame themselves "
                "\u2014 but a professional who serves it does.",
            )
