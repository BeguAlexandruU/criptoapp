
from typing import Optional
import uuid
from cripto_app.payments.stripe import StripeClient
from cripto_app.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
from cripto_app.settings import RESET_TOKEN_SECRET, VERIFICATION_TOKEN_SECRET
from cripto_app.db.database import get_user_db
from cripto_app.db.models import User, Referal
from fastapi import Depends, HTTPException, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import (
    AuthenticationBackend, 
    BearerTransport,
    JWTStrategy,
    CookieTransport
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from cripto_app.db.crud import CrudBase
from cripto_app.db.database import SessionLocal
from cripto_app.db.schemas.referal_s import ReferalCreate


CrudReferal = CrudBase(Referal)
CrudUser = CrudBase(User)
Stripe = StripeClient(STRIPE_SECRET_KEY)

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_token_secret = RESET_TOKEN_SECRET
    verification_token_secret = VERIFICATION_TOKEN_SECRET
    
    async def on_after_register(self,user: User, request: Optional[Request] = None) :
        #try:

            async with SessionLocal() as db:

                res = Stripe.create_customer(user.email, user.name)

                if res :
                    updated_user = await CrudUser.update_by_column(db, user.id, "id_stripe_customer", res.id)
                    print(updated_user[0].__dict__)

                if user.ref_code_parent != '' :
                    
                    ref_p_users = await CrudUser.read_by_column(db, 'ref_code', user.ref_code_parent)
                    if ref_p_users is None:
                        raise HTTPException(status_code=404, detail="Referal parent not found, invalid ref code")
                        
                    NewRef = ReferalCreate(
                        id_parent=ref_p_users[0].id,
                        id_child=user.id
                    )
                        
                    new_ref = await CrudReferal.create(db, NewRef)
                        
                    if new_ref is None:
                        raise HTTPException(status_code=404, detail="Error creating referal")

                            
        #except Exception as err:
            #raise HTTPException(status_code=404, detail=f"Internal error: {err}")
        

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
cookie_transport = CookieTransport(
    cookie_name="CriptoAppUser",
    cookie_max_age=3600,
)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=VERIFICATION_TOKEN_SECRET, lifetime_seconds=3600)


jwt_auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

cookie_auth_backend = AuthenticationBackend(
    name="jwt-cookie",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [jwt_auth_backend, cookie_auth_backend])

current_active_user = fastapi_users.current_user(active=True)
    