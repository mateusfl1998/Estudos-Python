"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys

filename = 'letras.txt'

def print_words(filename):
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
                # print(lista)
                for i in lista:
                    if i not in lista_carecteres_n_repetidos:
                        lista_carecteres_n_repetidos.append(i)
                lista_carecteres_n_repetidos.sort()
                # print(lista_carecteres_n_repetidos)
                for i in lista_carecteres_n_repetidos:
                            quantidade_de_itens.append(lista.count(i))
                for i in lista_carecteres_n_repetidos:
                     print(i, quantidade_de_itens[contador] )
                     contador  += 1
                     
            except:
                print('erro')
            else:
                pass

def print_top(filename):
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
                nova_lista = []
                for i in lista2:
                    i = list(i)
                    i = f'{i[0]} tem {i[1]} repetições'
                    nova_lista.append(i)
                for c in nova_lista:
                     print(c)
                    
            except:
                print('erro')
            else:
                pass

def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
