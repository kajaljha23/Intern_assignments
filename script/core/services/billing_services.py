"""Importing API Router"""
from fastapi import APIRouter
from script.utility.mongo_query import Item
from script.core.handlers.billing_handler import ItemHandler
from script.core.handlers.email_handler import send_email, Email
from script.constants.app_constants import APis
from script.exception.exception_code import Billing_ServicesException
from script.logging.logger import logger

item_router = APIRouter()


@item_router.get(APis.view_all_items_api)
def view_all_items():
    """Function to view all items"""
    try:
        logger.info("services:view_all_items")
        item_object = ItemHandler()
        return item_object.read_data()
    except Exception as e:
        logger.error(Billing_ServicesException.EX007.format(error=str(e)))
        return {"message": "failed"}


@item_router.post(APis.create_api)
def create_item(item: Item):
    """Function to create item"""
    try:
        logger.info("services:create_item")
        item_object = ItemHandler()
        return item_object.create_data(item)
    except Exception as e:
        logger.error(Billing_ServicesException.EX008.format(error=str(e)))


@item_router.put(APis.update_api)
def update_item(item_id: int, item: Item):
    """Function to update item"""
    try:
        logger.info("services:update_item")
        item_object = ItemHandler()
        return item_object.update_data(item_id, item)
    except Exception as e:
        logger.error(Billing_ServicesException.EX009.format(error=str(e)))
        return {"message": "failed"}


@item_router.delete(APis.delete_api)
def delete_item(item_id: int):
    """Function to delete item"""
    try:
        logger.info("services:delete_item")
        item_object = ItemHandler()
        return item_object.delete_data(item_id)
    except Exception as e:
        logger.error(Billing_ServicesException.EX0010.format(error=str(e)))
        return {"message": "failed"}


@item_router.post(APis.send_email)
def send_item(email: Email):
    """Function to send item"""
    try:
        logger.info("services:send_item")
        item_handler = ItemHandler()
        result = item_handler.pipeline_aggregation()
        message1 = f"total amount is {result}"
        send_email(message1, email)
        logger.info("send_item: Email Sent")
        return {"message": "email sent"}
    except Exception as e:
        logger.error(Billing_ServicesException.EX0011.format(error=str(e)))
        return {"message": "failed"}


@item_router.get(APis.get_api)
def get_billing():
    """Function to get the total billing"""
    try:
        logger.info("services:get_billing")
        item_handler = ItemHandler()
        result = item_handler.pipeline_aggregation()
        return result
    except Exception as e:
        logger.error(Billing_ServicesException.EX0012.format(error=str(e)))
        return {"message": "failed"}