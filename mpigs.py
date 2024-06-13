import requests
from requests.auth import HTTPBasicAuth
import json
import base64
from datetime import datetime

# Configuration
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
short_code = 'YOUR_SHORTCODE'
lipa_na_mpesa_online_short_code = 'YOUR_LIPA_NA_MPESA_ONLINE_SHORT_CODE'
lipa_na_mpesa_online_passkey = 'YOUR_LIPA_NA_MPESA_ONLINE_PASSKEY'
phone_number = 'USER_PHONE_NUMBER'
amount = 'AMOUNT_TO_PAY'

# Get the current timestamp
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

# Generate Password
password = base64.b64encode(f'{lipa_na_mpesa_online_short_code}{lipa_na_mpesa_online_passkey}{timestamp}'.encode('utf-8')).decode('utf-8')

# Mock function to simulate obtaining OAuth Token
def get_oauth_token(consumer_key, consumer_secret):
    return "mock_access_token"

# Mock function to simulate initiating STK Push
def initiate_stk_push(access_token, payload):
    # Simulate a successful response
    return {
        "MerchantRequestID": "12345",
        "CheckoutRequestID": "67890",
        "ResponseCode": "0",
        "ResponseDescription": "Success. Request accepted for processing",
        "CustomerMessage": "Success. Request accepted for processing"
    }

# Obtain OAuth Token (using mock function here)
access_token = get_oauth_token(consumer_key, consumer_secret)

# Initiate STK Push (using mock function here)
stk_push_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
headers = {'Authorization': f'Bearer {access_token}'}
payload = {
    'BusinessShortCode': lipa_na_mpesa_online_short_code,
    'Password': password,
    'Timestamp': timestamp,
    'TransactionType': 'CustomerPayBillOnline',
    'Amount': amount,
    'PartyA': phone_number,
    'PartyB': lipa_na_mpesa_online_short_code,
    'PhoneNumber': phone_number,
    'CallBackURL': 'YOUR_CALLBACK_URL',
    'AccountReference': 'YOUR_ACCOUNT_REFERENCE',
    'TransactionDesc': 'YOUR_TRANSACTION_DESCRIPTION'
}
response = initiate_stk_push(access_token, payload)

# Print the response
print(json.dumps(response, indent=4))
