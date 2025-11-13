from fastapi import FastAPI  # We bring in FastAPI to build our little web app
from pydantic import BaseModel  # We use Pydantic to check that the data we get looks right
from app.db import init_db, save_question  # We import helpers to set up and talk to our database

app = FastAPI(title="My First FastAPI")  # This makes our app; think of it like turning the lights on

class Query(BaseModel):  # This is a simple box that says what we expect in a request
    question: str  # Inside the box, we expect a word/sentence called "question"

@app.on_event("startup")  # When the app wakes up, do something first
def startup_event():  # This is the thing we do first
    init_db()  # We set up our table in the database if it isn't there yet

@app.get("/")  # When someone visits the front door ("/"), we say hello
def home():  # This is how we say hello
    return {"message": "Hello from myFirstFastAPI"}  # We send back a small message

@app.post("/ask")  # When someone sends us a question to the /ask door
def ask(query: Query):  # We take their question and put it in our Query box to check it
    save_question(query.question)  # We write their question down in our database notebook
    return {"status": "saved", "question": query.question}  # We tell them "saved" and repeat their question back
