"""Slides — the two all-trainings charts on context length: reliability per provider, and with / without reasoning.

NG, 2026-11-22: "ces deux graphiques sont aussi intéressants pour les participants […] je pensais les rajouter après
les nôtres" — they follow bck_llm_context_benchmark. Copied from streamtex-all-trainings
(content/atoms/bck_llm_rag_context_benchmark_01 and _02, planche contexte1): same data, same drawing tool, same
trainer notes (English). The figures live in modules/shared-blocks/data/context_reliability_scores.json; redraw with

    uv run python scripts/draw_context_reliability_chart.py
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


_IMAGES = "_SHARED/images/diagrams/context-reliability"
_slide_top = Style("justify-content:flex-start;margin-top:0;", "ctxrel_slide_top")


class BlockStyles:
    """Context reliability slides styles."""
    heading = s.project.titles.slide_title + s.center_txt
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


_NOTES_PROVIDERS = [
    ("What the chart shows",
     "Seven recent models, one per provider (August 2026). All of them lose reliability as the context grows: the "
     "best still score about 90 at 128K tokens, then drop; Mistral Medium 3.5 reaches the chance level at 128K."),
    ("The test",
     "MRCR v2 with 8 needles (Google DeepMind): the model receives a very long fictional conversation. In eight "
     "places, the user made exactly the same request (« write a poem about tapirs ») and each time received a "
     "different poem; around them, dozens of other similar requests muddy the trail. At the end, the model is asked: "
     "« reproduce the 3rd poem about tapirs ». It must find the eight, count them in order and reproduce the right "
     "one. The task is the same at every length: only the conversation around it grows longer."),
    ("Reading the score",
     "The score measures how close the answer is to the right one (0 to 100); it is not a right/wrong accuracy. "
     "Picking one of the eight answers at random gives about 15: the dotted line."),
    ("The pages",
     "Order of magnitude: one token ≈ three quarters of a word, one page ≈ 500 words. 128K tokens ≈ 200 pages."),
    ("The choices",
     "For each model, the highest reasoning effort measured. Claude Opus 4.7 is left out (below 3 from 128K at every "
     "effort: a failure, not a result). Beyond 512K only Gemini has a point: the 1M prompts do not fit the other "
     "models."),
    ("The lesson",
     "A large context window does not mean the model uses all of it well. Giving it only the relevant passages, which "
     "is what RAG does, keeps it in the zone where it is reliable."),
    ("References",
     "Context Arena, the measures plotted; the MRCR v2 test by Google DeepMind; Chroma, « Context Rot », the same drop "
     "on 18 models and several tasks; NoLiMa (Adobe), the drop when the question and the answer share no word."),
]

_NOTES_REASONING = [
    ("What the chart shows",
     "GPT-5.5 on the same test, at maximum reasoning effort and with reasoning off. At 32K tokens (about 50 pages): "
     "95.8 with reasoning, 35.0 without."),
    ("Why",
     "Reasoning lets the model go back over the context before answering: here, find the eight identical requests "
     "and count to the right one. Without it, the model answers in one pass."),
    ("In practice",
     "The setting matters as much as the model: the same name can hide very different reliability. Reasoning costs "
     "time and tokens; reducing the context (RAG) is the other lever."),
    ("Reading the score",
     "Same score as the previous slide: closeness to the right answer, 0 to 100; chance ≈ 15."),
]

# (title, image, notes, citations)
_SLIDES = [
    ("The longer the context, the less reliable the model", "context-length", _NOTES_PROVIDERS,
     ["uzar2026contextarena", "gdm2025mrcrv2", "hong2025contextrot", "modarressi2025nolima"]),
    ("The same model, with and without reasoning", "context-length-reasoning", _NOTES_REASONING,
     ["uzar2026contextarena", "gdm2025mrcrv2"]),
]


def build():
    for idx, (title, image, notes, refs) in enumerate(_SLIDES):
        with st_slide(cut=idx > 0, marker=(title if idx > 0 else None), style=_slide_top):
            with st_grid(cols="92% 8%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(46):   # long titles kept on one line
                    st_write(bs.heading, title, tag=t.div, toc_lvl="1" if idx == 0 else "2")
                with h.cell():
                    st_hover_tooltip(title=f"Trainer notes — {title}", entries=notes, position="left",
                                     width="50vw")
            st_image(uri=f"{_IMAGES}/{image}-en.png", width="100%", max_vh=64, align="center")
            with st_block(s.center_txt):
                parts = []
                for i, key in enumerate(refs):
                    parts += ([" · "] if i else []) + [cite(key)]
                st_write(bs.source, *parts)
