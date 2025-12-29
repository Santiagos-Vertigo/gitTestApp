import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
MY_DATA = BASE_DIR / "data" / "raw"

df = pd.read_csv(MY_DATA / "employees.csv")

print("\n=== DATAFRAME LOADED SUCCESSFULLY ===")

print("\nShape:")
print(df.shape)

print("\n+++++++++++++++++++++++++++++++++++++++")

print("\nColumns:")
print(df.columns)

print("\n+++++++++++++++++++++++++++++++++++++++")

print("\nData types:")
print(df.dtypes)

print("\n+++++++++++++++++++++++++++++++++++++++")

print("\nFirst 5 rows:")
print(df.head())

print("\n+++++++++++++++++++++++++++++++++++++++")
