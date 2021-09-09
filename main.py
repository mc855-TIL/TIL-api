from fastapi import FastAPI
# import pydantic
app = FastAPI()

@app.get('/')
def index():
    return {'key': 'value'}