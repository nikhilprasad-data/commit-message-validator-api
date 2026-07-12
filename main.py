from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers.comment_router import comment

app = FastAPI(title="Commit Validator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"status": "Commit Validator API is running smoothly 🚀", "version": "1.0.0"}

app.include_router(comment, prefix="/api", tags=["Comment Validation"])