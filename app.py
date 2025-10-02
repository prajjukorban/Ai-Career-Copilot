import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai

genai.configure(api_key="AIzaSyBMl0IeB6js1nuAFE3Dtjzn1eFN__LCfTs")

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Resume Career Guide", layout="centered")
st.title("📄 AI Career Copilot")
st.write("Upload your resume and get instant career role prediction & missing skills suggestion")

# File uploader
uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    query = text + "\n\nThis is my resume. Predict the most suitable role and tell me what skills are missing (in 2–4 lines). Be honest and act as a career guide."


    with st.spinner("Analyzing your resume..."):
        result = model.generate_content(query)
        response = result.text.strip()


    st.subheader("🔮 Career Role Prediction & Feedback")
    st.write(response)
