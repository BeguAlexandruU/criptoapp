from cripto_app.db.auth.schemas import UserRead
from cripto_app.db.auth.users import current_active_user
from cripto_app.db.crud import CrudBase
from cripto_app.db.models import Order, Product, User, Wallet
from cripto_app.db.schemas.order_s import OrderCreate
from cripto_app.db.schemas.wallet_s import WalletCreate
from cripto_app.payments.schemas.nowpayment_s import InvoiceRequerements
from fastapi import APIRouter, Depends, HTTPException, Header, Request, status
from cripto_app.db.database import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from cripto_app.settings import NOWPAYMENT_PUBLIC_KEY, NOWPAYMENT_SECRET_KEY
from nowpayment import NowPayments


DBD = Annotated[Session, Depends(get_db)]

# Create a NowPayment instance
np = NowPayments(NOWPAYMENT_SECRET_KEY)

router = APIRouter(
    prefix="/nowpayment",
    tags=["nowpayment"],
    responses={404: {"description": "Not found"}},
)

@router.post("/invoice/create", status_code=status.HTTP_201_CREATED)
async def create_invoice(invoiceRequerements: InvoiceRequerements, db: DBD, user: UserRead = Depends(current_active_user)):
    try:

        #get product info
        product = await CrudBase(Product).read(db, invoiceRequerements.product_id)

        #create new order        
        newOrder: OrderCreate = OrderCreate(
            id_user= user.id,
            id_product= product.id,
            amount= str(product.price), 
            currency= "USD",
            payment_amount= str(product.price),
            payer_currency= "USD" 
        )
        res_newOrder = await CrudBase(Order).create(db, newOrder)

        # Create Invoice
        res = np.payment.create_invoice(
            price_amount=product.price,
            price_currency="USD",
            order_id= str(res_newOrder.id),
            order_description=product.title,
            customer_email= user.email,
            success_url= "http://localhost:3000/profile",
            cancel_url= "http://localhost:3000/profile",
            ipn_callback_url= "http://localhost:5001/nowpayment/webhook"
        )
        print(res)
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