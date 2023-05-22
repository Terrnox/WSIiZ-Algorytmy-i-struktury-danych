def wyszukaj_binarnie(lista,szukana):
    rozmiar = len(lista)
    while rozmiar != 0:
        srodek = rozmiar // 2
        if(lista[srodek] == szukana):
            return True
        elif(lista[srodek]>szukana):
            lista = lista[0:srodek]
            rozmiar = len(lista)
        else:
            lista = lista[(srodek+1):rozmiar]
            rozmiar = len(lista)
    else:
        return False

lista = [0,8,7,6,90,56]
''' 0 6 7 8 56 90 '''
szukana = float(input("Podaj szukaną wartość:"))
lista.sort()

print(wyszukaj_binarnie(lista,szukana))