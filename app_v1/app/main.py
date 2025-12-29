from fastapi import FastAPI
from app.services.employees import get_employee_roster

app = FastAPI(title="Internal  Service")

@app.get("/api/employees")
def employees():
    return get_employee_roster()
