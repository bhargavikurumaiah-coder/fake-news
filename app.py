import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from model import predict

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="wide")

# -----------------------
# CUSTOM CSS
# -----------------------
st.markdown("""
<style>
body {
    background-color: #f0f2f6;
}
.title {
    font-size: 45px;
    font-weight: bold;
    color: #1f77b4;
}
.subtitle {
    font-size: 18px;
    color: gray;
}
.card {
    padding: 20px;
    border-radius: 10px;
    background-color: white;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# HEADER
# -----------------------
st.markdown('<p class="title">📰 Fake News Detection App</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Analyze news and detect whether it is REAL or FAKE</p>', unsafe_allow_html=True)

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.header("⚙️ App Controls")
st.sidebar.info("Enter news text and click analyze")

# -----------------------
# INPUT AREA
# -----------------------
st.markdown("## ✍️ Enter News Content")

user_input = st.text_area("Paste your news here...", height=180)

col1, col2 = st.columns(2)

analyze = col1.button("🔍 Analyze")
clear = col2.button("🗑️ Clear")

if clear:
    user_input = ""

# -----------------------
# RESULT
# -----------------------
if analyze:
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text!")
    else:
        label, fake_p, real_p = predict(user_input)

        st.markdown("## 📊 Result")

        if label == "FAKE":
            st.error(f"🚨 FAKE News ({fake_p*100:.2f}%)")
        else:
            st.success(f"✅ REAL News ({real_p*100:.2f}%)")

        # -----------------------
        # GRAPH
        # -----------------------
        st.markdown("## 📈 Confidence Graph")

        fig, ax = plt.subplots()
        categories = ["Fake", "Real"]
        values = [fake_p, real_p]

        ax.bar(categories, values)
        ax.set_ylabel("Probability")
        ax.set_title("Prediction Confidence")

        st.pyplot(fig)

        # -----------------------
        # TABLE
        # -----------------------
        df = pd.DataFrame({
            "Category": ["Fake", "Real"],
            "Probability": [fake_p, real_p]
        })

        st.markdown("## 📋 Data Table")
        st.dataframe(df)

# -----------------------
# FOOTER
# -----------------------
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")