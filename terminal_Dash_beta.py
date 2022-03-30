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
cnt=0

while True:
    # Realizando as requisições
    btc = float(buscar_dados("BTC"))
    eth = float(buscar_dados("ETH"))
    xrp = float(buscar_dados("XRP"))

    # Armazenando os dados em listas para comparações
    list_btc.append(btc)
    list_eth.append(eth)
    list_xrp.append(xrp)

    # Contador para plotar no gráfico os ultimos 50 registros
    cnt=cnt+1
    if(cnt>80):
        list_btc.pop(0)
        list_eth.pop(0)
        list_xrp.pop(0)
   
    valor = list_btc
    valor2 = list_eth
    valor3 = list_xrp

   
    l = 1000
    x = range(1, l + 1)
    frames = 30
    
    plt.title("Streaming Data")
    plt.clc()

    for i in range(frames):
        plt.clt()
        plt.cld()
        plt.subplots(1,3)
        
        #Grafico BTC
        plt.subplot(1,1)
        plt.scatter(x,valor, color = "red", marker="dot", label="Bitcoin")
        plt.frame(True)
        plt.grid(True)
        plt.plot_size(40, 20)
        plt.xlim(-10, +100)
        plt.ylim(valor[-1]-1000, valor[-1]+1000)
        plt.xlabel('Bitcoin')
        plt.clc()
    
        # Grafico ETH
        # plt.title("Ethereum")
        plt.subplot(1,2)
        plt.plot(x,valor2, color = "purple", marker="dot",label="Ethereum")
        plt.frame(True)
        plt.grid(True)
        plt.plot_size(40, 20)
        plt.xlim(-10, +100)
        plt.ylim(valor2[-1]-1000, valor2[-1]+1000)
        plt.xlabel('Ethereum')
        plt.clc()

        # Grafico XRP
        plt.subplot(1,3)
        plt.plot(x,valor3, color="green", marker="dot",label="XRP")
        plt.frame(True)
        plt.grid(True)
        plt.plot_size(40, 20)
        plt.xlim(-10, +100)
        plt.ylim(valor3[-1]-2, valor3[-1]+5)
        plt.xlabel('XRP')
        plt.clc()

    plt.sleep(0.02)
    plt.show()
    # print(valor,valor2,valor3)
    print("=" * 125 +"\n")
    # time.sleep(2)
    