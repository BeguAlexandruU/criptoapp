from cripto_app.db.crud import CrudBase
from cripto_app.db.models import Product, User, Wallet
from cripto_app.db.schemas.wallet_s import WalletCreate
from fastapi import APIRouter, Depends, HTTPException, Header, Request, status
from cripto_app.db.database import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from cripto_app.payments.schemas.stripe_s import Customer, Subscription
from cripto_app.payments.stripe import StripeClient
from cripto_app.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET
import stripe

DBD = Annotated[Session, Depends(get_db)]

Stripe = StripeClient(STRIPE_SECRET_KEY)
stripe.api_key = STRIPE_SECRET_KEY

router = APIRouter(
    prefix="/stripe",
    tags=["stripe"],
    responses={404: {"description": "Not found"}},
)

@router.post("/invoice/create", status_code=status.HTTP_201_CREATED)
async def create_invoice(db: DBD, customer: Customer):
    try:

        res = Stripe.create_customer(customer.email, customer.name)
        return res
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Item not found, error: {e}")
    
@router.post('/webhook')
async def webhook(request: Request, db: DBD, stripe_signature: str = Header(str) ):
    payload = await request.body()

    print(payload)

    # try:
    #     event = stripe.Webhook.construct_event(
    #         payload=payload,
    #         sig_header=stripe_signature,
    #         secret=STRIPE_WEBHOOK_SECRET
    #     )
    # except ValueError as e:
    #     # Invalid payload
    #     print("Invalid payload:", e)
    #     raise HTTPException(status_code=400, detail="Invalid payload")
    # except stripe.error.SignatureVerificationError as e:
    #     # Invalid signature
    #     print("Invalid signature:", e)
    #     raise HTTPException(status_code=400, detail="Invalid signature")

    # # Handle the event
    # if event['type'] == 'customer.subscription.created':
    #     subscription = event['data']['object']
    #     print("subscription:", subscription.id)
    #     print("customer:", subscription.customer)
    #     print("price:", subscription.plan.id)
    #     print("current_period_start:", subscription.current_period_start)
    #     print("current_period_end:", subscription.current_period_end)


    #     user = await CrudBase(User).read_by_column(db, "id_stripe_customer", subscription.customer)
    #     product = await CrudBase(Product).read_by_column(db, "id_stripe_price", subscription.plan.id)

    #     newWallet: WalletCreate = WalletCreate(
    #         id_user = user[0].id,
    #         id_product = product[0].id,
    #         id_stripe_subscription = subscription.id,
    #         status = 0,
    #         start_date = subscription.current_period_start,
    #         end_date = subscription.current_period_end
    #     )
        
    #     res = await CrudBase(Wallet).create(db, newWallet)

    # # ... handle other event types
    # else:
    #     print('Unhandled event type {}'.format(event['type']))



    return {"success": True}