import os
from dotenv import load_dotenv


load_dotenv()

FLASK_ENV = os.getenv("FLASK_ENV")

HOST = os.getenv('DB_HOST')
DATABASE = os.getenv('DB_NAME')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASS')

# AWS CREDENTIALS
AWS_ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
AWS_BUCKET_NAME_RECURSOS = os.getenv("AWS_BUCKET_NAME_RECURSOS")

# EMAIL CREDENTIALS
EMAIL_SENDER = "servicios@gruporedsalud.com"
EMAIL_SMTP = os.getenv("EMAIL_SMTP")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
WSP_META = os.getenv("WSP_META")
WSP_META_IDENTIFER_PHONE=os.getenv("WSP_META_IDENTIFER_PHONE")

# DATABASE CREDENTIALS
DATABASE_URI = os.getenv("DATABASE_URI")
SEC_DATABASE_URI = os.getenv("SEC_DATABASE_URI")