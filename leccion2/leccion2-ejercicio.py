'''
Tema: Una startup de recetas de cocina saludables.

Tu tarea:

Usa sentence-transformers + faiss (como en el ejemplo).

Crea tu propia base de datos con al menos 10 recetas en una lista.

Implementa un pequeño buscador:

El usuario escribe una consulta (por consola o en un input).

El sistema devuelve las 3 recetas más similares.

Muestra además la distancia de similitud.

(Opcional avanzado): guarda el índice FAISS en disco y recárgalo después.
'''
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

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

model = SentenceTransformer("all-MiniLM-L6-v2")

K = 3

embeddings = model.encode(recipes, convert_to_numpy=True)
embeddings = np.array(embeddings, dtype="float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

while True:
    query = input("¿Qué receta buscas? (o escribe salir): ")
    if query.lower() == "salir":
        break

    query_vector = model.encode([query])
    query_vector = np.array(query_vector, dtype="float32")

    distances, indices = index.search(query_vector, K)

    for idx, dst in zip(indices[0],distances[0]):
        print(f"Receta: {recipes[idx]} (distancia: {dst:.4f})")
