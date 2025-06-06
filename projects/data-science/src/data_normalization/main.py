import pandas as pd

def data_normalization(csv_path: str) -> pd.DataFrame:
    """
    Reads and normalizes data from SSB-format to long format.
    Args:
        csv_path (str): Filepath to original csv
    Returns:
        pd.DataFrame: Normalized DataFrame
    """

    # Define column names
    columns = ["statistikkvariabel", "region", "kjønn", "alder",
    "2011", "2012", "2013", "2014", "2015", "2016",
    "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]

    # Read with correct seperator and encoding
    df = pd.read_csv(csv_path, sep="\t", quotechar='"', names=columns, header=None, skiprows=1, encoding="utf-8")

    # Melt broad data into long format
    df_long = df.melt(
        id_vars=["statistikkvariabel", "region", "kjønn", "alder"],
        var_name="år",
        value_name="antall"
    )

    df_long["år"] = df_long["år"].astype(int)
    df_long["antall"] = pd.to_numeric(df_long["antall"], errors="coerce")

    return df_long

#if __name__ == "__main__":

    #df = data_normalization("../data/ssb.csv")
    #print("Kolonner:", df.columns.tolist())
