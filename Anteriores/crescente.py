print ("programa para por em ordem crescente")

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

if a <= b <= c: # teste1: a-> b-> c
    print (a , b , c)

elif a <= c <= b: # teste2: a-> c-> b
    print (a, c, b)
    
elif b <= a <= c: # teste3: b-> a -> c
    print (b, a, c)

elif b <= a <= c: # teste4: b-> c-> a
       print (b, c, a)

elif c <= a and a <= b: # teste5: c-> a-> b
    print (c, a, b)

    
else:
    print (c, b, a)

