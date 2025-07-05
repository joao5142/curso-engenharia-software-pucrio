# Dicionários

# criar e imprimir um dicionário
notas = {"Ana": 8, "Maria": 5, "Thais": 10}
print(notas)

# acessar o valor correspondente à chave "Thais"
print(notas["Thais"])

# incluir novo item
notas["Zaira"] = 9
print(notas)

# remover item
del notas["Thais"]
print(notas)

# checar se notas contém o item "Maria"
print("Maria" in notas)