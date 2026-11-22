"""Slides — Artificial Analysis Intelligence Index: four charts drawn from a CSV.

NG, 2026-11-22: charts generated from data (no more screenshots), so the next edition only refreshes the CSV:

    uv run python scripts/update_ai_index.py      # rewrites _SHARED/csv/ai-index.csv

Fair comparison: only models of the same generation (released within three months) and with a result on each
of the nine evaluations of the index. The fourth view is score vs. cost per task: with a single generation, the
former "score vs. release date" view no longer says anything.
"""
# @guideline: maximize-viewport
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go

import streamtex as stx
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


_CSV_PATH = Path(__file__).parent.parent.parent / "shared-blocks" / "static" / "_SHARED" / "csv" / "ai-index.csv"

_HEIGHT = 720          # chart height in pixels (title + chart + source fit 1920x1080)
_FONT = 26             # base font size inside the charts (projection)
_PROVIDER_COLORS = {   # main providers; every other one is grey
    "Anthropic": "#F39C12",
    "OpenAI": "#2EC4B6",
    "Google": "#7AB8F5",
}
_OTHER_COLOR = "#B8A9C9"
_COURSE_LINE = "#FFFFFF"
# Title + chart + source fill the screen: each slide top-aligned, without the st_slide top margin.
_slide_top = Style("justify-content:flex-start;margin-top:0;", "aiidx_slide_top")


class BlockStyles:
    """Benchmark slides styles."""
    heading = s.project.titles.slide_title + s.center_txt
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


_TOKEN_ENTRIES = [
    ("Output tokens (chart)", "Tokens the model generated to run the whole index: its visible answers, tool calls "
                              "and, for reasoning models, its internal thinking."),
    ("Input tokens (hover)", "Tokens sent to the model at each turn of the agent loop — prompt, conversation history "
                             "and tool results, re-sent every turn. Often 100x the output: this is what you pay for."),
    ("Reading it", "A verbose model costs more and takes longer per task, even at the same price per token."),
]


def _load() -> pd.DataFrame:
    df = pd.read_csv(_CSV_PATH)
    df["label"] = df["model"] + df["open_weights"].map({1: " ◆", 0: ""})
    df["color"] = df["provider"].map(_PROVIDER_COLORS).fillna(_OTHER_COLOR)
    return df


def _layout(fig: go.Figure, xaxis: dict, yaxis: dict | None = None) -> go.Figure:
    fig.update_layout(
        template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#0E1117",
        font={"size": _FONT}, height=_HEIGHT, autosize=True, showlegend=False,
        margin={"l": 20, "r": 40, "t": 20, "b": 90},
        xaxis={"tickfont": {"size": _FONT}, "title": {"font": {"size": _FONT}}, **xaxis},
        yaxis=yaxis or {"autorange": "reversed", "tickfont": {"size": _FONT}, "automargin": True},
        hoverlabel={"font": {"size": _FONT}},
    )
    return fig


def _bars(df: pd.DataFrame, column: str, fmt: str, axis_title: str, hover: str) -> go.Figure:
    df = df.sort_values(column, ascending=False)
    fig = go.Figure(go.Bar(
        x=df[column], y=df["label"], orientation="h",
        marker={"color": df["color"],
                "line": {"color": [_COURSE_LINE if c else "rgba(0,0,0,0)" for c in df["course_model"]],
                         "width": 5}},
        text=[fmt.format(v) + ("   ← course model" if c else "") for v, c in zip(df[column], df["course_model"])],
        textposition="outside", textfont={"size": _FONT}, cliponaxis=False,
        customdata=df[["provider", "input_tokens_m", "cost_per_task", "minutes_per_task"]],
        hovertemplate=hover + "<extra>%{customdata[0]}</extra>",
    ))
    return _layout(fig, {"title": {"text": axis_title}, "range": [0, df[column].max() * 1.35]})


def _score_vs_cost(df: pd.DataFrame) -> go.Figure:
    fig = go.Figure(go.Scatter(
        x=df["cost_per_task"], y=df["score"], mode="markers+text",
        marker={"size": 26, "color": df["color"],
                "line": {"color": [_COURSE_LINE if c else df["color"].iloc[i] for i, c in enumerate(df["course_model"])],
                         "width": 4}},
        text=df["label"],
        # alternate above / below, by score rank, so that close points do not overlap their labels
        textposition=["top center" if r % 2 == 0 else "bottom center"
                      for r in df["score"].rank(method="first", ascending=False).astype(int)], textfont={"size": round(_FONT * 0.8)},
        customdata=df[["provider"]],
        hovertemplate="%{text}<br>score %{y}<br>$%{x:.2f} per task<extra>%{customdata[0]}</extra>",
    ))
    return _layout(
        fig,
        {"title": {"text": "Cost per task (USD, log scale) — cheaper ←"}, "type": "log"},
        {"title": {"text": "Intelligence Index", "font": {"size": _FONT}}, "tickfont": {"size": _FONT},
         "range": [df["score"].min() - 6, df["score"].max() + 6]},
    )


def _views(df: pd.DataFrame):
    """(title, figure, tooltip entries) of the four slides."""
    return [
        ("AI Index: Results",
         _bars(df, "score", "{:.0f}", "Artificial Analysis Intelligence Index (9 evaluations)",
               "%{y}: %{x}<br>$%{customdata[2]:.2f} per task"), None),
        ("AI Index: Token Usage",
         _bars(df, "output_tokens_m", "{:.0f}M", "Output tokens to run the index (millions)",
               "%{y}: %{x:.0f}M output<br>%{customdata[1]:,.0f}M input"), _TOKEN_ENTRIES),
        ("AI Index: Cost per Task",
         _bars(df, "cost_per_task", "${:.2f}", "Average cost of one index task (USD)",
               "%{y}: $%{x:.2f} per task<br>%{customdata[3]:.1f} min per task"), None),
        ("AI Index: Score vs. Cost", _score_vs_cost(df), None),
    ]


def build():
    df = _load()
    snapshot = df["snapshot"].iloc[0]
    window = f"{pd.to_datetime(df['released'].min()):%b}–{pd.to_datetime(df['released'].max()):%b %Y}"
    for idx, (title, fig, notes) in enumerate(_views(df)):
        with st_slide(cut=idx > 0, marker=(title if idx > 0 else None), style=_slide_top):
            with st_block(s.center_txt):
                st_write(bs.heading, title, tag=t.div, toc_lvl="1" if idx == 0 else "2")
                if notes:
                    st_hover_tooltip(title="Token Types", entries=notes, scale="2vw", width="65vw",
                                     position="center")
            stx.st_html(fig.to_html(include_plotlyjs="cdn", full_html=True, config={"displayModeBar": False}),
                        height=_HEIGHT)
            with st_block(s.center_txt):
                st_write(
                    bs.source, cite("artificialanalysis2026"),
                    f" — {snapshot} · released {window} · ◆ open weights",
                )
