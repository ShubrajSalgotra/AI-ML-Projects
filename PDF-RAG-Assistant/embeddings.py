"""Mission 3: Turn text into numbers (embeddings)."""
import os
from google.genai import types

def embed_texts(client, texts, task_type):
    if not texts:
        return []
    model = os.getenv("EMBEDDING_MODEL", "gemini-embedding-001")
    # TASK 04: Call client.models.embed_content:
    # model=model, contents=texts,
    # config=types.EmbedContentConfig(task_type=task_type, output_dimensionality=768)
    # Store the result in 'response'.
    raise NotImplementedError("TASK 04")
    return [item.values for item in response.embeddings]
