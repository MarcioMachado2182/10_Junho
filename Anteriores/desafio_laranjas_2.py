print ("Codigo para saber se Pedro está Feliz")

print("Pedro pega a Cesta")
laranjas = int(input("Quantas laranjas Pedro colocou na cesta?  "))
perdidas = int(input("Quantas laranjas Pedro perdeu?  "))

sobrou = (laranjas - perdidas)

if sobrou >=7:
    print("sobraram: ", sobrou, "laranjas")
    print("Pedro esta feliz")
    print("Pedro volta para casa")

elif sobrou < 7 or sobrou >= 5:
    print("sobraram; ", sobrou, "laranjas")
    print("Pedro Esta com Raiva")
    print("Pedro volta para casa")


else:
    print("sobraram: ", sobrou, "laranjas")
    print("Pedro esta triste")
    print("Pedro volta para casa")


    

    
