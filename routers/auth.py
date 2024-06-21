from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from passlib.context import CryptContext
from pydantic import BaseModel
from database import SessionLocal
from models import Users

router = APIRouter()
db_dependency = Annotated[SessionLocal, Depends(get_db)]
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class CreateUserRequest(BaseModel):
    id: int
    username: str
    password: str
    email: str

@router.get("/auth")
async def get_user():
    return {"message": "user authenticated"}

@router.post("/auth")
async def create_user(user: CreateUserRequest):
    hashed_password = bcrypt_context.hash(user.password)
    create_user_model = Users(
        id=user.id, 
        username=user.username, 
        password=user.password, 
        email=user.email)
    return create_user_model

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()