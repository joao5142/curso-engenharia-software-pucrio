class Aluno:
    def __init__(self):
        self.idade = 18
        self.nome = 'Zé'

    def dobra_idade(self):
        return self.idade * 2

aluno_1 = Aluno()
aluno_1.nome = "Maria"

aluno_2 = Aluno()
aluno_2.idade = 21

print(aluno_1.nome)
print(aluno_2.nome)

print(aluno_1.dobra_idade())
print(aluno_2.dobra_idade())