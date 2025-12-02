"""
Initialize the sentiment analysis FastAPI backend package.
"""

from .model import predict_sentiment

__all__ = ["predict_sentiment"]
__version__ = "1.0.0"

