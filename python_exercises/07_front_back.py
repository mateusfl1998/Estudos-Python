"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
'KitDontenut')
"""
def front_back(a, b):
    if len(a) % 2 == 0:
        ametade = int(len(a) / 2)
        afrente = a[0:ametade]    
        atras = a[ametade:]
        
    else:
        ametade = int(len(a) / 2)
        ametade_com_1 = ametade+1
        afrente = a[0:ametade_com_1]
        atras= a[ametade_com_1:]
    
    if len(b) % 2 == 0:
        bmetade = int(len(b) / 2)
        bfrente = b[0:bmetade]    
        btras = b[bmetade:]
    else:
        bmetade = int(len(b) / 2)
        bmetade_com_1 = bmetade+1
        bfrente = b[0:bmetade_com_1]
        btras= b[bmetade_com_1:]
    umaa = afrente+bfrente+atras+btras
    return umaa

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
