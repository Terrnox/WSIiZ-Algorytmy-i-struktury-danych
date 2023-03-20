import numpy as np

n = int(input("Podaj ilość wierszy tablicy:"))
m = int(input("Podaj ilość kolumn tablicy:"))

# Tworzenie dwuwymiarowej tablicy o wymiarach n x m oraz wypełnienie jej losowymi liczbami z przedziału 0-10 (przykładowe dane)
T = np.random.randint(10,size=(n,m))

print("Tablica przed zamianą")
print(T)

for i in range(n):
    tmp_min = T[i][0]
    for j in range(m):
        if T[i][j] <= tmp_min:
            tmp_min = T[i][j]
            tmp_ind = j
    tmp = T[i][0]
    T[i][0] = tmp_min
    T[i][tmp_ind] = tmp

print("Tablica po zamianie")
print(T)

#Wypisywanie minimum w wierszu
for k in range(n):
 print(f"Mininum w wierszu {k} wynosi {T[k][0]}")
