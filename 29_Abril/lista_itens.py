itens = ['casa', 'manga', 'rosa', 'cafe', 'pao', 'ze', 'tuba', 'ka', 'gato', 'foca' ]
"""
def remove_itens():
    global itens
    print(itens)
    if len(itens) > 0:
        itens.pop()
        remove_itens()

    else: 
        print('vazio')

remove_itens()



"""
def remove_itens(l:list):
    
    print(l)
    if len(l) > 0:
        l.pop()
        remove_itens(l)

    else: 
        print('vazio')

remove_itens(itens)

#"""