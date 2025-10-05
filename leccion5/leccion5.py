import os
import pickle
import faiss
from openai import embeddings
from sentence_transformers import CrossEncoder, SentenceTransformer

current_folder = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_folder, "book_summaries.pkl")

with open(input_path, "rb") as file:
    summaries = pickle.load(file)

model = SentenceTransformer("all-MiniLM-L6-v2")
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
K=5

embeddings = model.encode(summaries, convert_to_numpy=True).astype("float32")
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

query = "quiero un libro sobre poesía o poemas (poemario)"
query_vector = model.encode([query], convert_to_numpy=True).astype("float32")

distances, indices = index.search(query_vector, K)

candidates = [summaries[i] for i in indices[0]]
pairs = [[query, sum] for sum in candidates]

scores = reranker.predict(pairs)
sorted_results = sorted(zip(candidates, scores), key = lambda x: x[1], reverse=True)

print("\nResultados Re-Rankeados:")
for cand, score in sorted_results:
    print(f"{cand} (score: {score:4f})")


