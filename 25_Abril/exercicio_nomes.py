lista_nomes = []
quant = 1


while quant <= 4:
    nomes = str(input(f'informe o {quant}º nome: '))
    lista_nomes.append(nomes)
    quant += 1
    #print (lista_nomes)

nome_procurar = str(input('informe nome a ser procurado na lista: '))
if nome_procurar in lista_nomes:
    print(f'{nome_procurar} esta na lista')
    print (lista_nomes)

else:
    print(f'{nome_procurar} não esta na lista')
    print (lista_nomes)

            

