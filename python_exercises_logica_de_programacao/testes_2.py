class Retangulo():

    def _init_(self):
        self.comprimento = 0
        self.largura = 0

    def set_comprimento(self,comprimento):
        self.comprimento = comprimento 

    def set_largura(self,largura):
        self.largura = largura

    def get_comprimento(self):
        return self.comprimento

    def get_largura(self):
        return self.largura

    def get_area(self):
      return self.comprimento * self.largura
     

    def get_perimetro(self):
      return 2 *self.comprimento + self.largura 

a1 = Retangulo()
a1.set_comprimento(2)
a1.set_largura(3)
# print(a1.set_comprimento())
print(a1.get_comprimento())
