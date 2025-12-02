# fastapi_app/main.py
"""
FastAPI application exposing the sentiment model as an API.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .model import predict_sentiment
from .schemas import SentimentRequest, SentimentResponse

app = FastAPI(
    title="Real-Time NLP Sentiment API",
    description=(
        "Transformer-based sentiment analysis API using "
        "distilbert-base-uncased-finetuned-sst-2-english."
    ),
    version="1.0.0",
)

# Allow Streamlit frontend / browsers to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production you can restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=SentimentResponse, tags=["Prediction"])
def predict(req: SentimentRequest):
    text = req.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text must not be empty")

    result = predict_sentiment(text)
    return SentimentResponse(**result)
