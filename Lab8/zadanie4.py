def dodaj_posort(lista,element):
    dl = len(lista)
    i = 0
    if lista == []:
        lista.append(element)
        return lista
    else:
        while i < dl:
            if(element == lista[i]):
                lista.insert(i, element)
                return lista
            elif(element < lista[i]):
                lista.insert(i, element)
                return lista
            elif(i == dl-1):
                lista.append(element)
                return lista

            i+=1



lista = []

elementy_dodania = [6,1,7,45,0,94,5]
for i in range(len(elementy_dodania)):
    print(dodaj_posort(lista,elementy_dodania[i]))
