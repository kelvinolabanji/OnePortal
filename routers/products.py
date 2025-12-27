from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Product

router = APIRouter()

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
