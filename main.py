import time
import ccxt
from termcolor import cprint
import random


def binance_withdraw(address, amount_to_withdrawal, symbolWithdraw, network, API_KEY, API_SECRET):

    account_binance = ccxt.binance({
        'apiKey': API_KEY,
        'secret': API_SECRET,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'spot'
        }
    })

    try:
        account_binance.withdraw(
            code    = symbolWithdraw,
            amount  = amount_to_withdrawal,
            address = address,
            tag     = None, 
            params  = {
                "network": network
            }
        )
        cprint(f">>> 成功 | {address} | {amount_to_withdrawal}", "green")
    except Exception as error:
        cprint(f">>> 失败 | {address} | error : {error}", "red")

if __name__ == "__main__":
    
    with open("wallets.txt", "r") as f:
        wallets_list = [row.strip() for row in f]

    symbolWithdraw = 'BNB'
    network        = 'BSC' # ETH | BSC | AVAXC | MATIC | ARBITRUM | OPTIMISM | APT

    # api_keys of binance
    API_KEY     = ""
    API_SECRET  = ""
    AMOUNT_FROM = 0.01001
    AMOUNT_TO   = 0.0105

    cprint('\a\n/// start withdrawing...', 'white')
    for wallet in wallets_list:
        amount_to_withdrawal = round(random.uniform(AMOUNT_FROM, AMOUNT_TO), 6) # amount from ... to ...
        binance_withdraw(wallet, amount_to_withdrawal, symbolWithdraw, network, API_KEY, API_SECRET)
        time.sleep(random.randint(10, 30))


