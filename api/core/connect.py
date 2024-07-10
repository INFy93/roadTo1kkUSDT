#connect to bybit

#connect enf file
from dotenv import load_dotenv
import os
load_dotenv()

from pybit.unified_trading import HTTP

client = HTTP(
    testnet=False,
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('SECRET'),
)