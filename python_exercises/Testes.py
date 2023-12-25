def sort_last(tuples):
    nova_lista = []
    for conjunto in tuples:
        conjunto = list(conjunto)
        x0 = conjunto[0]
        x1 = conjunto[1]
        novo_conjunto = x1,x0
        novo_conjunto = tuple(novo_conjunto)
        nova_lista.append(novo_conjunto)
    print(nova_lista)
sort_last([(1, 3), (3, 2), (2, 1)])