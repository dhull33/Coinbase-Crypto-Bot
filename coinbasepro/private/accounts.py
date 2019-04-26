import os, requests, json
from .coinbase_auth import CoinbaseAuth
from requests.auth import AuthBase
from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv('API_KEY')
SECRET = os.getenv('API_SECRET')
PASS = os.getenv('API_PASS')

class Accounts:
    def __init__(self):
        self.url = 'https://api.pro.coinbase.com'

    def list_trading_accounts(self, auth=None):
        accounts = requests.get(self.url + 'accounts', auth)
        return accounts.json()


