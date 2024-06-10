custo_fabrica = float(input('Informe o Custo de fabrica do Veiculo: '))
impostos_fabricante  = custo_fabrica * 0.28
print('Valor dos impostos e R$ ' , impostos_fabricante)



custo_com_impostos = custo_fabrica + impostos
print('o valor com os impostos e de R$ ', custo_com_impostos)
percentagem_distribuidor = custo_com_impostos * 0.28
print('A percentagem do distribuidor e de R$%.2f ', percentagem_distribuidor)

def valor_consumidor():
    valor_final = custo_com_impostos + percentagem_distribuidor
    return valor_final

valor_total = valor_consumidor()
print('O valor final do veiculo ao consumidor sera de R% ', valor_total)
