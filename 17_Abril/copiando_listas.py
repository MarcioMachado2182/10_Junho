bandas = ["acdc", "iron maiden", "metalica"]

print("-----------------------------------------------------------")
print (bandas)
print("bandas2 recebe bandas")
bandas2 = bandas #bandas recebe bandas
print (bandas2)
print("-----------------------------------------------------------")
print("")

bandas2.insert(0, "ramones") #o valor inserido em "bandas2" tbm sera inserido em "bandas"
print(bandas)
print(bandas2)
print ("o valor inserido em bandas2 tbm sera inserido em bandas")
print("-----------------------------------------------------------")
print("")

print("aqui é criada um copia independente de bandas em bandas 3")
bandas3 = bandas.copy() #aqui é criada um copia independente de "bandas" em "bandas 2"
print("")
bandas3.insert(0, "the clash")
print("")

print(bandas)
print(bandas2)
print(bandas3)
print ("neste caso as alterações foram feitas apenas em bandas")
print("-----------------------------------------------------------")
