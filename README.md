# 🤖 Real-Time NLP Sentiment Analysis

A **production-style ML Engineer project**:

- Transformer-based sentiment analysis (DistilBERT, Hugging Face)
- FastAPI backend with documented `/predict` endpoint (Swagger)
- Streamlit frontend that calls the API
- Tests, Dockerfile, and GitHub Actions CI

---

## 🌐 Demo

- **API docs (Swagger):** _add Render URL here later_  
- **Streamlit app:** _add Streamlit Cloud URL here later_

---

## 🧠 Tech Stack

- Python 3.11
- FastAPI + Uvicorn
- Transformers (Hugging Face) – `distilbert-base-uncased-finetuned-sst-2-english`
- Streamlit
- Docker
- GitHub Actions
- Pytest

---

## ▶️ Run locally

### Backend (FastAPI)

```bash
uvicorn fastapi_app.main:app --reload
# API at http://127.0.0.1:8000
# Docs at http://127.0.0.1:8000/docs
