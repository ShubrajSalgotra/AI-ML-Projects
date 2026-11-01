"""Mission 1: Read typed words from each PDF page."""
import pymupdf

def get_page_text(page):
    # TASK 01: Return the words on this PDF page.
    # Hint: page.get_text()
    raise NotImplementedError("TASK 01")

def read_pdf(path):
    pages = []
    with pymupdf.open(path) as pdf:
        for number, page in enumerate(pdf, start=1):
            text = get_page_text(page)
            if text.strip():
                pages.append({"page": number, "text": text})
    if not pages:
        raise ValueError("Use a PDF containing selectable text.")
    return pages
