from fastapi import APIRouter, Depends, HTTPException, status
from cripto_app.db.database import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from cripto_app.payments.schemas.stripe_s import Customer, Subscription
from cripto_app.payments.stripe import StripeClient
from cripto_app.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY

DBD = Annotated[Session, Depends(get_db)]

Stripe = StripeClient(STRIPE_SECRET_KEY)

router = APIRouter(
    prefix="/stripe",
    tags=["stripe"],
    responses={404: {"description": "Not found"}},
)

@router.post("/customer/create", status_code=status.HTTP_201_CREATED)
async def create_customer(db: DBD, customer: Customer):
    try:
        res = Stripe.create_customer(customer.email, customer.name)
        return res
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Item not found, error: {e}")

@router.post("/subscription/create", status_code=status.HTTP_201_CREATED)
async def create_subscription(db: DBD, subscription: Subscription):
    try:
        res = Stripe.create_subscription(subscription.customer_id, subscription.price_id)
        print(res)
        return res
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Item not found, error: {e}")