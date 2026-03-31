"""StreamTeX project setup — configures import paths."""
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
MODULES_DIR = PROJECT_DIR.parent

# Shared blocks for cross-module imports (appended — lower priority than project dir)
SHARED_BLOCKS_DIR = MODULES_DIR / "shared-blocks"
if SHARED_BLOCKS_DIR.exists() and str(SHARED_BLOCKS_DIR) not in sys.path:
    sys.path.append(str(SHARED_BLOCKS_DIR))
