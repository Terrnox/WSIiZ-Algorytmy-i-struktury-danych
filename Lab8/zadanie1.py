def wyszukaj(lista,wartosc):
    pozycje = []
    dl = len(lista)
    for i in range(dl):
        if(lista[i] == wartosc):
            pozycje.append(i)

    if pozycje == []:
        print("Wartość nie znajduje się w liście")
    else:
        print("Podana wartość znajduje się na pozycjach: " + str(pozycje))


lista = [1,7,13,2,4,56,4,0]
szukana_wartosc = int(input("Podaj szukaną wartość w liście:"))
wyszukaj(lista,szukana_wartosc)