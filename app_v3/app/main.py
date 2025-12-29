from app.services.employee_service import (
    load_employees,
    clean_employees,
    salary_by_department,
)
from pathlib import Path

def main():
    df = load_employees()
    df = clean_employees(df)
    summary = salary_by_department(df)

    html_table = summary.to_html(index=False)

    template = Path("app/templates/report.html").read_text()
    output = template.replace("{{ table }}", html_table)

    output_path = Path("output.html")
    output_path.write_text(output)

    print("Report generated:", output_path.resolve())

if __name__ == "__main__":
    main()
