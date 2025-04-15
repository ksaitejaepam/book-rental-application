from pydantic import BaseModel
from uuid import UUID

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    available_copies: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    id: UUID

    class Config:
        orm_mode = True
