"""Loaders for the raw tables in ``data/raw``."""
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
