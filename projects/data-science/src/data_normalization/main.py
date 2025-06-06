import pandas as pd

def data_normalization(csv_path: str) -> pd.DataFrame:
    """
    Reads and normalizes data from SSB-format to long format.
    Args:
        csv_path (str): Filepath to original csv
    Returns:
        pd.DataFrame: Normalized DataFrame
    """

    # Read with correct seperator
    df = pd.read_csv(csv_path, sep=",", encoding="utf-8")

    return df
