import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.get_or_create_collection(name="recetas_saludables")

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "Tortilla de patatas sin cebolla.",
    "Paella de mariscos valenciana.",
    "Sopa miso con tofu y algas.",
    "Pizza napolitana con mozzarella fresca."
]

embeddings = model.encode(texts).tolist()

collection.add(
    documents=texts,
    embeddings=embeddings,
    metadatas=[{"type": "recipe"} for _ in texts],
    ids=[f"id_{i}" for i in range(len(texts))],
)

query = "Cómo preparar tortilla española"
query_vector = model.encode([query]).tolist()

results = collection.query(
    query_embeddings = query_vector,
    n_results = 3
)

print("\nResultados:")
for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
    print(f"- {doc} ({meta})")

