def bekeres():
    kor = int(input("Kérek egy kort [0,120]: "))

    return kor


def lista_keszitese():
    lista = []
    for i in range(5):
        lista.append(bekeres())

    print("II/A, B, C:")
    print("\t", lista[0], end="")
    for i in range(1, len(lista)):
        print(f" : {lista[i]}", end="")
    print()

    return lista


def elso_idos(lista):
    idosindex = 0
    idosebb = False
    while idosebb != True or idosindex < len(lista):
        if lista[idosindex] > 70:
            idosebb = True
        idosindex += 1
    print(idosindex)

    return idosindex


def konzolra_ir(elsoidos):
    print("II/D, E:")
    print(f"\tElső idős ember korának helye a listában: {elsoidos}")
    eredmeny = "Első idős ember korának helye a listában: {elsoidos}"
    return eredmeny

def fajl_ir(elsoidos):
    f = open("oreg.txt", "w", encoding="utf8")
    f.write(elsoidos)