class BombaCombustivel:
    def __init__(self, tipo_combustivel,valor_do_litro, qt_combustivel_na_bomba):
        self.tipo_combustivel = tipo_combustivel
        self.valor_do_litro = float(valor_do_litro)
        self.quantidade_de_combustivel_na_bomba = float(qt_combustivel_na_bomba)

    def abastecerporvalor(self, valor):
        quantidade_por_valor = valor / self.valor_do_litro
        print(f'Com R${valor:.2f} você consegue abastecer {quantidade_por_valor:.2f} litros de {self.tipo_combustivel}')

    def abatecerporlitro(self,litros):
        a_ser_pago_por_litros = litros*self.valor_do_litro
        print(f'Para abastecer {litros} litros de {self.tipo_combustivel} você deverá pagar R${a_ser_pago_por_litros:.2f}')
    
    def change_valor_litro(self, novo_valor):
            self.valor_do_litro = novo_valor
            print(f'O novo valor do {self.tipo_combustivel} é de R${novo_valor:.2f}')

    def change_combustivel(self, combustivel):
            self.tipo_combustivel = combustivel
            print(f'Você alterou o combustivel para {self.tipo_combustivel}')