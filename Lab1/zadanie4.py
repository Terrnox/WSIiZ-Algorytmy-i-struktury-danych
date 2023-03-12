import random as r

T = []

n = int(input("Podaj wielkość tablicy:"))

# Wypełnianie tablicy losowymi danymi liczbowymi z przedziału 1-11
for j in range(n):
    T.append(r.randint(1,11))

print(T)

minimum = T[0]
for i in range(len(T)):
    if T[i] < minimum:
        minimum = T[i]

print("Wartość minimalna wynosi " + str(minimum))