import openai
import weaviate
import uuid
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = weaviate.Client(os.getenv("WEAVIATE_URL"))

CLASS_NAME = "BugTicket"

# Ensure class exists
def init_class():
    if not client.schema.contains({"class": CLASS_NAME}):
        client.schema.create_class({
            "class": CLASS_NAME,
            "vectorizer": "none",
            "properties": [
                {"name": "title", "dataType": ["text"]},
                {"name": "description", "dataType": ["text"]},
                {"name": "tags", "dataType": ["text[]"]},
                {"name": "category", "dataType": ["text"]},
                {"name": "summary", "dataType": ["text"]}
            ]
        })

init_class()

def get_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response['data'][0]['embedding']

def store_ticket(title, description, result):
    vector = get_embedding(f"{title}\n{description}")
    client.data_object.create(
        {
            "title": title,
            "description": description,
            "tags": result["tags"],
            "category": result["category"],
            "summary": result["summary"],
        },
        class_name=CLASS_NAME,
        vector=vector
    )

def search_similar(query):
    vector = get_embedding(query)
    results = client.query.get(CLASS_NAME, ["title", "summary", "tags", "category"])\
        .with_near_vector({"vector": vector})\
        .with_limit(5)\
        .do()
    
    return results["data"]["Get"][CLASS_NAME]
