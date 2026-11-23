"""Slide — How much AI-generated code? + Do you review it? Interactive questions."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

# Page fill container
_page_fill = s.project.containers.page_fill_center

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

_NOTES_USAGE = [
    ("Trainer action",
     "Learners do it — show of hands, in the room. Everyone places themselves on the 0–100 % line of the next slide; read two or three answers aloud."),
    ("The question",
     "An opening poll, by show of hands or on the 0–100 % line of the next slide: how much of the code you wrote "
     "last month came from an AI?"),
    ("How to run it",
     "Ask people to place themselves on the line (0 % … 100 %), note two or three answers aloud. No right answer: "
     "the point is to see the spread in the room."),
    ("Keep it for later",
     "« Your answer today will change by the end of this training. » Come back to it at the end of the week."),
]

_NOTES_REVIEW = [
    ("Trainer action",
     "Learners do it — show of hands, in the room. Everyone places themselves between « Never review » and « Always review » on the next slide; ask one person from each end why."),
    ("The question",
     "Second poll: when an AI gives you code, do you read it before you use it? Never, sometimes, always?"),
    ("Why it matters",
     "This is the line that separates VibeCoding (accept without closely reviewing) from VibeEngineering "
     "(human review at the boundaries). The whole session is about where you stand on it."),
    ("How to run it",
     "Same gesture: people place themselves between « Never review » and « Always review ». Ask one person from "
     "each end why."),
]


def _header(title, notes, lvl, style):
    """Title and « i » on the same line (NG, 2026-11-23)."""
    with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
        with h.cell():
            st_write(style, title, tag=t.div, toc_lvl=lvl)
        with h.cell():
            st_hover_tooltip(title=f"Trainer notes — {title}", entries=notes, position="left", width="50vw")


def build():
    # Sub-slide 1: Billboard question — AI usage
    with st_block(_page_fill):
        with st_zoom(60):
            _header("How Much of Your Code Is AI-Generated?", _NOTES_USAGE, "1", bs.question)
    st_space("v", "30vh")
    st_slide_break()

    # Sub-slide 2: AI usage spectrum
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(150):
                st_write(bs.heading, "Your AI Usage Today", tag=t.div, toc_lvl="2")
                st_space("v", 2)

                with st_block(_spectrum_bar_1):
                    st_write(
                        bs.body,
                        (bs.spectrum_left_blue, "0%"),
                        (bs.body, "  \u2194  "),
                        (bs.spectrum_right, "100%"),
                    )

            st_space("v", 3)
            with st_zoom(150):
                st_write(
                    bs.explanation,
                    "Your answer today will change by the end of this training.",
                )
    st_space("v", "30vh")
    st_slide_break()

    # Sub-slide 3: Billboard question — review habits
    with st_block(_page_fill):
        with st_zoom(65):
            _header("Do You Review AI-Generated Code?", _NOTES_REVIEW, "2", bs.question)
    st_space("v", "30vh")
    st_slide_break()

    # Sub-slide 4: Review spectrum
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(140):
                st_write(bs.heading, "The Review Spectrum", tag=t.div, toc_lvl="2")
                st_space("v", 2)

                with st_block(_spectrum_bar_2):
                    st_write(
                        bs.body,
                        (bs.spectrum_left, "Never review"),
                        (bs.body, "  \u2194  "),
                        (bs.spectrum_right, "Always review"),
                    )

            st_space("v", 3)
            with st_zoom(150):
                st_write(
                    bs.explanation,
                    "This spectrum defines your relationship with AI-generated code.",
                )
