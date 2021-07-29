class Veiculo():
    def __init__(self, cor, rodas, marca, modelo, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.modelo = modelo
        self.tanque = tanque

    def abastercer(self, litros):
        self.tanque += litros
