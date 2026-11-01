"""Optional browser interface — solve the nine tasks first."""
import hashlib
import os
import tempfile
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
from google import genai
from rag_assistant import RAGAssistant

load_dotenv()
st.set_page_config(page_title="My First PDF RAG", page_icon="📚")
st.title("📚 My First PDF RAG")
key = os.getenv("GEMINI_API_KEY")
if not key or key == "put_your_key_here":
    st.error("Put your Gemini API key in .env")
    st.stop()
upload = st.file_uploader("Choose a PDF containing selectable text", type="pdf")
if upload is None:
    st.stop()
data = upload.getvalue()
pdf_id = hashlib.sha256(data).hexdigest()
if st.session_state.get("pdf_id") != pdf_id:
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp:
        temp.write(data)
        path = temp.name
    try:
        with st.spinner("Reading PDF..."):
            assistant = RAGAssistant.from_pdf(path, genai.Client(api_key=key))
        st.session_state["assistant"] = assistant
        st.session_state["pdf_id"] = pdf_id
    except Exception as e:
        st.error(str(e))
        st.stop()
    finally:
        Path(path).unlink(missing_ok=True)
question = st.text_input("Ask your PDF a question")
if st.button("Ask") and question.strip():
    try:
        result = st.session_state["assistant"].ask(question)
        st.write(result["answer"])
        with st.expander("Sources"):
            for source in result["sources"]:
                st.write("Page", source["page"], source["excerpt"])
    except Exception as e:
        st.error(str(e))
