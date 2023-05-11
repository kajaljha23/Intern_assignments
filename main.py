from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from scripts.utility import mongodb
app = FastAPI()
inventory_list = []


@app.get("/")
async def hello():
    return "welcome to application"


class Inventory(BaseModel):
    category: str
    product_id: int
    product_name: Optional[str] = None
    quantity: int
    price: int


@app.post("/add_product")
async def items(inventory: Inventory):
    inventory_list.append(inventory)
    return {"Inventory": inventory_list}
