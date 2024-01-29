from typing import Self
from classes import Controle
from interface import *
from trat_erro import *
from time import sleep

controle1 = Controle()
while True:
    headline('CONTROLE DA TV SAMSUNG')
    menu(['Ligar/Desligar TV','Trocar de Canal','Aumentar/Diminuir Volume'])
    select = inputer('Digite uma opção: ')

    if select == 1:
        controle1.on_off()
        sleep(3)
    elif select == 2:
        if controle1.ligado == False:
                print('Televisão Desligada. Por favor ligue para trocar o canal!')
                sleep(2)   
        else:
            canal = int(input(f'Digite um dos seguintes canais: {controle1.lista_de_canais}: '))
            controle1.selecionar_canal(canal)
            sleep(2)
    elif select == 3:
        if controle1.ligado == False:
                print('Televisão Desligada. Por favor ligue para alterar o volume!')
                sleep(2)
        else:   
            while True:
                vol = input('Digite +/- para aumentar ou diminuir o volume ou digite 1 para voltar ao menu principal: ')
                vol = vol.upper()
                if vol != '+' and vol != "-" and vol != '1':
                    print('Opção inválida ')
                else: 
                    if vol == '+':
                        controle1.aumentarvolume()
                    if vol == "-":
                        controle1.diminuir_volume()
                    if vol == '1':
                        break
        