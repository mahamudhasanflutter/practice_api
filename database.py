from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

print("Starting Database Setup...")

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print("Database URL Loaded")

engine = create_engine(
    DATABASE_URL
)

print("Engine Created Successfully")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

print("SessionLocal Ready")

Base = declarative_base()

print("Base Class Ready")