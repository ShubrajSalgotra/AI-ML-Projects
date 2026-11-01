"""Mission 5: Give the question and relevant clues to Gemini."""
import os

def build_prompt(question, best_chunks):
    clues = "\n\n".join(f"PAGE {c['page']}:\n{c['text']}" for c in best_chunks)
    # TASK 07: Return an f-string prompt containing {question} and {clues}.
    # Tell Gemini to use ONLY clues, and admit if the PDF doesn't say.
    raise NotImplementedError("TASK 07")

def generate_answer(client, prompt):
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    # TASK 08: client.models.generate_content(model=model, contents=prompt).
    # Save result as 'response'.
    raise NotImplementedError("TASK 08")
    return response.text or "Sorry, I couldn't answer this time."
