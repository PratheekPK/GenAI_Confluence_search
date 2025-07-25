import streamlit as st
from rag_chain import load_rag_chain

st.set_page_config(page_title="Confluence AI Assistant", page_icon="📘")
st.title("Confluence Documentation Assistant")

st.markdown(
    "Ask any technical question about Atlassian Confluence, Jira, or Bitbucket documentation. "
    "The assistant uses RAG (Retrieval-Augmented Generation) to fetch precise information."
)

# Load chain
@st.cache_resource
def get_chain():
    return load_rag_chain()

qa_chain = get_chain()

# User query input
query = st.text_input("🔎 What would you like to know?", placeholder="e.g. How do I enable SAML SSO in Confluence?")

if query:
    with st.spinner("Searching documentation..."):
        result = qa_chain(query)
        answer = result['result']
        sources = result['source_documents']

    st.markdown("### Answer")
    st.write(answer)

    st.markdown("---")
    st.markdown("### Sources")
    for doc in sources:
        url = doc.metadata.get("source", "Unknown")
        st.markdown(f"🔗 [{url}]({url})")

st.markdown("---")
st.markdown("Built using OpenAI + LangChain + Streamlit")
