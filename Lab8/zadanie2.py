def usun(lista,wezel):
    i = 0
    dl = len(lista)
    while i < dl:
        if i == wezel:
            lista.remove(lista[wezel])
            return lista
        i+=1

#Przykładowe wywołanie
wezel = 2
lista = [6,8,9,5]
lista = usun(lista,wezel)
print(f"Lista po usunięciu {wezel}. wezła zawiera następujące elementy: {lista}")