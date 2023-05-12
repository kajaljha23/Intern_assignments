from fastapi import FastAPI
from scripts.core.handlers.library_handler import create_book1, get_all_data, get_book_id, update_book, delete_book
from scripts.schemas.models import Book
app = FastAPI()


@app.post("/books/")
def create_book(book: Book):
    return create_book1(book)


@app.get("/")
async def fetch_data(book: Book):
    return get_all_data(book)


@app.get("/book_based_on_id/{id}")
async def fetch_book_id(book_id: int):
    return get_book_id(book_id)


@app.put("/books/{book_id}")
def change_book(book_id: int, book: Book):
    return update_book(book_id, book)


@app.delete("/books/{book_id}")
def remove_book(book_id: int):
    return delete_book(book_id)
