# 📚 My First PDF RAG Assistant

A **fill-in-the-code** RAG project for a young Python learner. The real application is mostly ready, but **9 important puzzle pieces** are intentionally left unfinished.

## How RAG works

1. **Read** the typed text in the PDF.
2. **Chunk** the text into small pieces.
3. **Embed** every chunk (turn text meaning into numbers).
4. **Retrieve** the chunks closest to the question (cosine similarity).
5. **Generate** an answer with Gemini using those chunks.

This is real embedding-based retrieval, with a plain Python list instead of a complicated vector database. The same RAG pipeline powers a terminal chatbot and a future Streamlit web app.

## Getting started

Install Python 3.10+.

```bash
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env`, add your Gemini API key, then run:

```bash
python make_sample_pdf.py
python check_progress.py
python main.py
```

An unfinished task produces `NotImplementedError` on purpose. Read **WORKSHEET.md**, complete the nine tasks in order, and run `python check_progress.py` after each one.

Once finished, ask: "Which planet is biggest?" or "Who teaches camp?" Try an impossible question to see whether AI admits that the answer isn't in the document.

## Optional: The Streamlit web app

```bash
python -m pip install -r requirements-streamlit.txt
streamlit run streamlit_app.py
```

Both interfaces import `RAGAssistant`; no RAG logic needs to be rewritten.

## Notes

- The beginner version handles **one PDF at a time**, with selectable/typed text. It does not perform OCR.
- Embeddings are made again when the PDF is loaded; there is no persistent database.
- Gemini usage may incur charges or rate limits. Model access varies: set `GEMINI_MODEL` in `.env` if needed.
- Keep your `.env` private. Never commit an actual API key.
- This is for learning, not secure production document processing.

## For the teacher

Nine TODO markers cover the actual RAG logic, and the rest is scaffolded. The hardest concept is cosine similarity; demonstrate it with short number lists first. After students understand the terminal flow, show them the included Streamlit UI.
