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

---
🚀 Real-Time NLP Sentiment Analysis (Production-Ready ML Project)

A deployment-ready AI system that performs real-time sentiment analysis using a Transformer-based NLP model and exposes predictions via a FastAPI backend with a Streamlit web interface for end-users.

This project demonstrates true ML Engineer skills — beyond notebooks — including API design, model serving, Docker, CI/CD structure, and modular code.

✨ Key Features

🔹 Transformer model (DistilBERT — auto-loaded from Hugging Face)
🔹 Real-time inference API (/predict endpoint using FastAPI)
🔹 Streamlit web UI for interactive prediction
🔹 Modular & scalable codebase (fastapi_app + streamlit_app)
🔹 Production-ready folder structure & requirements
🔹 Dockerfile for containerized deployment
🔹 CI/CD-ready repository

🧠 System Architecture
User ↔ Streamlit UI ↔ FastAPI API ↔ Transformer Model ↔ Prediction ↔ Response

🧪 API Documentation (FastAPI)
Method	Endpoint	Body	Output
POST	/predict	{"text": "I love this!"}	Sentiment + Confidence

🔗 Swagger UI (deployment coming soon)
🔗 ReDoc docs (deployment coming soon)

🌐 Web App (Streamlit)

The UI allows users to:

Enter text

Run sentiment inference

View live confidence score

🔗 Streamlit Cloud link → coming soon

📦 Tech Stack
Component	Technology
Language	Python 3.11
NLP Model	DistilBERT (Hugging Face)
Backend	FastAPI + Uvicorn
Frontend	Streamlit
Container	Docker
Testing	Pytest (test-ready repo structure)
Version Control	Git + GitHub
🗂 Folder Structure
.
├── fastapi_app
│   ├── main.py
│   ├── model.py
│   ├── schemas.py
│   └── __init__.py
├── streamlit_app
│   └── app.py
├── requirements.txt
├── Dockerfile
└── README.md

▶ Run Locally
Backend (FastAPI)
uvicorn fastapi_app.main:app --reload


Docs available locally at:

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

Frontend (Streamlit)
streamlit run streamlit_app/app.py

🚀 Deployment (Next Steps)
Deployment	Status
FastAPI on Render	pending
Streamlit Web App	pending
CI/CD (GitHub Actions)	pending

📌 Deployment links will be added to this README once live

🎯 Use Cases

✔ Customer feedback monitoring
✔ Product review classification
✔ Social media sentiment tracking
✔ Customer support emotion detection

👤 Author

Cheva Kavitha
📧 Email: (you can tell me later which email to add — placeholder for now)
🔗 LinkedIn: https://www.linkedin.com/in/cheva-kavitha/

🔗 GitHub: https://github.com/chevvakavitha

📄 License

This project is released for learning and demonstration purposes.

⭐ If you like this project, don't forget to star the repo!
