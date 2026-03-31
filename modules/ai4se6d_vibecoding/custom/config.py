"""Project-level environment flags for local vs deployed mode.

Variables:
    IS_EDITABLE:  Show image editing panels (default: False — opt-in via env).
    IS_EXPORTABLE: Show export buttons in sidebar (default: False — opt-in via env).

Enable in local development by creating a .env file in the module root:
    STX_EDITABLE=true
    STX_EXPORT=true
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

IS_EDITABLE = os.environ.get("STX_EDITABLE", "false").lower() == "true"
IS_EXPORTABLE = os.environ.get("STX_EXPORT", "false").lower() == "true"
