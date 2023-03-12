import random as r

#Funkcja wypisz
def wypisz(T_ind):
    dl = len(T_ind)
    wypisanie = ""
    for i in range(dl):
        wypisanie = wypisanie + str(i) + ','
    print(f"Szukana wartość występuje na pozycjach {wypisanie}")

T = []

N = int(input("Podaj wielkość tablicy:"))

# Wypełnianie tablicy losowymi danymi liczbowymi z przedziału 1-11
for j in range(N):
    T.append(r.randint(1,11))

print(T)

szukana = float(input("Podaj szukaną wartość:"))
licznik_wys = 0

for i in range(N):
    if T[i] == szukana:
        if licznik_wys == 0:
            T_ind = []
            T_ind.append(i)
            licznik_wys = licznik_wys + 1
        else:
            T_ind.append(i)
            licznik_wys = licznik_wys + 1

if licznik_wys == 0:
    print("Szukana wartość nie występuje w tablicy")
else:
    wypisz(T_ind)