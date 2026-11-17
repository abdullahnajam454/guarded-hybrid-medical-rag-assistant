from rag.embeddings import get_embedding
from langchain_chroma import Chroma
from pathlib import Path

DB_DIR=Path("index/chroma_db")

def get_vectorstore():
    return Chroma(
        collection_name="docs",
        embedding_function=get_embedding(),
        persist_directory=DB_DIR
        )

