from Loan import Loan
import AccessTokenGenerator
import json, Account , Order, Note
from RequestHandler import RequestHandler
access_token = '53efa27c-7725-4933-b450-33ef49d7895b'
refresh_token = 'e1746f0e-ed98-413d-aedf-7ea0d0b7f4e0'
token_type = 'bearer'
base_url = 'https://api.prosper.com/v1/'

headers = { 'Authorization': "bearer " + access_token, 'Accept': "application/json" }

o = Order.Order()
print(o.get_orders())
















