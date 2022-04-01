import json
import requests
import locale

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

def buscar_dados(coin):
    request = requests.get(f"https://www.mercadobitcoin.net/api/{coin}/ticker")
    payload = json.loads(request.content)
    coin = payload['ticker']['last']
    return float(coin)

def loop(coin):
    if coin == 'btc':
        btc = buscar_dados("btc")
        return btc
    elif coin == 'eth':
        eth = buscar_dados("eth")
        return eth
    elif coin == 'xrp':
        xrp = buscar_dados("xrp")
        return xrp
    elif coin == 'paxg':
        paxg = buscar_dados("paxg")
        return paxg
    elif coin == 'usdc':
        usdc = buscar_dados("usdc")
        return usdc
    else:
        print('Erro')

