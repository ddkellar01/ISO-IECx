"""Vector database wrapper using ChromaDB for ISO/IEC standard embeddings."""
import os
import chromadb
from chromadb.config import Settings

class VectorStore:
    def __init__(self):
        host = os.getenv("CHROMA_HOST", "localhost")
        port = int(os.getenv("CHROMA_PORT", "8000"))
        self.client = chromadb.HttpClient(host=host, port=port, settings=Settings(allow_reset=True))
        self.collection = self.client.get_or_create_collection(name="iso_iec_standards")

    def upsert_standard(self, standard_id: str, metadata: dict, analysis: str):
        """Stores standard metadata and Gemini analysis embeddings."""
        self.collection.upsert(
            documents=[analysis],
            metadatas=[metadata],
            ids=[f"ISO-{standard_id}"]
        )

    def search_similar(self, query: str, n_results: int = 3):
        """Queries the vector store for matching compliance concepts."""
        return self.collection.query(query_texts=[query], n_results=n_results)
