from fastapi import FastAPI

app = FastAPI(title='JobBoard', version="1.0.0")

@app.get('/')
def hello():
    return "hello world"