meses = ["janeiro", "fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
dias_do_mes = [31, 28,31,30,31,30,31,31,30,31,30,31]

#01/01/901

def dia(dia, mes, ano):
    if(int(dia) > 31 or int(dia) < 1 ):
        return "Data invalida"

    if (int(mes) > 12 or int(mes) < 1):
        return "Data invalida"

    posicao_mes = int(mes) - 1

    return  dia + " de " + meses[posicao_mes]  + " de " + ano


valor_dia, valor_mes , valor_ano = input().split("/")


print(dia(valor_dia,valor_mes, valor_ano))

