# main.py

from fastapi import FastAPI
from tortoise import Tortoise
from routers.survey_routes import router as survey_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()

@app.on_event("shutdown")
async def shutdown():
    await Tortoise.close_connections()

app.include_router(survey_router, prefix="/api")
