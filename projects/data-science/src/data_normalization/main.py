import pandas as pd

def data_normalization(csv_path: str) -> pd.DataFrame:
    """
    Normalizes the personality dataset.

    This dataset is already in a tidy format, 
    but contains numeric values stored as floats,
    and two categorical columns with "Yes"/"No" values.

    Missing numeric values are filled with the column
    mean and the Yes/No columns are converted to
    binary integers.

    Args:
        csv_path (str): Filepath to personality csv.

    Returns:
        pd.DataFrame: Normalized DataFrame
    """

    # Read with correct seperator
    df = pd.read_csv(csv_path, sep=",", encoding="utf-8")

    # Converting Yes/No values to binary integers
    binary_cols = ["Stage_fear", "Drained_after_socializing"]
    for col in binary_cols:
        df[col] = df[col].map({"Yes": 1, "No": 0})
        df[col] = df[col].fillna(0).astype(int)

    # Replacing empty values with column mean
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())
    
    # Labeling "personality" column as categorical
    df["Personality"] = df["Personality"].astype("category")

    return df

def feature_engineering(csvpath: str) -> pd.DataFrame:
    pass
