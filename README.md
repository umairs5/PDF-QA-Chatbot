# PDF-QA-Chatbot

A powerful AI-powered question-answering system that allows users to upload PDF documents and ask questions about their content. Built with Gradio for the web interface, LangChain for document processing, and integrated with Groq's LLM and Astra DB for efficient vector storage.

## ✨ Features

- **📤 PDF Upload & Processing**: Extract and process text from PDF documents
- **🔍 Intelligent Search**: Vector-based semantic search for relevant content
- **💬 Natural Language Q&A**: Ask questions in plain English
- **🎯 Context-Aware Responses**: Answers based on document content with source attribution
- **🌐 Web Interface**: User-friendly Gradio-based interface
- **⚡ Fast Performance**: Powered by Groq's optimized LLM infrastructure

## 🏗️ Architecture

```
PDF Upload → Text Extraction → Text Chunking → Vector Embeddings → Astra DB
                                                                        ↓
User Question → Semantic Search → Context Retrieval → LLM Processing → Answer
```

## 🛠️ Tech Stack

- **Frontend**: Gradio
- **Document Processing**: PyPDF2, LangChain
- **Embeddings**: HuggingFace Transformers (sentence-transformers/all-MiniLM-L6-v2)
- **Vector Database**: Astra DB (Cassandra)
- **LLM**: Groq (Llama 3.1 8B Instant)
- **Environment Management**: python-dotenv

## 📋 Prerequisites

Before running this application, you'll need:

1. **Python 3.8+**
2. **Astra DB Account**: Sign up at [astra.datastax.com](https://astra.datastax.com)
3. **Groq API Key**: Get your API key from [groq.com](https://groq.com)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/pdf-qa-chatbot.git
   cd pdf-qa-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   ASTRA_DB_APPLICATION_TOKEN=your_astra_db_token
   ASTRA_DB_ID=your_astra_db_id
   GROQ_API_KEY=your_groq_api_key
   ```

## 📦 Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
gradio>=4.0.0
PyPDF2>=3.0.1
langchain>=0.1.0
langchain-huggingface>=0.0.3
langchain-groq>=0.1.0
cassio>=0.1.0
python-dotenv>=1.0.0
sentence-transformers>=2.2.0
```

## 🔧 Configuration

### Astra DB Setup

1. Create a new database at [astra.datastax.com](https://astra.datastax.com)
2. Generate an Application Token with Database Administrator permissions
3. Copy your Database ID from the database dashboard
4. Add these credentials to your `.env` file

### Groq API Setup

1. Sign up at [groq.com](https://groq.com)
2. Generate an API key from your dashboard
3. Add the API key to your `.env` file

## 🎯 Usage

1. **Start the application**
   ```bash
   python main.py
   ```

2. **Open your browser**
   
   Navigate to `http://localhost:7860` (or the URL shown in terminal)

3. **Upload a PDF**
   - Click "Choose PDF file" and select your document
   - Click "Upload and Process" to process the document

4. **Ask questions**
   - Type your question in the text box
   - Click "Ask" or press Enter
   - Get AI-powered answers based on your document content

## 💡 Example Questions

- "What is the main topic of this document?"
- "Can you summarize the key points?"
- "What are the conclusions or recommendations?"
- "Are there any specific dates or numbers mentioned?"
- "Who are the main people or organizations discussed?"

## 📁 Project Structure

```
pdf-qa-chatbot/
├── main.py              # Main application file with Gradio interface
├── utils.py             # Utility functions for PDF processing and LLM setup
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## 🔍 How It Works

1. **Document Processing**: 
   - PDF text is extracted using PyPDF2
   - Text is cleaned and split into manageable chunks
   - Chunks are converted to vector embeddings

2. **Vector Storage**: 
   - Embeddings are stored in Astra DB for fast retrieval
   - Semantic search finds relevant content chunks

3. **Question Answering**: 
   - User questions are matched against document chunks
   - Relevant context is sent to Groq's LLM
   - AI generates answers based on document content

## ⚙️ Customization

### Adjusting Chunk Size
In `utils.py`, modify the `CharacterTextSplitter` parameters:
```python
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=800,        # Increase for longer chunks
    chunk_overlap=200,     # Adjust overlap as needed
    length_function=len
)
```

### Changing the LLM Model
In `utils.py`, update the model name:
```python
return ChatGroq(
    model="llama-3.1-70b-versatile",  # Use different Groq model
    temperature=0,
    api_key=GROQ_API_KEY
)
```

### Modifying Search Results
In `main.py`, adjust the number of search results:
```python
result = vectorstore.similarity_search_with_score(query, k=5)  # Get more results
```

## 🐛 Troubleshooting

### Common Issues

1. **"Missing required environment variable"**
   - Ensure all environment variables are set in your `.env` file
   - Check for typos in variable names

2. **"Failed to initialize LLM"**
   - Verify your Groq API key is valid
   - Check your internet connection

3. **"No text could be extracted from PDF"**
   - Ensure the PDF contains readable text (not just images)
   - Try with a different PDF file

4. **Vector store connection issues**
   - Verify Astra DB credentials
   - Check if your database is active

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Gradio](https://gradio.app/) for the amazing UI framework
- [LangChain](https://langchain.com/) for document processing tools
- [Groq](https://groq.com/) for fast LLM inference
- [DataStax Astra](https://astra.datastax.com/) for vector database services
- [HuggingFace](https://huggingface.co/) for embedding models

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/pdf-qa-chatbot/issues) page
2. Create a new issue with detailed information
3. Include error messages and system information

---

⭐ **Star this repository if you find it helpful!**
