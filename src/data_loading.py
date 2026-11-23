"""Loaders for the raw tables in ``data/raw``."""
import ast

import pandas as pd

from src.config import PLATFORMS, RAW_DIR, TABLES


def table_path(platform: str, name: str):
    """Return the path of ``data/raw/<platform>/<name>.csv`` after checking both names."""
    if platform not in TABLES:
        raise ValueError(f"Unknown platform {platform!r}; expected one of {PLATFORMS}")
    if name not in TABLES[platform]:
        raise ValueError(f"Table {name!r} does not exist for {platform}; expected one of {TABLES[platform]}")
    return RAW_DIR / platform / f"{name}.csv"


def load_table(platform: str, name: str, **read_csv_kwargs) -> pd.DataFrame:
    """Load one raw table for one platform.

    Parameters
    ----------
    platform : str
        One of ``src.config.PLATFORMS``.
    name : str
        Table name without file extension, one of ``src.config.TABLES[platform]``.
    **read_csv_kwargs
        Passed to ``pandas.read_csv``. Use ``usecols``, ``dtype`` or ``nrows``
        for the large tables (``src.config.LARGE_TABLES``).

    Returns
    -------
    pandas.DataFrame
        The table as stored in ``src.config.RAW_DIR``.
    """
    return pd.read_csv(table_path(platform, name), **read_csv_kwargs)


def load_all(name: str, **read_csv_kwargs) -> pd.DataFrame:
    """Load table ``name`` for every platform that has it and stack the results.

    Parameters
    ----------
    name : str
        Table name without file extension.
    **read_csv_kwargs
        Passed to ``pandas.read_csv`` for every platform.

    Returns
    -------
    pandas.DataFrame
        All platforms concatenated, with a ``platform`` column added. Columns
        that exist only on some platforms are NaN for the others.
    """
    frames = [
        load_table(platform, name, **read_csv_kwargs).assign(platform=platform)
        for platform in PLATFORMS
        if name in TABLES[platform]
    ]
    return pd.concat(frames, ignore_index=True)


# --- Player-side tables ---------------------------------------------------------------------------------------
# Read arguments for the player-side tables (see notebook 01, section 2.1). They cut memory by 40-90% and stop
# pandas from changing values silently. Steam player ids (7.6e16) need int64; the PlayStation and Xbox ids fit int32.

# players tables: only an empty cell means "missing". With the default setting pandas also turns the literal
# nickname "null" (one Xbox player) into NaN.
_ONLY_EMPTY_IS_NA = {"keep_default_na": False, "na_values": [""]}

_REVIEW_DTYPES = {"reviewid": "int32", "playerid": "int64", "gameid": "int32",
                  "helpful": "int32", "funny": "int32", "awards": "int32"}

PLAYER_READ_ARGS = {
    ("steam", "players"): {"dtype": {"playerid": "int64", "country": "category"},
                           "parse_dates": ["created"], **_ONLY_EMPTY_IS_NA},
    ("playstation", "players"): {"dtype": {"playerid": "int32", "nickname": "string", "country": "category"},
                                 **_ONLY_EMPTY_IS_NA},
    ("xbox", "players"): {"dtype": {"playerid": "int32", "nickname": "string"}, **_ONLY_EMPTY_IS_NA},
    ("steam", "history"): {"dtype": {"playerid": "int64", "achievementid": "string"},
                           "parse_dates": ["date_acquired"]},
    ("playstation", "history"): {"dtype": {"playerid": "int32", "achievementid": "string"},
                                 "parse_dates": ["date_acquired"]},
    ("xbox", "history"): {"dtype": {"playerid": "int32", "achievementid": "string"},
                          "parse_dates": ["date_acquired"]},
    ("steam", "purchased_games"): {"dtype": {"playerid": "int64"}},
    ("playstation", "purchased_games"): {"dtype": {"playerid": "int32"}},
    ("xbox", "purchased_games"): {"dtype": {"playerid": "int32"}},
    ("steam", "reviews"): {"dtype": _REVIEW_DTYPES, "parse_dates": ["posted"]},
    ("steam", "friends"): {"dtype": {"playerid": "int64"}},
    ("steam", "private_steamids"): {"dtype": {"playerid": "int64"}},
}

PLAYER_SIDE_TABLES = list(PLAYER_READ_ARGS)


def load_player_table(platform: str, name: str, **overrides) -> pd.DataFrame:
    """Load one player-side table with the memory-saving settings in ``PLAYER_READ_ARGS``.

    Parameters
    ----------
    platform, name : str
        Must be a key of ``PLAYER_READ_ARGS``, e.g. ``("steam", "history")``.
    **overrides
        Replace or add ``pandas.read_csv`` arguments. Useful ones: ``usecols`` (e.g. leave out the
        ``review`` text, which is 94% of the memory of ``reviews``), ``nrows`` (sample), ``chunksize``.

    Returns
    -------
    pandas.DataFrame
        The table with compact dtypes and parsed dates. ``history`` has 10-20 million rows
        (1.0-1.6 GB): load one platform at a time and drop what you do not need.
    """
    if (platform, name) not in PLAYER_READ_ARGS:
        raise ValueError(f"No player-side settings for ({platform!r}, {name!r}); expected one of {PLAYER_SIDE_TABLES}")
    return load_table(platform, name, **{**PLAYER_READ_ARGS[(platform, name)], **overrides})


def count_list_items(series: pd.Series) -> pd.Series:
    """Count the items of a column that stores a list as text (``"[60, 1670]"`` or ``"['7656…', '7656…']"``).

    Much faster than parsing every list: items are separated by commas, so the count is the number of
    commas plus one. Empty cells (``NaN``) and ``"[]"`` count as 0. Returns an ``Int64`` series.
    """
    counts = series.str.count(",") + 1
    return counts.where(series.notna() & (series != "[]"), 0).astype("Int64")


def parse_id_list(text) -> list:
    """Turn one list stored as text into a Python list of ids (as ``str``); ``NaN``/``"[]"`` give ``[]``.

    >>> parse_id_list("[60, 1670]")
    ['60', '1670']
    >>> parse_id_list("['765611', '765612']")
    ['765611', '765612']
    """
    if not isinstance(text, str) or text == "[]":
        return []
    return [item.strip().strip("'\"") for item in text.strip("[]").split(",")]


# --- Game-side tables -----------------------------------------------------------------------------------------
# Read arguments for the game-side tables (see notebook 01, section 2.1).
# - Game ids are at most about 3.4 million on every platform, so they fit int32.
# - achievementid is read as "string", the same dtype as history.achievementid, so the two tables join directly.
# - achievements: only an empty cell means "missing". By default pandas also turns achievement titles such as
#   "NA", "NULL" or "null" into NaN (19 titles and descriptions across the three platforms).
# - Prices stay float64: float32 would store 4.99 as 4.9899998 and make price comparisons unreliable.
# - The default C parser is used everywhere: the pyarrow engine fails on PlayStation achievements, whose
#   descriptions contain line breaks inside quoted cells.
_GAMES_ARGS = {"dtype": {"gameid": "int32"}, "parse_dates": ["release_date"]}
_ACHIEVEMENTS_DTYPES = {"achievementid": "string", "gameid": "int32"}
_PRICES_ARGS = {"dtype": {"gameid": "int32"}, "parse_dates": ["date_acquired"]}

# PlayStation trophy grades in their real order (alphabetical order would put Gold before Silver)
TROPHY_GRADES = pd.CategoricalDtype(["Bronze", "Silver", "Gold", "Platinum"], ordered=True)

GAME_READ_ARGS = {
    ("steam", "games"): _GAMES_ARGS,
    ("playstation", "games"): {**_GAMES_ARGS, "dtype": {"gameid": "int32", "platform": "category"}},
    ("xbox", "games"): _GAMES_ARGS,
    ("steam", "achievements"): {"dtype": _ACHIEVEMENTS_DTYPES, **_ONLY_EMPTY_IS_NA},
    ("playstation", "achievements"): {"dtype": {**_ACHIEVEMENTS_DTYPES, "rarity": TROPHY_GRADES}, **_ONLY_EMPTY_IS_NA},
    # Xbox points are whole numbers with a few missing values: nullable Int16 keeps them as integers
    ("xbox", "achievements"): {"dtype": {**_ACHIEVEMENTS_DTYPES, "points": "Int16"}, **_ONLY_EMPTY_IS_NA},
    ("steam", "prices"): _PRICES_ARGS,
    ("playstation", "prices"): _PRICES_ARGS,
    ("xbox", "prices"): _PRICES_ARGS,
}

GAME_SIDE_TABLES = list(GAME_READ_ARGS)

# Columns of the games tables that store a list as text, e.g. "['Action', 'Indie']"
GAME_LIST_COLUMNS = ["developers", "publishers", "genres", "supported_languages"]


def load_game_table(platform: str, name: str, **overrides) -> pd.DataFrame:
    """Load one game-side table with the settings in ``GAME_READ_ARGS``.

    Parameters
    ----------
    platform, name : str
        Must be a key of ``GAME_READ_ARGS``, e.g. ``("steam", "prices")``.
    **overrides
        Replace or add ``pandas.read_csv`` arguments, e.g. ``usecols`` or ``nrows``. When ``usecols``
        leaves out a date column, also pass ``parse_dates=None``.

    Returns
    -------
    pandas.DataFrame
        The table with compact dtypes and parsed dates. List columns (``GAME_LIST_COLUMNS``) are still
        text; convert them with ``parse_list_column``.
    """
    if (platform, name) not in GAME_READ_ARGS:
        raise ValueError(f"No game-side settings for ({platform!r}, {name!r}); expected one of {GAME_SIDE_TABLES}")
    return load_table(platform, name, **{**GAME_READ_ARGS[(platform, name)], **overrides})


def parse_list_column(series: pd.Series) -> pd.Series:
    """Turn a column of lists stored as text into Python lists, keeping missing cells as ``NaN``.

    Uses ``ast.literal_eval``, which reads the text as a Python literal. Unlike counting commas
    (``count_list_items``), it handles names that contain a comma, such as ``"TALESSHOP Co., Ltd."``.

    >>> parse_list_column(pd.Series(["['Action', 'Indie']", "['TALESSHOP Co., Ltd.']", float("nan")])).tolist()
    [['Action', 'Indie'], ['TALESSHOP Co., Ltd.'], nan]
    """
    return series.map(ast.literal_eval, na_action="ignore")
