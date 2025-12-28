from fastapi import FastAPI
from database import Base, engine
from routers import auth  # add other routers later: tickets, products, admin

Base.metadata.create_all(bind=engine)

app = FastAPI(title="OM OnePortal Backend")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "OM OnePortal Backend is live!"}
