from statistics import median

class ListaDeNumeros:
    def __init__(self, numeros):
        self.numeros = numeros

    def __str__(self):
        return ','.join([str(n) for n in self.numeros])

    def soma(self):
        return sum(self.numeros)

    def media(self):
        return median(self.numeros)

minha_lista = ListaDeNumeros([1,2,3,4,5])

print(f"A soma de {minha_lista} é : {minha_lista.soma()}")
print(f"A média de {minha_lista} é : {minha_lista.media()}")