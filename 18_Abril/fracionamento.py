"""
semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo']

print(semana[1:5])
print(semana[3:4])
print("*****************************************************")

semana2 = semana[0:8]
semana2.pop()
print("*****************************************************")

print(semana)
print(semana2)
print("*****************************************************")


if 'Sexta' in semana:
    print("*****************************************************")
    print("Sim, ", 'Sexta', "está na lista")
    print("*****************************************************")

else:
    print ("Não está")
    

if 'sexta' in semana:
    print("Sim, ", 'Sexta', "está na lista")
else:
    print("*****************************************************")
    print ("Não ", 'sexta',  "está na lista")
    print("*****************************************************")
"""

nomes = ["joao","maria","pedro"]
animais_de_estimacao = ["cachorro","gato","pato"]

for nome in nomes:
    for animal in animais_de_estimacao:
        print(nome,animal)