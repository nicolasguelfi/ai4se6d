"""Environment flags for editable / exportable modes."""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

IS_EDITABLE = os.environ.get("STX_EDITABLE", "false").lower() == "true"
IS_EXPORTABLE = os.environ.get("STX_EXPORT", "false").lower() == "true"
