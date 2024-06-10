

#print("Programa para ver se o Aluno foi: Aprovado, Reprovado ou está em Recuperação")
aluno = str(input("Digite o nome do Aluno: "))
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))


media = ((nota1 + nota2) / 2)

match media:
    case x if x >= 7.1:
        print (aluno,", sua nota final foi: ", media)
        resultado = str("APROVADO")
        print("Você foi " + resultado + ": PARABENS, " + aluno + "!")
    
    case x if x <= 7  and x >= 4.1:
        print (aluno,", sua nota final foi: ", media)
        resultado = str(", vocÊ está em Exame")
        print(aluno + resultado)
    
    case x if x <= 4 and x >= 0:
        print (aluno, ", sua nota final foi: ", media)
        resultado = str(", você foi REPROVADO!")
        print(aluno + resultado)

