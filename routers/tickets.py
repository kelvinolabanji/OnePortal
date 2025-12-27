from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import get_db
from models import Ticket, User
from routers.auth import SECRET_KEY, ALGORITHM
from jose import jwt, JWTError

router = APIRouter()

def get_current_user(authorization: str = Header(...), db: Session = Depends(get_db)):
    try:
        token = authorization.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = db.query(User).filter(User.email == payload["sub"]).first()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except (IndexError, JWTError):
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/")
def create_ticket(title: str, description: str, user=Depends(get_current_user), db: Session = Depends(get_db)):
    ticket = Ticket(title=title, description=description, user_id=user.id)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

@router.get("/")
def get_my_tickets(user=Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Ticket).filter(Ticket.user_id == user.id).all()

