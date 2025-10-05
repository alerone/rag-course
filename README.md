# 🧠 RAG Course – Building Retrieval-Augmented Generation Systems

This repository contains the complete code and lessons from a **hands-on RAG (Retrieval-Augmented Generation) course**, developed step by step with the assistance of **ChatGPT**.  
The course covers the main concepts and practical techniques behind modern RAG systems — from vector embeddings and FAISS indexing to re-ranking, vector databases, and LangChain chunking.

## 📚 Course Overview

Each lesson introduces a specific concept of RAG, with code examples and small projects to practice.  
All lessons are implemented in Python, and embeddings are built with **SentenceTransformers** and **FAISS**.

| Lesson | Topic | Commit |
|:-------|:------|:-------|
| **Lesson 2** | Simple RAG with a recipe search example | `110a9a4` |
| **Lesson 3** | Chunking text, reading files, and creating a contextual chatbot | `dd8d6cd` |
| **Lesson 4** | Saving and loading FAISS indexes and serialized chunks with pickle | `3419bad` |
| **Lesson 5** | Re-Ranking with CrossEncoder for improved response quality | `aa0930b` |
| **Lesson 6** | Introduction to Vector Databases (automatic indexing & retrieval) | `fc559a4` |
| **Final Project** | LangChain-based chunking and advanced RAG pipeline using ChatGPT | `final` |

## 🧩 Project Structure

```
.
├── final
│   ├── final_exercise.py                # Final LangChain + ChatGPT RAG example
│   └── lang_chain_chunking.py           # LangChain text splitting utilities
│
├── leccion2
│   ├── leccion2.py                      # Core example: simple RAG with recipes
│   └── leccion2-ejercicio.py            # Hands-on practice version
│
├── leccion3
│   ├── archivos/                        # Example text documents
│   │   ├── recetas.txt
│   │   ├── recetas2.txt
│   │   └── texto.txt
│   ├── chunk_file.py                    # File-level chunking utilities
│   ├── chunk_text.py                    # Chunking functions
│   ├── get_files_from_folder.py         # File loader
│   └── leccion3.py                      # RAG chatbot with context via OpenAI
│
├── leccion4
│   ├── leccion4-read.py                 # Load FAISS index and embeddings
│   ├── leccion4-write.py                # Save FAISS index and chunks
│   ├── archivos.pkl                     # Pickle with text chunks
│   ├── my_faiss_index.faiss             # FAISS index file
│   └── write_index.py / read_index.py   # Helper utilities
│
├── leccion5
│   ├── write_book_summary.py            # Store book embeddings
│   ├── reranker.py                      # CrossEncoder re-ranker
│   ├── leccion5.py                      # Main re-ranking demo
│   └── book_summaries.pkl               # Serialized summaries
│
├── leccion6
│   └── vector_db.py                     # Example using a Vector Database
│
└── requirements.txt                     # All dependencies
```

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/rag-course.git
cd rag-course
pip install -r requirements.txt
```

## ▶️ Running Examples

You can run any lesson directly using Python’s `-m` module syntax:

```bash
python -m leccion2.leccion2
```

Example for loading a saved FAISS index (Lesson 4):

```bash
python -m leccion4.leccion4-read
```

To test the final LangChain-based RAG pipeline:

```bash
python -m final.final_exercise
```

## 💡 Features Learned

- Embedding text using **SentenceTransformers**  
- Creating and searching **FAISS indexes**  
- **Chunking** documents for semantic retrieval  
- Building simple **RAG chatbots** with contextual memory  
- Storing and reloading vector indexes with **pickle**  
- **Re-ranking** search results with a CrossEncoder  
- Using **Vector Databases** for automatic storage and retrieval  
- Integrating **LangChain** and **ChatGPT** for advanced RAG workflows  

## 🧰 Requirements

Main dependencies (full list in `requirements.txt`):

- `sentence-transformers`
- `faiss-cpu`
- `numpy`
- `openai`
- `langchain`
- `python-dotenv`

## 🧑‍💻 Credits

This RAG learning project was created collaboratively with **ChatGPT** (OpenAI),  
as part of a guided course to explore **Retrieval-Augmented Generation** systems step by step.
