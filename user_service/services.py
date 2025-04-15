from fastapi import HTTPException
from models import User
from schemas import UserCreate, UserLogin
from auth import hash_password, verify_password, create_access_token

async def create_user(user_data: UserCreate):
    existing_user = await User.filter(email=user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pwd = hash_password(user_data.password)
    user = await User.create(name=user_data.name, email=user_data.email, password=hashed_pwd)
    return user

async def authenticate_user(login_data: UserLogin):
    user = await User.filter(email=login_data.email).first()
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
