import json
import locale
import time
from datetime import datetime

import colorama
import requests
from pyfiglet import figlet_format
from rich import print
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table

colorama.init(autoreset=True)
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")


def logo(titulo: str = "") -> None:
    print("=" * 80)
    print(figlet_format(text=titulo, font="standard", justify="center"))
    print("=" * 80)


def obter_hora() -> str:
    data_e_hora_atuais = datetime.now()

    return data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S")


def buscar_dados(coin: str) -> float:
    request = requests.get(f"https://www.mercadobitcoin.net/api/{coin}/ticker")
    payload = json.loads(request.content)
    coin = payload['ticker']['last']

    return float(coin)


def calcula_percentual_de_alta_ou_baixa(valor_novo: float = 0, valor_antigo: float = 0) -> float:
    if valor_antigo == 0:
        return 0
    elif valor_novo == 0:
        return 100
    else:
        return (1 - (valor_antigo / valor_novo))


def formata_em_valor_moeda(valor: str) -> str:
    return locale.currency(float(valor), grouping=True)


def formata_em_valor_porcentagem(valor: float) -> str:
    return "{:.3%}".format(valor)


def cria_tabela_de_dados(titulo: str = "") -> Table:
    tabela = Table(title=titulo)
    tabela.add_column("Criptomoeda", justify="center", no_wrap=True)
    tabela.add_column("Valor", justify="center")
    tabela.add_column("Data/Hora", justify="center")
    tabela.add_column("Status", justify="center")
    tabela.add_column("Porcentagem", justify="center")

    return tabela


logo("Mercado Bitcoin")

print(Panel.fit("Desenvolvido por: Vinícius Azevedo. \nObrigado por testar a nova versão!", ))

# Lista de moedas a serem cotadas:
ticker_para_cotacao = {
    "BTC": {"nome": "BITCOIN", "antigo": 0, "novo": 0},
    "ETH": {"nome": "ETHEREUM", "antigo": 0, "novo": 0},
    "XRP": {"nome": "XRP", "antigo": 0, "novo": 0},
    "PAXG": {"nome": "PAXG", "antigo": 0, "novo": 0},
    "USDC": {"nome": "USDC", "antigo": 0, "novo": 0},
}

# Tempo em segundos para nova cotacao
tempo_para_nova_cotacao = 60

while True:
    data_hora = obter_hora()
    tabela = cria_tabela_de_dados()

    for ticker in ticker_para_cotacao:
        ticker_para_cotacao[ticker]['novo'] = round(buscar_dados(ticker), 3)

        nome_ticker = ticker_para_cotacao[ticker]['nome']
        valor_novo = ticker_para_cotacao[ticker]['novo']
        valor_antigo = ticker_para_cotacao[ticker]['antigo']

        valor_em_reais = locale.currency(
            valor_novo,
            grouping=True
        )

        porcentagem = calcula_percentual_de_alta_ou_baixa(
            valor_novo,
            valor_antigo
        )

        if valor_antigo == 0:
            status = "⧖"
            estilo = "blue"

        elif porcentagem > 0:
            status = "⬆"
            estilo = "green"

        elif porcentagem < 0:
            status = "⬇"
            estilo = "red"

        else:
            status = "="
            estilo = "yellow"

        tabela.add_row(
            nome_ticker,
            valor_em_reais,
            data_hora,
            status,
            formata_em_valor_porcentagem(porcentagem),
            style=estilo
        )

        ticker_para_cotacao[ticker]['antigo'] = ticker_para_cotacao[ticker]['novo']

    console = Console()
    console.print(tabela, justify="left")

    print("=" * 80)
    time.sleep(tempo_para_nova_cotacao)
