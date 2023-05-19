from fastapi import APIRouter
from script.core.handlers.billing_handler import ItemHandler
from script.utility.mongodb import Item
from script.core.handlers.email_handler import send_email, Email
from script.constants.app_constants import APis

item_router = APIRouter()


@item_router.get(APis.view_all_items_api)
def viewing_data():
    item_object = ItemHandler()
    return item_object.read_data()


@item_router.post(APis.create_api)
def creating_new_item(item: Item):
    item_object = ItemHandler()
    return item_object.create_data(item)


@item_router.put(APis.update_api)
def updating_things(item_id: int, item: Item):
    item_object = ItemHandler()
    return item_object.update_data(item_id, item)


@item_router.delete(APis.delete_api)
def deleting_things(item_id: int):
    item_object = ItemHandler()
    return item_object.delete_data(item_id)


@item_router.post(APis.send_api)
def send_item(email: Email):
    item_handler = ItemHandler()
    result = item_handler.pipeline_aggregation()
    message = f"total amount is {result}"
    send_email(message, email)
    return {"message": "email sent"}


@item_router.get(APis.get_api)
def total_billing():
    item_handler = ItemHandler()
    result = item_handler.pipeline_aggregation()
    return result
