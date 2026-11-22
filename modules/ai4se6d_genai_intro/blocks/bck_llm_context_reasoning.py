"""Slide — the same model, with and without reasoning (GPT-5.5) (streamtex-all-trainings chart, content/atoms/bck_llm_rag_context_benchmark_02).

NG, 2026-11-22: "ces deux graphiques sont aussi intéressants pour les participants […] je pensais les rajouter après
les nôtres"; then "vraiment sur des slides séparés": one block per chart, layout in blocks/_context_charts.py. Same
data, drawing tool and trainer notes (English) as all-trainings (planche contexte1); the figures live in
modules/shared-blocks/data/context_reliability_scores.json.
"""
# @guideline: maximize-viewport
from blocks._context_charts import chart_slide


class BlockStyles:
    """Layout and styles in blocks/_context_charts.py (shared by the two chart slides)."""
bs = BlockStyles


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


def build():
    chart_slide("The same model, with and without reasoning", "context-length-reasoning", _NOTES_REASONING,
                ["uzar2026contextarena", "gdm2025mrcrv2"], "1")   # its own page: a level-1 marker
