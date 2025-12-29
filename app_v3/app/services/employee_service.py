import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/employees.csv")

def load_employees():
    return pd.read_csv(DATA_PATH)

def clean_employees(df):
    df["hire_date"] = pd.to_datetime(df["hire_date"])
    df["active"] = df["active"].astype(bool)
    return df

def salary_by_department(df):
    return (
        df[df["active"]]
        .groupby("department", as_index=False)["salary"]
        .mean()
        .round(2)
    )
