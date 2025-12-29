from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.services.data_cleaning import load_and_clean

app = FastAPI(title="app_v5 – Analyst Server")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def root():
    return {"status": "app_v5 server running"}


@app.get("/report", response_class=HTMLResponse)
def report(request: Request):
    df, summary = load_and_clean()

    return templates.TemplateResponse(
        "report.html",
        {
            "request": request,
            "columns": df.columns.tolist(),
            "rows": df.to_dict(orient="records"),
            "summary": summary,
        },
    )
