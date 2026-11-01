"""Mission 2: Divide a long PDF into small chunks."""
def words_from_text(text):
    # TASK 02: Split text into a list of words.
    raise NotImplementedError("TASK 02")

def make_chunks(pages, chunk_size=100, overlap=20):
    if chunk_size <= overlap or overlap < 0:
        raise ValueError("chunk_size must be bigger than overlap.")
    chunks = []
    for page in pages:
        words = words_from_text(page["text"])
        start = 0
        while start < len(words):
            end = start + chunk_size
            # TASK 03: Join words[start:end] with spaces into chunk_text.
            raise NotImplementedError("TASK 03")
            chunks.append({"page": page["page"], "text": chunk_text})
            start += chunk_size - overlap
    return chunks
