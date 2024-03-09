from typing import Union
from fastapi import FastAPI
from cripto_app.routes import users_routes

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(users_routes.router)
