numeros = [1, 10, 100, 1000]
print(numeros)

# list comprehension
print([item * 2 for item in numeros])

# imprimir o elemento de índice 2 - inicia no 0
print(numeros[2])

# Operações de Listas

# incluir 2 itens na lista usando +=
numeros += [10000, 100000]
print(numeros)

# incluir 1 item na lista usando append
numeros.append(1000000)
print(numeros)

# substituir os itens nas posições 1 e 2 por 7
# [índice_incluído:índice_excluído]
numeros[1:3] = [7]
print(numeros)

# remover os itens nas posições 1 e 2 da lista
numeros[1:3] = []
print(numeros)

# tamanho da lista
print(len(numeros))