from fastapi import FastAPI
from database import Base, engine
from routers import auth, tickets, products, admin

Base.metadata.create_all(bind=engine)

app = FastAPI(title="OM OnePortal Backend")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(tickets.router, prefix="/tickets", tags=["Tickets"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
def root():
    return {"message": "OM OnePortal Backend is live!"}
