"""Small helpers shared by the notebooks."""
import pandas as pd


def report_rows(df: pd.DataFrame, step: str, n_before: int | None = None) -> pd.DataFrame:
    """Print the row count after a step that changes the data (spec 3.4).

    Parameters
    ----------
    df : pandas.DataFrame
        The table after the step.
    step : str
        Short description of the step, e.g. ``"drop games without a USD price"``.
    n_before : int, optional
        Row count before the step; when given, the change is printed too.

    Returns
    -------
    pandas.DataFrame
        ``df`` unchanged, so the call can wrap the step:
        ``df = report_rows(df.dropna(subset=["usd"]), "drop missing USD", len(df))``.
    """
    n = len(df)
    change = "" if n_before is None else f" ({n - n_before:+,} rows)"
    print(f"{step}: {n:,} rows{change}")
    return df
