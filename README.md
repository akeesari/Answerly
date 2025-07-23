# Answely – AI-Powered Document Search Assistant

Answely is a simple AI proof-of-concept (POC) project that takes a natural language question and searches the content from PDF and Word documents to find relevant answers using vector embeddings and a large language model (LLM).

This project is built using Python, Streamlit, SentenceTransformers, FAISS, and OpenAI.

## Features

- Upload `.pdf` and `.docx` files into the `data/` folder
- Automatically extracts and embeds document content
- Accepts user input as a natural language question
- Uses semantic search and a large language model to answer based on document content
- Web interface powered by Streamlit

## Folder Structure

```

Answely/
├── app/
│   ├── main.py               # Streamlit chat UI
│   ├── pipeline.py           # Query → search → LLM logic
│   ├── document\_loader.py    # Extracts text from PDF and Word
│   ├── embedder.py           # Embedding logic using SentenceTransformers
│   ├── vector\_store.py       # FAISS vector database
│   ├── llm.py                # OpenAI API integration
│   └── **init**.py
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

## Notes

* Make sure to keep your `.env` file safe and never commit it to public repositories.
* This project is for demonstration and learning purposes and can be extended with features like file upload, chat history, and multiple data sources.

## License

This project is released under the MIT License.


