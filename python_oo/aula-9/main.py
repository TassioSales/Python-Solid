from veiculos import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('Rosa', 8,'Ford', 'Brutus', 10)
carro_azul = Carro('Azul', 4, "Fiat", 'Uno', 30)


print(caminhao_rosa)

print(type(caminhao_rosa))


print("\n")

print("Cor: ", caminhao_rosa.cor)
print("Rodas: ", caminhao_rosa.rodas)
print("Marca: ", caminhao_rosa.marca)
print('Modelo: ', caminhao_rosa.modelo)
print("Tanque: ", caminhao_rosa.tanque)

print("\n")

print("Cor: ", carro_azul.cor)
print("Rodas: ", carro_azul.rodas)
print("Marca: ", carro_azul.marca)
print('Modelo: ', carro_azul.modelo)
print("Tanque: ", carro_azul.tanque)
carro_azul.abastercer(35)
print("Tanque", carro_azul.tanque)