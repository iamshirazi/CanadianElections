from fastapi import FastAPI
from routers import districts, search
from database import engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Canadian Elections API")

### Generate all tables in Postgres
models.Base.metadata.create_all(bind=engine)

### ALLOW localhost AND canadianelections.net REQUESTS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "https://canadianelections.net",
        "https://www.canadianelections.net"
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(districts.router)
app.include_router(search.router)
