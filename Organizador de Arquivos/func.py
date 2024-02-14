import os
import shutil

nomes_das_pastas= [
    'Pasta Arquivos EXECUTÁVEIS',
    'Pasta Arquivos World e TXT',
    'Pasta Arquivos PDF',
    'Pasta Arquivos PNG',
    'Pasta Arquivos JPG',
    'Pasta Arquivos Torrent',
    'Pasta Arquivos Rar',
    'Pasta Para Pastas',
]


def criando_pastas(diretorio):
    contador = 0
    for i in nomes_das_pastas:
        diretorio = f'/Users/MTec Celulares/Desktop/{nomes_das_pastas[contador]}'
        os.makedirs(diretorio)
        contador +=1

# criando_pastas('/Users/MTec Celulares/Desktop')

# def move_archives():
#     contador = 0
#     diretorio_padrao = '/Users/MTec Celulares/Desktop'
#     arquivos = os.listdir(diretorio_padrao)
#     print(diretorio_com_arquivo)
#     for i in arquivos:
#     diretorio_com_arquivo = f'{diretorio_padrao}/{item} '
#         item = arquivos[contador]
#         if item[-4:] == '.zip':
#             item = arquivos[contador]
#             shutil.move(diretorio_com_arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos Rar')
#             contador +=1
#         if item[-4:] == '.Pdf':
#             item = arquivos[contador]
#             shutil.move(diretorio_com_arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos PDF')
#             contador +=1
#         if item[-4:] == '.docx':
#             item = arquivos[contador]
#             shutil.move(diretorio_com_arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos World')
#             contador +=1
#         if item[-4:] == '.png':
#             item = arquivos[contador]
#             shutil.move(diretorio_com_arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos PNG')
#             contador +=1
#         if item[-4:] == '.jpg':
#             item = arquivos[contador]
#             shutil.move(diretorio_com_arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos JPG')
#             contador +=1
#         if item[-4:] == '.rar':
#             item = arquivos[contador]
#             shutil.move(diretorio_com_arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos Rar')
#             contador +=1
#         if item[-4:] == '.Pdf':
#             item = arquivos[contador]
#             shutil.move(diretorio_com_arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos PDF')
#             contador +=1

def move_archives():
    diretorio = os.listdir('/Users/MTec Celulares/Desktop')
    n = 0

    for i in diretorio:
        arquivo = f'/Users/MTec Celulares/Desktop/{diretorio[n]}'
        print(arquivo)
        n += 1
        if i[-4:] == '.zip' or i[-4:] =='.rar' or i[-3:] =='.7z':
            shutil.move(arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos Rar')
        if i[-4:] == '.exe':
            shutil.move(arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos EXECUTÁVEIS')
        if i[-4:] == '.jpg' or i[-4:] == '.png':
            shutil.move(arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos JPG')
        if i[-4:] == '.pdf':
            shutil.move(arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos PDF')
        if i[-5:] == '.docx' or i[-4:] == '.txt':
            shutil.move(arquivo, '/Users/MTec Celulares/Desktop/Pasta Arquivos World e TXT')
        elif i != 'Organizador de Arquivos' or i != 'Pasta Para Pastas':
            shutil.move(arquivo, '/Users/MTec Celulares/Desktop/Pasta Para Pastas')

move_archives()
    