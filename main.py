from fastapi import FastAPI
from database import Base, engine
from routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="OM OnePortal Backend")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"status": "Backend is live"}
