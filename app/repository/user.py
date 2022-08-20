from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status
from datetime import datetime

def get_all(db: Session):
    users = db.query(models.UserProfile).all()
    return users

def create(request: schemas.UserProfile,db: Session):
    new_user= models.UserProfile(
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
    customer = db.query(models.Customer).filter(models.Customer.id == id)

    if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id {id} not found")

    customer.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Customer, db:Session):
    customer = db.query(models.Customer).filter(models.Customer.id == id)

    if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id {id} not found")

    customer.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    customer = db.query(models.Customer).filter(models.Customer.id == id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with the id {id} is not available")
    return customer