from document_loader import load_documents
from embedder import get_embedding
from vector_store import initialize_vector_store, search_similar_chunks
from llm import query_llm

# Load and embed documents once when the app starts
documents = load_documents("data/")
initialize_vector_store(documents)

def get_answer(question: str) -> str:
    try:
        # Step 1: Embed the user's question
        question_embedding = get_embedding(question)

        # Step 2: Retrieve top-matching chunks from vector store
        top_chunks = search_similar_chunks(question_embedding, top_k=3)

        if not top_chunks:
            return "No relevant content found in the documents."

        # Step 3: Build prompt for the LLM
        context = "\n\n".join(top_chunks)
        prompt = f"Use the following context to answer the question:\n{context}\n\nQuestion: {question}"

        # Step 4: Get answer from the LLM
        answer = query_llm(prompt)
        return answer or "No answer was generated."

    except Exception as e:
        return f"An error occurred: {str(e)}"
