#Adivinhe um numero entre 1 e 10
print('Programa para adivinhar numeros')

import random

num_sorteado = random.randint(1, 10)
num = None
tentativas = 0

while num != num_sorteado:
    print (num_sorteado)
    num = int(input('Adivinhe o numero entre 1 e 10: '))
    tentativas += 1

    if num >=1 and num <= 10:

        if num < num_sorteado:
           print ('o proximo numero deve ser maior')
        else:
           print('o proximo numero deve ser menor')

    else:
        print('numero invalido')



print ('Parabéns! Você adivinhou o numero em', tentativas,  'tentativas.')
print('teste')
"""outra alteracao"""