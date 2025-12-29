from app.services.data_cleaning import clean_and_summarize
from pathlib import Path

TEMPLATE = Path("app/templates/report.html")
OUTPUT = Path("report.html")


def render_report(summary_df):
    rows = ""

    for _, row in summary_df.iterrows():
        rows += (
            f"<tr>"
            f"<td>{row['department']}</td>"
            f"<td>{row['avg_salary']:.2f}</td>"
            f"<td>{row['employee_count']}</td>"
            f"</tr>"
        )

    html = TEMPLATE.read_text()
    html = html.replace("{{rows}}", rows)

    OUTPUT.write_text(html)


if __name__ == "__main__":
    summary = clean_and_summarize()
    render_report(summary)
    print("Report generated: report.html")
