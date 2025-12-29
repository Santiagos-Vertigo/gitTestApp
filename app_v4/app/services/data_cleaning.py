import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/raw/employees.csv")
PROCESSED_FILE = Path("data/processed/employees_clean.csv")


def clean_and_summarize():
    df = pd.read_csv(RAW_FILE)

    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
    df["salary"] = df["salary"].fillna(df["salary"].mean())

    df["department"] = df["department"].str.strip()

    PROCESSED_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_FILE, index=False)

    summary = (
        df.groupby("department", as_index=False)
          .agg(
              avg_salary=("salary", "mean"),
              employee_count=("employee_id", "count")
          )
    )

    return summary
