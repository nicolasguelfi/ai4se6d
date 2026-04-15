"""Configure sys.path so shared-blocks imports work."""

import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
MODULES_DIR = PROJECT_DIR.parent
SHARED_BLOCKS_DIR = MODULES_DIR / "shared-blocks"

# Project dir first (highest priority), then shared-blocks
for p in (str(PROJECT_DIR), str(SHARED_BLOCKS_DIR)):
    if p not in sys.path:
        sys.path.append(p)
