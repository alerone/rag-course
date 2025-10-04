from chunk_text import chunk_text

READ_CHUNK_SIZE = 1024 * 1024

def chunk_file(path, max_words = 20, overlap = 5):
    selected_chunks = []
    with open(path, "r") as file:
        while True:
            read_chunk = file.read(READ_CHUNK_SIZE)
            if not read_chunk:
                break
            selected_chunks.extend(chunk_text(read_chunk, max_words, overlap))
    return selected_chunks
