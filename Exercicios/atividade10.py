

valor_compra = float(input('Digite o valor da venda: '))
def valor_prestacao():
    valor_cada_prestacao = valor_compra / 5

    return valor_cada_prestacao
prestacao = valor_prestacao()


i = 0 
while i != 5:
    i += 1
    print('O valor da ' ,i , 'ª prestação e de R$ ' , prestacao)
      
    