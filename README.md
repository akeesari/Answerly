# Answerly – AI-Powered Document Search Assistant

Answerly is a simple AI proof-of-concept (POC) project that takes a natural language question and searches the content from PDF and Word documents to find relevant answers using vector embeddings and a large language model (LLM).

This project is built using Python, Streamlit, SentenceTransformers, FAISS, and OpenAI.

## Features

- Upload `.pdf` and `.docx` files into the `data/` folder
- Automatically extracts and embeds document content
- Accepts user input as a natural language question
- Uses semantic search and a large language model to answer based on document content
- Web interface powered by Streamlit

## Folder Structure

```

Answerly/
├── app/
│   ├── main.py               # Streamlit chat UI
│   ├── pipeline.py           # Query → search → LLM logic
│   ├── document_loader.py    # Extracts text from PDF and Word
│   ├── embedder.py           # Embedding logic using SentenceTransformers
│   ├── vector_store.py       # FAISS vector database
│   ├── llm.py                # OpenAI API integration
│   └── __init__.py
├── data/                     # Place your .pdf and .docx files here
├── .env                      # API keys (not checked into git)
├── requirements.txt
└── README.md

````

## Setup Instructions

1. Clone the repository or download the source.

2. Create and activate a Python virtual environment.

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Command to exit the (venv) if any issues

deactivate
````

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root folder.

```ini
OPENAI_API_KEY=your-openai-api-key
```

5. Place your `.pdf` or `.docx` files in the `data/` directory.

6. Run the Streamlit app.

```bash
python streamlit run app/main.py
```

7. Ask a question in the browser interface and see results based on your uploaded documents.

## Build and Run with Docker

Step 1: Build the Docker image

```bash
docker build -t answerly .
```

Step 2: Run the container

```bash
docker run -p 8501:8501 --env-file .env answerly
```

## Build and Run with Docker Compose

Step 1: Build and start the container

```bash
docker-compose up --build
docker-compose up   # without --build unless dependencies changed
```

Step 2: Stop the container

```bash
docker-compose down
```

## Test the App locally

Your app will be available at: http://localhost:8501

## Notes

* Make sure to keep your `.env` file safe and never commit it to public repositories.
* This project is for demonstration and learning purposes and can be extended with features like file upload, chat history, and multiple data sources.

## Other useful commands

```bash
# Confirm Streamlit is installed
pip show streamlit
pip show openai
pip install openai==0.28
pip install --upgrade openai
```

**Tech Stack Used**
--------------------------

| Layer | Technology | Purpose / Role |
| --- | --- | --- |
| **Frontend/UI** | [**Streamlit**](https://streamlit.io/) | Lightweight web-based UI for chat interaction |
| **Backend (API Logic)** | **Python** (native) | Core logic, modular pipeline, and helper code |
| **Embeddings** | [**SentenceTransformers**](https://www.sbert.net/) – `all-MiniLM-L6-v2` | Converts text into vector form (semantic embedding) |
| **Vector Store** | [**FAISS**](https://github.com/facebookresearch/faiss) | For fast similarity search between text embeddings |
| **LLM API** | [**OpenAI GPT-3.5/4**](https://platform.openai.com/) | Generates intelligent answers using context |
| **Environment Management** | `venv` (Python Virtual Environment) | Isolated environment for dependencies |
| **Secrets Management** | `python-dotenv` (`.env` file) | Load API keys like OpenAI token safely |
| **Document Parsing** | Standard Python file reading (`.txt`, `.md`) | Parses static files during development (future: PyMuPDF, python-docx, etc.) |
| **Dependency Management** | `requirements.txt` | Lists and installs Python packages |
| **Development Tools** | [**VS Code**](https://code.visualstudio.com/) | IDE for editing and debugging |

* * *

Future Expansion (Optional)
------------------------------------------------

| Tool | Use Case |
| --- | --- |
| **LangChain** | For more advanced RAG pipelines or multi-agent chat |
| **ChromaDB / Pinecone** | If you want managed or cloud-based vector DB |
| **Ollama + LLaMA3** | Run open-source LLMs locally instead of OpenAI |
| **FastAPI** | Convert backend logic into a REST API later |
| **Azure Blob / S3** | Store and fetch documents securely at scale |
| **Confluence REST API** | Pull real-time Confluence pages for dynamic indexing |

* * *

## References

- https://github.com/openai/openai-python
- https://platform.openai.com/api-keys