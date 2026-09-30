import json
from pathlib import Path
from fastapi_mail import ConnectionConfig
from fastapi_mail import (FastMail,MessageSchema,MessageType)
from fastapi import BackgroundTasks

import os
from dotenv import load_dotenv
load_dotenv()

file_path = Path(__file__).resolve().parent.parent / "data" / "products.json"


def get_all_product():

    with open(file_path, "r", encoding="utf-8") as p:
        return json.load(p)
   
def create_all_product(products):
    with open(file_path, "w", encoding="utf-8") as p:
        json.dump(products, p, indent=4)


email_conf = ConnectionConfig(
     
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_USERNAME"),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",

    MAIL_FROM_NAME="FastAPI Course Demo",

    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,

    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

async def send_email(email: str):
    html = """<p>Hi Your Order has placed successfully</p>"""

    message = MessageSchema(
        subject="Order Confirmation",
        recipients=[email],      # <-- [ ] लगा दिया
        body=html,
        subtype=MessageType.html,
    )

    fm = FastMail(email_conf)
    await fm.send_message(message)
    print("Email Send Successfully")
    