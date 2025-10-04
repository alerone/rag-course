def chunk_text(text, max_words = 20, overlap = 5):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = min(start + max_words, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += max_words - overlap
    return chunks



