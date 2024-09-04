import logging
import sys
import os
from dotenv import load_dotenv, dotenv_values

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.nomic import NomicEmbedding
from llama_index.embeddings.ollama import OllamaEmbedding

from llama_index.llms.ollama import Ollama

# Chroma db vectore store imports
import chromadb
from embed import *
from get_vector_db import *
from llama_index.vector_stores.chroma import ChromaVectorStore
#from chromadb.config import DEFAULT_TENANT, DEFAULT_DATABASE, Settings

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))



#return embedding model
Settings.embed_model = get_embed_model()

#return vector store
storage_context = get_vector_storage()

#load private data from a directory
#documents = SimpleDirectoryReader(input_dir=os.getenv("INPUT_DATA_DIR")).load_data()
reader = SimpleDirectoryReader(
    input_dir=os.getenv("INPUT_DATA_DIR"),
    recursive=True,
)

documents = []
for docs in reader.iter_data():
    for doc in docs:
        # do something with the doc
        logging.info("reading docs....")
        doc.text = doc.text.upper()
        documents.append(doc)

print(len(documents))

# Ollama to run local LLM models
Settings.llm = Ollama(model=os.getenv("LLM_MODEL"), request_timeout=360.0)
#private_data_index = VectorStoreIndex.from_documents(documents)
private_data_index = VectorStoreIndex(documents, storage_context=storage_context)




query_engine = private_data_index.as_query_engine()
response = query_engine.query("Total Medicaid Enrollees in the year 2020")
print(response)




