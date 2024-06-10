ordem = 1
lista = []


while ordem != 11:
    num = int(input(f'Digite a {ordem}º numero: '))
    lista.append(num)
    ordem +=1

print (f'Lista na ordem em que foi digitada {lista}')
lista.reverse()
print (f'Lista reversa: {lista}')
