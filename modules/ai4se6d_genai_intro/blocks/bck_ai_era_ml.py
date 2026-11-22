"""Slide — 1990s Machine Learning: balanced image + key points."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip


_page_fill = s.project.containers.page_fill_top

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "ai_era_ml_cell",
)


class BlockStyles:
    """Slide: Machine Learning — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "ai_era_ml_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "ai_era_ml_keyword",
    )
    keyword_orange = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.text.wrap.hyphens,
        "ai_era_ml_keyword_orange",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A scatter plot of data points in teal, with a smooth electric blue curve "
    "fitting through them. A few amber outlier points. Clean axes without labels. "
    f"Represents learning patterns from data. {_SUFFIX}"
)


# Trainer notes behind the "i" (NG, 2026-11-22): the "Limitation" bullet in detail.
_NOTES = [
    ("Manual feature engineering",
     "Classical methods (logistic regression, SVMs, decision trees, random forests) do not see raw pixels, "
     "sound or text. A human first turns the raw data into a fixed list of measured features: edges or "
     "SIFT/HOG descriptors for images, word counts and n-grams for text, MFCC coefficients for speech."),
    ("Why it limits",
     "The model can only be as good as the features someone thought of. Designing them takes domain "
     "experts weeks or months, and they rarely transfer: features built for spam filtering are useless "
     "for medical images."),
    ("Neural networks already existed",
     "Backpropagation was popularised in 1986 and LeCun's LeNet read handwritten digits around 1989-1998. "
     "Neural networks can learn their own features, but only with many layers, lots of data and lots "
     "of computation."),
    ("Why they could not scale",
     "In the 1990s training ran on CPUs, labelled datasets were small, and deep networks were slow and "
     "unstable to train (vanishing gradients). So shallow, hand-fed classical methods usually won."),
    ("What changed next",
     "Around 2010: GPUs, very large datasets such as ImageNet (2009) and better training techniques. In 2012 "
     "AlexNet learned its features from raw pixels and beat hand-crafted ones by a wide margin: the deep "
     "learning era of the next slide."),
    ("Ask the room",
     "\"Who has written rules or regexes to pre-process data before a model?\" That was feature engineering."),
]


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_grid(cols="92% 8%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell():
                    st_write(bs.heading, "1990s — Machine Learning", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — the limitation in detail", entries=_NOTES,
                                     position="left", width="45vw")
            st_space("v", 1.5)

            with st_grid(
                cols="1.5fr 3.5fr",
                gap="24px",
                cell_styles=_cell,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ai_era_ml",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(120):
                        with st_list(
                            list_type=lt.unordered,
                            li_style=bs.body,
                            item_gap=0.6,  # 0.6 em between items — streamtex st_list(item_gap=), 0.7.85 (NG, 2026-11-22)
                        ) as l:
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Data-driven"),
                                    (bs.body, " — Algorithms learn from examples, not rules"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Paradigms"),
                                    (bs.body, " — Supervised, unsupervised, reinforcement"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Limitation"),
                                    (bs.body, " — Classical methods need "),
                                    (bs.keyword_orange, "manual feature engineering"),
                                    (bs.body, "; neural networks lack compute to scale"),
                                )
