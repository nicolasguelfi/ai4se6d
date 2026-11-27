"""Slide — Too big to read every line? (2/2): hundreds and thousands of files (NG « ok », 2026-11-27).

Second half of bck_git_review_scale (same table, notes and styles), split so both halves fit one screen.
"""
# @guideline: minimalist-visual + maximize-viewport
from blocks.bck_git_review_scale import _ROWS, render


class BlockStyles:
    """Styles live in bck_git_review_scale (same table)."""
bs = BlockStyles


def build():
    render(_ROWS[2:], "Too Big to Read Every Line? (2/2)",
           "Keep changes small: one task, one branch — then reading stays possible.")
