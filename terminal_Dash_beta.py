import json
import locale
import requests
import plotext as plt
import time

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

def buscar_dados(coin):
    request = requests.get(f"https://www.mercadobitcoin.net/api/{coin}/ticker")
    payload = json.loads(request.content)
    coin = payload['ticker']['last']
    return float(coin)

list_btc = []
list_eth = []
list_xrp = []

while True:
    # Realizando as requisições
    btc = float(buscar_dados("BTC"))
    eth = float(buscar_dados("ETH"))
    xrp = float(buscar_dados("XRP"))

    # Armazenando os dados em listas para comparações
    list_btc.append(btc)
    list_eth.append(eth)
    list_xrp.append(xrp)
   
    valor = list_btc
    valor2 = list_eth
    valor3 = list_xrp

   
    l = 1000
    x = range(1, l + 1)
    frames = 50
    for i in range(frames):
        plt.clt()
        plt.cld()
        plt.subplots(1,3)
        
        #Grafico BTC
        plt.subplot(1,1)
        plt.scatter(valor, color = "red", marker="dot", label="Bitcoin")
        plt.frame(True)
        plt.grid(True)
        plt.plot_size(40, 20)
        plt.xlim(-10, +100)
        plt.ylim(valor[-1]-1000, valor[-1]+1000)
        plt.xlabel('Bitcoin')
        # plt.clc()
    
        # Grafico ETH
        # plt.title("Ethereum")
        plt.subplot(1,2)
        plt.plot(valor2, color = "purple", marker="dot",label="Ethereum")
        plt.frame(True)
        plt.grid(True)
        plt.plot_size(40, 20)
        plt.xlim(-10, +100)
        plt.ylim(valor2[-1]-1000, valor2[-1]+1000)
        plt.xlabel('Ethereum')
        # plt.clc()

        # Grafico XRP
        plt.subplot(1,3)
        plt.plot(valor3, color="green", marker="dot",label="XRP")
        plt.frame(True)
        plt.grid(True)
        plt.plot_size(40, 20)
        plt.xlim(-10, +100)
        plt.ylim(valor3[-1]-2, valor3[-1]+5)
        plt.xlabel('XRP')
        # plt.clc()

    plt.show()
    print("=" * 125 +"\n")
    time.sleep(2)
    