def suma(T,n):
    if n == 0:
        return 0
    elif n == 1:
        return T[0]
    else:
        srodek = n // 2
        prawy = n - srodek
        lewa_suma = suma(T,srodek)
        prawa_suma = suma(T[srodek:n],prawy)
        return lewa_suma + prawa_suma

T = [2,3,5,7,8,96,3,9] #przykładowe dane
n = len(T) #rozmiar listy/tablicy

print(f"Suma elementów w tablicy jest równa: {suma(T,n)}")