from sentence_transformers import CrossEncoder

MODEL=CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
 
# Three candidate documents
documents = [
    # Fever
    "A fever is a temporary rise in body temperature, usually above 38°C (100.4°F), "
    "and is often a sign that the body is fighting an infection.",
    # Dehydration
    "Common signs of dehydration include extreme thirst, dark yellow urine, dry mouth, "
    "fatigue, dizziness, and infrequent urination. Drinking fluids helps restore balance.",
    # Medication safety
    "Always read the label before taking any medication, never exceed the recommended dose, "
    "and keep all medicines out of reach of children.",
]

def rerank_documents(question, documents, top_k=2):

    pairs = [(question, doc) for doc in documents]


    scores = MODEL.predict(pairs)

    print(f"Question: {question}")

    ranked = sorted(
        zip(documents, scores),
        key=lambda item: item[1],
        reverse=True
    )
    return ranked[:top_k]


if __name__ == "__main__":
    question = "What are the signs of dehydration in adults?"
    ranked = rerank_documents(question, documents)
    for doc, score in ranked:
        print(f"Score: {score:.4f}")
        print(f"Document: {doc}\n")

