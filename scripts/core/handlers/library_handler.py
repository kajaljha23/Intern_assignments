from scripts.schemas.models import Book
from scripts.utility.db import database


def create_book1(book: Book):
    database.insert(book.dict())
    return {"message": "Book created successfully"}


async def get_all_data():
    books = database.find({})
    details = []
    for book in books:
        detail = {'id': book['id'], 'title': book['title'], 'author': book['author'], 'borrowed': book['borrowed']}
        details.append(detail)
    return {"details": details}


async def get_book_id(book_id: int):
    books = database.find({})
    details = []
    for book in books:
        if book['id'] == id:
            detail = {'id': book['id'], 'title': book['title'], 'author': book['author'], 'borrowed': book['borrowed']}
            details.append(detail)
    return {"details": details}


def update_book(book_id: int, book: Book):
    result = database.update_one({"id": book_id}, {"$set": book.dict()})

    if result.modified_count > 0:
        return {"message": "Book updated successfully"}
    else:
        return {"error": "Book not found"}


# Delete a book
def delete_book(book_id: int):
    result = database.delete_one({"id": book_id})

    if result.deleted_count > 0:
        return {"message": "Book deleted successfully"}
    else:
        return {"error": "Book not found"}
