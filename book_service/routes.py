from fastapi import APIRouter, HTTPException
from models import Book
from schemas import BookCreate, BookUpdate, BookResponse
from uuid import UUID

router = APIRouter()

# Create a new book
@router.post("/", response_model=BookResponse)
async def create_book(book_data: BookCreate):
    book = await Book.create(**book_data.dict())
    return book

# Get all books
@router.get("/", response_model=list[BookResponse])
async def get_books():
    return await Book.all()

# Get a book by ID
@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: UUID):
    book = await Book.get_or_none(id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Update a book
@router.put("/{book_id}", response_model=BookResponse)
async def update_book(book_id: UUID, book_data: BookUpdate):
    book = await Book.get_or_none(id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    await book.update_from_dict(book_data.dict())
    await book.save()
    return book

# Delete a book
@router.delete("/{book_id}")
async def delete_book(book_id: UUID):
    book = await Book.get_or_none(id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    await book.delete()
    return {"message": "Book deleted successfully"}
