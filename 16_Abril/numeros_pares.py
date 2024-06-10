print ("Contagem Par")

num = int(input("Digite o numero inicial: "))
max  = int(input('Digite um numero para o laço While: '))

print('numeros pares entre: ', num,  'e ', max)

while num <= max:
    if num%2 == 0:
        print(num, end = " ")
    num +=1

