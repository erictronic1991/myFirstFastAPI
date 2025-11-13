from fastapi import FastAPI
from pydantic import BaseModel
from app.db import init_db, save_question

app = FastAPI(title="My First FastAPI")

class Query(BaseModel):
    question: str

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def home():
    return {"message": "Hello from myFirstFastAPI"}

@app.post("/ask")
def ask(query: Query):
    save_question(query.question)
    return {"status": "saved", "question": query.question}
