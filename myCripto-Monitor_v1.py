import requests
import json
import time
import locale
import colorama
from datetime import datetime
from pyfiglet import figlet_format
from colorama import Fore, Back, Style

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
    coin = payload['ticker']['last']
    return float(coin)

def calc_porc(anterior,nova):
    anterior = anterior
    nova = nova

    if anterior < nova:
        x = (nova*100.00) / anterior
        x = 100.00 - x
        x = str(x)
        x = x.replace('-','')
        x = float(x)
        x = round(x,2)
        x = ("+"+ str(x))
        return x
    
    elif anterior > nova:
        x = (nova*100.00) / anterior
        x = 100.00 - x
        x = str(x)
        x = float(x)
        x = round(x,2)
        x = ("-"+ str(x))
        return x
    
    else:
        x = ("-%")
        return x

logo()
list_btc = [1.00]
list_eth = [1.00]
list_xrp = [1.00]
list_paxg = [1.00]
list_usdc = [1.00]

while True:
    # Realizando as requisições
    btc = float(buscar_dados("BTC"))
    eth = float(buscar_dados("ETH"))
    xrp = float(buscar_dados("XRP"))
    paxg = float(buscar_dados("PAXG"))
    usdc = float(buscar_dados("USDC"))

    # Armazenando os dados em listas para comparações
    list_btc.append(btc)
    btc = locale.currency(btc, grouping=True)
    list_eth.append(eth)
    eth = locale.currency(eth, grouping=True)
    list_xrp.append(xrp)
    xrp = locale.currency(xrp, grouping=True)
    list_paxg.append(paxg)
    paxg = locale.currency(paxg, grouping=True)
    list_usdc.append(usdc)
    usdc = locale.currency(usdc, grouping=True)
    
    # Monitoramento BTC
    if list_btc[-1] > list_btc[-2]:
        if list_btc[-2] == 1.00:
            response = "Calculando.."
        else:
            response = str(calc_porc(list_btc[-2],list_btc[-1]))
        print("BTC: \t" + str(btc) + "\t" +  obter_hora() + Fore.GREEN+"\tSubindo!"+Style.RESET_ALL + "  " +response)
    elif list_btc[-1] < list_btc[-2]:
        response = str(calc_porc(list_btc[-2],list_btc[-1]))
        print("BTC: \t" + str(btc) + "\t" +  obter_hora() + Fore.RED +"\tCaindo!\t"+Style.RESET_ALL + "  " +response)
    else:
        print("BTC: \t" + str(btc) + "\t" +  obter_hora() + Fore.LIGHTYELLOW_EX +"\tEstável!"+Style.RESET_ALL + "  " +"-%")

    # Monitoramento ETH
    if list_eth[-1] > list_eth[-2]:
        if list_eth[-2] == 1.00:
            response = "Calculando.."
        else:
            response = str(calc_porc(list_eth[-2],list_eth[-1]))
        print("ETH: \t" + str(eth) + "\t" +  obter_hora() + Fore.GREEN +"\tSubindo!"+Style.RESET_ALL + "  " +response)
    elif list_eth[-1] < list_eth[-2]:
        print("ETH: \t" + str(eth) + "\t" +  obter_hora() + Fore.RED +"\tCaindo!"+Style.RESET_ALL + "  " +response)
    else:
        print("ETH: \t" + str(eth) + "\t" +  obter_hora() + Fore.LIGHTYELLOW_EX +"\tEstável!"+Style.RESET_ALL + "  " +"-%")

    # Monitoramento XRP
    if list_xrp[-1] > list_xrp[-2]:
        if list_xrp[-2] == 1.00:
            response = "Calculando.."
        else:
            response = str(calc_porc(list_xrp[-2],list_xrp[-1]))
        print("XRP: \t" + str(xrp) + "\t\t" +  obter_hora() + Fore.GREEN +"\tSubindo!"+Style.RESET_ALL + "  " +response)
    elif list_xrp[-1] < list_xrp[-2]:
        print("XRP: \t" + str(xrp) + "\t\t" +  obter_hora() + Fore.RED +"\tCaindo!"+Style.RESET_ALL + "  " +response)
    else:
        print("XRP: \t" + str(xrp) + "\t\t" +  obter_hora() + Fore.LIGHTYELLOW_EX +"\tEstável!"+Style.RESET_ALL + "  " +"-%")
    
    # Monitoramento PAXG
    if list_paxg[-1] > list_paxg[-2]:
        if list_paxg[-2] == 1.00:
            response = "Calculando.."
        else:
            response = str(calc_porc(list_paxg[-2],list_paxg[-1]))
        print("PAXG:\t" + str(paxg) + "\t" +  obter_hora() + Fore.GREEN +"\tSubindo!"+Style.RESET_ALL + "  " +response)
    elif list_paxg[-1] < list_paxg[-2]:
        print("PAXG:\t" + str(paxg) + "\t" +  obter_hora() + Fore.RED +"\tCaindo!"+Style.RESET_ALL + "  " +response)
    else:
        print("PAXG:\t" + str(paxg) + "\t" +  obter_hora() + Fore.LIGHTYELLOW_EX +"\tEstável!"+Style.RESET_ALL + "  " +"-%")
        
    # Monitoramento USDC
    if list_usdc[-1] > list_usdc[-2]:
        if list_usdc[-2] == 1.00:
            response = "Calculando.."
        else:
            response = str(calc_porc(list_usdc[-2],list_usdc[-1]))
        print("USDC:\t" + str(usdc) + "\t\t" +  obter_hora() + Fore.GREEN +"\tSubindo!"+Style.RESET_ALL + "  " +response)
    elif list_usdc[-1] < list_usdc[-2]:
        print("USDC:\t" + str(usdc) + "\t\t" +  obter_hora() + Fore.RED +"\tCaindo!"+Style.RESET_ALL + "  " +response)
    else:
        print("USDC:\t" + str(usdc) + "\t\t" +  obter_hora() + Fore.LIGHTYELLOW_EX +"\tEstável!"+Style.RESET_ALL + "  " +"-%")

    print("======================================================================")
    time.sleep(60)
