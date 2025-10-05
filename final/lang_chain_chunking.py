from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_file(file_path, chunk_size = 300, chunk_overlap = 50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap
    )

    with open(file_path, "r") as file:
        chunks = splitter.split_text(file.read())
    return chunks
