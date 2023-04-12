import numpy as np

def minimum(a,b):
    if a < b:
        return a
    else:
        return b

def dwumian(n,m):
    if (n == m or m == 0):
        return 1

    w = int(n) + 1
    k = int(m) + 1
    T = np.zeros((w, k))
    i = 0
    while i<=n:
        j = 0
        while j <= minimum(i,m):
            if (i == j or j == 0):
                T[i][j] = 1
            else:
                T[i][j] = T[i - 1][j - 1] + T[i - 1][j]
            j+=1
        i+=1
    print(T)
    return T[n][m]


n = int(input("Podaj n:"))
m = int(input("Podaj m:"))

if n>=0 and m>=0 and n>=m:
    print(f"Dwumian dla {n} i {m} wynosi {dwumian(n,m)}")
else:
    print("Podano złe dane")

