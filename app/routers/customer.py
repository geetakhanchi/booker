from typing import List
from fastapi import APIRouter,Depends,status
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import customer

router = APIRouter(
    prefix="/customer",
    tags=['Customers']
)

get_db = database.get_db

@router.get('/')
def all(db: Session = Depends(get_db)):
    return customer.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Customer, db: Session = Depends(get_db)):
    return customer.create(request, db)



@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db)):
    return customer.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Customer, db: Session = Depends(get_db)):
    return customer.update(id,request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowCustomer)
def show(id:int, db: Session = Depends(get_db)):
    return customer.show(id,db)    