from typing import List
from fastapi import FastAPI, HTTPException

# creating instence 
app = FastAPI()

items = ["apple", "banana", "orange"]


# get the router 
@app.get("/")
async def root():
   return items


@app.get("/item")
async def create_item(item: str):
    items.append(item)
    return items

@app.get("/item/{item_id}")
async def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")