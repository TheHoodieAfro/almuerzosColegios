from contextlib import asynccontextmanager

from db import Base, engine
from fastapi import FastAPI
from routers import attendance


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)  # runs on startup
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(attendance.router)
