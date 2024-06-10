entrada = input("Deseja escrever uma frase: [a] sim [b] nao")
while entrada == 'a' or entrada == 'A':
    
        arquivo = open("atividade/frases.txt","a")
        frases = input('digite:')
        entrada = input("Deseja escrever uma frase: [a] sim [b] nao")
        arquivo = open("atividade/frases.txt","a")
        arquivo.write(f'{frases}\n')
        #print(frases)
        arquivo.close()

else:
       arquivo = open("atividade/frases.txt","r")
       print(arquivo.read())
       arquivo.close()




    


