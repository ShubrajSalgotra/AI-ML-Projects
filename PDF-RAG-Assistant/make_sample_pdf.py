"""Create a fun 2-page practice PDF."""
from pathlib import Path
import pymupdf

PAGES = [
    ("Space Camp: Solar System", [
        "Earth is the third planet from the Sun.",
        "Jupiter is the biggest planet in the solar system.",
        "Mars is the Red Planet.",
        "Saturn has beautiful rings.",
        "Mercury is closest to the Sun.",
    ]),
    ("Space Camp: Class Information", [
        "Our teacher is Maya.",
        "Space camp starts at 9 AM on Monday.",
        "Students should bring a blue notebook and a pencil.",
        "We make paper rockets on Monday.",
        "The camp ends at 2 PM.",
    ]),
]

def main():
    pdf = pymupdf.open()
    for title, facts in PAGES:
        page = pdf.new_page()
        page.insert_text((45, 55), title, fontsize=17)
        for i, fact in enumerate(facts):
            page.insert_text((45, 95 + i * 35), fact, fontsize=11)
    path = Path(__file__).with_name("space_camp.pdf")
    pdf.save(path)
    pdf.close()
    print("Created", path)

if __name__ == "__main__":
    main()
