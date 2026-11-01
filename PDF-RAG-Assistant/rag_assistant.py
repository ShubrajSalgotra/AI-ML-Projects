"""All five RAG steps connected (same class works in Streamlit)."""
from pdf_reader import read_pdf
from chunker import make_chunks
from embeddings import embed_texts
from retriever import find_best_chunks
from answer_generator import build_prompt, generate_answer

class RAGAssistant:
    def __init__(self, client, chunks):
        self.client = client
        self.chunks = chunks

    @classmethod
    def from_pdf(cls, path, client):
        pages = read_pdf(path)
        chunks = make_chunks(pages)
        if not chunks:
            raise ValueError("No chunks found in PDF.")
        vectors = embed_texts(client, [c["text"] for c in chunks], "RETRIEVAL_DOCUMENT")
        for chunk, vector in zip(chunks, vectors):
            chunk["embedding"] = vector
        return cls(client, chunks)

    def ask(self, question):
        if not question.strip():
            raise ValueError("Enter a question.")
        # TASK 09: Finish the chain:
        # question_vector = embed_texts(self.client, [question], "RETRIEVAL_QUERY")[0]
        # best_chunks = find_best_chunks(question_vector, self.chunks, top_k=3)
        # prompt = build_prompt(question, best_chunks)
        # answer = generate_answer(self.client, prompt)
        raise NotImplementedError("TASK 09")
        return {"answer": answer, "sources": [
            {"page": c["page"], "score": round(c["score"], 3), "excerpt": c["text"][:160]}
            for c in best_chunks
        ]}
