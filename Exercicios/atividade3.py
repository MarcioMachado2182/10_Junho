#Medidor de combustivel

odo_ini = int(input('digite o valor do inicial do odometro: '))
odo_fim = int(input('digite o valor final do odometro: '))
combustivel_gasto = int(input('digite a quantidade de combutivel gasto: '))

distancia = odo_fim - odo_ini


def consumo():
    consumo  = distancia / combustivel_gasto
    return consumo

media = consumo()

print('a mdedia de consumo por litro foi de: ', media)





