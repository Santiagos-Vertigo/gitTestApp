from pathlib import Path

# -------------------------------------------------------------------
# 1. Anchor paths to the script location (PROJECT-SAFE METHOD)
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
MY_DATA = BASE_DIR / "data" / "raw"

print("=== DATA DIRECTORY ===")
print(MY_DATA)

# -------------------------------------------------------------------
# 2. List all items in the data directory
# -------------------------------------------------------------------
print("\n=== DIRECTORY CONTENTS ===")
for item in MY_DATA.iterdir():
    print(item.name)

# -------------------------------------------------------------------
# 3. Distinguish files vs directories
# -------------------------------------------------------------------
print("\n=== FILE TYPES ===")
for item in MY_DATA.iterdir():
    if item.is_file():
        print(f"FILE: {item.name}")
    elif item.is_dir():
        print(f"DIR : {item.name}")

# -------------------------------------------------------------------
# 4. Filter only CSV files
# -------------------------------------------------------------------
csv_files = [f for f in MY_DATA.iterdir() if f.is_file() and f.suffix == ".csv"]

print("\n=== CSV FILES ===")
for f in csv_files:
    print(f.name)

# -------------------------------------------------------------------
# 5. Inspect file metadata (size only, no content)
# -------------------------------------------------------------------
print("\n=== CSV FILE SIZES ===")
for f in csv_files:
    size_kb = f.stat().st_size / 1024
    print(f"{f.name:30} {size_kb:8.1f} KB")

# -------------------------------------------------------------------
# 6. Select a target file intentionally
# -------------------------------------------------------------------
target = MY_DATA / "employees.csv"
print(f"\n=== TARGET FILE ===\n{target.name}")

# -------------------------------------------------------------------
# 7. Preview file contents (first 5 lines)
# -------------------------------------------------------------------
print("\n=== FILE PREVIEW (FIRST 5 LINES) ===")
with open(target, "r", encoding="utf-8") as f:
    for _ in range(5):
        print(f.readline().rstrip())

# -------------------------------------------------------------------
# 8. Count total lines (record size check)
# -------------------------------------------------------------------
line_count = 0
with open(target, "r", encoding="utf-8") as f:
    for _ in f:
        line_count += 1

print(f"\nTotal lines in {target.name}: {line_count}")

# -------------------------------------------------------------------
# 9. Create a derived output file (safe manipulation)
# -------------------------------------------------------------------
preview_file = MY_DATA / "employees_preview.txt"

with open(preview_file, "w", encoding="utf-8") as out:
    out.write("Preview of employees.csv\n")
    out.write("-------------------------\n")

    with open(target, "r", encoding="utf-8") as src:
        for _ in range(5):
            out.write(src.readline())

print(f"\nCreated preview file: {preview_file.name}")

# -------------------------------------------------------------------
# 10. Rename the derived file
# -------------------------------------------------------------------
renamed_file = MY_DATA / "employees_preview_renamed.txt"
preview_file.rename(renamed_file)

print(f"Renamed preview file to: {renamed_file.name}")

# -------------------------------------------------------------------
# 11. (Optional) Move file to an archive directory
# -------------------------------------------------------------------
archive_dir = MY_DATA / "archive"
archive_dir.mkdir(exist_ok=True)

archived_file = archive_dir / renamed_file.name
renamed_file.replace(archived_file)

print(f"Moved preview file to archive/: {archived_file.name}")

# -------------------------------------------------------------------
# 12. (Optional) Delete generated file safely
# -------------------------------------------------------------------
if archived_file.exists():
    archived_file.unlink()
    print(f"Deleted archived file: {archived_file.name}")
