# Importa o dicionário de vendas do arquivo vendas.py
from vendas import registro_vendas


def calcular_stockout(vendas):
    """Calcula o percentual de stockout da empresa.

    Parâmetros:
        vendas (dicionário): dicionário com os registros de vendas

    Retorna:
        stockout (float): percentual de stockout
    """

    numerador = 0
    denominador = 0

    for id_venda, informacoes_venda in vendas.items():
        total, status, motivo_cancelamento = informacoes_venda
        if status == "Concluído":
            denominador += total
        elif status == "Cancelado" and motivo_cancelamento == "Estoque em Falta":
            denominador += total
            numerador += total
        else:
            pass

    stockout = numerador / denominador
    return stockout


# Calcula o percentual de stockout
percentual_stockout = calcular_stockout(registro_vendas)

# Exibe o resultado
print(f"Stockout: {percentual_stockout:.2%}")
