codigo = int(input('Informe o codigo do produto: '))


match codigo:
    case 1:
        if codigo == 1:
            print ("Alimento não-perecível")
    case x if x >=2 and x <= 4:
            print('Alimento perecível')
    case x if x >= 5 and x <= 6:
            print('Vestuario')
    case 7:
        if codigo == 7:
            print ("Higiene Pessoal")
    case x if x >= 8 and x <= 15:
            print('Limpeza e Utensilios Domesticos')
    case _:
        print('Codigo inválido')



