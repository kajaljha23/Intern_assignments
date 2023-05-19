from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient  # import mongo client to connect
from script.constants.app_constants import DBConstants

app = FastAPI()

# Creating instance of mongo client
client = MongoClient(DBConstants.DB_URI)
# Creating database
db = client[DBConstants.DB_DATABASE]
# # Creating document
billing = db[DBConstants.DB_COllECTION]


# creating class
class Item(BaseModel):
    id: int
    name: str
    quantity: int
    cost: int


def read_item():
    data = []
    for items in billing.find():
        del items['_id']
        data.append(items)
    return {
        "db": data
    }


def create_item(item: Item):
    billing.insert_one(item.dict())
    db[item.id] = item.name
    return {
        "db": db
    }


def update_item(item_id: int, item: Item):
    billing.update_one({"id": item_id}, {"$set": item.dict()})


def delete_item(item_id: int):
    billing.delete_one({"id": item_id})
    return {"message": "deleted"}


def pipeline_aggregation(pipeline: list):
    return billing.aggregate(pipeline)
