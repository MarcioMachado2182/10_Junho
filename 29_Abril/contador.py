import time

minutos = 1
segundos  = 15

for i in range(segundos):
    print(f'{minutos}:{segundos}')
    segundos = segundos-1
    minutos -= 1

    if minutos > 0:
        minutos = minutos - 1
        print(f'{minutos}:{segundos}')
        segundos = segundos-1
    
    time.sleep(0.9)
