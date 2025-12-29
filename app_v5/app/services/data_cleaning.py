import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "raw" / "employees.csv"


def load_and_clean():
    df = pd.read_csv(DATA_FILE)

    # Basic analyst cleaning
    df.columns = df.columns.str.strip().str.lower()
    df = df.drop_duplicates()

    summary = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
    }

    return df, summary
