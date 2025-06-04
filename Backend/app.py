from fastapi import FastAPI
from database import db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привет, ПСБ"}

@app.get("/items/add/{name}")
def add_item(name: str):
    collection = db["items"]
    collection.insert_one({"name": name})
    return {"status": "Item added"}

@app.get("/items")
def get_items():
    collection = db["items"]
    items = list(collection.find({}, {"_id": 0}))  # Не возвращаем _id
    return {"items": items}