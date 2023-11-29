
import etlap



etlap_meret: int = 36


etelekNev = ["Hal","Hús"]
etelekAr = [1590, 1660]


dessertNev = ["Fagyi","Brownie"]
dessertAr = [1270, 1490]



#ETLAP
def EtlapMegjelenit(lista, listaAr, szoveg):
	etlap.jelsor("*", etlap_meret)
	etlap.cimsor("*",szoveg,"*", etlap_meret)

	for i in range(len(lista)):	
		etlap.szoveg_ar(lista[i], str(listaAr[i])+" Ft", etlap_meret)
	etlap.jelsor("=", etlap_meret)


EtlapMegjelenit(etelekNev, etelekAr, "Főételek")
EtlapMegjelenit(dessertNev, dessertAr, "Desszertek")


#RENDELÉS/SZÁMOLÁS

import modulok

modulok.rendeles(halar,husar,fagyiar,browniear,etlap_meret)






