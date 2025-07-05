class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

pessoa_1 = Pessoa("João")
print(pessoa_1)

pessoa_2 = Pessoa("Maria")
print(pessoa_2)