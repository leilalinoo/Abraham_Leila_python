import random
def generalt_szam():
    szam = random.randint(1, 50)

    print("I/A:")
    print(f"A generált szám: {szam}")

    return szam

def oszthato(szam):
    if szam % 5 == 0 and szam % 3 ==0:
        return "A szám öttel és hárommal is osztható!"
    elif szam % 5 == 0:
        return "A szám öttel osztható!"
    elif szam % 3 == 0:
        return "A szám hárommal  osztható!"


