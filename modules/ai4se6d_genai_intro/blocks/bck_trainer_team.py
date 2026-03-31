"""Slide 2 — Your Trainers."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s


# P1: viewport-filling container — content distributed vertically
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:2rem;",
    "trainers_page_fill",
)

# Larger photo circle to fill more space (P1 + P3)
_photo_circle = ns(
    "width: 260px; height: 260px; border-radius: 50%; "
    "background: linear-gradient(135deg, #7AB8F5 0%, #2EC4B6 100%); "
    "margin: 0 auto;",
    "photo_circle",
)


class BlockStyles:
    """Slide: Trainers — maximize-viewport archetype: balanced (2 columns)."""
    heading = s.project.titles.section_title + s.center_txt
    name = Style.create(
        s.project.colors.primary + s.bold + s.huge,
        "trainer_name",
    )
    role = Style.create(
        s.project.titles.body,
        "trainer_role",
    )
    email = Style.create(
        s.project.colors.accent + s.Large,
        "trainer_email",
    )
    photo_placeholder = Style.create(
        _photo_circle + s.container.layouts.center,
        "trainer_photo_placeholder",
    )
bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Your Trainers", tag=t.div, toc_lvl="1")

            with st_grid(
                cols=s.project.containers.responsive_2col,
                grid_style=s.project.containers.gap_32,
            ):
                # Trainer 1 — Nicolas Guelfi
                with st_block(s.center_txt):
                    with st_block(bs.photo_placeholder):
                        st_write(s.giant + s.center_txt + s.project.colors.primary, "NG")
                    st_space("v", 1)
                    st_write(bs.name, "Dr. Prof. Nicolas Guelfi")
                    st_space("v", 0.5)
                    st_write(bs.role, "Universite du Luxembourg")
                    st_write(bs.email, "nicolas.guelfi@ros.lu", link="mailto:nicolas.guelfi@ros.lu")

                # Trainer 2 — Tiago Sousa
                with st_block(s.center_txt):
                    with st_block(bs.photo_placeholder):
                        st_write(s.giant + s.center_txt + s.project.colors.primary, "TS")
                    st_space("v", 1)
                    st_write(bs.name, "Tiago Sousa")
                    st_space("v", 0.5)
                    st_write(bs.role, "ROS")
                    st_write(bs.email, "tiago.sousa@ros.lu", link="mailto:tiago.sousa@ros.lu")
