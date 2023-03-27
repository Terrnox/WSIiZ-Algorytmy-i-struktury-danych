def NWD_1_rek(a,b): # Wersja pierwsza metoda rekurancyjna
    if a == b:
        return a
    elif a > b:
        a = a - b
        return NWD_1_rek(a, b)
    else:
        b = b - a
        return NWD_1_rek(a, b)

print("Wersja pierwsza metoda rekurancyjna")
print("Największy wspólny dzielnik wynosi:",NWD_1_rek(12,18))
print("Największy wspólny dzielnik wynosi:",NWD_1_rek(28,24))

def NWD_1_iter(a,b): #Wersja pierwsza metoda iteracyjna
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print("Wersja pierwsza metoda iteracyjna")
print("Największy wspólny dzielnik wynosi:",NWD_1_iter(12,18))
print("Największy wspólny dzielnik wynosi:",NWD_1_iter(28,24))

def NWD_2_rek(a, b):
    if b == 0:
        return a
    else:
        tmp = a % b
        a = b
        b = tmp
        return NWD_2_rek(a, b)

print("Wersja druga metoda rekurancyjna")
print("Największy wspólny dzielnik wynosi:",NWD_2_rek(12,18))
print("Największy wspólny dzielnik wynosi:",NWD_2_rek(28,24))

def NWD_2_iter(a,b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

print("Wersja druga metoda iteracyjna")
print("Największy wspólny dzielnik wynosi:",NWD_2_iter(12,18))
print("Największy wspólny dzielnik wynosi:",NWD_2_iter(28,24))