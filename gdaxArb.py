import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase

# Create custom authentication for Exchange
class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').rstrip('\n')

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

api_url = 'https://api.gdax.com/'

# Enter credentials here
auth = CoinbaseExchangeAuth(API_KEY, API_SECRET, API_PHRASE)

#Enter balance you want to trade with here
tradeCapital = 10
 
while True:
    btcusd = "https://api.gdax.com/products/btc-usd/ticker"
    ltcbtc = "https://api.gdax.com/products/ltc-btc/ticker"
    ltcusd = "https://api.gdax.com/products/ltc-usd/ticker"

    buyBtc = requests.get(btcusd).json()
    buyBtc = float(buyBtc['ask'])
    buyLtc = requests.get(ltcbtc).json()
    buyLtc = float(buyLtc['bid'])
    sellLtc = requests.get(ltcusd).json()
    sellLtc = float(sellLtc['bid'])
        
    buyBtcT = (tradeCapital/buyBtc)*afterFee
    buyLtcT = (buyBtc/buyLtc)*afterFee
    sellLtcT = (buyLtc*sellLtc)*afterFee
    
    if sellLtcT>tradeCapital:
        buyTheBtc = {
            'size': tradeCapital/buyBtc,
            'price': buyBtc,
            'side': 'buy',
            'product_id': 'BTC-USD',
        }
        r = requests.post(api_url + 'orders', json=buyTheBtc, auth=auth)
        print r.json()
        
        buyTheLtc = {
            'size': ((tradeCapital/buyBtc)/buyLtc),
            'price': buyLtc,
            'side': 'buy',
            'product_id': 'LTC-BTC',
        }
        r = requests.post(api_url + 'orders', json=buyTheLtc, auth=auth)
        print r.json()
        
        sellTheLtc = {
            'size': ((tradeCapital/buyBtc)/buyLtc),
            'price': sellLtc,
            'side': 'sell',
            'product_id': 'LTC-USD',
        }
        r = requests.post(api_url + 'orders', json=sellTheLtc, auth=auth)
        print r.json()
        
    else:
        print("Not profitable")
