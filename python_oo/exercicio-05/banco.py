import random


class Clientes:
    def __init__(self, nome, cpf, idade, saldo):
        self.agencia = random.randint(1, 200)
        self.numero = random.randint(1000, 2000)
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.saldo = saldo

    def conta(self):
        print('CONTA CORRENTE')
        print(f"AGENCIA {self.agencia}")
        print(f'CONTA {self.numero}')
        print(f'NOME {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'IDADE: {self.idade}')
        print(f'Saldo em conta e R$ {self.saldo}')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Valor a que voce quer sacar maior que saldo disponivel")

    def depositar(self, valor):
        self.saldo += valor

    def consulta_saldo(self):
        print(f"O saldo atual e R$ {self.saldo}")


if __name__ == "__main__":
    cliente1 = Clientes('Tassio', '000011110000', 30, 100)
    Clientes.conta(cliente1)
    Clientes.depositar(cliente1, 100)
    Clientes.consulta_saldo(cliente1)
    Clientes.sacar(cliente1, 50)
    Clientes.consulta_saldo(cliente1)