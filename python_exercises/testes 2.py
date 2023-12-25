
filename = 'letras.txt'

def linear_merge(filename):
    try:
        a = open(filename, 'rt')

    except:
        print('Erro ao abrir arquivo')
    else:
        try:
            conteudo = a.read()
        except:
            print('Erro ao ler arquivo')
        else:
            try:
                lista_carecteres_n_repetidos = []
                lista = conteudo.split(' ')
                lista = list(map(str.upper, lista))
                quantidade_de_itens = []
                contador = 0
                lista2 = []
                # print(lista)
                for i in lista:
                    if i not in lista_carecteres_n_repetidos:
                        lista_carecteres_n_repetidos.append(i)
                lista_carecteres_n_repetidos.sort()
                # print(lista_carecteres_n_repetidos)
                for i in lista_carecteres_n_repetidos:
                            quantidade_de_itens.append(lista.count(i))
                # print(quantidade_de_itens)
                for i in lista_carecteres_n_repetidos:
                     lista2.append((lista_carecteres_n_repetidos[contador],quantidade_de_itens[contador]) )
                     contador += 1
                print(lista2)
                nova_lista = []
                for i in lista2:
                    i = list(i)
                    i = f'{i[0]} tem {i[1]} repetições'
                    nova_lista.append(i)
                print(nova_lista)
                    
            except:
                print('erro')
            else:
                pass

linear_merge(filename)