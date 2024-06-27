from fastapi import FastAPI
from src.auth import router as auth_router
from src.posts import router as posts_router

app = FastAPI()

app.include_router(auth_router.router, prefix="/auth", tags=["auth"])
app.include_router(posts_router.router, prefix="/posts", tags=["posts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}
