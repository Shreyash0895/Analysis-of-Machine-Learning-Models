import pandas as pd

def validate_dataframe(df, target_column):
    if df is None or df.empty:
        raise ValueError("❌ Uploaded dataset is empty")

    if target_column not in df.columns:
        raise ValueError(f"❌ Target column '{target_column}' not found")

    return df


