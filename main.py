from fastapi import FastAPI

from database import engine
from models import Base

from routers.auth_router import router as auth_router
from routers.product_router import router as product_router

print("Application Starting...")

app = FastAPI(
    title="Practice API",
    version="1.0.0"
)

print("Creating Tables...")

Base.metadata.create_all(bind=engine)

print("Tables Ready")


@app.get("/")
def home():
    return {
        "message": "FastAPI Running Successfully"
    }


# Authentication Routes
app.include_router(auth_router)

# Product Routes
app.include_router(product_router)