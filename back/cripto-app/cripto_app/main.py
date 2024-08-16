from typing import Annotated
from cripto_app.settings import ORIGINS
from fastapi import Depends, FastAPI
from cripto_app.routes.db import card_routes, demo_order_routes, level_routes, notification_routes, post_routes, product_routes, referal_routes, wallet_routes
from cripto_app.routes.ws import notifications as ws_notifications
import fastapi_users
from cripto_app.db.database import get_db
from cripto_app.db.auth.users import jwt_auth_backend, fastapi_users, current_active_user, verify_jwt_token
from cripto_app.db.auth.schemas import UserCreate, UserRead, UserUpdate
from cripto_app.db.models import User
from sqlalchemy.orm import Session
from cripto_app.routes.payments import stripe_routes
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(
    title="criptoapp",
    description="invetitions in cripto",
    version="0.0.1"
)

""" Configuration CORS """
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

DBD = Annotated[Session, Depends(get_db)]

# user routes
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
    include_in_schema=True
)
app.include_router(
    fastapi_users.get_auth_router(jwt_auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
    include_in_schema=True
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
    include_in_schema=True
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
    include_in_schema=True
)

# @app.get("/verify_token")
# async def verify_token(token: str):
    
#     user = verify_jwt_token(token)
#     print(user)
#     return user

@app.get("/auth/curent_user")
def protected_route(user: UserRead = Depends(current_active_user)):
    return user

#stripe routes
app.include_router(stripe_routes.router)

app.include_router(card_routes.router)
app.include_router(demo_order_routes.router)
app.include_router(level_routes.router)
app.include_router(notification_routes.router, dependencies=[Depends(current_active_user)])
app.include_router(post_routes.router)
app.include_router(product_routes.router)
app.include_router(referal_routes.router)
app.include_router(wallet_routes.router, dependencies=[Depends(current_active_user)])

#websocket routes
app.include_router(ws_notifications.router)

