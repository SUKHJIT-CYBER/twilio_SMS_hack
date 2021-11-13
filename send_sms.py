import os
from twilio.rest import Client
from credentials import account_sid , auth_token ,my_cell,my_twilio
from main import your_msg
client = Client(account_sid, auth_token)
msg="Hello"
message = client.messages \
                .create(
                     body=msg + your_msg,
                     from_=my_twilio,
                     to=my_cell
                 )
