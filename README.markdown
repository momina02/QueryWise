# 🧠 RAG Chatbot: Revolutionizing Document Interaction

<div style="display: flex; gap: 10px;">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.0+-red.svg" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pinecone-VectorDB-green.svg" alt="Pinecone">
  <img src="https://img.shields.io/badge/LangChain-0.1+-orange.svg" alt="LangChain">
  <img src="https://img.shields.io/badge/Grok-LLaMA3-blueviolet.svg" alt="Grok">
  <img src="https://img.shields.io/badge/PyPDF2-3.0+-yellow.svg" alt="PyPDF2">
  <img src="https://img.shields.io/badge/pandas-2.0+-lightgreen.svg" alt="pandas">
  <img src="https://img.shields.io/badge/python--docx-1.0+-purple.svg" alt="python-docx">
  <img src="https://img.shields.io/badge/python--pptx-0.6+-pink.svg" alt="python-pptx">
</div>

Welcome to the **RAG Chatbot**, a state-of-the-art application that combines Retrieval-Augmented Generation (RAG) to transform how you interact with your documents. This project allows you to upload files (PDF, Word, Excel, PPT), extract their content, and ask questions with responses powered by a Grok language model and a Pinecone vector database. Dive into the future of document querying with an intuitive Streamlit interface!

---

## 📖 Table of Contents

- [What is RAG?](#what-is-rag)
- [How RAG Works](#how-rag-works)
- [Why Use RAG?](#why-use-rag)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [How It Works](#how-it-works)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 What is RAG?

Retrieval-Augmented Generation (RAG) is an advanced technique that enhances large language models (LLMs) by integrating external knowledge retrieval. Unlike traditional LLMs, which rely solely on pre-trained, static knowledge (frozen in time), RAG combines the parametric knowledge of an LLM with a non-parametric, updatable source like a vector database. This hybrid approach ensures responses are both contextually rich and dynamically updated.

![RAG vs Traditional LLM](rag memo.png)
_Left: Traditional LLM with frozen knowledge. Right: RAG with dynamic vector database integration._

---

## 🔍 How RAG Works

RAG operates through a seamless pipeline visualized below:

![RAG Workflow](rag flow.png)

1. **Document Loader**: Imports documents from various sources (e.g., web, uploads).
2. **Text Splitter**: Breaks documents into manageable chunks.
3. **Embedding Model**: Converts text chunks into vector representations.
4. **Vector Store**: Stores embeddings for efficient retrieval.
5. **Query Input**: User submits a question.
6. **Retriever**: Performs semantic search to find the most relevant chunks.
7. **Prompt Creation**: Combines query with relevant context.
8. **LLM**: Generates a response using the augmented prompt.

This process ensures the LLM leverages both its training and real-time document data, delivering accurate and context-specific answers.

---

## 🚀 Why Use RAG?

- **Dynamic Knowledge**: Overcomes the limitation of LLMs being "frozen in time" by incorporating up-to-date information.
- **Improved Accuracy**: Retrieves relevant context, reducing hallucinations and enhancing response quality.
- **Scalability**: Handles large document sets with efficient vector search.
- **Customization**: Tailors responses to specific document corpora, ideal for enterprise or personal use cases.
- **Cost-Effective**: Reduces the need for frequent model retraining by updating the vector store instead.

---

## ✨ Features

- **Multi-format Support**: Upload and process PDF, Word (.docx), Excel (.xlsx), and PowerPoint (.pptx) files.
- **Text Extraction**: Automatically extracts text from diverse file types.
- **Vector Search**: Leverages Pinecone for high-speed similarity search.
- **Context-Aware Chat**: Uses Grok (via LangChain) for intelligent, document-backed responses.
- **Interactive UI**: Streamlit-powered interface for seamless interaction.
- **Index Reset**: Clear the Pinecone index to start fresh with new files.

---

## 🛠 Tech Stack

- **Python**: Core programming language.
- **Streamlit**: Web app framework for the UI.
- **Pinecone**: Vector database for storing and searching embeddings.
- **LangChain**: Integrates embeddings and LLMs.
- **Grok (LLaMA3)**: Advanced language model for response generation.
- **HuggingFace Embeddings**: Uses `sentence-transformers/all-MiniLM-L6-v2` for embeddings.
- **PyPDF2, python-docx, pandas, python-pptx**: Libraries for text extraction.

---

## 🚀 Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/rag-chatbot.git
   cd rag-chatbot
   ```

2. **Install Dependencies**:
   Ensure Python 3.8+ is installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the project root and add:

   ```
   PINECONE_API_KEY=your-pinecone-api-key
   GROQ_API_KEY=your-groq-api-key
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## 📚 Usage

1. Open the app in your browser (usually `http://localhost:8501`).
2. Upload supported files (PDF, Word, Excel, PPT).
3. Wait for processing and indexing confirmation.
4. Ask a question in the text input to query the documents.
5. View the response, enhanced by document context or Grok’s knowledge.
6. Click "Refresh" to clear the index and upload new files.

---

## 📂 File Structure

```
rag-chatbot/
├── app.py                # Streamlit frontend
├── vector_db.py          # Pinecone vector database setup
├── extractor.py          # Text extraction from files
├── chat_model.py         # Chat logic with RAG pipeline
├── .env                  # Environment variables (not tracked)
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## 🔍 How It Works

1. **File Upload & Text Extraction**:

   - Users upload files via Streamlit.
   - `extractor.py` extracts text based on file type.

2. **Vector Storage**:

   - `vector_db.py` generates embeddings with HuggingFace and stores them in Pinecone.

3. **Query Processing**:

   - `chat_model.py` retrieves relevant docs via similarity search.
   - Augments the prompt with context for Grok to generate responses.

4. **Chat Interface**:
   - `app.py` provides the UI for uploads, queries, and responses.

---

## 🔑 Environment Variables

Create a `.env` file with:

```
PINECONE_API_KEY=your-pinecone-api-key
GROQ_API_KEY=your-groq-api-key
```

- Get `PINECONE_API_KEY` from [Pinecone](https://www.pinecone.io/).
- Get `GROQ_API_KEY` from [Grok](https://x.ai/api).

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
