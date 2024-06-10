linguagem = input('Qual linguagem de programção voce quer estudar? ')
#linguagem = linguagem.lower()

match linguagem:
    case "JavaScript":
        print('você pode se tornar um desenvolvedor web.')
    case "Python":
        print('você pode se tornar um cientista de dados.')
    case "PHP":
        print('você pode se tornar um desenvolvedor backend.')
    case "Solidity":
        print('você pode se tornar um desenvolvedor Blockchain.')
    case "Java":
        print('você pode se tornar um desenvolvedor de aplicativos mobile.')
    case _:
        print("o idioma não importa, o que importa é resolver problemas.")

