def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n-1)

n = int(input("Podaj n:"))
print(f"Wartość silni dla {n} wynosi: {silnia(n)}")