# 🤖 Real-Time NLP Sentiment Analysis

A production-ready NLP sentiment analysis system using DistilBERT, FastAPI, and Streamlit — deployed end-to-end so users can test predictions in real time.

---
## 🚀 Live Demo

| Component | URL |
|----------|-----|
| 🌐 Streamlit Web App (Frontend) | 🔗 https://real-time-sentiment.streamlit.app/ |
| ⚙️ FastAPI Backend (Swagger Docs) | 🔗 https://real-time-sentiment.onrender.com/docs#/ |

---

## 🌟 Features
- 🔥 DistilBERT Transformer model from Hugging Face
- ⚡ FastAPI backend with `/predict` endpoint
- 🖥️ Streamlit web UI for real-time prediction
- 📦 Docker containerization
- 📁 Modular architecture (`fastapi_app + streamlit_app`)
- 🚀 Ready for CI/CD & deployment

---

## 🧠 System Architecture
User → Streamlit Web UI → FastAPI API → DistilBERT Transformer Model → Response (Sentiment + Confidence)

yaml
Copy code

---

## 🗂 Folder Structure
.
├── fastapi_app
│ ├── main.py
│ ├── model.py
│ ├── schemas.py
│ └── init.py
├── streamlit_app
│ └── app.py
├── requirements.txt
├── Dockerfile
└── README.md

yaml
Copy code

---

## 🧰 Tech Stack
| Layer | Technology |
|-------|------------|
| Language | Python 3.11 |
| Model | DistilBERT – distilbert-base-uncased-finetuned-sst-2-english |
| Backend | FastAPI + Uvicorn |
| Frontend | Streamlit |
| Containerization | Docker |
| Testing | Pytest |
| Version Control | Git + GitHub |

---

## ▶ Run Locally

## 🟦 Start Backend (FastAPI)
```bash
uvicorn fastapi_app.main:app --reload
```

## 📌 Local API documentation:
```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

---

## 🟩 Start Frontend (Streamlit)
```bash
streamlit run streamlit_app/app.py
```

---

## 🚀 Deployment Roadmap

| Task | Status |
|------|--------|
| Deploy FastAPI on Render | ⏳ completed |
| Deploy Streamlit Web App | ⏳ completed |

---

## 🌍 Real-World Use Cases

- Customer review sentiment analysis  
- Social media emotion detection  
- Brand reputation tracking  
- Customer support chat sentiment analysis  
- Product feedback monitoring  

---

## 💼 Project Highlights (Recruiter-Friendly Summary)

- Built a complete end-to-end ML application (not just a notebook)  
- Real-time inference using a Transformer (DistilBERT)  
- Modular production-like architecture with FastAPI + Streamlit  
- Seamless backend ↔ frontend ↔ model integration  
- Demonstrates strong Python + ML + API + deployment skills  

---

## 👤 Author

**Cheva Kavitha**  
🔗 LinkedIn: https://www.linkedin.com/in/cheva-kavitha/  
🔗 GitHub: https://github.com/chevvakavitha  

If you like this project, please ⭐ star the repository — it helps a lot!



