class Animal():
    
    def emitir_som(self):
        print('')

class Cachoro(Animal):
    def emitir_som(self):
        print('Au au!')

class Gato(Animal):
    def emitir_som(self):
        print('Miau')

cachorro1 = Cachoro()
cachorro1.emitir_som()

gato1 = Gato()
gato1.emitir_som()