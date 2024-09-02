
import chromadb
from llama_index.core import StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
import os
from dotenv import load_dotenv, dotenv_values
import logging
# Creating an object
log = logging.getLogger()

def get_vector_storage():
    #Create chroma db client
   
    if os.getenv("CHROMA_PERSISTENT") == "true":
        log.info("Using persistent chroma vector store")
        #setts = chromadb.config.Settings(is_persistent=True)
        client = chromadb.PersistentClient(os.getenv("CHROMA_DB_DIR"))
    else:
        log.info("Using non-persistent chroma vector store")
        db = chromadb.config.Settings(is_persistent=False)
        client = chromadb.Client(settings=db)

    chroma_collection = client.get_or_create_collection(os.getenv("CHROMA_COLLECTION"))
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    return storage_context