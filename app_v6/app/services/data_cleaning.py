import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_FILE = BASE_DIR / "data" / "raw" / "employees.csv"
PROCESSED_FILE = BASE_DIR / "data" / "processed" / "employees_clean.csv"


def clean_employee_data():
    df = pd.read_csv(RAW_FILE)

    # minimal, safe cleaning
    df.columns = df.columns.str.lower().str.strip()
    df = df.dropna()

    PROCESSED_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_FILE, index=False)

    return df
