"""Project-wide paths and constants."""
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

RAW_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DIR = ROOT_DIR / "data" / "processed"
FIG_DIR = ROOT_DIR / "reports" / "figures"

PLATFORMS = ["steam", "playstation", "xbox"]

# Seed for every random step (sampling, train/test split, models) so results can be reproduced
RANDOM_STATE = 42

# Tables shipped for every platform: data/raw/<platform>/<table>.csv
COMMON_TABLES = ["games", "achievements", "players", "history", "purchased_games", "prices"]

# Tables per platform; Steam has three extra ones
TABLES = {
    "steam": COMMON_TABLES + ["reviews", "friends", "private_steamids"],
    "playstation": COMMON_TABLES,
    "xbox": COMMON_TABLES,
}

# history.csv is 600-800 MB per platform: read it in chunks or with usecols/dtype
LARGE_TABLES = {"history", "friends", "reviews"}
