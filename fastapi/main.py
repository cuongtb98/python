from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime

app = FastAPI()

items = []

class item(BaseModel):
    id: int
    name: str
    age: int

# get all items
@app.get("/items")
def home():
    for i in items:
        print(i)
    return items

# get items by id
@app.get("/items/{id}")
def getItems(id: int):
    return {items.id}

# post items
@app.post("/items")
def postItems(item: item):
    items.append(item.dict())
    print(items)
    return {"save success"}