from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.posts import schemas, models, service
from src.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return service.create_post(db=db, post=post)

@router.get("/", response_model=list[schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service.get_posts(db, skip=skip, limit=limit)
