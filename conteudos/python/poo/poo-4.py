class Calculadora:
    valor_interno = 5

    def adicionar(self  ,numero):
        return self.valor_interno + numero

total= Calculadora()
total2= Calculadora()

print("resultado %d" % total.adicionar(3))

print("resultado %d" % total.adicionar(2))