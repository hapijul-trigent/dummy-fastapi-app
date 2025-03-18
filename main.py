from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
p
# Dummy database
items = {
    1: {"name": "Laptop", "price": 999.99, "description": "A gaming laptop"},
    2: {"name": "Phone", "price": 599.99, "description": "A smartphone"},
}

# Pydantic model for item validation
class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

@app.get("/")
def read_root():
    return {"message": "Welcome to Daksh-DevOps!!"}

@app.get("/items/")
def get_all_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items[item_id] = item.dict()
    return {"message": "Item added", "item": items[item_id]}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted"}
