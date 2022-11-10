import os

from dotenv import load_dotenv
from handlers.handler import check_schedule_day
from twilio.rest import Client

load_dotenv()


def send_sms(*args, **kwargs):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    my_number = os.getenv("TWILIO_NUMBER")
    receiver_number = os.getenv("RECEIVER_NUMBER")

    client = Client(account_sid, auth_token)
    sms = check_schedule_day()

    message = client.messages.create(to=receiver_number, from_=my_number, body=sms)
    print(message.sid)
    print(sms)
