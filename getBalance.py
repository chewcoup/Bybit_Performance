from config import BYBIT_API_KEY, BYBIT_API_SECRET
from pybit.unified_trading import HTTP

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

print(session.get_wallet_balance(
    accountType="SPOT"
)['result']['list'][0]['coin'][1]['walletBalance']+" $")

exit()