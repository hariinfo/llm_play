#Sample flask application
from fastapi import FastAPI
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()
TEMP_FOLDER = os.getenv('TEMP_FOLDER', './_temp')
os.makedirs(TEMP_FOLDER, exist_ok=True)

app = FastAPI()



@app.get("/health")
def hello():
    date = datetime.now()
    health = [
    { 'status': 'OK'},
    { 'date': date.strftime("%d/%m/%y T%H:%M:%SZ")}
]
    return health

@app.post('/embed')
def route_embed():
    return {"message": "Embedded successfully"}

@app.post('/query')
def route_query():
    return {"message": "Query successful"}