aves = ["galinha", "avestruz", "papagaio", "codorna", "pato", "pavão"]
print (aves)




aves.pop(-1) #deleta um indice e seu valor
print (aves)

aves.append("falcão") #adiciona valor no final da lista
print (aves)

aves.insert(0,"aguia") #insere no indice indicado
print (aves)

aves.remove("avestruz") #remove o valor
print (aves)

aves[0] = "condor" #atribui um valor ao indice ou substitui o anterior
print (aves)

aves.sort()
print (aves)

aves.reverse()
print (aves)



if "beija-flor" in aves:
    print("acharam o beija-flor")
else:
    print("nao acharam o beija-flor")

aves.append("beija-flor")

if "beija-flor" in aves:
    print("acharam o beija-flor")
else:
    print("nao acharam o beija-flor")
