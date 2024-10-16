from sqlalchemy.orm import Session
from typing import List

import models, schemas

def get_all_persons(db: Session):
       return db.query(models.Persons).all()

# auto generated route, get a record
def get_persons_by_rollnumber(db: Session, rollnumber: int):
      return db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()

def create_persons(db: Session, rollnumber: int, fullname: str, age: int, profession: str):
      record_to_be_added = {'rollnumber': rollnumber, 'fullname': fullname, 'age': age, 'profession': profession}
      new_persons = models.Persons(**record_to_be_added)
      db.add(new_persons)
      db.commit()
      return new_persons

def update_persons_by_rollnumber(db: Session, rollnumber: int, fullname: str, age: int, profession: str):
      record_to_update = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()
      for key, value in {'rollnumber': rollnumber, 'fullname': fullname, 'age': age, 'profession': profession}.items():
          setattr(record_to_update, key, value)
      db.commit()
      db.refresh(record_to_update)
      return record_to_update


def delete_persons_by_rollnumber(db: Session, rollnumber: int):
      record_to_delete = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()

      if record_to_delete:
          db.delete(record_to_delete)
          db.commit()

      return record_to_delete

