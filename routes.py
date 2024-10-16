from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud_service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/persons/', response_model=List[schemas.Persons])
def get_all_persons(db: Session = Depends(get_db)):
    return crud_service.get_all_persons(db)

@router.get('/persons/rollnumber', response_model=schemas.Persons)
def get_persons_by_rollnumber(rollnumber: int, db: Session = Depends(get_db)):
    return crud_service.get_persons_by_rollnumber(db, rollnumber)

@router.post('/persons/', response_model=schemas.Persons)
def create_persons(rollnumber: int, fullname: str, age: int, profession: str, db: Session = Depends(get_db)):
    return crud_service.create_persons(db, rollnumber, fullname, age, profession)

@router.put('/persons/rollnumber/', response_model=schemas.Persons)
def update_persons_by_rollnumber(rollnumber: int, fullname: str, age: int, profession: str, db: Session = Depends(get_db)):
    return crud_service.update_persons_by_rollnumber(db, rollnumber, fullname, age, profession)

@router.delete('/persons/rollnumber', response_model=schemas.Persons)
def delete_persons_by_rollnumber(rollnumber: int, db: Session = Depends(get_db)):
    return crud_service.delete_persons_by_rollnumber(db, rollnumber)

