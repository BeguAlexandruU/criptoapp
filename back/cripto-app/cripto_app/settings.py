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