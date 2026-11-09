# Adapted from streamtex-all-trainings@7707c1c5:content/deep_learning/llm_models.json
# Adapted from streamtex-all-trainings@7707c1c5:content/llm/context_length_scores.json
# Adapted from streamtex-all-trainings@7707c1c5:content/atoms/bck_llm_tokens_fragments.py
"""Slides — Model Families, Your Key, Tokens = Cost (two slides).

Edition 2, day-1 notion 3 (board peda1, P10). Family-level wording only: the two all-trainings data files
disagree on model names, so only names checked on the web (Nov 2026) appear — product lines (GPT, Claude,
Gemini, Llama, Gemma, gpt-oss, Qwen, Kimi) and two dated flagships (Mistral Large 3, Dec 2025; DeepSeek V4,
Apr 2026). The reference model of the course is still to be decided: placeholder wording.
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


_page_fill = s.project.containers.page_fill_top

_family = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md,
    "mc_family",
)
_panel = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md,
    "mc_panel",
)
_calc_box = Style.create(s.project.containers.callout + s.center_txt, "mc_calc_box")


class BlockStyles:
    """Slides: model families (2x2 grid) / key + tokens (two panels + calculation)."""
    heading = s.project.titles.section_title + s.center_txt
    asof = Style.create(s.project.colors.muted + s.italic + s.text.sizes.pt24 + s.center_txt, "mc_asof")
    fam_title = Style.create(
        s.project.colors.accent + s.bold + s.text.sizes.pt32 + s.text.wrap.hyphens, "mc_fam_title",
    )
    names = Style.create(
        s.project.colors.primary + s.bold + s.text.sizes.pt24, "mc_names",
    )
    body = Style.create(s.text.sizes.pt24, "mc_body")
    key = Style.create(s.text.sizes.pt24 + s.bold + s.project.colors.highlight, "mc_key")
    footer = Style.create(s.text.sizes.pt24 + s.center_txt, "mc_footer")
    panel_title = Style.create(
        s.project.colors.accent + s.bold + s.text.sizes.pt32 + s.text.wrap.hyphens, "mc_panel_title",
    )
    code = Style.create(
        s.text.sizes.pt24 + s.text.fonts.font_monospace + s.project.colors.primary, "mc_code",
    )
    sentence = Style.create(s.text.sizes.pt44 + s.bold + s.center_txt, "mc_sentence")
    tok_a = Style.create(s.project.colors.primary, "mc_tok_a")
    tok_b = Style.create(s.project.colors.accent, "mc_tok_b")
    tok_c = Style.create(s.project.colors.highlight, "mc_tok_c")
    tok_m = Style.create(s.project.colors.muted, "mc_tok_m")
    rule = Style.create(s.text.sizes.pt28 + s.bold + s.project.colors.highlight + s.center_txt, "mc_rule")
    calc = Style.create(s.text.sizes.pt28, "mc_calc")
    calc_key = Style.create(s.text.sizes.pt28 + s.bold + s.project.colors.highlight, "mc_calc_key")


bs = BlockStyles

# (family, names, what it means for you)
_FAMILIES = [
    ("US closed models", "OpenAI GPT · Anthropic Claude · Google Gemini",
     "Often at the top of coding benchmarks. API only — weights not published."),
    ("Open-weight models", "Meta Llama · Google Gemma · OpenAI gpt-oss · Qwen …",
     "Weights downloadable: run them yourself (locally, on your server) or through a provider."),
    ("Mistral — European", "Mistral Large 3 (Dec 2025) · Mistral Medium …",
     "EU-based provider; many models with open weights."),
    ("Chinese models", "DeepSeek V4 (Apr 2026) · Qwen (Alibaba) · Kimi (Moonshot) …",
     "Often open-weight and cheap per token; check where your data is processed."),
]

_NOTES_FAMILIES = [
    ("Message", "Same agent, different model: quality, speed, price and data location change. "
                "opencode is provider-agnostic, so the choice is a configuration line."),
    ("Names", "Version numbers change every few months: speak about families, not versions."),
    ("Check before class", "Re-check the two dated flagships the week before (Nov 2026)."),
]

_NOTES_COST = [
    ("Message", "You pay for every token sent and received; an agent re-sends the context at every turn."),
    ("The split", "\"Luxembourg\" cut in two is illustrative: each model has its own tokenizer."),
    ("Habits", "One task per session, short AGENTS.md, point to the files needed (@file) instead of the whole repo."),
]


def _header(title, lvl, notes):
    with st_grid(cols="92% 8%", cell_styles=s.project.containers.grid_cell_centered) as h:
        with h.cell():
            st_write(bs.heading, title, tag=t.div, toc_lvl=lvl)
        with h.cell():
            st_hover_tooltip(title=f"Trainer notes — {title}", entries=notes, position="left", width="45vw")


def _families_slide():
    with st_block(_page_fill):
        _header("Four Model Families", "1", _NOTES_FAMILIES)
        st_write(bs.asof, "As of Nov 2026 — names change fast, families do not.", tag=t.div)
        with st_grid(cols="1fr 1fr", gap="16px", cell_styles=_family) as g:
            for family, names, meaning in _FAMILIES:
                with g.cell():
                    st_write(bs.fam_title, family, tag=t.div)
                    st_write(bs.names, names, tag=t.div)
                    st_space("v", 1)
                    st_write(bs.body, meaning, tag=t.div)
        st_write(
            bs.footer,
            "Same agent, different model ⇒ different quality, speed and price. "
            "This week: ", (bs.key, "one reference model chosen by the trainer"), ", plus a backup.",
            tag=t.div,
        )


def _cost_slide():
    with st_block(_page_fill):
        _header("Your Key · Tokens = Cost", "2", _NOTES_COST)
        with st_grid(cols="1fr 1fr", gap="16px", cell_styles=_panel) as g:
            with g.cell():
                st_write(bs.panel_title, "What your key gives you", tag=t.div)
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                    with l.item():
                        st_write(bs.body, (bs.key, "One capped budget"), " — when it is spent, calls stop.")
                    with l.item():
                        st_write(bs.body, (bs.key, "One reference model"), " chosen by the trainer: ",
                                 (bs.code, "⟨reference model⟩"), ".")
                    with l.item():
                        st_write(bs.body, (bs.key, "A secret"), " — never in a prompt, a commit or an issue.")
                    with l.item():
                        st_write(bs.body, "Cost grows with ", (bs.key, "context size"), " × ",
                                 (bs.key, "number of turns"), ".")
            with g.cell():
                st_write(bs.panel_title, "The model reads tokens", tag=t.div)
                st_space("v", 2)
                st_write(
                    bs.sentence,
                    "« ", (bs.tok_a, "Luxem"), (bs.tok_b, "bourg"), (bs.tok_c, " is"),
                    (bs.tok_a, " a"), (bs.tok_m, " ____"), " »",
                    tag=t.div,
                )
                st_space("v", 2)
                st_write(bs.body, "Fragments, not words — each one a number.", tag=t.div)
                st_space("v", 1)
                st_write(bs.rule, "1 token ≈ 4 characters ≈ ¾ of a word", tag=t.div)

        with st_block(_calc_box):
            st_write(
                bs.calc,
                "Back of the envelope — a long agent session re-sends ",
                (bs.calc_key, "50k tokens × 40 turns = 2M input tokens"),
                ". Short sessions, one task each, only the files needed.",
            )


def build():
    _families_slide()
    st_slide_break()
    _cost_slide()
