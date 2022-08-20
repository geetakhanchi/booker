from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status

def get_all(db: Session):
    hotels = db.query(models.Hotel).all()
    return hotels

def create(request: schemas.Hotel,db: Session):
    new_hotel= models.Hotel(
        hotel_name=request.hotel_name,
        location=request.location,
        state=request.state,
        rating=request.rating,
        hotel_image=request.hotel_image,
        gym_available=request.gym_available,
        food_available=request.food_available,
        allow_booking=request.allow_booking
    )
    db.add(new_hotel)
    db.commit()
    db.refresh(new_hotel)
    return new_hotel

def destroy(id:int,db: Session):
    hotel = db.query(models.Hotel).filter(models.Hotel.id == id)

    if not hotel.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Hotel with id {id} not found")

    hotel.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Hotel, db:Session):
    hotel = db.query(models.Hotel).filter(models.Hotel.id == id)

    if not hotel.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Hotel with id {id} not found")

    hotel.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    hotel = db.query(models.Hotel).filter(models.Hotel.id == id).first()
    if not hotel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Hotel with the id {id} is not available")
    return hotel