"""Terminal version of the RAG chatbot."""
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from rag_assistant import RAGAssistant

def main():
    load_dotenv()
    key = os.getenv("GEMINI_API_KEY")
    if not key or key == "put_your_key_here":
        print("First add your Gemini API key in .env")
        return
    default_path = Path(__file__).with_name("space_camp.pdf")
    path = input(f"PDF path [Enter for {default_path}]: ").strip() or str(default_path)
    if not Path(path).is_file():
        print("PDF missing. Run: python make_sample_pdf.py")
        return
    try:
        client = genai.Client(api_key=key)
        assistant = RAGAssistant.from_pdf(path, client)
        print("Ready! Ask anything about your PDF. Type exit to stop.")
        while True:
            question = input("You: ").strip()
            if question.lower() == "exit":
                break
            if not question:
                continue
            result = assistant.ask(question)
            print("AI:", result["answer"])
            print("Pages used:", sorted(set(c["page"] for c in result["sources"])))
    except NotImplementedError as e:
        print("Complete this puzzle first:", e)
    except Exception as e:
        print("Problem:", e)

if __name__ == "__main__":
    main()
