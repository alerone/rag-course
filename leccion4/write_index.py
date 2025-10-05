from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

current_folder = os.path.dirname(os.path.abspath(__file__))

model = SentenceTransformer("all-MiniLM-L6-v2")
K = 3

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

embeddings = model.encode(recipes, convert_to_numpy=True)
embeddings = np.array(embeddings, dtype="float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss.write_index(index, os.path.join(current_folder, "my_faiss_index.faiss"))
