import locale
import time
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from utils.horas import obter_hora
from utils.logo import logo
from utils.porcentagem import calc_porc
from utils.requisição import buscar_dados

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

logo("Mercado Bitcoin")
list_btc = [1.00]
list_eth = [1.00]
list_xrp = [1.00]
list_paxg = [1.00]
list_usdc = [1.00]

print(Panel.fit("Desenvolvido por: Vinícius Azevedo" ))

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

    table = Table(title="")
    table.add_column("Criptomoeda", justify="center", no_wrap=True)
    table.add_column("Valor", justify="center")
    table.add_column("Data/Hora", justify="center")
    table.add_column("Status", justify="center")
    table.add_column("Porcentagem", justify="center")

    data_hora = obter_hora()

    # Monitoramento BTC
    if list_btc[-1] > list_btc[-2]:
        if list_btc[-2] == 1.00:
            response = "Calculando.."
        else:
            response = str(calc_porc(list_btc[-2], list_btc[-1]))
        table.add_row(
            "BITCOIN",
            str(btc),
            data_hora,
            "⬆",
            response,
            style="green"
        )
        console = Console()

    elif list_btc[-1] < list_btc[-2]:
        response = str(calc_porc(list_btc[-2], list_btc[-1]))
        table.add_row("BITCOIN", str(btc), data_hora,
                      "⬇", response, style="red")
        console = Console()

    else:
        table.add_row("BITCOIN", str(btc), data_hora, "=", "%", style="yellow")
        console = Console()

    # Monitoramento ETH
    if list_eth[-1] > list_eth[-2]:
        if list_eth[-2] == 1.00:
            response = "Calculando.."
        else:
            response = str(calc_porc(list_eth[-2], list_eth[-1]))
        table.add_row("ETHEREUM", str(eth), data_hora,
                      "⬆", response, style="green")
        console = Console()

    elif list_eth[-1] < list_eth[-2]:
        response = str(calc_porc(list_eth[-2], list_eth[-1]))
        table.add_row("ETHEREUM", str(eth), data_hora,
                      "⬇", response, style="red")
        console = Console()

    else:
        table.add_row("ETHEREUM", str(eth), data_hora,
                      "=", "%", style="yellow")
        console = Console()

    # Monitoramento XRP
    if list_xrp[-1] > list_xrp[-2]:
        if list_xrp[-2] == 1.00:
            response = "Calculando.."
        else:
            response = str(calc_porc(list_xrp[-2], list_xrp[-1]))
        table.add_row("XRP", str(xrp), data_hora, "⬆", response, style="green")
        console = Console()

    elif list_xrp[-1] < list_xrp[-2]:
        response = str(calc_porc(list_xrp[-2], list_xrp[-1]))
        table.add_row("XRP", str(xrp), data_hora, "⬇", response, style="red")
        console = Console()

    else:
        table.add_row("XRP", str(xrp), data_hora, "=", "%", style="yellow")
        console = Console()

    # Monitoramento PAXG
    if list_paxg[-1] > list_paxg[-2]:
        if list_paxg[-2] == 1.00:
            response = "Calculando.."
        else:
            response = str(calc_porc(list_paxg[-2], list_paxg[-1]))
        table.add_row("PAXG", str(paxg), data_hora,
                      "⬆", response, style="green")
        console = Console()

    elif list_paxg[-1] < list_paxg[-2]:
        response = str(calc_porc(list_paxg[-2], list_paxg[-1]))
        table.add_row("PAXG", str(paxg), data_hora, "⬇", response, style="red")
        console = Console()

    else:
        table.add_row("PAXG", str(paxg), data_hora, "=", "%", style="yellow")
        console = Console()

    # Monitoramento USDC
    if list_usdc[-1] > list_usdc[-2]:
        if list_usdc[-2] == 1.00:
            response = "Calculando.."
        else:
            response = str(calc_porc(list_usdc[-2], list_usdc[-1]))
        table.add_row("USDC", str(usdc), data_hora,
                      "⬆", response, style="green")
        console = Console()
        console.print(table)

    elif list_usdc[-1] < list_usdc[-2]:
        response = str(calc_porc(list_usdc[-2], list_usdc[-1]))
        table.add_row("USDC", str(usdc), data_hora, "⬇", response, style="red")
        console = Console()
        console.print(table)

    else:
        table.add_row("USDC", str(usdc), data_hora, "=", "%", style="yellow")
        console = Console()
        console.print(table)

    print("==============================================================================")
    time.sleep(60)
