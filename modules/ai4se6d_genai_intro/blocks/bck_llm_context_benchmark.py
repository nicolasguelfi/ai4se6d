"""Slide — Context Performance Benchmark: interactive Plotly chart from CSV.

Data: scripts/update_context_arena.py rewrites the CSV from the Context Arena API (NG, 2026-11-22: a
generator, so the next edition only reruns the script). Shown by default: the `featured` rows (best model
of Anthropic, OpenAI, Google, Mistral and of the best open-weights provider); the snapshot month is in the CSV.
"""
# @guideline: maximize-viewport
import streamlit as st  # noqa: F401
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

import streamtex as stx
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


_page_fill = s.project.containers.page_fill_top

_CSV_PATH = (
    Path(__file__).parent.parent.parent
    / "shared-blocks" / "static" / "_SHARED" / "csv"
    / "mrcr-line-chart-8-nee.csv"
)

# Date of the Context Arena export in _CSV_PATH. UPDATE when the CSV is
# re-downloaded (planned 23-24/11/2026). Source sheet: docs/trainer/day1/sources.md

_CONTEXT_ORDER = ["8k", "16k", "32k", "64k", "128k", "256k", "512k", "1M"]

# The first five go to the featured models (shown by default): five clearly distinct hues.
_COLORS = [
    "#00D4AA", "#FF6B6B", "#FFE66D", "#7AB8F5", "#F39C12",
    "#B8A9C9", "#A8E6CF", "#FF8B94", "#4ECDC4", "#F7DC6F", "#C39BD3", "#85C1E9",
]

# ── Visible by default (model_slug values from CSV) ──────────────────

# ── Chart dimensions & scaling ───────────────────────────────────────
_HEIGHT = 1100   # chart height in pixels (width auto-fills iframe)
_SCALE_FONT = 1.5  # font/stroke scale inside Plotly

# Base font/stroke values (at _SCALE_FONT = 1.0) — sized for fullwidth chart
_BASE_TITLE = 36
_BASE_AXIS_TITLE = 30
_BASE_TICK_X = 26
_BASE_TICK_Y = 24
_BASE_LEGEND = 22
_BASE_HOVER = 24
_BASE_DATA_LABEL = 20
_BASE_LINE_WIDTH = 4
_BASE_MARKER_SIZE = 14

# Shorthand
_sf = _SCALE_FONT


class BlockStyles:
    """Slide: Context Performance Benchmark — maximize-viewport: full-width chart."""
    heading = s.project.titles.slide_title + s.center_txt
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def _clean_name(slug: str) -> str:
    provider, model_part = slug.split("/", 1)
    model = model_part.split(":")[0]
    return f"{provider.capitalize()} — {model}"


def _build_chart() -> go.Figure:
    df = pd.read_csv(_CSV_PATH)
    featured = set(df.loc[df["featured"] == 1, "model_slug"])
    df["model"] = df["model_slug"].apply(_clean_name)
    df["context_bin"] = pd.Categorical(
        df["context_bin"], categories=_CONTEXT_ORDER, ordered=True,
    )
    df = df.sort_values(["model", "context_bin"])
    df["avg_score"] = df["avg_score"].astype(float)

    fig = go.Figure()

    slugs = sorted(df["model_slug"].unique(), key=lambda x: (x not in featured, x))  # featured first
    for i, slug in enumerate(slugs):
        mdf = df[df["model_slug"] == slug].sort_values("context_bin")
        model = _clean_name(slug)
        color = _COLORS[i % len(_COLORS)]
        visible = True if slug in featured else "legendonly"
        fig.add_trace(go.Scatter(
            x=mdf["context_bin"].astype(str),
            y=mdf["avg_score"],
            mode="lines+markers+text",
            name=model,
            visible=visible,
            line={"color": color, "width": round(_BASE_LINE_WIDTH * _sf)},
            marker={"size": round(_BASE_MARKER_SIZE * _sf)},
            text=[f"{v:.0f}" for v in mdf["avg_score"]],
            textposition="top center",
            textfont={"size": round(_BASE_DATA_LABEL * _sf), "color": color},
            hovertemplate="%{x}<br>%{y:.1f}%<extra>%{fullData.name}</extra>",
        ))

    fig.update_layout(
        title={
            "text": "Performance vs Context Size (MRCR — 8 Needles)",
            "font": {"size": round(_BASE_TITLE * _sf)},
            "x": 0.5,
        },
        xaxis={
            "title": {"text": "Context Size", "font": {"size": round(_BASE_AXIS_TITLE * _sf)}},
            "tickfont": {"size": round(_BASE_TICK_X * _sf)},
            "categoryorder": "array",
            "categoryarray": _CONTEXT_ORDER,
        },
        yaxis={
            "title": {"text": "MRCR Score (%)", "font": {"size": round(_BASE_AXIS_TITLE * _sf)}},
            "tickfont": {"size": round(_BASE_TICK_Y * _sf)},
            "range": [0, 105],
            "dtick": 10,
        },
        legend={
            "font": {"size": round(_BASE_LEGEND * _sf)},
            "bgcolor": "rgba(26,26,46,0.8)",
            "bordercolor": "#333",
            "borderwidth": 1,
        },
        hoverlabel={"font": {"size": round(_BASE_HOVER * _sf)}},
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117",
        autosize=True,
        height=_HEIGHT,
        margin={"l": 120, "r": 200, "t": 100, "b": 100},
    )

    return fig


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Context Performance Benchmark", tag=t.div, toc_lvl="1")
            st_hover_tooltip(
                title="MRCR 8 Needles — What this test measures",
                entries=[
                    (
                        "MRCR",
                        "Multi-Round Co-reference Resolution (OpenAI). A long "
                        "conversation contains several near-identical requests, "
                        "e.g. 'write a poem about tapirs'. The model is then asked: "
                        "'return the 2nd poem about tapirs'.",
                    ),
                    (
                        "8 Needles",
                        "8 identical requests ('needles') are hidden in the "
                        "conversation ('haystack'). The model must pick the right "
                        "one by its order. More needles = harder.",
                    ),
                    (
                        "Context sizes",
                        "Each model is tested at 8k, 16k, 32k, 64k, 128k, 256k, 512k, "
                        "and 1M tokens. A score drop at larger sizes means the model "
                        "'forgets' information buried deep in its context window.",
                    ),
                    (
                        "Score",
                        "Text similarity between the answer and the expected one "
                        "(0-100%). A perfect model scores 100% at all context sizes.",
                    ),
                ],
                scale="1.5vw",
                width="50vw",
            )

        fig = _build_chart()
        fig_html = fig.to_html(
            include_plotlyjs="cdn", full_html=True,
            config={"scrollZoom": True},
        )
        stx.st_html(fig_html, height=_HEIGHT)

        with st_block(s.center_txt):
            st_write(
                bs.source,
                cite("contextarena2026"), " · ", cite("openai-mrcr2025"),
                f" — data snapshot {pd.read_csv(_CSV_PATH, usecols=['snapshot'])['snapshot'].iloc[0]}",
            )
