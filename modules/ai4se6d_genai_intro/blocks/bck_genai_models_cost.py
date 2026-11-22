# Adapted from streamtex-all-trainings@7707c1c5:content/deep_learning/llm_models.json
# Adapted from streamtex-all-trainings@7707c1c5:content/llm/context_length_scores.json
# Adapted from streamtex-all-trainings@7707c1c5:content/atoms/bck_llm_tokens_fragments.py
"""Slides — Model Families, Your Key, Tokens = Cost (two slides).

Edition 2, day-1 notion 3 (board peda1, P10). Family-level wording only: the two all-trainings data files
disagree on model names, so only names checked on the web (Nov 2026) appear — product lines (GPT, Claude,
Gemini, Llama, Gemma, gpt-oss, Qwen, Kimi) and two dated flagships (Mistral Large 4 — API preview 2026-10-06,
open weights end of Oct 2026, re-checked 2026-11-22; DeepSeek V4, Apr 2026).
Course models (ai4se-kit opencode.base.json, syllabus hd09): main openrouter/deepseek/deepseek-v4.1-flash,
backup openrouter/minimax/minimax-m3.1-flash. Key budget: $30 per learner (NG, 2026-11-22; first given as $10), shown in tokens only:
OpenRouter prices 2026-11-22 — DeepSeek $0.0498 / $0.1992 per M tokens in / out, MiniMax $0.075 / $0.30
→ $30 ≈ 600 M tokens sent to the main model (≈ 400 M on the backup, ≈ 150 M generated).
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


# Inside each st_slide box (min-height 80vh, centred, 10vh margins = one screen per slide): stack the
# content from the top, without page_fill_top's own 85vh, which would make each slide taller than the screen.
# The cost slide is taller than the families slide: top-aligned, no top margin, so it fits one screen.
_slide_top = Style("justify-content:flex-start;margin-top:0;", "mc_slide_top")
_slide_body = Style("display:flex;flex-direction:column;justify-content:flex-start;gap:1.5rem;", "mc_slide_body")

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
    rule = Style.create(s.text.sizes.pt44 + s.bold + s.project.colors.highlight + s.center_txt, "mc_rule")
    calc = Style.create(s.text.sizes.pt28, "mc_calc")
    calc_key = Style.create(s.text.sizes.pt28 + s.bold + s.project.colors.highlight, "mc_calc_key")


bs = BlockStyles

# (family, names, what it means for you)
_FAMILIES = [
    ("US closed models", "OpenAI GPT · Anthropic Claude · Google Gemini",
     "Often at the top of coding benchmarks. API only — weights not published."),
    ("Open-weight models", "Meta Llama · Google Gemma · OpenAI gpt-oss · Qwen …",
     "Weights downloadable: run them yourself (locally, on your server) or through a provider."),
    ("Mistral — European", "Mistral Large 4 (Oct 2026) · Medium 3.5 · Small 4",
     "EU-based provider; its models, Large 4 included, have open weights."),
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
    ("Habits", "One task per session, short AGENTS.md, point to the files needed (@file) instead of the whole repo."),
    ("The budget", "Each key is capped at $30 on OpenRouter. DeepSeek V4.1 Flash costs about $0.05 per million tokens "
                   "sent and $0.20 per million generated: $30 ≈ 600 M tokens sent (≈ 400 M on the MiniMax backup). "
                   "An agent mostly sends: ≈ 300 long sessions of 2M tokens. With GPT-6.2 Sol ($2 per million) the "
                   "same key would send ≈ 15 M tokens: 7 or 8 long sessions."),
]


def _header(title, lvl, notes):
    with st_grid(cols="92% 8%", cell_styles=s.project.containers.grid_cell_centered) as h:
        with h.cell():
            st_write(bs.heading, title, tag=t.div, toc_lvl=lvl)
        with h.cell():
            st_hover_tooltip(title=f"Trainer notes — {title}", entries=notes, position="left", width="50vw")


def _families_slide():
    with st_block(_slide_body):
        _header("Four Model Families", "1", _NOTES_FAMILIES)
        st_write(bs.asof, "As of Nov 2026 — names change fast, families do not.", tag=t.div)
        with st_grid(cols="1fr 1fr", gap="16px", cell_styles=_family) as g:
            for family, names, meaning in _FAMILIES:
                with st_zoom(130),g.cell():
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
    with st_block(_slide_body):
        _header("Your Key · Tokens = Cost", "2", _NOTES_COST)
        # NG, 2026-11-22: right panel removed; the token rule moves under the title, in orange;
        # the single panel at 160 % and the line below zoomed too.
        st_write(bs.rule, "1 token ≈ ¾ of a word", tag=t.div)
        with st_zoom(160), st_block(_panel):
            st_write(bs.panel_title, "What your key gives you", tag=t.div)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(bs.body, (bs.key, "≈ 600 million tokens"),
                             " — when they are spent, calls stop.")
                with l.item():
                    st_write(bs.body, (bs.key, "Main model"), ": ", (bs.code, "deepseek-v4.1-flash"))
                with l.item():
                    st_write(bs.body, (bs.key, "Backup model"), ": ", (bs.code, "minimax-m3.1-flash"))
                with l.item():
                    st_write(bs.body, (bs.key, "A secret"), " — never in a prompt, a commit or an issue.")
                with l.item():
                    st_write(bs.body, "Cost grows with ", (bs.key, "context size"), " × ",
                             (bs.key, "number of turns"), ".")
        with st_zoom(115), st_block(_calc_box):
            st_write(
                bs.calc,
                "Back of the envelope — a long agent session re-sends ",
                (bs.calc_key, "50k tokens × 40 turns = 2M input tokens"),
                ". Short sessions, one task each, only the files needed.",
            )


def build():
    # Two slides, each in its own st_slide box (NG, 2026-11-22: "bien séparer les deux slides"),
    # as in streamtex-all-trainings. The second one gets its own listed marker.
    with st_slide():
        _families_slide()
    with st_slide(cut=True, marker="Your Key · Tokens = Cost", style=_slide_top):
        _cost_slide()
