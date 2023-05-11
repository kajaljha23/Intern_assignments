from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from pymongo import MongoClient  # import mongo client to connect

# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
# Creating database
db = client.interns_b2_23

# # Creating document
inventory = db.Kajal_kumari

app = FastAPI()


@app.get("/")
async def hello():
    return "welcome to application"


class Inventory(BaseModel):
    category: str
    product_id: int
    quantity: int
    price: int


@app.post("/add_product")
async def items(inventor: Inventory):
    inventory.insert_one(inventor.dict())
    return {"Successful"}
