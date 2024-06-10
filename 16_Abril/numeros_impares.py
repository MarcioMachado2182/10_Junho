print ("Contagem Impar")

num = int(input("digite o numero inicial: "))
max  = int(input('Digite um numero para o laço While: '))

print('numeros impares entre: ', num,  'e ', max)

while num <= max:
    if num%2 == 1:
        print(num, end = " ")
    num +=1

