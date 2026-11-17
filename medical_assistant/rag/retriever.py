
from rag.vector_store import get_vectorstore

TOP_K = 3

MAX_DISTANCE = 0.9

def retrieve_documents(question: str):
    store = get_vectorstore()

    results = store.similarity_search_with_score(
        question,
        k=TOP_K
    )

    relevant_docs = [
        (doc, score)
        for doc, score in results
        if score <= MAX_DISTANCE
    ]

    return relevant_docs


if __name__ == "__main__":
    question = "What should I do if I have a fever?"

    docs = retrieve_documents(question)

    for index, (doc, score) in enumerate(docs, start=1):
        print(f"\nDocument {index}")
        print("Similarity distance:", score)
        print("Content:", doc.page_content)
        print("Source:", doc.metadata.get("source"))
        print("Page:", doc.metadata.get("page"))
