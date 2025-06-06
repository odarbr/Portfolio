import pandas as pd

def data_normalization(csv_path: str) -> pd.DataFrame:
    """
    Reads and normalizes data from SSB-format to long format.
    Args:
        csv_path (str): Filepath to original csv
    Returns:
        pd.DataFrame: Normalized DataFrame
    """

    # Read with correct seperator and encoding
    df = pd.read_csv(csv_path, sep=";", encoding="latin1")

    # Clean column names
    df.columns = [col.strip().replace("�", "ø").replace(" ", "_").lower() for col in df.columns]

    # Melt broad data into long format
    df_long = df.melt(
        id_vars=["statistikkvariabel", "region", "kjønn", "alder"],
        var_name="år",
        value_name="antall"
    )

    df_long["år"] = df_long["år"].astype(int)
    df_long["antall"] = pd.to_numeric(df_long["antall"], errors="coerce")

    return df_long