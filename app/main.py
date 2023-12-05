from fastapi import FastAPI
from app.bookings.router import router as bookings_router
from app.users.router import router as users_router


app = FastAPI()
app.include_router(bookings_router)
app.include_router(users_router)


@app.get("/home/")
def get_home():
    return {'Message': 'Welcome to UFC'}
