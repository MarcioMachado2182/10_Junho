dolar = float(input('informe o valor em dolares: US$ '))
valor_dolar_hoje = float(input('informe a cotação do dolar hoje: R$ '))

def conversao():
    conversao_real = dolar * valor_dolar_hoje
    return conversao_real
real = conversao()

print('O valor em dolares é US$ ', dolar)
print('A cotação do dia e de R$%.2f ', valor_dolar_hoje)
print('O valor em Reais apos a conversao e de R$ ', real)
