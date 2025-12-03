# streamlit_app/app.py
"""
Streamlit frontend for the Real-Time NLP Sentiment Analysis project.
For the public demo we run the Transformer model directly in Streamlit
to avoid external API timeouts.
"""

import textwrap

import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Real-Time Sentiment Analysis",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Real-Time NLP Sentiment Analysis")
st.markdown(
    """
This app uses a **Transformer model** (DistilBERT)  
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
    st.caption("Model: `distilbert-base-uncased-finetuned-sst-2-english`")


# 👇 Load the model once and cache it (important for speed)
@st.cache_resource(show_spinner=True)
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
    )


classifier = load_model()

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
        with st.spinner("Running the Transformer model..."):
            result = classifier(user_text)[0]

        label = result["label"]
        score = float(result["score"])

        if label == "POSITIVE":
            emoji = "😊"
        elif label == "NEGATIVE":
            emoji = "😞"
        else:
            emoji = "😐"

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Result")
            st.metric("Sentiment", f"{label} {emoji}", delta=None)
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
            "Backend logic: Transformers pipeline • "
            "Model: distilbert-base-uncased-finetuned-sst-2-english"
        )
else:
    st.info("Type some text and click **Analyze sentiment**.")
