"""Slide — Exercise sheet "quality" (check part), rendered from the single source exercise_sheets.py (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from exercise_sheet import exercise_sheet


class BlockStyles:
    """Layout and styles come from the shared exercise_sheet component."""
bs = BlockStyles


def build():
    exercise_sheet("quality", part="check")
