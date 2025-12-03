# streamlit_app/app.py
"""
Streamlit frontend for the Real-Time NLP Sentiment API.
"""

import os
import textwrap

import requests
import streamlit as st

# 👇 You can change this when backend is deployed
DEFAULT_API_URL = "https://real-time-sentiment.onrender.com"
API_URL = os.getenv("API_URL", DEFAULT_API_URL).rstrip("/")

st.set_page_config(
    page_title="Real-Time Sentiment Analysis",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Real-Time NLP Sentiment Analysis")
st.markdown(
    """
This app talks to a **FastAPI backend** that uses a **Transformer model**  
to classify your text as **POSITIVE** or **NEGATIVE** in real time.
"""
)

with st.sidebar:
    st.header("⚙️ Settings")
    max_chars = st.slider(
        "Maximum input characters",
        min_value=100,
        max_value=2000,
        value=600,
        step=100,
    )
    st.markdown(f"API URL: `{API_URL}`")

default_text = "I really love how easy this app is to use, it's amazing!"
user_text = st.text_area(
    "Enter text here:",
    value=default_text,
    height=200,
    max_chars=max_chars,
)

if st.button("🔍 Analyze sentiment"):
    if not user_text.strip():
        st.warning("Please enter some text first 🙏")
    else:
        try:
            with st.spinner("Talking to the model..."):
                resp = requests.post(
                    f"{API_URL}/predict",
                    json={"text": user_text},
                    timeout=30,
                )
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            st.error(f"Error calling API: {e}")
        else:
            label = data["label"]
            score = float(data["score"])

            if label == "POSITIVE":
                emoji = "😊"
            elif label == "NEGATIVE":
                emoji = "😞"
            else:
                emoji = "😐"

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Result")
                st.metric("Sentiment", label, delta=None)
                st.metric("Confidence", f"{score:.2%}")
                st.progress(score)

            with col2:
                st.subheader("Input preview")
                st.code(
                    textwrap.shorten(
                        user_text, width=300, placeholder=" ... (trimmed)"
                    ),
                    language="text",
                )

            st.caption(
                "Backend: FastAPI + Transformers • "
                "Model: distilbert-base-uncased-finetuned-sst-2-english"
            )
else:
    st.info("Type some text and click **Analyze sentiment**.")

