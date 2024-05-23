from stat_funcs import StatsN2

if __name__ == "__main__":
    stat = StatsN2()

    numeros_unimodal = [1, 1, 1, 2, 3, 4, 5]
    numeros_multimodal = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    numeros_amodal = [1, 2, 3, 4, 5]
    pesos = [1, 2, 3, 4, 5]

    multimodal = stat.multimodal(lista=numeros_multimodal)
    print(f" Distribuição multimodal {multimodal}")
    unimodal = stat.unimodal(lista=numeros_unimodal)
    print(f" Distribuição unimodal {unimodal}")
    amodal = stat.amodal(lista=numeros_amodal)
    print(f" Distribuição amodal {amodal}")

    media = stat.media(lista=numeros_amodal)
    print(f" Média {media}")

    media_ponderada = stat.media_ponderada(lista=numeros_amodal, pesos=pesos)
    print(f" Média ponderada {media_ponderada}")

    mediana = stat.mediana(lista=numeros_multimodal)
    print(f" Mediana {mediana}")

    variancia = stat.variancia(lista=numeros_multimodal)
    print(f" Variância {variancia}")

    desvio = stat.dpadrao(var=variancia)
    print(f" Desvio Padrão {desvio}")

    assimetria = stat.skew(lista=numeros_multimodal)
    print(f" Distribuição: {assimetria}")
