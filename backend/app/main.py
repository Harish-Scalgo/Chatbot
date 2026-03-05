from fastapi import FastAPI, UploadFile, File
from app.core.guardrails import validate_input, validate_output
from app.core.router import route_query
from app.rag.pdf_loader import load_pdf
from app.rag.vector_store import create_vector_store
from app.db.database import engine
from app.db.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    text = load_pdf(file)
    create_vector_store(text)
    return {"message": "PDF processed and indexed."}

@app.post("/chat")
async def chat(query: str):
    if not validate_input(query):
        return {"response": "Only medical-related queries allowed."}

    response = route_query(query)

    if not validate_output(response):
        return {"response": "I can only provide general medical educational information."}

    return {"response": response}