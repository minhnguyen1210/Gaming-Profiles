"""Loaders for the raw tables in ``data/raw``."""
import pandas as pd


def load_table(platform: str, name: str) -> pd.DataFrame:
    """Load one raw table for one platform.

    Parameters
    ----------
    platform : str
        One of ``src.config.PLATFORMS``.
    name : str
        Table name without file extension. TODO: list the valid names.

    Returns
    -------
    pandas.DataFrame
        The table as stored in ``src.config.RAW_DIR``.
    """
    raise NotImplementedError


def load_all(name: str):
    """Load table ``name`` for every platform in ``src.config.PLATFORMS``.

    Parameters
    ----------
    name : str
        Table name without file extension.

    Returns
    -------
    TODO: decide the return shape (e.g. one frame per platform, or a single
    combined frame) and document it here.
    """
    raise NotImplementedError
