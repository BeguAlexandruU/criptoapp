from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv('../.env'))

mysql_user = os.getenv('MYSQL_USER')
mysql_password = os.getenv('MYSQL_PASSWORD')
mysql_host = os.getenv('MYSQL_HOST')
mysql_port = os.getenv('MYSQL_PORT')
mysql_db = os.getenv('MYSQL_DATABASE')

RESET_TOKEN_SECRET = os.getenv('RESET_TOKEN_SECRET')
VERIFICATION_TOKEN_SECRET = os.getenv('VERIFICATION_TOKEN_SECRET')

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')


NOWPAYMENT_PUBLIC_KEY = os.getenv('NOWPAYMENT_PUBLIC_KEY')
NOWPAYMENT_SECRET_KEY = os.getenv('NOWPAYMENT_SECRET_KEY')

ORIGINS = [
    # "*",
    "http://localhost:3000",
]