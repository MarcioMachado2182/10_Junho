numero = []


def novo_num():
    num = int(input('digite um numero\ncaso o numero seja "0" o programa sera encerrado: '))
    if num == 0:
        print ("voce digitou '0' o programa fechara")
        print (numero)
    else:
        numero.appened(num)
        novo_num()
novo_num()

