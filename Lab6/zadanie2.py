import random

def sr_wazona(n):
    l = 0
    Ta = [] #Lista do sprawdzewnia wpisanych wartości - niepotrzebne do działania algorytmu
    Twag = [] #Lista do sprawdzenia losowych wag - niepotrzebne do działania algorytmu
    wag = 0
    for i in range(n):
        a = int(input("Podaj wartość:"))
        waga = random.randint(1,5) #Psuedolosowe całkowite wagi o wartościach od 1 do 5
        l = l + a * waga
        Ta.append(a) #Uzupełnianie listy wartości - niepotrzebne do działania algorytmu
        Twag.append(waga) #Uzupełnianie listy wag - niepotrzebne do działania algorytmu
        wag = wag + waga

    print(f"Lista wartości: {Ta}") #Wyświetlanie listy wartości - niepotrzebne do działania algorytmu
    print(f"Lista wag: {Twag}") #Wyświetlanie listy wag - niepotrzebne do działania algorytmu
    sr = l / wag
    return sr

n = int(input("Podaj liczbę elementów:"))
print(f"Średnia ważona dla {n} elementów wynosi {sr_wazona(n)}")