def dzies_na_bin(liczba, reszta =""):
    if liczba > 0:
        reszta = reszta + str(liczba % 2)
        liczba = liczba // 2
        return dzies_na_bin(liczba, reszta)
    elif liczba == 0 and reszta == "":
        reszta = reszta + "0"
    else:
        return reszta[::-1]


liczba = int(input("Podaj liczbę dziesiętną:"))
liczba_bin = dzies_na_bin(liczba)
print(f"Liczba dziesiętna {liczba} w postaci binarnej wynosi",liczba_bin)