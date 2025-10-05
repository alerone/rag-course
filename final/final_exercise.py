from openai import OpenAI
from .lang_chain_chunking import chunk_file
from leccion3.get_files_from_folder import get_files_from_folder
from dotenv import load_dotenv
import faiss
from sentence_transformers import CrossEncoder, SentenceTransformer
import os

# --- OpenAI Client ---
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
K = 4

client = OpenAI(api_key=OPENAI_API_KEY)

# --- Chunking ---
current_folder = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(current_folder, os.pardir, "leccion3", "archivos")

files = get_files_from_folder(input_folder)

all_chunks = []
for file in files:
    all_chunks.extend(chunk_file(file)) # chunk_file uses lang_chain chunking

# --- Model and Reranker ---
model = SentenceTransformer("all-MiniLM-L6-v2")
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

# --- Embeddings and Index ---
embeddings = model.encode(all_chunks, convert_to_numpy=True).astype("float32")
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def create_prompt(user_query, chunks):
    prompt = f"""
    Pregunta: {user_query}

    Contexto:
            {'\n'.join(chunks)}

    Instrucciones: usa el contexto para responder a la pregunta del usuario
    """
    return prompt

while True:
    query = input("¿Que quieres buscar? (o 'salir'): ")
    if query.lower() == "salir":
        break

    query_vector = model.encode([query], convert_to_numpy=True).astype("float32")

    # --- Search with FAISS Index
    distances, indices = index.search(query_vector, K)

    # --- Re-ranking with CrossEncoder ---
    candidates = [all_chunks[i] for i in indices[0]]
    pairs = [[query, chunk] for chunk in candidates]

    scores = reranker.predict(pairs)
    sorted_results = sorted(zip(candidates, scores), key = lambda x: x[1], reverse=True)

    selected_chunks = [chnk for chnk, _ in sorted_results]

    prompt_chunks = []
    for chnk, score in sorted_results:
        if abs(score) < 3: 
            prompt_chunks.append(chnk)

    if len(prompt_chunks) == 0:
        chnk_selected, score_selected = min(sorted_results, key=lambda x: abs(x[1]))
        prompt_chunks.append(chnk_selected)
        print("WARNING -- No chunks with abs(score) lower than 3")

    # --- Prompt creation and sending ---
    prompt = create_prompt(query, prompt_chunks)
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    print(f"Re-Ranking Scores\n")
    for chnk, score in sorted_results:
        print(f"{chnk} (score: {score:4f})")

    print(f"ChatGPT Prompt\n{prompt}\n\nChatGPT Response\n{response.choices[0].message.content}")
