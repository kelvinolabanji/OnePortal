from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Ticket, User
from routers.tickets import get_current_user

router = APIRouter()

def admin_user(user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return user

@router.get("/tickets")
def get_all_tickets(admin=Depends(admin_user), db: Session = Depends(get_db)):
    return db.query(Ticket).all()
