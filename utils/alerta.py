def verificar_alerta(lista, limite):
    if len(lista) < 3:
        return False  # Evita alertas na primeira execução (menos de 2 variações)
    valor_anterior = lista[-2]
    valor_atual = lista[-1]
    porcentagem = abs((valor_atual - valor_anterior) / valor_anterior) * 100
    return porcentagem >= limite
