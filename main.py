from fastapi import FastAPI
from pydantic import BaseModel

from pymongo import MongoClient  # import mongo client to connect

# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
# Creating database
db = client.interns_b2_23

# # Creating document
lib = db.Kajal_kumari

app = FastAPI()


# Model for a book
class Book(BaseModel):
    id: int
    title: str
    author: str
    borrowed: bool


class book_up(BaseModel):
    borrowed: bool


# Create a new book
@app.post("/books/")
def create_book(book: Book):
    lib.insert_one(book.dict())
    return {"message": "Book created successfully"}


# Get a book by ID

@app.get("/")
async def get_all_data():
    books = lib.find({})
    details = []
    for book in books:
        detail = {'id': book['id'], 'title': book['title'], 'author': book['author'], 'borrowed': book['borrowed']}
        details.append(detail)
    return {"details": details}


@app.get("/book_based_on_id/{id}")
async def get_book_id(id: int):
    books = lib.find({})
    details = []
    for book in books:
        if book['id'] == id:
            detail = {'id': book['id'], 'title': book['title'], 'author': book['author'], 'borrowed': book['borrowed']}
            details.append(detail)
    return {"details": details}


@app.put("/books/{book_id}")
def update_book(book_id: int, book: book_up):
    result = lib.update_one({"id": book_id}, {"$set": book.dict()})

    if result.modified_count > 0:
        return {"message": "Book updated successfully"}
    else:
        return {"error": "Book not found"}


# Delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    result = lib.delete_one({"id": book_id})

    if result.deleted_count > 0:
        return {"message": "Book deleted successfully"}
    else:
        return {"error": "Book not found"}
