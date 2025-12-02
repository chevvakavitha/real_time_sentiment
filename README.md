# 🤖 Real-Time NLP Sentiment Analysis

A **production-style ML Engineer project** that performs **real-time sentiment analysis** using a **Transformer model (DistilBERT)**.  
The system runs a **FastAPI backend** for inference and a **Streamlit frontend** for user interaction — similar to modern industry ML systems.

---

## 🌟 Features
- 🔥 DistilBERT Transformer model from Hugging Face
- ⚡ FastAPI backend with `/predict` endpoint
- 🖥️ Streamlit web UI for real-time prediction
- 📦 Docker containerization
- 📁 Modular architecture (`fastapi_app + streamlit_app`)
- 🚀 Ready for CI/CD & deployment

---

## 📺 Demo (deployments coming soon)
| Component | Status |
|----------|--------|
| FastAPI Docs (Swagger) | 🔜 Link will be added after deploy |
| Streamlit Web App | 🔜 Link will be added after deploy |

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

### 1️⃣ Start Backend (FastAPI)
uvicorn fastapi_app.main:app --reload
---
API Documentation available locally:
arduino
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
---
2️⃣ Start Frontend (Streamlit)
streamlit run streamlit_app/app.py
---
🔮 Deployment Roadmap
Task	Status
Deploy FastAPI on Render	⏳ pending
Deploy Streamlit on Streamlit Cloud	⏳ pending
Add CI/CD (GitHub Actions)	⏳ pending
---
🎯 Real-World Applications
Customer review analysis
Social media sentiment monitoring
Brand perception tracking
Customer support emotion detection
Product feedback analytics
---
💼 Project Highlights (for recruiters)
Built an end-to-end ML application — not just a notebook
Converts a transformer model into a real-time inference API
Modular and scalable architecture for production
Demonstrates strong Python + ML + backend development skills
---
👤 Author
Cheva Kavitha
🔗 LinkedIn: https://www.linkedin.com/in/cheva-kavitha/
🔗 GitHub: https://github.com/chevvakavitha
📧 Email can be added on request



