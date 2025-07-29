from sqlalchemy.orm import Session
from typing import Optional, List
from . import models, schemas

def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(
        name=user.name,
        email=user.email,
        role=user.role,
        status=user.status
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, role: Optional[str] = None, status: Optional[str] = None) -> List[models.User]:
    query = db.query(models.User)
    if role is not None:
        query = query.filter(models.User.role == role)
    if status is not None:
        query = query.filter(models.User.status == status)
    return query.all()

def update_user(db: Session, db_user: models.User, user: schemas.UserUpdate) -> models.User:
    update_data = user.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, db_user: models.User) -> models.User:
    db.delete(db_user)
    db.commit()
    return db_user
