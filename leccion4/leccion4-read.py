from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os
import numpy as np


current_folder = os.path.dirname(os.path.abspath(__file__))

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index(os.path.join(current_folder, "archivos_faiss_index.faiss"))

with open(os.path.join(current_folder, "archivos.pkl"), "rb") as file:
    texts = pickle.load(file)

query = "Como hacer la pizza Napolitana?"

query_vector = np.array(model.encode([query]), dtype="float32")

distances, indices = index.search(query_vector, 3)

for ind, dist in zip(indices[0], distances[0]):
    print(f"Chunk {ind}: {texts[ind]}\t(distance: {dist})\n")
