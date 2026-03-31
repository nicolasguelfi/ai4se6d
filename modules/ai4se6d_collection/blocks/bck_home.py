"""Collection home — gradient header + project cards from collection.toml.

Cards are generated dynamically from collection.toml.
To add a module: add a [projects.xxx] section in collection.toml
and set STX_URL_XXX env var in Coolify. No code change needed.
"""

import math
import os
import tomllib
from pathlib import Path

import streamlit as st
from custom.styles import Styles as s

import streamtex as stx
from streamtex import *
from streamtex.enums import Tags as t
from streamtex.styles import Style

# Load collection config once
_TOML_PATH = Path(__file__).parent.parent / "collection.toml"
with open(_TOML_PATH, "rb") as _f:
    _CONFIG = tomllib.load(_f)

_CARDS_PER_ROW = _CONFIG.get("collection", {}).get("cards_per_row", 3)

# Build sorted project list with resolved URLs
_PROJECTS = []
for _key, _data in sorted(
    _CONFIG.get("projects", {}).items(),
    key=lambda item: item[1].get("order", 0),
):
    env_key = "STX_URL_" + _key.upper().replace("-", "_")
    _PROJECTS.append({
        "key": _key,
        "title": _data.get("title", _key),
        "description": _data.get("description", ""),
        "emoji": _data.get("emoji", ""),
        "button_label": _data.get("button_label", "Open"),
        "url": os.environ.get(env_key, _data.get("project_url", "#")),
    })


class BlockStyles:
    """Styles for the collection home page."""

    header = Style(
        "background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); "
        "padding: 40px 20px; border-radius: 8px;",
        "collection_header",
    )
    level_box = Style(
        "background: rgba(122, 184, 245, 0.08); "
        "border-left: 4px solid #7AB8F5; "
        "padding: 20px 24px; border-radius: 0 8px 8px 0;",
        "collection_level_box",
    )
    level_label = Style(
        "color: #7AB8F5; font-weight: bold; font-size: 14pt; "
        "text-transform: uppercase; letter-spacing: 2px;",
        "collection_level_label",
    )
    description = s.large
    card_container = Style(
        "border: 1px solid rgba(255,255,255,0.1); "
        "border-radius: 12px; padding: 24px; "
        "background: rgba(255,255,255,0.03); "
        "transition: transform 0.2s, box-shadow 0.2s;",
        "collection_card",
    )
    card_description = s.medium
    project_title = Style(
        "font-weight: bold; font-size: 22pt;",
        "project_title",
    )
    grid_with_gap = stx.StxStyles.container.grid.gap_24
    footer = Style.create(
        s.medium + s.text.colors.white + "opacity:0.6;text-align:center;",
        "collection_footer",
    )


bs = BlockStyles


def _render_card(project: dict) -> None:
    """Render a single project card from a project dict."""
    with st_block(bs.card_container):
        st_space("v", 1)
        st_write(s.huge + "text-align:center;", project["emoji"])
        st_space("v", 1)
        st_write(bs.project_title + "text-align:center;", project["title"])
        st_space("v", 1)
        st_write(bs.card_description + "text-align:center;", project["description"])
        st_space("v", 2)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.link_button(
                f"{project['emoji']} {project['button_label']}",
                project["url"],
                use_container_width=True,
            )
        st_space("v", 1)


def build():
    """Render the collection home: header, level badge, project cards."""

    # === Gradient header ===
    st_space("v", 1)
    with st_block(bs.header):
        st_write(
            stx.StxStyles.Huge + stx.StxStyles.text.colors.white,
            "AI for Software Engineering 6D",
            tag=t.div,
            toc_lvl="1",
        )
        st_write(
            stx.StxStyles.large + stx.StxStyles.text.colors.white,
            "Formation en ingenierie logicielle augmentee par IA",
            tag=t.div,
        )
    st_space("v", 1)

    # === Level badge ===
    with st_block(bs.level_box):
        st_write(bs.level_label, "Training Collection")
        st_space("v", 0.5)
        st_write(
            s.Large + s.text.weights.bold_weight,
            "Explore the AI4SE 6D Learning Paths",
        )
        st_space("v", 1)
        st_write(
            bs.description,
            "Browse the AI4SE 6D training modules. "
            "Each module is self-contained and can be launched independently.",
        )
        st_space("v", 1)
        with st_list(list_type="ul") as l:
            for proj in _PROJECTS:
                with l.item():
                    st_write(s.medium, f"{proj['title']}: {proj['description']}")

    # === Project cards — dynamic rows ===
    st_space("v", 2)

    num_rows = math.ceil(len(_PROJECTS) / _CARDS_PER_ROW)
    for row_idx in range(num_rows):
        row_projects = _PROJECTS[row_idx * _CARDS_PER_ROW:(row_idx + 1) * _CARDS_PER_ROW]
        cols_in_row = len(row_projects)

        with st_grid(cols=cols_in_row, responsive=True, grid_style=bs.grid_with_gap):
            for proj in row_projects:
                _render_card(proj)

        if row_idx < num_rows - 1:
            st_space("v", 1)

    # === Footer ===
    st_space("v", 3)
    st.divider()
    st_space("v", 2)
    st_write(
        bs.footer,
        "AI4SE 6D Training Collection | "
        "AI for Software Engineering",
    )
    st_space("v", 2)
