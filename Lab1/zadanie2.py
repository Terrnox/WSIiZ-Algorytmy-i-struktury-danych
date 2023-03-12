N = int(input("Podaj ilość liczb:"))

while N <= 0:
    N = int(input("Podaj ilość liczb:"))

licznik_u = 0

for i in range(N):
    liczba=int(input("Podaj liczbę całkowitą:"))
    if liczba < 0:
        licznik_u += 1

print(f"Ilość całkowitych liczb ujemnych wynosi: {licznik_u}")