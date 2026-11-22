"""Slide — the longer the context, the less reliable the model (one model per provider) (streamtex-all-trainings chart, content/atoms/bck_llm_rag_context_benchmark_01).

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
    ("Why 7 models here, 5 on the previous slide",
     "The previous slide keeps models of the same generation (online May–August 2026) with a score at every length "
     "up to 512K: 5 models, data read on 2026-11-22. This chart comes from the all-trainings course and keeps one "
     "model per provider, so it adds Grok 4.6 (no score at 512K) and Mistral Medium 3.5 (April 2026, an older "
     "generation). Same test, same measures (up to 2026-08-14)."),
    ("The lesson",
     "A large context window does not mean the model uses all of it well. Giving it only the relevant passages, which "
     "is what RAG does, keeps it in the zone where it is reliable."),
    ("References",
     "Context Arena, the measures plotted; the MRCR v2 test by Google DeepMind; Chroma, « Context Rot », the same drop "
     "on 18 models and several tasks; NoLiMa (Adobe), the drop when the question and the answer share no word."),
]


def build():
    chart_slide("The longer the context, the less reliable the model", "context-length", _NOTES_PROVIDERS,
                ["uzar2026contextarena", "gdm2025mrcrv2", "hong2025contextrot", "modarressi2025nolima"], "1")
