from fastapi import FastAPI
from sqlalchemy.orm import Session
from models import Item, Base
from database import engine, SessionLocal

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Тест проекта"}

@app.get("/items")
def read_items():
    db = SessionLocal()
    items = db.query(Item).all()
    return {"items": [item.name for item in items]}

@app.get("/items/add/{name}")
def add_item(name: str):
    db = SessionLocal()
    new_item = Item(name=name)
    db.add(new_item)
    db.commit()
    return {"status": "Item added"}