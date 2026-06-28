from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

### PULL THESE VARIABLES FROM THE postgres-secret SECRET
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres-service:5432/{POSTGRES_DB}"

### FOR TESTING LOCALLY
# POSTGRES_USER = "myuser"
# POSTGRES_PASSWORD = "mypassword"
# POSTGRES_DB = "mydatabase"

# DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5050/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
