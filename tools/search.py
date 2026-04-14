from pathlib import Path

FILE = Path(__file__).resolve().parent.parent / "data" / "notes.txt"

def search_docs(query):
    if not FILE.exists():
        return "No data found."

    text = FILE.read_text().lower()
    chunks = text.split("\n")

    scores = []

    for chunk in chunks:
        score = sum(word in chunk for word in query.lower().split())
        scores.append((score, chunk))

    scores.sort(reverse=True)

    best = scores[0][1] if scores else "No match found"
    return best.strip()