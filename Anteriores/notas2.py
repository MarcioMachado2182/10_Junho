print("Programa para ver se o Aluno foi: Aprovado, Reprovado ou está em Recuperação")


entrada = ""

while entrada != "fim":
    
    aluno = input("Digite o nome do Aluno (ou 'fim' para sair): ")
    print('Notas do Aluno ', aluno)
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    nota3 = float(input('Digite a 3ª nota: '))
    nota4 = float(input('Digite a 4ª nota: '))

    media = ((nota1 + nota2 + nota3 + nota4) / 4)
    
    if media >= 7:
        print (aluno,", sua nota final foi: ", media )
        print('Aprovado, parabens')
            
    elif media >= 5 < 7:
        print (aluno,", sua nota final foi: ", media)
        print('Esta em Recuperação')
                  
    else:
        print (aluno,", sua nota final foi: ", media)
        print('Esta esta REPROVADO')



    

    
