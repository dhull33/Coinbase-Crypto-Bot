import os, requests, json
from coinbase_auth import CoinbaseAuth
from requests.auth import AuthBase
from dotenv import load_dotenv
load_dotenv()

# Un-comment this for using real account
# KEY = os.getenv('API_KEY')
# SECRET = os.getenv('API_SECRET')
# PASS = os.getenv('API_PASS')

# Using Sandbox API for testing and development found at https://public.sandbox.pro.coinbase.com
SAND_KEY = os.getenv('SAND_KEY')
SAND_SECRET = os.getenv('SAND_SECRET')
SAND_PASS = os.getenv('SAND_PASS')

class Accounts:
    def __init__(self):
        # URL for actual api
        # self.url = 'https://api.pro.coinbase.com'

        # URL for sandbox
        self.url = 'https://api-public.sandbox.pro.coinbase.com/'

    def list_trading_accounts(self, autho):
        accounts = requests.get(self.url + 'accounts', auth=autho)
        return accounts.json()



autho = CoinbaseAuth(SAND_KEY, SAND_SECRET, SAND_PASS)
account = Accounts()
print(account.list_trading_accounts(autho))