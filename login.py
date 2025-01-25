from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    username: str 
    message: str

login_router = APIRouter()

@login_router.post('/login', response_model=LoginResponse)
async def login(request: LoginRequest):
    if not isinstance(request.username, str) or not isinstance(request.password, str):
        raise HTTPException(status_code=400, detail="Username and password must be strings")
    return {"username": request.username, "message": f"{request.username} was successfully logged in"}
