from sentence_transformers import SentenceTransformer
from typing import List

_model = None

def load_model():
    global _model
    if _model is None:
        _model = SentenceTransformer('all-MiniLM-L6-v2')
    return _model

def get_embedding(text: str) -> List[float]:
    model = load_model()
    return model.encode(text).tolist()
