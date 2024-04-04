import json
import os
from datetime import datetime
from dotenv import load_dotenv
from nacl.bindings import crypto_sign
import requests
from urllib.parse import quote  # Додано імпорт quote

load_dotenv()

secret_key  = os.environ.get("DM_PRIVATE_KEY")
public_key = os.environ.get("DM_PUBLIC_KEY")

# Змініть URL на продакшн
rootApiUrl = "https://api.dmarket.com"

def get_offer_from_market():
    market_response = requests.get(rootApiUrl + "/exchange/v1/market/items?gameId=a8db&limit=1&currency=USD")
    offers = json.loads(market_response.text)["objects"]
    return offers[0]

def build_target_body_from_offer(offer):
    return {"targets": [
        {"amount": 1, "gameId": offer["gameId"], "price": {"amount": "2", "currency": "USD"},
         "attributes": {"gameId": offer["gameId"],
                        "categoryPath": offer["extra"]["categoryPath"],
                        "title": offer["title"],
                        "name": offer["title"],
                        "image": offer["image"],
                        "ownerGets": {"amount": "1", "currency": "USD"}}}
    ]}

class LastSales:
    URL = 'https://api.dmarket.com/trade-aggregator/v1/last-sales'

    def __init__(self, options=None):
        self.options = options

    def call(self):
        try:
            response = requests.get(self.URL, params=self.options)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return None

nonce = str(round(datetime.now().timestamp()))
api_url_path = "/exchange/v1/target/create"
method = "POST"
offer_from_market = get_offer_from_market()
body = build_target_body_from_offer(offer_from_market)
string_to_sign = method + api_url_path + json.dumps(body) + nonce
signature_prefix = "dmar ed25519 "
encoded = string_to_sign.encode('utf-8')
secret_bytes = bytes.fromhex(secret_key)
signature_bytes = crypto_sign(encoded, bytes.fromhex(secret_key))
signature = signature_bytes[:64].hex()
headers = {
    "X-Api-Key": public_key,
    "X-Request-Sign": signature_prefix + signature,
    "X-Sign-Date": nonce
}

# resp = requests.post(rootApiUrl + api_url_path, json=body, headers=headers)
# print(resp.text)

options = {
    "gameId": "a8db",
    "title": "Chroma 2 Case",
    }

last_sales_api = LastSales(options)
response = last_sales_api.call()
print(response)
