import logging
import sys

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.nomic import NomicEmbedding
from llama_index.embeddings.ollama import OllamaEmbedding

from llama_index.llms.ollama import Ollama

# Chroma db vectore store imports
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
#from chromadb.config import DEFAULT_TENANT, DEFAULT_DATABASE, Settings

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

#Using embedding model hosted by Ollama
Settings.embed_model = OllamaEmbedding(
    model_name="nomic-embed-text",
    base_url="http://localhost:11434",
    ollama_additional_kwargs={"mirostat": 0},
)

# using embedding model from hugging face
#Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
#Settings.embed_model = NomicEmbedding(model_name="nomic-embed-text")


#Create chroma db client
setts = chromadb.config.Settings(is_persistent=False)
client = chromadb.Client(settings=setts)
chroma_collection = client.get_or_create_collection("demo")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

#load private data from a directory
documents = SimpleDirectoryReader("data").load_data()

# Ollama to run local LLM models
Settings.llm = Ollama(model="llama3", request_timeout=360.0)
#private_data_index = VectorStoreIndex.from_documents(documents)
private_data_index = VectorStoreIndex(documents, storage_context=storage_context)




query_engine = private_data_index.as_query_engine()
response = query_engine.query("tell me about Zuko")
print(response)




