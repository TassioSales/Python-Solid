class Alismento:
    def __init__(self, idade, peso, altura):
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def aptidao(self):
        if self.idade < 18 or self.peso < 60 or self.altura < 1.70:
            print("Voce não esta apto a se alistar")
        else:
            print("Voce esta apto a se alista")
    

if __name__ == "__main__":
    idade = input('Digite sua idade: ')
    peso = input("Digite seu peso: ")
    altura = input("digite sua Altura: ")
        
    alistado = Alismento(int(idade),float(peso),float(altura))
    
    print(Alismento.aptidao(alistado))  