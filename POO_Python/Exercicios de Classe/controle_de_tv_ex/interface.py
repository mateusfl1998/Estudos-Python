def headline(txt):
    print('=' * 50)
    print(txt.center(50))
    print('=' * 50)

def menu(lista):
    opcoes = [1,2,3]
    contador = 0
    for i in lista:
        print (f'{opcoes[contador]} - {i}')
        contador += 1
    print('=' * 50)
    