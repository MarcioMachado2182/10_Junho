print("Programa para ver se o Aluno foi: Aprovado, Reprovado ou está em Recuperação")
aluno = str(input("Digite o nome do Aluno: "))
nota1 = int(input('Digite a 1ª nota: '))
nota2 = int(input('Digite a 2ª nota: '))
nota3 = int(input('Digite a 3ª nota: '))
nota4 = int(input('Digite a 4ª nota: '))

media = ((nota1 + nota2 + nota3 + nota4) / 4)

if media >= 7:
    print (aluno,", sua nota final foi: ", media)
    resultado = str("APROVADO")
    print("Você foi " + resultado + ": PARABENS, " + aluno + "!")
    
elif media < 7  or media >= 5:
    print (aluno,", sua nota final foi: ", media)
    resultado = str(", vocÊ está em RECUPERAÇÂO")
    print(aluno + resultado)
    
else:
    print (aluno, ", sua nota final foi: ", media)
    resultado = str(", você foi REPROVADO!")
    print(aluno + resultado)
