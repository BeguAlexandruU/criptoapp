import stripe

class StripeClient:
    def __init__(self, access_token):
        stripe.api_key = access_token

    def create_customer(self, email, name):
        return stripe.Customer.create(email=email, name=name)

    def create_subscription(self, customer_id, plan_id):
        return stripe.Subscription.create(customer=customer_id, items=[{"plan": plan_id}])

    def create_payment_intent(self, customer_id, amount, currency='usd'):
        return stripe.PaymentIntent.create(customer=customer_id, amount=amount, currency=currency, payment_method_types=['card'])

    def retrieve_payment_intent(self, payment_intent_id):
        return stripe.PaymentIntent.retrieve(payment_intent_id)
        