class Carro:
    def __init__(self,tipo_de_combustivel = "Gasolina",km_por_litro=12, qt_combustivel=float(0)):
        self.km_por_litro = km_por_litro
        self.qt_combustivel = qt_combustivel
        self.tipo_de_combustivel = tipo_de_combustivel

    def set_combustivel(self,litros):
        self.qt_combustivel = litros

    def obterGasolina(self):
        print(self.qt_combustivel)
    
    def andar(self, km):
        a = km/self.km_por_litro
        self.qt_combustivel = self.qt_combustivel - a
        print(f'Ao andar {km}km você gastou {a:.2f} litros de gasolina. O seu tanque agora tem {self.qt_combustivel:.2f} litros de gasolina')