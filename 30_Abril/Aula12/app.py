import os
#opan("Caminho", "r")

#Mode
# r - Leitura
# a - Append / incrementar
# w - Escrita
# x - Criar Arquivo
# r+ - Leitura  + Escrita

#arquivo = open("Aula12/text3.txt","x")

#print(arquivo.readable()) # nos retorna se o arquivo pode
#print(arquivo.read()) # retorna palavras escritas no txt
#print(arquivo.readline()) # retorna so a primeira linha
#print(arquivo.readlines()) # retorna uma lista, onde cada linha vira uma lista

#arquivo.write("n\SQL") # o write aliado ao modo 'a' apenas adicona uma nova palavra

#lista = arquivo.readlines()
#print (lista)
#print(lista[0])

#arquivo.write("C\n")
#arquivo.write("C++\n")
#arquivo.write("Terraform\n")
"""
if os.path.exists("Aula12/text2.txt"):
    os.remove
else:
    print('nao existe')

"""

os.rmdir("Aula12/pasta_texte")






#arquivo.close #necessario fechar o arquivo ao final das operações