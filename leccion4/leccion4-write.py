from leccion3.chunk_file import chunk_file
from leccion3.get_files_from_folder import get_files_from_folder
from sentence_transformers import SentenceTransformer 
import pickle
import numpy as np
import faiss
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
archivos_path = os.path.join(current_folder, os.pardir, "leccion3", "archivos")

files = get_files_from_folder(archivos_path)

all_chunks = []
for file in files:
    all_chunks.extend(chunk_file(file, 50, 10))

model = SentenceTransformer("all-MiniLM-L6-v2")

# Guardar los Chunks de datos pickle (guarda datos python)
with open(os.path.join(current_folder, "archivos.pkl"), "wb") as file:
    pickle.dump(all_chunks, file)

embeddings = np.array(model.encode(all_chunks), dtype="float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss.write_index(index, os.path.join(current_folder, "archivos_faiss_index.faiss"))
