def scal(lista1,lista2):
    dl1 = len(lista1)
    dl2 = len(lista2)
    dl3 = dl1 + dl2
    lista3 = []
    i = 0
    while i<dl3:
        if(dl1>0 and dl2>0):
            if lista1[0] > lista2[0]:
                lista3.append(lista2[0])
                lista2.remove(lista2[0])
                dl2 = dl2 - 1
            elif lista1[0] < lista2[0]:
                lista3.append(lista1[0])
                lista1.remove(lista1[0])
                dl1 = dl1 - 1
            else:
                lista3.append(lista1[0])
                lista1.remove(lista1[0])
                dl1 = dl1 - 1
        elif(dl1 == 0 and dl2>0):
            lista3.append(lista2[0])
            lista2.remove(lista2[0])
            dl2 = dl2 - 1
        elif(dl1 > 0 and dl2 == 0):
            lista3.append(lista1[0])
            lista1.remove(lista1[0])
            dl1 = dl1 - 1

        i+=1

    return lista3

lista1 = [1,4,5,6,11,13,98]
lista2 = [0,7,8,10,11,90,100]

print(scal(lista1,lista2))