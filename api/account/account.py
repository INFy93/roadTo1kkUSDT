#all methotds to work with account data


from api.core.connect import client


def get_wallet_balance(currency='USDT'):
    balance_data = client.get_wallet_balance(accountType='UNIFIED', coin=currency)

    return balance_data['result']['list'][0]['coin'][0]['walletBalance']
