
a = int(input('numero 1: '))
b = int(input('numero 2: '))
 
def soma():
    soma = a + b
    return soma
resultado_soma = soma()
    
def sub():
    sub = a - b
    return sub
resultado_sub = sub()

def multi():
    multi = a * b
    return multi
resultado_multi = multi()

def div():
    div = a / b
    return div
resultado_div = div()

print('a soma dos numero e: ' , resultado_soma)
print('a subtracao dos numero e: ' , resultado_sub)
print('a multiplicação dos numero e: ' , resultado_multi)
print('a divisao dos numero e: ' , resultado_div)



