
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.document_loader import load_document
from rag.vector_store import get_vectorstore

DATA_DIR = Path("data")
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


def ingest(
    path: Path = DATA_DIR,
    size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP
):
    if size <= 0 or overlap < 0 or overlap >= size:
        raise ValueError("Invalid chunk size or overlap.")

    docs = load_document(path)

    if not docs:
        raise FileNotFoundError(
            f"No .pdf/.txt/.md files found in '{path}'."
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=size,
        chunk_overlap=overlap
    )

    chunks = splitter.split_documents(docs)

    chunk_ids = [
        f"chunk_{index}"
        for index in range(len(chunks))
    ]

    store = get_vectorstore()

    existing = store.get()
    if existing["ids"]:
        store.delete(ids=existing["ids"])

    store.add_documents(chunks,ids=chunk_ids)
    
    for i, chunk in enumerate(chunks[:2]):
        print(f"\nChunk {i + 1}")
        print(f"Content: {chunk.page_content}")
        print(f"MetaData: {chunk.metadata}")

    return len(chunks)


if __name__ == "__main__":
    result = ingest()
    print(f"Successfully indexed {result} chunks.")
