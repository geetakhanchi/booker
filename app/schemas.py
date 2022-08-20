
from pydantic import BaseModel
from . import models

class Hotel(BaseModel):
    hotel_name: str 
    location: str
    state: str
    rating: int
    hotel_image: str
    gym_available: bool
    food_available: bool
    allow_booking: bool

class ShowHotel(BaseModel):
    id: int
    hotel_name: str
    location: str
    state: str
    rating: int
    hotel_image: str
    gym_available: bool
    food_available: bool
    allow_booking: bool

    class Config():
        orm_mode = True


class Room(BaseModel):
    hotel_id: int
    room_type: str
    rating: int
    image_link: str
    room_no: int

class ShowRoom(BaseModel):
    id: int
    hotel_id: int
    room_type: str
    created_at: str
    updated_at: str
    rating: int
    image_link: str
    room_no: int

    class Config():
        orm_mode = True 

class Staff(BaseModel):
    name: str


class ShowStaff(BaseModel):
    id: int
    name: str


    class Config():
        orm_mode = True   

class User(BaseModel):
    user_name: str
    email: str
    email_verified: bool 
    password: str  

class ShowUser(BaseModel):
    id: int
    user_name: str
    email: str
    email_verified:bool 
    password: str  

    class Config():
        orm_mode = True   

class Customer(BaseModel):
    user_id: int
    name: str
    mobile_no: str
    mobile_verified: bool 
    dob: str
    active: bool     

class ShowCustomer(BaseModel):
    id: int
    user_id: int
    name: str
    mobile_no: str
    mobile_verified:bool
    created_at: str
    updated_at: str 
    dob: str
    active:bool

    class Config():
        orm_mode = True              

class Booking(BaseModel):
    room_id: int
    customer_id: int
    booking_status: str
    checks_complete: bool
    total_price: float

class ShowBooking(BaseModel):
    id: int
    room_id: int
    customer_id: int
    booking_start_date: str
    booking_end_date: str
    booking_status: str
    checks_complete: bool
    total_price: float

    class Config():
        orm_mode = True              


