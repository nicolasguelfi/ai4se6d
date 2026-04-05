"""Slide — How much AI-generated code? + Do you review it? Interactive questions."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

<<<<<<< HEAD

# Billboard centered container
_page_fill_billboard = s.project.containers.page_fill_center

# Standard top-aligned container
_page_fill = s.project.containers.page_fill_top

=======
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
# Spectrum bar styles
_spectrum_bar_1 = Style(
    "background:linear-gradient(90deg, rgba(122,184,245,0.15) 0%, rgba(46,196,182,0.3) 100%);"
    "border-radius:12px;padding:16px 32px;",
    "ai_usage_spectrum_bar",
)

_spectrum_bar_2 = Style(
    "background:linear-gradient(90deg, rgba(243,156,18,0.3) 0%, rgba(46,196,182,0.3) 100%);"
    "border-radius:12px;padding:16px 32px;",
    "review_spectrum_bar",
)

class BlockStyles:
    """Review habits slide styles."""
    question = Style.create(
        s.Giant + s.bold + s.center_txt + s.project.colors.accent,
        "review_habits_question",
    )
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    spectrum_left = Style.create(
        s.Large + s.bold + s.project.colors.highlight,
        "review_spectrum_left",
    )
    spectrum_right = Style.create(
        s.Large + s.bold + s.project.colors.accent,
        "review_spectrum_right",
    )
    spectrum_left_blue = Style.create(
        s.Large + s.bold + s.project.colors.primary,
        "ai_usage_spectrum_left",
    )
    explanation = Style.create(
        s.Large + s.center_txt,
        "review_explanation",
    )
bs = BlockStyles

def build():
    # Sub-slide 1: Billboard question — AI usage
    with st_block(s.project.containers.page_fill_center):
        st_write(
            bs.question,
            "How Much of Your Code Is AI-Generated?",
            tag=t.div,
            toc_lvl="1",
        )
    st_space("v", "30vh")

    st_slide_break()

    # Sub-slide 2: AI usage spectrum
<<<<<<< HEAD
    with st_zoom(160),st_block(_page_fill):
=======
    with st_zoom(160),st_block(s.project.containers.page_fill_top):
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
        with st_block(s.center_txt):
            st_write(bs.heading, "Your AI Usage Today", tag=t.div, toc_lvl="2")
            st_space("v", 2)

            with st_block(_spectrum_bar_1):
                st_write(
                    bs.body,
                    (bs.spectrum_left_blue, "0%"),
                    (bs.body, "  \u2194  "),
                    (bs.spectrum_right, "100%"),
                )

            st_space("v", 2)
            st_write(
                bs.explanation,
                "Your answer today will change by the end of this training.",
            )

    st_slide_break()

    # Sub-slide 3: Billboard question — review habits
    with st_block(s.project.containers.page_fill_center):
        st_write(
            bs.question,
            "Do You Review AI-Generated Code?",
            tag=t.div,
            toc_lvl="2",
        )

    st_slide_break()

    # Sub-slide 4: Review spectrum
<<<<<<< HEAD
    with  st_zoom(140),st_block(_page_fill):
=======
    with  st_zoom(140),st_block(s.project.containers.page_fill_top):
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
        with st_block(s.center_txt):
            st_write(bs.heading, "The Review Spectrum", tag=t.div)
            st_space("v", 2)

            with st_block(_spectrum_bar_2):
                st_write(
                    bs.body,
                    (bs.spectrum_left, "Never review"),
                    (bs.body, "  \u2194  "),
                    (bs.spectrum_right, "Always review"),
                )

            st_space("v", 2)
            st_write(
                bs.explanation,
                "This spectrum defines your relationship with AI-generated code.",
            )
            