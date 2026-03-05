# from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from app.config import VECTOR_DB_PATH
# import os

# embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# def create_vector_store(text):
#     from langchain_text_splitters import RecursiveCharacterTextSplitter

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=150
#     )

#     docs = splitter.create_documents([text])
#     db = FAISS.from_documents(docs, embeddings)

#     db.save_local(VECTOR_DB_PATH)

# def load_vector_store():
#     if os.path.exists(VECTOR_DB_PATH):
#         return FAISS.load_local(
#             VECTOR_DB_PATH,
#             embeddings,
#             allow_dangerous_deserialization=True
#         )
#     return None
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# In-memory global DB
vector_db = None

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vector_store(text):
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    global vector_db

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    docs = splitter.create_documents([text])
    vector_db = FAISS.from_documents(docs, embeddings)


def load_vector_store():
    return vector_db