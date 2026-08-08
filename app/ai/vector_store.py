# Real version later: use Chroma, FAISS, or Pinecone here.
# from chromadb import Client
# client = Client()

_mock_documents_store = []  # temporary in-memory list, replaced by real vector DB

def add_to_vector_store(file_path: str, doc_type: str) -> str:
    """
    MOCK: real version chunks the document, generates embeddings,
    and stores them in a vector DB collection. Returns a collection ID.
    """
    collection_id = f"mock_collection_{len(_mock_documents_store)}"
    _mock_documents_store.append({
        "collection_id": collection_id,
        "file_path": file_path,
        "doc_type": doc_type,
    })
    return collection_id

def search_vector_store(question: str, doc_type_filter: str | None = None) -> list[dict]:
    """
    MOCK: real version embeds the question and does a similarity search
    against stored chunks. Returns matching chunks with metadata.
    """
    results = []
    for doc in _mock_documents_store:
        if doc_type_filter and doc["doc_type"] != doc_type_filter:
            continue
        results.append({
            "filename": doc["file_path"].split("/")[-1],
            "page": 1,
            "text": f"Mock relevant excerpt related to '{question}'",
        })
    return results