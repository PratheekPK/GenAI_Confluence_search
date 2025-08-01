from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import SentenceTransformerEmbeddings
#from langchain_community.vectorstores import faiss
import os
from langchain_community.embeddings import HuggingFaceEmbeddings

DOC_DIR = "scraped_docs"
VECTORSTORE_DIR = "atlassian_docs_faiss"

def load_documents():
    docs = []
    for file in os.listdir(DOC_DIR):
        if file.endswith(".txt"):
            path = os.path.join(DOC_DIR, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                lines = content.splitlines()
                url = lines[0].replace("URL: ", "").strip()
                body = "\n".join(lines[2:]).strip()
                metadata = {"source": url}
                docs.append(Document(page_content=body, metadata=metadata))
    return docs

def build_index():
    docs = load_documents()
    texts = [doc.page_content for doc in docs]
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    #embeddings = embedding_model.encode(texts, convert_to_numpy=True, show_progress_bar=True)
    db = FAISS.from_documents(docs, embedding_model)
    db.save_local(VECTORSTORE_DIR)
    print(f"FAISS index saved to: {VECTORSTORE_DIR}")


