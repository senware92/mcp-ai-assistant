def summarize_text(query):
    words = query.split()
    return " ".join(words[:min(10, len(words))]) + "..."