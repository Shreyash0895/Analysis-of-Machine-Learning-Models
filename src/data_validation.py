import pandas as pd
import os

def validate_dataset(file_path, target_column):

    if not os.path.exists(file_path):
        raise FileNotFoundError("❌ Dataset file not found")

    if os.path.getsize(file_path) == 0:
        raise ValueError("❌ Dataset file is empty")

    df = pd.read_csv(file_path)

    if df.shape[1] == 0:
        raise ValueError("❌ Dataset has no columns")

    if target_column not in df.columns:
        raise ValueError("❌ Target column not found")

    if df.shape[0] < 100:
        raise ValueError("❌ Dataset has too few rows")

    return df
