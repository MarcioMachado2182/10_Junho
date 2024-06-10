numero = input('Digite um numero: ')
valor = input('Digite um valor: ')
ope =input('Escolha a operação  [1] Soma [2] Subtração [3] Multiplicação [4] Divisão : ' )

def ope_mate(n:int,v:int,o:int):
    global ope

    match ope:
        case 1:
            print('Voce optou por "Soma"')
            ope = numero + valor
            print(f'O resultado é: {ope}')
        case 2:
            print('Voce optou por "Subtração"')
            ope = numero - valor
            print(f'O resultado é: {ope}')
        case 3:
            print('Voce optou por "Multiplicação"')
            ope = numero * valor
            print(f'O resultado é: {ope}')
        case _:
            print('Voce optou por "Divisão"')
            ope = numero / valor
            print(f'O resultado é: {ope}')

            ope_mate(numero, valor, ope)

ope_mate(numero, valor, ope)
