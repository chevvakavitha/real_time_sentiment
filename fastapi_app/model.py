# fastapi_app/model.py
"""
Model loading & prediction logic for sentiment analysis.
"""

from functools import lru_cache
from transformers import pipeline


@lru_cache(maxsize=1)
def get_model():
    """
    Load the Hugging Face transformer model once and cache it.
    First call will download the model, later calls are fast.
    """
    sentiment_pipe = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
    )
    return sentiment_pipe


def predict_sentiment(text: str) -> dict:
    """
    Predict sentiment for input text.

    Returns a dict:
        {
            "label": "POSITIVE" | "NEGATIVE",
            "score": float [0, 1]
        }
    """
    text = (text or "").strip()
    if not text:
        return {"label": "NEUTRAL", "score": 0.0}

    pipe = get_model()
    result = pipe(text)[0]

    return {"label": result["label"], "score": float(result["score"])}
