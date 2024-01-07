class Controle:
        def __init__(self, ligado=False, canal=3, volume=99,lista_de_canais=[3,4,5,9]):
            self.lista_de_canais = lista_de_canais
            self.volume = volume
            self.canal = canal
            self.ligado = ligado
            print(f'Você acabou de pegar o controle da Televisão')
        
        def on_off(self):
            if self.ligado == True:
                self.ligado = False
                print(f'Televisão Desligada!')
            else:
                self.ligado = True
                print(f'Televisão Ligada!')
            

        def aumentarvolume(self):
            if self.ligado == False:
                print('Televisão Desligada. Por favor ligue para alterar o volume!')
            else: 
                if self.volume == 100:
                    print('A televisão já se encontra no volume máximo')
                else:
                    self.volume += 1
                print(f'A televisão está ligada e no volume {self.volume}!')
            
        def diminuir_volume(self):  
            if self.ligado == False:
                print('Televisão Desligada. Por favor ligue para alterar o volume!') 
            if self.volume == 0:
                    print('A televisão já se encontra no volume minímo!')
            else:
                self.volume -= 1
                print(f'A televisão está ligada e no volume {self.volume}!')

        def selecionar_canal(self, set_canal):
            if self.ligado == False:
                print('Televisão Desligada. Por favor ligue para trocar o canal!')
            else:
                if set_canal not in self.lista_de_canais:
                    print(f'Canal inválido! A televisão ainda está no canal {set_canal}')
                    

                else:
                    print(f'A televisão está no canal {set_canal}')