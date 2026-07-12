from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers.comment_router import comment


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(comment, prefix="/api", tags=["Comment Validation"])