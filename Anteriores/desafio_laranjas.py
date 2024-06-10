print ("Codigo para saber se Pedro ficara feliz oun triste")

laranjasPedro = 10
perdidas = int(input("Quantas laranjas Pedro perdeu?"))

sobrou = (laranjasPedro - perdidas)

if sobrou >=7:
    print("sobraram: ", sobrou)
    print("Pedro esta feliz")

else:
    print("sobraram: ", sobrou)
    print("Pedro esta triste")
    
