import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "raw" / "employees.csv"


def load_and_clean_employees():
    # Load data
    df = pd.read_csv(DATA_FILE)

    # Normalize columns
    df.columns = df.columns.str.strip().str.lower()

    # Basic cleaning
    df = df.drop_duplicates()

    # Simple metrics
    total_rows = int(df.shape[0])
    missing_cells = int(np.sum(df.isna().values))

    metrics = {
        "total_employees": total_rows,
        "missing_values": missing_cells,
    }

    return df, metrics
