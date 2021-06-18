from fastapi import FastAPI
import services

app = FastAPI(title='JobBoard', version="1.0.0")

services.create_db()

@app.get('/')
def hello():
    return "hello world"