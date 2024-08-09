import stripe

class StripeClient:
    def __init__(self, access_token):
        stripe.api_key = access_token

    def create_customer(self, email, name):
        return stripe.Customer.create(email=email, name=name)

    def create_subscription(self, customer_id, price_id):
        #return stripe.Subscription.create(customer=customer_id, items=[{"plan": plan_id}])
        return stripe.Subscription.create(customer=customer_id,  items=[{"price": price_id}])

    def create_payment_intent(self, customer_id, amount, currency='usd'):
        return stripe.PaymentIntent.create(customer=customer_id, amount=amount, currency=currency, payment_method_types=['card'])

    def retrieve_payment_intent(self, payment_intent_id):
        return stripe.PaymentIntent.retrieve(payment_intent_id)


    def create_product(self, product_name, product_description):
        return stripe.Product.create(name=product_name, description=product_description)
    
    def create_price(self, price_unit_amount, price_recurring_count, price_product_id):
        
        return stripe.Price.create(
                    currency="usd",
                    unit_amount=int(price_unit_amount*100),
                    recurring={"interval": "day", "interval_count": price_recurring_count},
                    product=price_product_id,
                )
    
