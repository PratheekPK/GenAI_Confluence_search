from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from scraper import scrape_confluence_docs
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

docs_raw = scrape_confluence_docs("https://confluence.atlassian.com/alldoc/atlassian-documentation-32243719.html")
documents = [Document(page_content=doc['text'], metadata={"source": doc['url']}) for doc in docs_raw]

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(split_docs, embeddings)
db.save_local("atlassian_docs_faiss")