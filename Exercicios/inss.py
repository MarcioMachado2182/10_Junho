sexo = str(input('qual o seu sexo [m] masculino [f] feminino '))
idade_inicio = int(input('com que idade voce começou a contribuir? '))

idade_aposentadoria_h = 65 - idade_inicio
idade_aposentadoria_m= 62 - idade_inicio

def calc_aposen_homem():
    global idade_inicio

    if idade_aposentadoria_h >= 25 and idade_aposentadoria_h < 30:
        print(f"voce tem {idade_aposentadoria_h} anos de contribuição, o que te dá direito a 70% sobre o beneficio")
    elif idade_aposentadoria_h >= 30 and idade_aposentadoria_h < 35:
        print(f"voce tem {idade_aposentadoria_h} anos de contribuição, o que te dá direito a 77.5% sobre o beneficio")
    elif idade_aposentadoria_h >= 35 and idade_aposentadoria_h < 40:
        print(f"voce tem {idade_aposentadoria_h} anos de contribuição, o que te dá direito a 87.5% sobre o beneficio")
    elif idade_aposentadoria_h >= 40:
        print(f"voce tem {idade_aposentadoria_h} anos de contribuição, o que te dá direito a 100% sobre o beneficio")
    else:
        print('Voce nao tem tempo minimo para se aposentar')

def calc_aposen_mulher():
    global idade_inicio

    if idade_aposentadoria_m >= 25 and idade_aposentadoria_m < 30:
        print(f"voce tem {idade_aposentadoria_m} anos de contribuição, o que te dá direito a 70% sobre o beneficio")
    elif idade_aposentadoria_m >= 30 and idade_aposentadoria_m < 35:
        print(f"voce tem {idade_aposentadoria_m} anos de contribuição, o que te dá direito a 77.5% sobre o beneficio")
    elif idade_aposentadoria_m >= 35 and idade_aposentadoria_m < 40:
        print(f"voce tem {idade_aposentadoria_m} anos de contribuição, o que te dá direito a 87.5% sobre o beneficio")
    elif idade_aposentadoria_m >= 40:
        print(f"voce tem {idade_aposentadoria_m} anos de contribuição, o que te dá direito a 100% sobre o beneficio")
    else:
        print('Voce nao tem tempo minimo para se aposentar')

if sexo == 'm' or sexo =='M':
    calc_aposen_homem()
elif sexo =='f' or sexo == 'F':
    calc_aposen_mulher()
else:
    print ('voce digitou errado')