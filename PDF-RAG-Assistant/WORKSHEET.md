# Nine RAG coding puzzles 🎯

Our story: **Read → Break → Numbers → Find → Answer.**

Run `python check_progress.py` whenever you finish a task. Replace each `raise NotImplementedError(...)` with your code.

1. **Read a PDF** (`pdf_reader.py`): Return `page.get_text()`. Why do we save page numbers?
2. **Split text** (`chunker.py`): Turn `"hello world"` into `["hello", "world"]` with `text.split()`.
3. **Create chunks** (`chunker.py`): Use `" ".join(words[start:end])` to fill `chunk_text`.
4. **Make embeddings** (`embeddings.py`): Call `client.models.embed_content(...)`. Text meaning becomes a list of numbers.
5. **Compare vectors** (`retriever.py`): Use the given cosine similarity formula.
6. **Retrieve clues** (`retriever.py`): Sort highest score first and return `[:top_k]`.
7. **Build a prompt** (`answer_generator.py`): Include the question AND PDF clues. Ask Gemini not to guess.
8. **Generate an answer** (`answer_generator.py`): Call `client.models.generate_content(...)`.
9. **Connect everything** (`rag_assistant.py`): Make a question embedding, retrieve best chunks, build the prompt, and generate an answer.

**Try it:** Run `python make_sample_pdf.py` and `python main.py`. Ask "Which planet is biggest?", then "What is my pet dragon's name?" The second answer should say the PDF doesn't mention that.

**Teacher:** Use one task per small lesson; draw the pipeline. No database or LangChain required.
