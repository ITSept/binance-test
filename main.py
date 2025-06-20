import requests
import time
import hmac
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

base_url = 'https://fapi.binance.com'
endpoint = '/fapi/v2/account'

timestamp = int(time.time() * 1000)
query_string = f'timestamp={timestamp}'

signature = hmac.new(API_SECRET.encode(), query_string.encode(), hashlib.sha256).hexdigest()

headers = {
    'X-MBX-APIKEY': API_KEY
}

url = f'{base_url}{endpoint}?{query_string}&signature={signature}'

try:
    response = requests.get(url, headers=headers, timeout=15)
    print(response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
