import numpy as np

def P(i,j):

    if i > 0 and j == 0:
        return 0
    elif i == 0 and j > 0:
        return 1

    w = int(i) + 1
    k = int(j) + 1
    T = np.zeros((w, k))
    for x in range(w):
        for y in range(k):
            if x==0 and y==0:
                pass
            elif x > 0 and y == 0:
                T[x][y] = 0
            elif x == 0 and y > 0:
                T[x][y] = 1
            else:
                T[x][y] = (T[x-1][y] + T[x][y-1]) / 2
    return T[i][j]

i = int(input("Podaj wartość dla i:"))
j = int(input("Podaj wartość dla j:"))

if( (i >= 0 and j >= 0) and (i != 0 or j != 0)):
    print(f"Wartość funkcji P({i},{j}) wynosi {P(i,j)}.")
else:
    print("Podano złe dane")