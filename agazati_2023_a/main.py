import gombak
import korok
import szam

vizsgalando_szam = szam.generalt_szam()
print(szam.oszthato(vizsgalando_szam))

#eletkor = korok.bekeres()
lista = korok.lista_keszitese()
elsoidos = korok.elso_idos(lista)
korok.konzolra_ir(elsoidos)
korok.fajl_ir(elsoidos)

#lista = gombak.beolvasas()
#gombak.gombak_szama(lista)
