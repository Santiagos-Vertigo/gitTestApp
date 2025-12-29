from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.services.employees import load_and_clean_employees

app = FastAPI(title="Employee Analytics")

templates = Jinja2Templates(directory="app/templates")


@app.get("/employees", response_class=HTMLResponse)
def employee_report(request: Request):
    df, metrics = load_and_clean_employees()

    return templates.TemplateResponse(
        "employees.html",
        {
            "request": request,
            "columns": df.columns.tolist(),
            "rows": df.to_dict(orient="records"),
            "metrics": metrics,
        },
    )
