"""Show which of the nine puzzles still need solutions."""
from pathlib import Path

TASKS = {"01":"pdf_reader.py","02":"chunker.py","03":"chunker.py","04":"embeddings.py",
         "05":"retriever.py","06":"retriever.py","07":"answer_generator.py",
         "08":"answer_generator.py","09":"rag_assistant.py"}
done = 0
for number, filename in TASKS.items():
    source = (Path(__file__).parent / filename).read_text(encoding="utf-8")
    missing = f'raise NotImplementedError("TASK {number}")' in source
    print(f"Task {number}: {'TO DO' if missing else 'DONE'} ({filename})")
    done += not missing
print(f"Completed {done}/9 tasks.")
