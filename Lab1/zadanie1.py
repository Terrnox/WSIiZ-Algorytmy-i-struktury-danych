import math as m

print("Podaj współczynniki równania kwadratowego a,b,c")
a = float(input("Podaj a:"))
b = float(input("Podaj b:"))
c = float(input("Podaj c:"))

if a!=0:
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b - m.sqrt(delta)) / (2 * a)
        x2 = (-b + m.sqrt(delta)) / (2 * a)
        print(f"Rozwiązania równania kwadratowego to: {x1} i {x2}")
    elif delta == 0:
        x1 = -b / (2 * a)
        print(f"Rozwiązaniem równania jest {x1}")
    else:
        print("Brak rozwiązań rzeczywistych")
else:
    print("To nie jest równanie kwadratowe")
