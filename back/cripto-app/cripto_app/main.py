from typing import Annotated, Union
from fastapi import Depends, FastAPI
from cripto_app.routes.db import admin_routes, card_routes, demo_order_routes, level_routes, notification_routes, post_routes, product_routes, referal_routes, wallet_routes
from cripto_app.routes.ws import notifications as ws_notifications
import fastapi_users
from cripto_app.db.database import get_db
from cripto_app.db.auth.users import jwt_auth_backend, fastapi_users, current_active_user
from cripto_app.db.auth.schemas import UserCreate, UserRead, UserUpdate
from cripto_app.db.models import User
from sqlalchemy.orm import Session
from cripto_app.routes.payments import stripe_routes

app = FastAPI(
    title="criptoapp",
    description="invetitions in cripto",
    version="0.0.1"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

DBD = Annotated[Session, Depends(get_db)]

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

#stripe routes
app.include_router(stripe_routes.router)

app.include_router(admin_routes.router)
app.include_router(card_routes.router)
app.include_router(demo_order_routes.router)
app.include_router(level_routes.router)
app.include_router(notification_routes.router)
app.include_router(post_routes.router)
app.include_router(product_routes.router)
app.include_router(referal_routes.router)
app.include_router(wallet_routes.router)

#websocket routes
app.include_router(ws_notifications.router)

