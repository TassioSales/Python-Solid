from veiculos import Veiculo


class Carro(Veiculo):
    def __init__(self, cor, rodas, marca, modelo, tanque):
        Veiculo.__init__(self, cor, rodas, marca, modelo, tanque)

    def abastercer(self, litros):
        if self.tanque + litros > 50:
            print("ERRO: Tanque cheio")
        else:
            self.tanque += litros