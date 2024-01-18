from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr

# creating instence 
app = FastAPI()



class Item(BaseModel):
    text: str = None
    is_done : bool = False

items = ["apple", "banana", "orange"]
# get the router 
@app.get("/")
async def root():
   return items

# get Create http://127.0.0.1:8000/item?item=%22banana%22
@app.get("/item")
async def create_item(item: Item):
    items.append(item)
    return items

# give the number of items http://127.0.0.1:8000/item?item=1 
# if not use default as 10
@app.get("/items")
async def list_items(limit: int = 10):
    return items[0:limit]


# get the item by id htttp://127.0.0.1:8000/item?item=1 
@app.get("/item/{item_id}")
async def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")