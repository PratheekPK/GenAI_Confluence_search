# app.py
import streamlit as st
from rag_chain import load_rag_chain

st.set_page_config(page_title="Confluence AI Assistant (Open Source)")
st.title("Confluence Documentation Assistant (OSS)")

st.markdown(
    "Ask any technical question about Atlassian Confluence, Jira, or Bitbucket documentation. "
    "Powered by open-source LLMs and sentence-transformer embeddings."
)

@st.cache_resource
def get_chain():
    return load_rag_chain()

qa_chain = get_chain()

query = st.text_input("What would you like to know?", placeholder="e.g. What is confluence Cloud?")

if query:
    with st.spinner("Searching documentation..."):
        result = qa_chain.invoke(query)
        answer = result['result']
        sources = result['source_documents']

    st.markdown("###Answer")
    st.write(answer)

    st.markdown("---")
    st.markdown("###Sources")
    for doc in sources:
        url = doc.metadata.get("source", "Unknown")
        st.markdown(f"[{url}]({url})")

st.markdown("---")
st.markdown("Built using Hugging Face + LangChain + Streamlit")
