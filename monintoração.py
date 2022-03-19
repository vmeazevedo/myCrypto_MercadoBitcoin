import requests
import json
import time
import locale
from datetime import datetime
from pyfiglet import figlet_format
from colorama import Fore, Back, Style
import colorama
colorama.init(autoreset=True)

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

def logo():
    print("======================================================================")
    print(figlet_format("Mercado Bitcoin ", font="standard"))
    print("======================================================================")

def obter_hora():
	data_e_hora_atuais = datetime.now()
	data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S")
	return data_e_hora_em_texto

def buscar_dados(coin):
    request = requests.get(f"https://www.mercadobitcoin.net/api/{coin}/ticker")
    payload = json.loads(request.content)
    coin = float(payload['ticker']['last'])
    coin = round(coin,2)
    # coin = locale.currency(coin, grouping=True)
    return int(coin)

logo()
list_btc = [0]
list_eth = [0]
list_xrp = [0]
list_paxg = [0]

while True:
    # Realizando as requisições
    btc = float(buscar_dados("BTC"))
    eth = float(buscar_dados("ETH"))
    xrp = float(buscar_dados("XRP"))
    paxg = float(buscar_dados("PAXG"))
    
    # Armazenando os dados em listas para comparações
    list_btc.append(btc)
    btc = locale.currency(btc, grouping=True)
    list_eth.append(eth)
    eth = locale.currency(eth, grouping=True)
    list_xrp.append(xrp)
    xrp = locale.currency(xrp, grouping=True)
    list_paxg.append(paxg)
    paxg = locale.currency(paxg, grouping=True)
    
    # Monitoramento BTC
    if list_btc[-1] > list_btc[-2]:
        print("BTC: \t" + str(btc) + "\t" +  obter_hora() + Fore.GREEN +"\tSubindo!"+Style.RESET_ALL)
    elif list_btc[-1] < list_btc[-2]:
        print("BTC: \t" + str(btc) + "\t" +  obter_hora() + Fore.RED +"\tCaindo!\t"+Style.RESET_ALL)
    else:
        print("BTC: \t" + str(btc) + "\t" +  obter_hora() + Fore.LIGHTYELLOW_EX +"\tEstável!"+Style.RESET_ALL)

    # Monitoramento ETH
    if list_eth[-1] > list_eth[-2]:
        print("ETH: \t" + str(eth) + "\t" +  obter_hora() + Fore.GREEN +"\tSubindo!"+Style.RESET_ALL)
    elif list_eth[-1] < list_eth[-2]:
        print("ETH: \t" + str(eth) + "\t" +  obter_hora() + Fore.RED +"\tCaindo!"+Style.RESET_ALL)
    else:
        print("ETH: \t" + str(eth) + "\t" +  obter_hora() + Fore.LIGHTYELLOW_EX +"\tEstável!"+Style.RESET_ALL)

    # Monitoramento XRP
    if list_xrp[-1] > list_xrp[-2]:
        print("XRP: \t" + str(xrp) + "\t\t" +  obter_hora() + Fore.GREEN +"\tSubindo!"+Style.RESET_ALL)
    elif list_xrp[-1] < list_xrp[-2]:
        print("XRP: \t" + str(xrp) + "\t\t" +  obter_hora() + Fore.RED +"\tCaindo!"+Style.RESET_ALL)
    else:
        print("XRP: \t" + str(xrp) + "\t\t" +  obter_hora() + Fore.LIGHTYELLOW_EX +"\tEstável!"+Style.RESET_ALL)
    
    # Monitoramento PAXG
    if list_paxg[-1] > list_paxg[-2]:
        print("PAXG:\t" + str(paxg) + "\t" +  obter_hora() + Fore.GREEN +"\tSubindo!"+Style.RESET_ALL)
    elif list_paxg[-1] < list_paxg[-2]:
        print("PAXG:\t" + str(paxg) + "\t" +  obter_hora() + Fore.RED +"\tCaindo!"+Style.RESET_ALL)
    else:
        print("PAXG:\t" + str(paxg) + "\t" +  obter_hora() + Fore.LIGHTYELLOW_EX +"\tEstável!"+Style.RESET_ALL)

    print("======================================================================")
    time.sleep(30)
