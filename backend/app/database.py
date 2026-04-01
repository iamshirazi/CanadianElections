from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

### PULL THESE VARIABLES FROM THE postgres-secret SECRET
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_URL = os.getenv("POSTGRES_URL")

engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
