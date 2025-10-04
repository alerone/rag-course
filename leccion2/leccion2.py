from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Paella valenciana con mariscos y pollo.",
    "Tacos al pastor con piña y salsa picante.",
    "Sopa de miso con tofu y algas.",
    "Pizza napolitana con tomate y mozzarella fresca.",
    "Curry de pollo con arroz basmati."
]

embeddings = model.encode(documents, convert_to_numpy=True)
embeddings = np.array(embeddings, dtype="float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

query = "quiero una receta de arroz con pollo"
query_vector = model.encode([query])
query_vector = np.array(query_vector, dtype="float32")


k = 2
distances, indices = index.search(query_vector, k)

for idx, distance in zip(indices[0], distances[0]):
    print(f"resultado: {documents[idx]} (distancia: {distance:.4f})")
