from openai import OpenAI
from chunk_file import chunk_file
from get_files_from_folder import get_files_from_folder
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# RAG Model
model = SentenceTransformer("all-MiniLM-L6-v2")
K = 6

load_dotenv()
openAIKey = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openAIKey)

pathToFolder = os.path.dirname(os.path.abspath(__file__))
pathToFolder = os.path.join(pathToFolder, "archivos")

files = get_files_from_folder(pathToFolder)

# Chunking files
all_chunks = []
for file in files:
    all_chunks.extend(chunk_file(file, 50, 10))

# Embeddings
embeddings = model.encode(all_chunks, convert_to_numpy=True)
embeddings = np.array(embeddings, dtype="float32")

# index with faiss
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def select_chunks(indices):
    selected = []
    for ind in indices:
        selected.append(all_chunks[ind])
    return selected


def create_prompt(user_query, chunks):
    prompt = f"""
    Pregunta: {user_query}

    Contexto:
            {'\n'.join(chunks)}

    Instrucciones: usa el contexto para responder a la pregunta del usuario
    """
    return prompt


while True:
    user_input = input("¿Qué quieres saber? (o 'salir'): ")
    if user_input == "salir":
        break

    query_vector = model.encode([user_input])
    query_vector = np.array(query_vector, dtype="float32")

    _, indices = index.search(query_vector, K)

    selected = select_chunks(indices[0])

    prompt = create_prompt(user_input, selected)
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    print(f"PROMPT:\n{prompt}RESPUESTA CHAT:\n{response.choices[0].message.content}\n")





