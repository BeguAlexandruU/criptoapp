from typing import Union
from fastapi import FastAPI
from cripto_app.routes import admin_routes, card_routes, demo_order_routes, level_routes, notification_routes, post_routes, product_routes, referal_routes, user_routes, wallet_routes

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(admin_routes.router)
app.include_router(card_routes.router)
app.include_router(demo_order_routes.router)
app.include_router(level_routes.router)
app.include_router(notification_routes.router)
app.include_router(post_routes.router)
app.include_router(product_routes.router)
app.include_router(referal_routes.router)
app.include_router(user_routes.router)
app.include_router(wallet_routes.router)

