from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

class SignUpRequest(BaseModel):
    firstname: str
    lastname: str
    Mobile_no: int
    email_id: str
    username: str
    password: str
    Re_type_password: str

class SignUpResponse(BaseModel):
    firstname: str
    lastname: str
    email_id: str

signup_router = APIRouter()

@signup_router.post('/signup', response_model= SignUpResponse)
async def signup(request: SignUpRequest):
    if not isinstance(request.firstname, str) or not isinstance(request.password, str):
        raise HTTPException(status_code=400, detail="firstname,lastname and password must be strings")
    return {"firstname": request.firstname, "lastname": request.lastname, "email_id": request.email_id, "message": f"{request.firstname} signed up successfully."}    
    
