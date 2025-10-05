from sentence_transformers import CrossEncoder, SentenceTransformer
import faiss

# -------- Modelo y Reranker (CrossEncoder) -------
model = SentenceTransformer("all-MiniLM-L6-v2")
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
# -------------------------------------------------

recipes = [
    "Paella valenciana con mariscos y pollo.",
    "Tacos al pastor con piña y salsa picante.",
    "Tortilla de patatas sin cebolla.",
    "Pizza napolitana con tomate y mozzarella fresca.",
    "Sopa de miso con tofu y algas."
]

embeddings = model.encode(recipes, convert_to_numpy=True).astype("float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

query = "Cómo hacer una tortilla de patatas?"
query_vector =  model.encode([query], convert_to_numpy=True).astype("float32")

distances, indices = index.search(query_vector, 3)

# -------- Re-Ranking -------
candidates = [recipes[i] for i in indices[0]]
pairs = [[query, doc] for doc in candidates]

scores = reranker.predict(pairs)

sorted_results = sorted(zip(candidates, scores), key = lambda x: x[1], reverse = True)

print("\nResultados re-rankeados:")
for doc, score in sorted_results:
    print(f"{doc} (score: {score:.4f})")
