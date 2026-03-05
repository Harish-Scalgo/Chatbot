import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.title("Medical AI Chatbot")

uploaded_file = st.file_uploader("Upload Medical PDF")

if uploaded_file:
    files = {"file": uploaded_file}
    res = requests.post(f"{BACKEND_URL}/upload", files=files)
    st.success(res.json()["message"])

query = st.text_input("Ask a medical question")

if st.button("Send"):
    res = requests.post(f"{BACKEND_URL}/chat", params={"query": query})
    st.write(res.json()["response"])