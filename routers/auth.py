from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database import get_db, User
from passlib.hash import bcrypt

router = APIRouter()

class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "client"  # default to client

@router.post("/signup")
def signup(request: SignupRequest, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Hash password and create user
    hashed_pw = bcrypt.hash(request.password)
    new_user = User(name=request.name, email=request.email, password=hashed_pw, role=request.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Signup successful", "user_id": new_user.id}
