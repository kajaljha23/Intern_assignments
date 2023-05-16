from fastapi import APIRouter
from script.core.handlers.billing_handler import ItemHandler
from script.utility.mongodb import Item
from script.core.handlers.email_handler import sending_email, Email

item_router = APIRouter()


@item_router.get("/")
def viewing_data():
    item_object = ItemHandler()
    return item_object.read_data()


@item_router.post("/items/")
def creating_new_item(item: Item):
    item_object = ItemHandler()
    return item_object.create_data(item)


@item_router.put("/items/{items_id}")
def updating_things(item_id: int, item: Item):
    item_object = ItemHandler()
    return item_object.update_data(item_id, item)


@item_router.delete("/delete/{items_id}/")
def deleting_things(item_id: int):
    item_object = ItemHandler()
    return item_object.delete_data(item_id)


@item_router.post("/send_email")
def sending_email(email: Email):
    item_handler = ItemHandler()
    result = item_handler.pipeline_aggregation()
    message = f"total amount is {result}"
    sending_email(message, email)
    return {"message": "email sent"}


@item_router.get("/billing-price")
def total_billing():
    item_handler = ItemHandler()
    result = item_handler.pipeline_aggregation()
    return result
