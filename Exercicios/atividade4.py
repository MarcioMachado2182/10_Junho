vendedor = str(input('informe o nome do vendedor: '))
salario_fixo = int(input(f'informe o salario fixo do vendedor {vendedor}: '))
vendas_efetuadas = int(input('informe p valor total de vendas do mes: '))
indice_comissao = 0,15
valor_comissao = vendas_efetuadas * 0.15

def salario_final_mes():
    return valor_comissao + salario_fixo

salario_liquido = salario_final_mes()


print ('O salario fixo do vendedor ', vendedor, 'é R$ ', salario_fixo)
print('O valor total de vendas do mes e de: R$ ', vendas_efetuadas)
print(f'O valor das comissões de {vendedor} foi de: R$ ', valor_comissao)
print(f"O vendedor {vendedor} recebera o valor total de R$ ", salario_liquido, "no mes")
salario_liquido