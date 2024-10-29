# survey_routes.py

from fastapi import APIRouter, HTTPException
from tortoise.contrib.pydantic import pydantic_model_creator
from models import Survey

router = APIRouter()

Survey_Pydantic = pydantic_model_creator(Survey)

@router.post("/surveys/", response_model=Survey_Pydantic)
async def create_survey(survey: Survey_Pydantic):
    survey_obj = await Survey.create(**survey.dict())
    return await Survey_Pydantic.from_tortoise_orm(survey_obj)

@router.get("/surveys/")
async def get_surveys():
    surveys = await Survey.all()
    return await Survey_Pydantic.from_queryset(surveys)

@router.get("/surveys/{survey_id}", response_model=Survey_Pydantic)
async def get_survey(survey_id: int):
    survey = await Survey.get(id=survey_id)
    return await Survey_Pydantic.from_tortoise_orm(survey)
