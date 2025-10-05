import faiss
from sentence_transformers import SentenceTransformer
import os 
import numpy as np

current_folder = os.path.dirname(os.path.abspath(__file__))
faiss_path = os.path.join(current_folder, "my_faiss_index.faiss")

model = SentenceTransformer("all-MiniLM-L6-v2")

recipes = [
    "Paella valenciana con mariscos y pollo.",
    "Tacos al pastor con piña y salsa picante.",
    "Sopa de miso con tofu y algas.",
    "Pizza napolitana con tomate y mozzarella fresca.",
    "Curry de pollo con arroz basmati.",
    "Spaggethi Carbonara con Guancciale",
    "Pizza Margarita",
    "Tortilla de patatas sin cebolla",
    "Pescadito frito con papas",
    "Entrecote de ternera a la plancha con salsa pimienta",
    "Trucha de río con ensalada de arroz y verduras",
]

index = faiss.read_index(faiss_path)

query = "Como se hace una paella Valenciana?"

query_vector = np.array(model.encode([query]), dtype="float32")


distances, indices = index.search(query_vector, 3)

for idx, dst in zip(indices[0],distances[0]):
    print(f"Receta: {recipes[idx]} (distancia: {dst:.4f})")


