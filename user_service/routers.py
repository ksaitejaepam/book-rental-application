from fastapi import APIRouter
from schemas import UserCreate, UserResponse, UserLogin, Token
from services import create_user, authenticate_user

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register_user(user_data: UserCreate):
    return await create_user(user_data)

@router.post("/login", response_model=Token)
async def login_user(user_data: UserLogin):
    return await authenticate_user(user_data)


