from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status
from datetime import datetime

def get_all(db: Session):
    users = db.query(models.User).all()
    return users

def create(request: schemas.User,db: Session):
    new_user= models.User(
        user_name = request.user_name,
        email = request.email,
        email_verified = request.email_verified,
        password = request.password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def destroy(id:int,db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    user.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.User, db:Session):
    user= db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    user.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user