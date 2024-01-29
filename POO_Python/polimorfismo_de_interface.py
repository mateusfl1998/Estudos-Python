class Animal():
    
    def emitir_som(self):
        pass

class Cachoro(Animal):
    def __init__(self,barulho):
        self.barulho = barulho

    def emitir_som(self):
        print(self.barulho)

class Gato(Animal):
    def __init__(self,barulho):
        self.barulho = barulho

    def emitir_som(self):
        print(self.barulho)

Cachoro1 = Cachoro('auau')
Cachoro1.emitir_som()

Gato1 = Gato('miau')
Gato1.emitir_som()'