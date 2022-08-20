from typing import List
from fastapi import APIRouter,Depends,status
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db

@router.get('/')
def all(db: Session = Depends(get_db)):
    return user.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)



@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db)):
    return user.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.User, db: Session = Depends(get_db)):
    return user.update(id,request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def show(id:int, db: Session = Depends(get_db)):
    return user.show(id,db)