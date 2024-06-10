#Calculando a poupança

valor_depositado = float(input('informe o valor do deposito: R$ '))

def juros():
    juros_mes = valor_depositado * 0.070
    print('O valor dos juros e de R$%.2f ', juros_mes)
    valor_com_rendimento = valor_depositado + juros_mes
    return valor_com_rendimento

total = juros()

print('O valor da conta com os rendimentos do mes e R$ ', total)



  