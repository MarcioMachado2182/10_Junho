num1 = int(input('Digite a 1º numero: '))
num2 = int(input('Digite a 2º numero: '))
operacao =int(input('Escolha a operação  [1] Média [2] Diferença [3] Produto [4] Divisão : ' ))

match operacao:

    case 1: 
        print ('Voce selecionou a Media entre os numeros')
        media = (num1 + num2) / 2
        print(f'A media entre os numeros é: {media}')

    case 2:
        print ('Voce selecionou a Diferença entre os numeros')
        dif = num1 - num2
        print(f'A diferença entre os numeros é: {dif}')

    case 3:
        print ('Voce selecionou o Produto entre os numeros')
        prod = num1 * num2 
        print(f'O produto entre os numeros é: {prod}')

    case 4:
        print ('Voce selecionou a Divisão entre os numeros')
        div = num1 / num2 
        print(f'O resultado da divisão entre os numeros é: {div}')

    case _:
        print('Opção invalida')
        #break:


