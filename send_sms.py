import os
from twilio.rest import Client

from credentials import account_sid , auth_token ,my_cell,my_twilio

client = Client(account_sid, auth_token)

my_msg = "Hey Fols Only 10 hours Left for Hackathon ...................."




message = client.messages \
                .create(
                     body=my_msg,
                     from_=my_twilio,
                     to=my_cell
                 )