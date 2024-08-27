#Sample flask application
from flask import Flask, jsonify, request
from datetime import datetime
from dotenv import load_dotenv
import os
from embed import embed
from query import query


load_dotenv()
TEMP_FOLDER = os.getenv('TEMP_FOLDER', './_temp')
os.makedirs(TEMP_FOLDER, exist_ok=True)

app = Flask(__name__)



@app.route("/health")
def hello():
    date = datetime.now()
    health = [
    { 'status': 'OK'},
    { 'date': date.strftime("%d/%m/%y T%H:%M:%SZ")}
]
    return jsonify(health)

@app.route('/embed', methods=['POST'])
def route_embed():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    embedded = embed(file)

    if embedded:
        return jsonify({"message": "File embedded successfully"}), 200

    return jsonify({"error": "File embedded unsuccessfully"}), 400

@app.route('/query', methods=['POST'])
def route_query():
    data = request.get_json()
    response = query(data.get('query'))

    if response:
        return jsonify({"message": response}), 200

    return jsonify({"error": "Something went wrong"}), 400