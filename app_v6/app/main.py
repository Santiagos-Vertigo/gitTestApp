from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.services.data_cleaning import clean_employee_data

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def report(request: Request):
    df = clean_employee_data()
    records = df.to_dict(orient="records")

    return templates.TemplateResponse(
        "report.html",
        {
            "request": request,
            "employees": records
        }
    )
