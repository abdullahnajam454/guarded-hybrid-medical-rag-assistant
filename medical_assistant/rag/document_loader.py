from langchain_community.document_loaders import PyPDFLoader, TextLoader
from pathlib import Path

DATA_DIR = Path("data")


def load_document(path: Path = DATA_DIR):
    docs = []
    for f in sorted(path.rglob("*")):
        if not f.is_file():
            continue
        suffix = f.suffix.lower()

        if suffix == ".pdf":
            pages = PyPDFLoader(str(f)).load()
            for page in pages:
                page.metadata["source_name"] = f.name
                page.metadata["total_pages"] = len(pages)
                page.metadata["page_number"] = page.metadata["page"] + 1
            docs.extend(pages)

        elif suffix in {".txt", ".md"}:
            loaded = TextLoader(str(f), encoding="utf-8").load()
            for d in loaded:
                d.metadata["source_name"] = f.name
            docs.extend(loaded)

    return docs
if __name__ == "__main__":
    docs = load_document()
    print(f"Loaded {len(docs)} documents")
    for d in docs[:3]:
        m = d.metadata
        print(m["source_name"], m.get("page_number"), "/", m.get("total_pages"))