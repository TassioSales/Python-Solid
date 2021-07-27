class Pessoa:
    def __init__(self, nome, cpf, endereco, idade, altura, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.idade = idade
        self.altura = altura
        self.telefone = telefone

    def imprime_dados_pesssoa(self):
        print(f"NOME:  {self.nome}")
        print(f'CPF:  {self.cpf}')
        print(f'ENDERECO:  {self.endereco}')
        print(f'IDADE:  {self.idade}')
        print(f'ALTURA:  {self.altura}')
        print(f"TELEFONE: {self.telefone}")


if __name__ == '__main__':
    nome = input("Digite seu nome:")
    cpf = input("Digite seu cpf: ")
    endereco = input('Digite seu endereco: ')
    idade = input("Digite sua idade: ")
    altura = input("digite sua altura: ")
    telefone = input("Digite o numero de telefone: ")

    pessoa1 = Pessoa(nome, cpf, endereco, idade, altura, telefone)
    
    print("\n")

    print(Pessoa.imprime_dados_pesssoa(pessoa1))
