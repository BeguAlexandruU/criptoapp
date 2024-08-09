from fastapi import APIRouter, Depends, HTTPException, Header, Request, status
from cripto_app.db.database import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from cripto_app.payments.schemas.stripe_s import Customer, Subscription
from cripto_app.payments.stripe import StripeClient
from cripto_app.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
import stripe

DBD = Annotated[Session, Depends(get_db)]

Stripe = StripeClient(STRIPE_SECRET_KEY)
stripe.api_key = STRIPE_SECRET_KEY
endpoint_secret = 'whsec_Cf42jJ7ZUSCok4eZnKhFK9S2EieLCPUQ'

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
    
@router.post('/event')
async def webhook(request: Request, stripe_signature: str = Header(str) ):
    event = None
    payload = await request.body()
    # sig_header = request.headers['STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
           payload=payload,
           sig_header=stripe_signature,
           secret=endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        raise e
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        raise e

    # Handle the event
    if event['type'] == 'account.external_account.created':
      external_account = event['data']['object']
    elif event['type'] == 'checkout.session.async_payment_succeeded':
      session = event['data']['object']
    elif event['type'] == 'checkout.session.completed':
      session = event['data']['object']
    # ... handle other event types
    else:
      print('Unhandled event type {}'.format(event['type']))

    return {"success": True}