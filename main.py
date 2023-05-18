"""importing fastapi module"""
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from script.core.services.billing_services import item_router

app = FastAPI()

app.include_router(item_router)
if __name__ == '__main__':
    load_dotenv()
    uvicorn.run(app="main:app", host="0.0.0.0", port=1234, reload=True)
