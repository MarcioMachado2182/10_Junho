codigo = int(input('Informe o codigo do produto: '))
quant = float(input('Informe a quantidade: '))
valor_conta = 0
valor_prod = 0

match codigo:
    case 100:
        valor_prod = 1.70
        valor_conta = quant * valor_prod
        print(f'Voce escolheu {quant} Cachorro(s) Quente(s) \n o total da sua conta e de R$ {valor_conta}')

    case 101:
        valor_prod = 2.30
        valor_conta = quant * valor_prod
        print(f'Voce escolheu {quant} Bauru(s) Simples \n o total da sua conta e de R$ {valor_conta}')

    case 102:
        valor_prod = 2.60
        valor_conta = quant * valor_prod
        print(f'Voce escolheu {quant} Bauru(s) com Ovo \n o total da sua conta e de R$ {valor_conta}')

    case 103:
        valor_prod = 2.40
        valor_conta = quant * valor_prod
        print(f'Voce escolheu {quant} Hamburguer(s) \n o total da sua conta e de R$ {valor_conta}')

    case 104:
        valor_prod = 2.50
        valor_conta = quant * valor_prod
        print(f'Voce escolheu {quant} Cheeseburguer(s) \n o total da sua conta e de R$ {valor_conta}')

    case 105:
        valor_prod = 1.00
        valor_conta = quant * valor_prod
        print(f'Voce escolheu {quant} Refrigerante(s) \n o total da sua conta e de R$ {valor_conta}')

    case _:
        print("Produto Inexistente")
