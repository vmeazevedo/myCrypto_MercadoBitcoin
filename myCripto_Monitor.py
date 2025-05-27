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
from utils.alerta import verificar_alerta 

# Configuração do sistema para R$
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

# Limite de variação percentual para alerta
LIMITE_ALERTA = 0.01  # em %

def monitorar_criptomoeda(nome, lista):
    try:
        # Realiza a requisição e armazena os dados na lista
        valor_atual = loop(nome)
        lista.append(valor_atual)

        # Formata o valor e calcula a porcentagem de variação
        valor_formatado = locale.currency(valor_atual, grouping=True)
        porcentagem = calc_porc(lista[-2], lista[-1]) if lista[-2] != 1.00 else "Calculando.."

        # Determina o estilo com base na variação do valor
        style = "green" if valor_atual > lista[-2] else "red" if valor_atual < lista[-2] else "yellow"

        return valor_formatado, porcentagem, style
    except Exception as e:
        # Em caso de erro, retorna valores vazios e registra a exceção
        print(f"Erro ao monitorar {nome}: {e}")
        return "", "", ""

def criar_tabela():
    # Cria uma tabela vazia com as colunas definidas
    table = Table(title="")
    table.add_column("Criptomoeda", justify="center", no_wrap=True)
    table.add_column("Valor", justify="center")
    table.add_column("Data/Hora", justify="center")
    table.add_column("Status", justify="center")
    table.add_column("Porcentagem", justify="center")
    return table

def main():
    # Inicializa as listas de criptomoedas
    criptomoedas = {
        "BTC": [1.00],
        "ETH": [1.00],
        "XRP": [1.00],
        "PAXG": [1.00],
        "USDC": [1.00]
        # Adicione novas criptomoedas aqui seguindo a mesma estrutura
    }

    # Imprime o logo e a mensagem de desenvolvimento
    logo("Mercado Bitcoin")
    print(Panel.fit("Desenvolvido por: Vinícius Azevedo"))

    while True:
        try:
            # Obtém a data/hora atual
            data_hora = obter_hora()

            # Cria uma instância do console Rich
            console = Console()

            # Cria uma nova tabela
            table = criar_tabela()

            # Preenche a tabela com os dados das criptomoedas
            for nome, lista in criptomoedas.items():
                valor, porcentagem, style = monitorar_criptomoeda(nome.lower(), lista)
                table.add_row(nome, str(valor), data_hora, "⬆" if style == "green" else "⬇" if style == "red" else "=", porcentagem, style=style)

                # Checagem de alerta
                if verificar_alerta(lista, LIMITE_ALERTA):
                    print(f"[bold yellow]⚠ ALERTA: {nome} variou mais de {LIMITE_ALERTA}%![/bold yellow]")

            # Imprime a tabela
            console.print(table)

            # Aguarda um intervalo de tempo antes de atualizar novamente
            time.sleep(10)

        except KeyboardInterrupt:
            # Em caso de interrupção pelo usuário (Ctrl+C), encerra o programa
            print("\nPrograma encerrado pelo usuário.")
            break
        except Exception as e:
            # Em caso de exceção não tratada, registra o erro e continua a execução
            print(f"Erro não tratado: {e}")

if __name__ == "__main__":
    main()