import requests
import json
import locale
from datetime import date, timedelta
from rich.table import Table
from rich.console import Console

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

def calc_diario_negoc(coin):
    ontem = date.today() - timedelta(days=1)
    ontem.strftime('%yy/%mm/%dd')
    ontem = str(ontem)
    ontem = ontem.replace('-', '/')
    request = requests.get(f"https://www.mercadobitcoin.net/api/{coin}/day-summary/{ontem}/")
    payload = json.loads(request.content)
    data = (payload['date'])
    abertura = (payload['opening'])
    fechamento = (payload['closing'])
    menor = (payload['lowest'])
    maior = (payload['highest'])
    return data,abertura,fechamento,menor,maior

def chamada_diario_negoc(coin):
    data = calc_diario_negoc(coin)[0]
    abertura = calc_diario_negoc(coin)[1]
    abertura = locale.currency(abertura, grouping=True)
    fechamento = calc_diario_negoc(coin)[2]
    fechamento = locale.currency(fechamento, grouping=True)
    menor = calc_diario_negoc(coin)[3]
    menor = locale.currency(menor, grouping=True)
    maior = calc_diario_negoc(coin)[4]
    maior = locale.currency(maior, grouping=True)
    return data,abertura,fechamento,menor,maior

def report_diario():
    lista = ['BTC','ETH','XRP','PAXG','USDC']
    
    table = Table(title=f"\nDiário de Negociações - {date.today()- timedelta(days=1)}")
    table.add_column("Criptomoeda", justify="center", no_wrap=True)
    table.add_column("Abertura", justify="center")
    table.add_column("Fechamento", justify="center")
    table.add_column("Menor", justify="center")
    table.add_column("Maior", justify="center")
    
    for coin in lista:
        abertura = chamada_diario_negoc(coin)[1]
        fechamento = chamada_diario_negoc(coin)[2]
        menor = chamada_diario_negoc(coin)[3]
        maior = chamada_diario_negoc(coin)[4]
        table.add_row(coin,abertura,fechamento,menor,maior,style="cyan")
        
    console = Console()
    console.print(table)

calc_diario_negoc("BTC")
report_diario()
