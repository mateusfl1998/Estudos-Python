class ContaBancaria():
    def __init__(self, numero_da_conta, titular, saldo):
        self.numero_da_conta = numero_da_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        self.saldo -= valor
    def consultar_saldo(self):
        print(self.saldo)

class ContaCorrente(ContaBancaria):
    def descontar_taxa_mensal(self, taxa_manutencao=15):
        self.saldo -= taxa_manutencao

class ContaPoupanca(ContaBancaria):
    def juros_mensais(self, porcentagem_de_juros=2):
        self.saldo += self.saldo + (porcentagem_de_juros * self.saldo) /100