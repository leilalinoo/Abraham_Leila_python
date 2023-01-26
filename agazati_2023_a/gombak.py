import Gombak_f

def beolvasas():
    f = open("gombak_jav.txt", "r", encoding="utf8")
    f.readline()
    adatok = f.readlines()
    gombaneve = []

    for i in range(len(adatok)):
        neve = Gombak_f.Gombak.darabok[i]
        gombaneve.append(neve)

    return gombaneve

def gombak_szama(lista):
    print("III/A, B:")
    print(f"A gombák száma: {len(lista)}")

# def papsapka(lista):
#     for i in range(len(lista)):
#         if