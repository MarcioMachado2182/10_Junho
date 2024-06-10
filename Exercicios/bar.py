bebida = 80
comida = 60
uber = 15
pessoas = 1
conta = 0

beber = str(input('Voce pretende beber?[1] sim [2] nao '))
comer = str(input('Voce pretende comer?[1] sim [2] nao '))
uber = str(input('Voce pretende usar uber?[1] sim [2] nao '))
amigos = int(input('Qauntas pessoas vao estar com vc?   '))
pessoas += amigos

def gasto_noite(b,c,u,p):
    global conta   
    if b == "1":
        conta += 80
        print(conta)
    if c == "1":
        conta += 60
        print(conta)
    if u == "1":
        conta += 15
        print(conta)
    if p > 0:
        conta*= pessoas
        print(conta)

        return conta
conta = gasto_noite(beber,comer,uber,pessoas)

#gasto_noite(beber,comer,uber,pessoas)



print('o gasto total da noite vai ser de R$: ', conta)
    
