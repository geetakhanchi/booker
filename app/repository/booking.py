from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status

def get_all(db: Session):
    bookings = db.query(models.Booking).all()
    return bookings

def create(request: schemas.Booking,db: Session):
    new_booking= models.Booking(
        room_id = request.room_id,
        customer_id = request.customer_id,
        booking_status = request.booking_status,
        checks_complete = request.checks_complete,
        total_price = request.total_price
    
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

def destroy(id:int,db: Session):
    booking = db.query(models.Booking.filter(models.Booking.id == id))

    if not booking.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Booking with id {id} not found")

    booking.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.models.Booking, db:Session):
    booking = db.query(models.models.Booking).filter(models.models.Booking.id == id)

    if not booking.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Booking with id {id} not found")

    booking.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    booking = db.query(models.Booking).filter(models.Booking.id == id).first()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Booking with the id {id} is not available")
    return booking