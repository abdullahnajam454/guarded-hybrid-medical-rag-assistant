from langchain_huggingface import HuggingFaceEmbeddings


EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"


def get_embedding():
    embedding = HuggingFaceEmbeddings(model_name = EMBEDDING_MODEL)
    return embedding