from app.rag.vector_store import load_vector_store
from app.llm.model_loader import generate_response
from app.core.prompts import MEDICAL_SYSTEM_PROMPT

def route_query(query):
    db = load_vector_store()

    if db:
        docs = db.similarity_search(query, k=3)
        context = "\n".join([d.page_content for d in docs])
        prompt = f"{MEDICAL_SYSTEM_PROMPT}\nContext:\n{context}\nQuestion:{query}"
    else:
        prompt = f"{MEDICAL_SYSTEM_PROMPT}\nQuestion:{query}"

    return generate_response(prompt)