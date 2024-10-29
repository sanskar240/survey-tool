# backend/schemas.py

from pydantic import BaseModel
from typing import List, Optional

class SurveyCreate(BaseModel):
    title: str
    questions: List[dict]  # Change based on your question format

class Survey(SurveyCreate):
    id: int

    class Config:
        orm_mode = True
