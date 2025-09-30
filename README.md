📘 AtlasMind (Confluence AI Assistant)

AtlasMind is an intelligent Confluence knowledge assistant built with Retrieval-Augmented Generation (RAG), FAISS vector search, and LLMs. It enables natural language querying of your Confluence knowledge base, returning accurate answers with document citations.

✨ Features

🔍 Semantic Search with FAISS – find the most relevant Confluence docs using vector similarity.

🤖 LLM-powered Q&A – integrates with Google Flan-T5 or lightweight open-source LLMs for reasoning.

📑 Source Transparency – shows the retrieved Confluence document snippets supporting each answer.

⚡ Streamlit Frontend – interactive, user-friendly UI to query and visualize results.

🛠️ Extensible – designed to easily plug in stronger LLMs or agentic AI tools.

🏗️ Project Architecture
flowchart TD
    A[User Query] --> B[Streamlit Frontend]
    B --> C[Retriever (FAISS + HuggingFace Embeddings)]
    C --> D[Relevant Confluence Docs]
    D --> E[LLM (Flan-T5 / Alt Model)]
    E --> F[Final Answer + Sources]

🚀 Installation
1. Clone Repository
git clone https://github.com/yourusername/AtlasMind.git
cd AtlasMind

2. Create Virtual Environment
conda create -n atlasmind python=3.11 -y
conda activate atlasmind

3. Install Dependencies
pip install -r requirements.txt

4. Set Up Environment Variables

Create a .env file:

HUGGINGFACEHUB_API_TOKEN=your_hf_token_here

⚡ Usage
1. Build Vectorstore
python db_creation.py

2. Run the Streamlit App
streamlit run app.py

3. Query Your Knowledge Base

Open the link in your browser.

Ask questions like:

“How do I enable SAML SSO on Confluence?”

“What are the steps to configure Jira integration?”

🔧 Configuration

Chunk Size & Overlap → Adjust in build_vectorstore.py for better retrieval.

Model Selection → Swap "google/flan-t5-base" with other models (e.g., llama.cpp, falcon, zephyr).

Retriever Parameters → Modify search_kwargs={"k": 4} to control how many docs are retrieved.

📌 Roadmap

 Add agentic AI features (e.g., auto-triaging tickets, suggesting workflows).

 Integrate with Confluence API for live updates instead of static docs.

 Support multiple LLM backends with automatic fallback.

 Deploy with Docker or Kubernetes for production use.

 Implement role-based access control for enterprise settings.

🛡️ Limitations

Currently limited by Flan-T5’s reasoning capacity on complex queries.

Large embeddings/LLMs may hit memory constraints on laptops with <32GB RAM.

Works on static data dumps (not yet real-time Confluence sync).

🤝 Contributing

Pull requests are welcome! For significant changes, please open an issue first to discuss your ideas.

📄 License

MIT License
