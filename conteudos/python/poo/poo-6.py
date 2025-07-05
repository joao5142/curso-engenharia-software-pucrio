import abc

class Pessoa(abc.ABC):  #Classe abstrata nao instancia
    def __init__(self, nome, login,senha):
        self.__nome = nome
        self.__login = login
        self.__senha = senha

    @abc.abstractmethod
    def get_nome(self): # metodo abstrato não é implementado só na subclasses
        pass

class Aluno(Pessoa):


    def __init__(self, nome, login, senha, curso):
        Pessoa.__init__(self, nome, login, senha)
        self.__curso = curso
    def get_curso(self):
        return self.__curso
    def get_nome(self):
        pass

class Professor(Pessoa):
    def __init__(self,  nome: str, login:str, senha:int, titulacao):
        Pessoa.__init__(self, nome, login, senha)
        self.__titulacao= titulacao

    def get_titulacao(self):
        return self.__titulacao

    def get_nome(self):
        pass

class EntradaUniversidade:
    def __init__(self, ):
        pass

    def permite_entrada(selfself, pessoa: Pessoa):
        print("Pode Entrar, " + pessoa.get_nome())


class Coordenador(Pessoa):
    def __init__(self, nome, login, senha):
        Pessoa.__init__(self, nome, login, senha)

entrada = EntradaUniversidade()

pessoa1 = Pessoa("Maria", "mary","m123")
print(pessoa1.get_nome())

aluno1 = Aluno("Viviane", "vivi","v123","Informatica")
print(aluno1.get_curso())

prof1 = Professor("Viviane", "vivi","v123","Doutorado")
print(prof1.get_titulacao())
print(entrada.permite_entrada(prof1))

coord1 = Coordenador("Marcos", "mary","m123")
print(entrada.permite_entrada(coord1))