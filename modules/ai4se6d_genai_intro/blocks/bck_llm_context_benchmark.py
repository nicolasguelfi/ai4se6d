"""Slide — Context Performance Benchmark: interactive Plotly chart from CSV."""
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

_CONTEXT_ORDER = ["8k", "16k", "32k", "64k", "128k", "256k", "512k", "1M"]

_COLORS = [
    "#00D4AA", "#FF6B6B", "#4ECDC4", "#FFE66D",
    "#A8E6CF", "#FF8B94", "#B8A9C9", "#F7DC6F",
]

# ── Visible by default (model_slug values from CSV) ──────────────────
_VISIBLE_SLUGS = {
    "anthropic/claude-opus-4.5:thinking",
    "google/gemini-3.1-pro-preview:thinking:high",
    "openai/gpt-5.2:thinking:xhigh",
    "mistralai/ministral-14b-2512"
}

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
    df["model"] = df["model_slug"].apply(_clean_name)
    df["context_bin"] = pd.Categorical(
        df["context_bin"], categories=_CONTEXT_ORDER, ordered=True,
    )
    df = df.sort_values(["model", "context_bin"])
    df["avg_score"] = df["avg_score"].astype(float)

    fig = go.Figure()

    for i, slug in enumerate(df["model_slug"].unique()):
        mdf = df[df["model_slug"] == slug].sort_values("context_bin")
        model = _clean_name(slug)
        color = _COLORS[i % len(_COLORS)]
        visible = True if slug in _VISIBLE_SLUGS else "legendonly"
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
                        "Multi-Round Coreference Resolution. The model must track "
                        "entities across multiple conversation turns — like remembering "
                        "who 'he' or 'it' refers to after many exchanges.",
                    ),
                    (
                        "8 Needles",
                        "8 specific facts are hidden ('needles') inside a long context "
                        "('haystack'). The model must retrieve all 8 correctly. "
                        "Tests real information retrieval, not just text generation.",
                    ),
                    (
                        "Context sizes",
                        "Each model is tested at 8k, 16k, 32k, 64k, 128k, 256k, 512k, "
                        "and 1M tokens. A score drop at larger sizes means the model "
                        "'forgets' information buried deep in its context window.",
                    ),
                    (
                        "Score",
                        "Percentage of needles correctly retrieved (0-100%). "
                        "A perfect model scores 100% at all context sizes.",
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
            st_write(bs.source, cite("contextarena2026"))
