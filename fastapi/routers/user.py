from fastapi import APIRouter

todo = APIRouter()

items = {

}
# get all items
@todo.get("/")
def home():
    return {items}

# get items by id
@todo.get("/items/{id}")
def getItems(id: int):
    return {items.id}

# post items
@todo.post("/items/{id}")
def postItems(id: int):
    return {"post success": id}