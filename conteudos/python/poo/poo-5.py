class Conta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.__saldo = saldo

conta1234 = Conta(1234, 750.84)

print(dir(conta1234))

