from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status

def get_all(db: Session):
    rooms = db.query(models.Room).all()
    return rooms

def create(request: schemas.Room,db: Session):
    new_room= models.Room(
    hotel_id = request.hotel_id,
    room_type = request.room_type,
    rating = request.rating,
    image_link = request.image_link,
    room_no = request.room_no,
    )
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room

def destroy(id:int,db: Session):
    room = db.query(models.Room).filter(models.Room.id == id)

    if not room.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Room with id {id} not found")

    room.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Room, db:Session):
    room = db.query(models.Room).filter(models.Room.id == id)

    if not room.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Room with id {id} not found")

    room.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    room = db.query(models.Room).filter(models.Room.id == id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Room with the id {id} is not available")
    return room