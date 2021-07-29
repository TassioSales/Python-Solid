cont = 0
qtd = int(input("Quantas pessoas deseja adicionar a lista de convidados: "))
listaConvi = []
while qtd > cont:
    nome = str(input("Digite o nome do convidado"))
    listaConvi.append(nome)
    cont += 1
print("As pessoas convidadas foram: ")
for nome in listaConvi:
    print(nome)