# backend/routes.py

from fastapi import APIRouter, HTTPException
from models import Survey
from schemas import Survey, SurveyCreate

router = APIRouter()

@router.post("/surveys/", response_model=Survey)
async def create_survey(survey: SurveyCreate):
    survey_obj = await Survey.create(**survey.dict())
    return survey_obj

@router.get("/surveys/{survey_id}", response_model=Survey)
async def read_survey(survey_id: int):
    survey_obj = await Survey.get_or_none(id=survey_id)
    if survey_obj is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey_obj
