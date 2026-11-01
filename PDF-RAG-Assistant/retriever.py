"""Mission 4: Find the best matching clues."""
import math

def cosine_similarity(a, b):
    # TASK 05: Return dot product / (length_a * length_b).
    # dot = sum(x * y for x, y in zip(a, b))
    # length_a = math.sqrt(sum(x*x for x in a))
    # length_b is similar. If a length is 0, return 0.
    raise NotImplementedError("TASK 05")

def find_best_chunks(question_vector, chunks, top_k=3):
    matches = []
    for chunk in chunks:
        score = cosine_similarity(question_vector, chunk["embedding"])
        matches.append({"page": chunk["page"], "text": chunk["text"], "score": score})
    # TASK 06: Sort by score (highest first); return first top_k matches.
    raise NotImplementedError("TASK 06")
