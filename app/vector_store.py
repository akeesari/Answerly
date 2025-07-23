import faiss
import numpy as np
from app.embedder import get_embedding

_index = None
_text_chunks = []

def initialize_vector_store(chunks: list):
    global _index, _text_chunks

    if not chunks:
        return

    embeddings = [get_embedding(chunk) for chunk in chunks]
    _text_chunks = chunks

    dimension = len(embeddings[0])
    _index = faiss.IndexFlatL2(dimension)

    np_embeddings = np.array(embeddings).astype('float32')
    _index.add(np_embeddings)

def search_similar_chunks(query_embedding, top_k=3) -> list:
    global _index, _text_chunks

    if _index is None or not _text_chunks:
        return []

    np_query = np.array([query_embedding]).astype('float32')
    distances, indices = _index.search(np_query, top_k)

    results = []
    for idx in indices[0]:
        if idx < len(_text_chunks):
            results.append(_text_chunks[idx])

    return results
