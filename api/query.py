import logging
import sys
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext
from llama_index.llms.ollama import Ollama
from embed import *
from get_vector_db import *

# Main function to handle the query process
def prompt(input):
    #return embedding model
    Settings.embed_model = get_embed_model()

    #return vector store
    storage_context = get_vector_storage()

    if input:
        #load private data from a directory
        documents = SimpleDirectoryReader("data").load_data()

        # Ollama to run local LLM models
        Settings.llm = Ollama(model=os.getenv("LLM_MODEL"), request_timeout=360.0)
        #private_data_index = VectorStoreIndex.from_documents(documents)
        private_data_index = VectorStoreIndex(documents, storage_context=storage_context)

        query_engine = private_data_index.as_query_engine()
        response = query_engine.query(input)
        return response