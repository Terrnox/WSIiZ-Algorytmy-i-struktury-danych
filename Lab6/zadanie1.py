def maks():
    a = int(input("Podaj wartość:"))
    maks = 0
    while a != 0:

        if a > maks:
            maks = a
        a = int(input("Podaj wartość:"))

    if maks == 0:
        print("Podano 0 na wejściu lub liczby ")
    else:
        print(f"Maksymalna wartość wynosi {maks}")

maks()