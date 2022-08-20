from typing import List
from fastapi import APIRouter,Depends,status
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import hotel

router = APIRouter(
    prefix="/hotel",
    tags=['Hotels']
)

get_db = database.get_db

@router.get('/')
def all(db: Session = Depends(get_db)):
    return hotel.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Hotel, db: Session = Depends(get_db)):
    return hotel.create(request, db)



@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db)):
    return hotel.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Hotel, db: Session = Depends(get_db)):
    return hotel.update(id,request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowHotel)
def show(id:int, db: Session = Depends(get_db)):
    return hotel.show(id,db)