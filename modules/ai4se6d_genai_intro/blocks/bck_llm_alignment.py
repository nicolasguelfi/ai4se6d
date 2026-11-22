"""Slide — Phase 3: Alignment (RLHF): balanced image + key points."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip


_page_fill = s.project.containers.page_fill_top

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "llm_alignment_cell",
)


class BlockStyles:
    """Slide: Alignment (RLHF) — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "llm_alignment_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_alignment_keyword",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} Two paths diverging from a central point: one path curves upward "
    "(preferred, in amber with a subtle thumbs-up shape), the other curves down "
    "(rejected, fading teal). An electric blue compass icon at the center. Represents "
    f"RLHF steering model toward human preferences. {_SUFFIX}"
)


# Trainer notes (NG, 2026-11-22: "tooltip bien explicative pour expliquer la logique et les notions")
_NOTES = [
    ("Why a third phase",
     "After pre-training the model predicts text; after fine-tuning it follows instructions. It can still answer in "
     "a way that is harmful, false or useless. Alignment steers its BEHAVIOUR towards what people want; it adds "
     "almost no knowledge."),
    ("HHH",
     "Helpful: does the task asked. Harmless: refuses dangerous requests. Honest: does not invent, says when it does "
     "not know. The three pull against each other: a model that is only harmless refuses too often, a model that is "
     "only helpful does anything it is asked."),
    ("RLHF, step by step",
     "Reinforcement Learning from Human Feedback. 1) The model writes several answers to the same prompt. 2) People "
     "rank them, best to worst. 3) A reward model learns from these rankings to predict the human score. 4) The LLM "
     "is trained by reinforcement learning to get high scores, with a penalty that keeps it close to the fine-tuned "
     "model (otherwise it drifts and produces odd text that fools the judge)."),
    ("The reward model",
     "A second neural network: a learned judge that gives a score to any answer. People cannot rate the millions of "
     "answers seen during training; they rate a sample, the reward model generalises their taste."),
    ("RLAIF and Constitutional AI",
     "Reinforcement Learning from AI Feedback: the ranking is done by an AI, following a written list of principles "
     "(the « constitution »). In Constitutional AI (Anthropic, Bai et al. 2022), the model criticises and rewrites "
     "its own answers against the principles, then an AI judge picks the better of two answers. Cheaper than human "
     "ranking, it scales, and the rules are written down, so they can be read and discussed."),
    ("Today",
     "Most models mix the two (human and AI feedback). Simpler methods such as DPO (Direct Preference Optimization, "
     "2023) learn directly from pairs « preferred / rejected answer », without a separate reward model."),
    ("The limits — and why a developer cares",
     "The model learns what PLEASES the judge, not what is TRUE: it can agree with you when you are wrong "
     "(sycophancy), sound confident, or refuse a harmless request. Alignment shapes the style of the answer, not the "
     "correctness of the code: review it and run the tests."),
    ("Ask the room",
     "« When the assistant answers \"You're absolutely right!\", is that the truth or the reward model? »"),
]


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            # the "i" on the title line: two-column header grid (NG, 2026-11-22)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell():
                    st_write(bs.heading, "Phase 3: Alignment (RLHF/RLAIF)", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — Alignment (RLHF/RLAIF)", entries=_NOTES,
                                     position="left", width="50vw")

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
                        name="llm_alignment",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(105):   # fits one screen with the 0.6 em item gap (NG, 2026-11-22)
                        with st_list(
                            list_type=lt.unordered,
                            li_style=bs.body,
                            text_align="left",  # bullets and wrapped lines start at the left edge (NG, 2026-11-22)
                            item_gap=0.6,  # 0.6 em between items — streamtex st_list(item_gap=), 0.7.85 (NG, 2026-11-22)
                        ) as l:
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "HHH"),
                                    (bs.body, " — Helpful, Harmless, Honest"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Reward model"),
                                    (bs.body, " — Guides LLM toward preferred responses"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Human feedback"),
                                    (bs.body, " — Evaluators rank model outputs (RLHF)"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Constitutional AI"),
                                    (bs.body, " — Anthropic's principle-based self-critique (RLAIF)"),
                                )
                        # REF: https://arxiv.org/abs/2212.08073
                        st_write(bs.source, cite("bai2022constitutional"))
