from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status
from datetime import datetime

def get_all(db: Session):
    staffs = db.query(models.Staff).all()
    return staffs

def create(request: schemas.Staff,db: Session):
    new_staff= models.Staff(
        name = request.name,
    )
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff

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