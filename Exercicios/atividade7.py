celsius = float(input('informe a temperatura e graus Celsios: '))


def temperatura_far():
    far = (9 * celsius +160) / 5
    return far
temp_far = temperatura_far()

print ('A temperatura em Graus celsius é de: ', celsius , 'e em graus Fahrenheit é: ', temp_far)