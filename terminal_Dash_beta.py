import json
import locale
import requests
import plotext as plt
import time
from pyfiglet import figlet_format
from rich.panel import Panel
from rich import print

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

def logo(titulo):
    print("=" * 125)
    print(figlet_format(text=titulo, font="standard"))
    print("=" * 125)

def buscar_dados(coin):
    request = requests.get(f"https://www.mercadobitcoin.net/api/{coin}/ticker")
    payload = json.loads(request.content)
    coin = payload['ticker']['last']
    return float(coin)

list_btc = []
list_eth = []
list_xrp = []
list_paxg = []
cnt=0

while True:
    # Realizando as requisições
    btc = float(buscar_dados("BTC"))
    eth = float(buscar_dados("ETH"))
    xrp = float(buscar_dados("XRP"))
    paxg = float(buscar_dados("PAXG"))

    # Armazenando os dados em listas para comparações
    list_btc.append(btc)
    list_eth.append(eth)
    list_xrp.append(xrp)
    list_paxg.append(paxg)

    # Contador para plotar no gráfico os ultimos 50 registros
    cnt=cnt+1
    if(cnt>80):
        list_btc.pop(0)
        list_eth.pop(0)
        list_xrp.pop(0)
        list_paxg.pop(0)
   
    valor = list_btc
    valor2 = list_eth
    valor3 = list_xrp
    valor4 = list_paxg
   
    l = 1000
    x = range(1, l + 1)
    frames = 20

    for i in range(frames):
        plt.clt()
        plt.cld()
        plt.subplots(1,4)
        
        logo("Mercado Bitcoin")
        print(Panel.fit("Terminal Dashboard. \nDesenvolvido por: Vinícius Azevedo."))
        
        #Grafico BTC
        plt.subplot(1,1)
        plt.scatter(x,valor, color = "red", marker="dot")
        plt.frame(True)
        plt.grid(True)
        plt.plot_size(30, 20)
        plt.xlim(-10, +100)
        plt.ylim(valor[-1]-1000, valor[-1]+1000)
        plt.xlabel('Bitcoin')
        plt.clc()   #Para habilitar a cor no terminal comente a linha
    
        # Grafico ETH
        # plt.title("Ethereum")
        plt.subplot(1,2)
        plt.plot(x,valor2, color = "purple", marker="dot")
        plt.grid(True)
        plt.plot_size(30, 20)
        plt.xlim(-10, +100)
        plt.ylim(valor2[-1]-1000, valor2[-1]+1000)
        plt.xlabel('Ethereum')
        plt.clc()   #Para habilitar a cor no terminal comente a linha

        # Grafico XRP
        plt.subplot(1,3)
        plt.plot(x,valor3, color="green", marker="dot")
        plt.frame(True)
        plt.grid(True)
        plt.plot_size(30, 20)
        plt.xlim(-10, +100)
        plt.ylim(valor3[-1]-2, valor3[-1]+5)
        plt.xlabel('XRP')
        plt.clc()   #Para habilitar a cor no terminal comente a linha

        # Grafico PAXG
        plt.subplot(1,4)
        plt.plot(x,valor4, color="blue", marker="dot")
        plt.frame(True)
        plt.grid(True)
        plt.plot_size(30, 20)
        plt.xlim(-10, +100)
        plt.ylim(valor4[-1]-500, valor4[-1]+500)
        plt.xlabel('PAXG')
        plt.clc()   #Para habilitar a cor no terminal comente a linha

    plt.sleep(0.0001)
    plt.show()
    print("=" * 125 +"\n")
    time.sleep(10)
    