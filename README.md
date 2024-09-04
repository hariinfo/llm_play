# RAG 101
1. First, we use the embedding model to create vector embeddings for the content we want to index.
The vector embedding is inserted into the vector database, with some reference to the original content the embedding was created from.

2. When the application issues a query, we use the same embedding model to create embeddings for the query and use those embeddings to query the database for similar vector embeddings. As mentioned before, those similar embeddings are associated with the original content that was used to create them.


Original data --> Embedding model --> Vector embeddings --> Vector Database --> Query --> Similar vector embeddings --> Original Content


# Create virtual environment
$python -m venv .venv

## Activate the virtual environment on windows
$source .venv/Scripts/activate

## Install requirements
$pip install -r requirements.txt


## Run standalone llama index, chromadb, ollama example
python .\test_llama_ollama.py

## Run the app
$cd api
$flask --app app --debug run