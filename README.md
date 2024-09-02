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