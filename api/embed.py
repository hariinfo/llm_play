from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.nomic import NomicEmbedding
from llama_index.embeddings.ollama import OllamaEmbedding

    
def embed_model():
    #Using embedding model hosted by Ollama
    embed_model = OllamaEmbedding(
        model_name="nomic-embed-text",
        base_url="http://localhost:11434",
        ollama_additional_kwargs={"mirostat": 0},
    )

    # using embedding model from hugging face
    #embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    #embed_model = NomicEmbedding(model_name="nomic-embed-text")

    return  embed_model