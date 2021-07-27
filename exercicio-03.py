class Convidados:
    def __init__(self, nome):
        self.nome = nome
    
    def lista_convidados(self):
        listaNome = []
        listaNome.append(self.nome)
        print(listaNome)

if __name__ == '__main__':
    qtd = int(input('Digite quantas pessoas deseja adicionar a lista: '))
contador = 0    
while contador > qtd:
    nome = input('Digite o nome da pessoa: ')
    pessoa = Convidados(nome)

Convidados.lista_convidados(pessoa)
        