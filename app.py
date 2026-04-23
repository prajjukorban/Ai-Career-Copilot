import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
import time
import os

genai.configure(api_key="AIzaSyBMl0IeB6js1nuAFE3Dtjzn1eFN__LCfTs")

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="AI Career Copilot", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #4CAF50;
        }
        .subtitle {
            text-align: center;
            color: #bbbbbb;
            margin-bottom: 25px;
        }
        .card {
            padding: 25px;
            border-radius: 15px;
            background-color: #161b22;
            box-shadow: 0 0 15px rgba(0,0,0,0.6);
        }
        .output-box {
            padding: 20px;
            border-radius: 12px;
            background-color: #1f2937;
            color: #e5e7eb;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🚀 AI Career Copilot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload your resume → Get Role Prediction, ATS Score & Skill Gaps</div>', unsafe_allow_html=True)

# Card

uploaded_file = st.file_uploader("📂 Upload Resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    # Show extracted text (debug / demo purpose)
    with st.expander("📄 View Extracted Resume Text"):
        st.write(text if text else "No text extracted")

    if st.button("✨ Analyze Resume"):
        
        # Progress bar animation
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        query = f"""
        This is my resume:

        {text}

        Tasks:
        1. Predict the most suitable job role
        2. Give ATS score out of 100
        3. List missing skills
        4. Give improvement tips

        Keep answer short (max 4–5 lines).
        Be honest and strict like a real career mentor.

        Format:
        Role:
        ATS Score:
        Missing Skills:
        Advice:
        """

        with st.spinner("🤖 AI is analyzing your resume..."):
            result = model.generate_content(query)
            response = result.text.strip()

        st.markdown("### 🔮 Career Insights")
        st.markdown(f'<div class="output-box">{response}</div>', unsafe_allow_html=True)

        # Download button
        st.download_button(
            label="📥 Download Report",
            data=response,
            file_name="career_report.txt",
            mime="text/plain"
        )

st.markdown('</div>', unsafe_allow_html=True)
