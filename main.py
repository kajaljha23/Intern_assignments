from fastapi import FastAPI
from script.core.services.billing_services import item_router
import uvicorn
from dotenv import load_dotenv
app = FastAPI()

app.include_router(item_router)
if __name__ == '__main__':
    load_dotenv()
    uvicorn.run(app="main:app", port=1234,reload=True)

