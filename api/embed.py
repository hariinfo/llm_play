from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.nomic import NomicEmbedding
from llama_index.embeddings.ollama import OllamaEmbedding
import os
from dotenv import load_dotenv, dotenv_values

#loading variables from .env file   
load_dotenv()

def get_embed_model():

    #Using embedding model hosted by Ollama
    embed_model = OllamaEmbedding(
        model_name=os.getenv("TEXT_EMBEDDING_MODEL"),
        base_url=os.getenv("OLLAMA_BASE_URL"),
        ollama_additional_kwargs={"mirostat": 0},
    )

    # using embedding model from hugging face
    #embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    #embed_model = NomicEmbedding(model_name="nomic-embed-text")

    return  embed_model