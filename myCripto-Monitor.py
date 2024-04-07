import locale
import time
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from utils.horas import obter_hora
from utils.logo import logo
from utils.porcentagem import calc_porc
from utils.requisição import loop

# Configurando o sistema para R$
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

def monitorar_criptomoeda(nome, lista):
    # Realizando as requisições e armazenando os dados em listas para comparações
    valor_atual = loop(nome)
    lista.append(valor_atual)
    valor_formatado = locale.currency(valor_atual, grouping=True)
    porcentagem = calc_porc(lista[-2], lista[-1]) if lista[-2] != 1.00 else "Calculando.."

    # Determina o estilo com base na variação do valor
    style = "green" if valor_atual > lista[-2] else "red" if valor_atual < lista[-2] else "yellow"
    
    return valor_formatado, porcentagem, style

def criar_tabela():
    table = Table(title="")
    table.add_column("Criptomoeda", justify="center", no_wrap=True)
    table.add_column("Valor", justify="center")
    table.add_column("Data/Hora", justify="center")
    table.add_column("Status", justify="center")
    table.add_column("Porcentagem", justify="center")
    return table

# Inicializando listas de criptomoedas
criptomoedas = {
    "BTC": [1.00],
    "ETH": [1.00],
    "XRP": [1.00],
    "PAXG": [1.00],
    "USDC": [1.00]
    # ADD NOVAS CRIPTOS AQUI SEGUINDO A MESMA REFERENCIA
}

logo("Mercado Bitcoin")
print(Panel.fit("Desenvolvido por: Vinícius Azevedo" ))

while True:
    data_hora = obter_hora()
    console = Console()

    table = criar_tabela()

    for nome, lista in criptomoedas.items():
        valor, porcentagem, style = monitorar_criptomoeda(nome.lower(), lista)
        table.add_row(nome, str(valor), data_hora, "⬆" if style == "green" else "⬇" if style == "red" else "=", porcentagem, style=style)

    console.print(table)
    print("==============================================================================")
    time.sleep(60)
