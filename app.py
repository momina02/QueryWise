import streamlit as st
from extractor import extract_text_from_file
from vector_db import ingest_to_pinecone, search_similar_docs, vectorstore, clear_index
from chat_model import chat_with_docs


st.set_page_config(page_title="🧠 RAG Chatbot", layout="centered")
st.title("🧠 Chat with your Files")

if st.button("🔄 Refresh (Clear all documents)"):
    from vector_db import clear_index
    clear_index()
    st.success("✅ Pinecone index cleared. You can now re-upload fresh files.")

st.markdown("Upload PDFs, Word, Excel, PPT files and ask questions from them.")

uploaded_files = st.file_uploader("Upload files", type=["pdf", "docx", "xlsx", "pptx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_content = file.read()
        # extracted_text = extract_text_from_file(file_content, file.name)
        from io import BytesIO
        file_stream = BytesIO(file_content)
        extracted_text = extract_text_from_file(file_stream, file.name)

        ingest_to_pinecone([extracted_text], [{"source": file.name, "text": extracted_text}])
    st.success("✅ Files processed and indexed!")

query = st.text_input("Ask a question about your files:")

if query:
    response = chat_with_docs(query, vectorstore)
    st.write("🧠 Response:")
    st.write(response)
