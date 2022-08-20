from operator import imod
from fastapi import FastAPI
from app.routers.hotel import router as hotel_router
from app.routers.room import router as room_router
from app.routers.customer import router as customer_router
from app.routers.booking import router as booking_router
from app.routers.user import router as profile_router
from app.routers.staff import router as staff_router
from app.models import Base
from app.database import engine


Base.metadata.create_all(engine)


app = FastAPI()

app.include_router(hotel_router)
app.include_router(room_router)
app.include_router(customer_router)
app.include_router(booking_router)
app.include_router(profile_router)
app.include_router(staff_router)
