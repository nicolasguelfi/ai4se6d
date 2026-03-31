"""Trainer profile — Tiago Sousa (imported from HTML)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "trainer_ts_page_fill",
)

# Shared image path
_IMG = "_SHARED/bck_trainer_ts"

# Cell style for the profile grid (table-roadmap pattern)
_cell = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "trainer_ts_cell",
)


class BlockStyles:
    """Trainer profile — Tiago Sousa."""
    heading = s.project.titles.section_title + s.center_txt
    name = Style.create(
        s.project.colors.primary + s.bold + s.huge + s.center_txt,
        "trainer_ts_name",
    )
    role = Style.create(
        s.project.titles.body + s.center_txt,
        "trainer_ts_role",
    )
    category_title = Style.create(
        s.project.colors.highlight + s.bold + s.Large + s.text.wrap.hyphens,
        "trainer_ts_cat_title",
    )
    category_item = Style.create(
        s.Large + s.text.wrap.hyphens,
        "trainer_ts_cat_item",
    )
    link_label = Style.create(
        s.project.colors.accent + s.Large + s.center_txt,
        "trainer_ts_link",
    )
bs = BlockStyles


def build():
    # -- Slide 1: Title + Photo + Name --
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Who? — Tiago", tag=t.div, toc_lvl="1")
            st_space("v", "10vh")

            st_image(s.none, uri=f"{_IMG}/image1.png", width="400px", height="400px")

            st_write(bs.name, "Tiago Sousa")
            st_write(bs.role, "Right-On-Skill")

    st_slide_break()

    # -- Slide 2: Profile grid --
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Profile", tag=t.div, toc_lvl="2")

            # Row 1: Expertise Domains
            with st_grid(
                cols="repeat(auto-fit, minmax(350px, 1fr))",
                gap="12px",
                cell_styles=_cell,
            ) as g:
                with g.cell():
                    st_write(bs.category_title, "Software Engineering")
                with g.cell():
                    st_write(bs.category_title, "Artificial Intelligence")
                with g.cell():
                    st_write(bs.category_title, "Sustainability")

            st_space("v", 0.5)

            # Row 2: Context + Logos
            with st_grid(
                cols="repeat(auto-fit, minmax(350px, 1fr))",
                gap="12px",
                cell_styles=_cell,
            ) as g:
                with g.cell():
                    st_write(bs.category_title, "Context")
                    st_space("v", 0.5)
                    st_write(bs.category_item, "Right-On-Skill sarl")
                    with st_grid(cols="repeat(auto-fit, minmax(60px, 1fr))", gap="8px") as lg:
                        with lg.cell():
                            st_image(s.none, uri=f"{_IMG}/image2.png", width="5vw")
                        with lg.cell():
                            st_image(s.none, uri=f"{_IMG}/image3.png", width="5vw")
                        with lg.cell():
                            st_image(s.none, uri=f"{_IMG}/image4.png", width="5vw")

    st_slide_break()

    # -- Slide 3: More information + LinkedIn --
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "More Information", tag=t.div)
            st_image(s.none, uri=f"{_IMG}/image5.png", width="200px")
            st_write(bs.link_label, "Connect on LinkedIn")
