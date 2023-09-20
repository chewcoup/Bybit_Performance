from config import BYBIT_API_KEY, BYBIT_API_SECRET, BYBIT_API_KEY_INTRA, BYBIT_API_SECRET_INTRA
from pybit.unified_trading import HTTP

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)
sessionOne = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY_INTRA,
    api_secret=BYBIT_API_SECRET_INTRA,
)

print(session.get_wallet_balance(accountType="SPOT")['result']['list'][0]['coin'][1]['walletBalance']+" $")

print(sessionOne.get_wallet_balance(accountType="CONTRACT")['result']['list'][0]['coin'][0]['equity']+" S")

exit()