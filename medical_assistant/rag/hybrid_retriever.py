from rank_bm25 import BM25Okapi
from rag.vector_store import get_vectorstore
from rag.multi_query import generate_multiple_queries
from rag.reranker import rerank_documents


def bm_result_index(queries, top_k=3):
    store = get_vectorstore()
    stored = store.get(
        include=["documents", "metadatas"]
    )

    chunk_ids = stored["ids"]
    corpus = stored["documents"]

    tokenized_corpus=[
                document.lower().split() for document in corpus
            ]
    bm25 = BM25Okapi(tokenized_corpus)

    rankings=[]
    for query in queries:

        tokenized_query = query.lower().split()

        scores = bm25.get_scores(tokenized_query)

        ranked = sorted(
            enumerate(scores),
            key=lambda item: item[1],
            reverse=True
        )
        bm_results=[]
        for rank, (index, score) in enumerate(ranked[:top_k], start=1):
            chunk_id = chunk_ids[index]
            bm_results.append((chunk_id, rank))
        rankings.append(bm_results)
    return rankings

def vector_result_index(queries, top_k=3):
    store = get_vectorstore()

    rankings=[]
    for query in queries:
        results = store._collection.query(
            query_texts=[query],
            n_results=top_k
        )
        chunk_ids = results["ids"][0]

        vectore_results=[]
        for rank, chunk_id in enumerate(chunk_ids, start=1):
            vectore_results.append((chunk_id, rank))
        rankings.append(vectore_results)
    return rankings

def reciprocal_rank_fusion(rankings, k=60):
    fusion_score = {}

    for ranking in rankings:
        for chunk_id, rank in ranking:
            fusion_score[chunk_id] = (fusion_score.get(chunk_id, 0) + 1 / (rank + k))

    ranked_results = sorted(
        fusion_score.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return ranked_results

def retrive_document(ranked_results):
    store = get_vectorstore()
    documents=[]
    for chunk_id, score in ranked_results:
        result = store.get(ids=[chunk_id])
        documents.append(result["documents"][0])
    return documents


if __name__ == "__main__":
    query = "Why am I feeling so hot?"

    queries=generate_multiple_queries(query)

    bm_results = bm_result_index(queries)
    vectore_results = vector_result_index(queries)
    rankings = bm_results + vectore_results
    ranked_results = reciprocal_rank_fusion(rankings)
    documents = retrive_document(ranked_results)
    reranked_documents = rerank_documents(query, documents, top_k=3)

    for index, query in enumerate(queries, start=1):
        print(f"Query{index}: ",query)
    print("Ranked Results:", ranked_results)
    print("\nReranked Documents:")

    for doc in reranked_documents:
        print(doc)