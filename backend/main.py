from db import Base, engine
from fastapi import FastAPI
from routers import attendance, reports

app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)  # creates tables if they don't exist


app.include_router(attendance.router)
app.include_router(reports.router)
