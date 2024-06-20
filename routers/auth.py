from fastapi import APIRouter, Depends, HTTPException, status

from pydantic import BaseModel
from models import Users

router = APIRouter()

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
    create_user_model = Users(
        id=user.id, 
        username=user.username, 
        password=user.password, 
        email=user.email)
    return create_user_model