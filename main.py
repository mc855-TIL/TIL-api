from fastapi import FastAPI

# import pydantic
app = FastAPI()

db = []

@app.get('/')
def index():
    return {'key': 'value'}
