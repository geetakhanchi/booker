from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Date, Float
from .database import Base
from sqlalchemy.sql import func



class Customer(Base):
    __tablename__ = 'customers'

    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user_profile.id'))
    name = Column(String)
    mobile_no = Column(String)
    mobile_verified = Column(Boolean)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    dob = Column(Date)
    active = Column(Boolean)

class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user_profile.id'))
    name = Column(String)
    mobile_no = Column(String)
    mobile_verified = Column(Boolean)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    dob = Column(Date) 
    active = Column(Boolean)


class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True, index=True)
    hotel_name = Column(String)
    location = Column(String)
    state =Column(String)
    rating = Column(Integer)
    hotel_image = Column(String)
    gym_available = Column(Boolean)
    food_available = Column(Boolean)
    allow_booking = Column(Boolean)

class Staff(Base):
    __tablename__ = 'staffs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user_profile.id'))
    name = Column(String)
    mobile_no = Column(String)
    mobile_verified = Column(Boolean)
    rating = Column(Integer)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Room(Base) :
    __tablename__ = 'rooms'
    
    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    room_type = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    rating = Column(Integer)
    image_link = Column(String)
    room_no = Column(Integer)

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    booking_start_date = Column(Date)
    booking_end_date = Column(Date)
    booking_status = Column(String)
    checks_complete = Column(Boolean)
    total_price = Column(Float)

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey('bookings.id')) 
    amount = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    email = Column(String)
    status = Column(String)
    notes = Column(String)

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    booking_id = Column(Integer, ForeignKey('bookings.id')) 
    amount = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    comment = Column(String)

class User(Base):
    __tablename__ = 'user_profile'

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email = Column(String)
    email_verified = Column(Boolean)
    password = Column(String)
    
class Staff(Base):
    __tablename__ = 'staffs_members'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
