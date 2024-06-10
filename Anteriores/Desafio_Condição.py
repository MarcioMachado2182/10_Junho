print ("Codigo para saber se Pedro ficara feliz oun triste")

laranjasPedro = int(input("Quantas laranjas Pedro tem na cesta?"))
perdidas = int(input("Quantas laranjas Pedro perdeu?"))

sobrou = (laranjasPedro - perdidas)

if sobrou >=7:
    print("sobraram: ", sobrou, "laranjas")
    print("Pedro esta feliz")

elif sobrou < 7 and sobrou >= 5:
    print("sobraram; ", sobrou, "laranjas")
    print("Esta com Raiva")

else:
    print("sobraram: ", sobrou, "laranjas")
    print("Pedro esta triste")
    
