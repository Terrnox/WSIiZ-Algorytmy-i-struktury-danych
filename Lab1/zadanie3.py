import random as r

T = []

N = int(input("Podaj wielkość tablicy:"))

# Wypełnianie tablicy losowymi danymi liczbowymi z przedziału 1-11 (przykładowe dane)
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
    print(T_ind)