from fastapi import FastAPI, HTTPException, Request
from classify import classify_bug
from embed import store_ticket, search_similar
from pydantic import BaseModel
import os

app = FastAPI()

class BugTicket(BaseModel):
    title: str
    description: str

class SearchQuery(BaseModel):
    query: str

@app.post("/classify")
async def classify(ticket: BugTicket):
    result = classify_bug(ticket.title, ticket.description)
    store_ticket(ticket.title, ticket.description, result)
    return result

@app.post("/search")
async def search(query: SearchQuery):
    return search_similar(query.query)
