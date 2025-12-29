import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DATA = BASE_DIR / "data" / "raw"
EMPLOYEES_FILE = RAW_DATA / "employees.csv"

def get_employee_roster():
    df = pd.read_csv(EMPLOYEES_FILE)

    # Basic Pandas usage
    df = df.rename(columns=str.lower)

    # NumPy usage
    total_employees = int(df.shape[0])
    missing_values = int(np.sum(df.isna().values))

    return {
        "total_employees": total_employees,
        "missing_values": missing_values,
        "columns": df.columns.tolist(),
        "employees": df.to_dict(orient="records")
    }
