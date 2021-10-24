import os
from twilio.rest import Client

from credentials import account_sid , auth_token ,my_cell,my_twilio

client = Client(account_sid, auth_token)

my_msg = "You can get everything in life you want if you will just help enough other people get what they want..............."




message = client.messages \
                .create(
                     body=my_msg,
                     from_=my_twilio,
                     to=my_cell
                 )
