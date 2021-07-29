def maior_numero(objeto):
    return max(objeto)

def menor_numero(objeto):
    return min(objeto)

listaNumero = [x**2 for x in range(155, 255)]

maior = maior_numero(listaNumero)
menor = menor_numero(listaNumero)

print(f"O maior numero e {maior}")
print(f"O menor numero e {menor}")