"""Project-wide paths and constants."""
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

RAW_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DIR = ROOT_DIR / "data" / "processed"
FIG_DIR = ROOT_DIR / "reports" / "figures"

PLATFORMS = ["steam", "playstation", "xbox"]
