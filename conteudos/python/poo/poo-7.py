import abc
import datetime

class Pessoa(abc.ABC):  #Classe abstrata nao instancia
    def __init__(self, nome, login,senha):
        self.__nome = nome
        self.__login = login
        self.__senha = senha

    @abc.abstractmethod
    def get_nome(self): # metodo abstrato não é implementado só na subclasses
        pass


class Historico():

    def __init__(self):
        self.__data_matricula = datetime.datetime.today()
        self.__ocorrencias = []

    def imprime(self):
        print("Matriculado em {}".format(self.__data_matricula))
        print("Ocorrências:")
        for o in self.__ocorrencias:
            print("- ", o)

    def add_ocorrencia(self, ocorrencia):
        self.__ocorrencias.append(ocorrencia)

class Aluno(Pessoa):

    def __init__(self, nome, login, senha, curso, orientador):
        Pessoa.__init__(self, nome, login, senha)
        self.__curso = curso
        self.__orientador = orientador
        self.__historico = Historico()

    def consulta_curso(self):
        return self.__curso

    def consulta_orientador(self):
        return self.__orientador

    def consulta_nome(self):
        return self.__nome

    def gera_ocorrencia(self, ocorrencia):
        self.__historico.add_ocorrencia(ocorrencia)

    def consulta_historico(self):
        self.__historico.imprime()


class Professor(Pessoa):
    def __init__(self, nome: str, login: str, senha: int, titulacao):
        Pessoa.__init__(self, nome, login, senha)
        self.__titulacao = titulacao

    def get_titulacao(self):
        return self.__titulacao

    def get_nome(self):
        pass



# Aluno tem uma associação simples (agregação) com professor , ambos podem existir independente
# Ex : Revista e artigo , podem existir separadamente
professorMarcos = Professor('Marcos', 'mk', 'm123', 'Doutor')

novoAluno = Aluno('Isabela', 'isa', 'i123', 'Engenharia', professorMarcos)

#Aluno tem
# uma associação de composição com historico, o historico nao pode existir sem o aluno
# Ex : Livro e capitulo , capitulo não pode existir sem o livro

novoAluno = Aluno('Isabela', 'isa', 'i123', 'Engenharia', professorMarcos)
novoAluno.gera_ocorrencia("Matriculou-se em Calculo 1")
novoAluno.gera_ocorrencia("Nota final de Calculo 1: 9,7")
novoAluno.consulta_historico()