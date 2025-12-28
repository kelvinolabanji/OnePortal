from pydantic import BaseModel, EmailStr

class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "client"

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True
