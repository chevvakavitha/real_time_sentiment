# fastapi_app/schemas.py
"""
Pydantic models for request and response bodies.
"""

from pydantic import BaseModel, Field


class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Input text in English")


class SentimentResponse(BaseModel):
    label: str = Field(..., description="Predicted sentiment label")
    score: float = Field(..., ge=0.0, le=1.0, description="Confidence score [0,1]")
