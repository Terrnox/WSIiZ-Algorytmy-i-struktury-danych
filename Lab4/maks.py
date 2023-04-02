def maks(T, lewy, prawy, maksimum):
    if lewy == prawy:
        return T[lewy]
    elif (lewy + 1) == prawy:
        return max(T[lewy], T[prawy])
    else:
        srodek = (lewy + prawy) // 2
        maksimum1 = maks(T, lewy, srodek, maksimum)
        maksimum2 = maks(T, srodek+1, prawy, maksimum)
        return max(maksimum1, maksimum2)

T = [9,0,6,7,17,6,8,19] #Przykładowy wektor
l = 0 #lewy indeks
p = len(T) - 1 #prawy indeks
maksi = T[0] #pierwsze maksimum
print(maks(T,l,p,maksi))