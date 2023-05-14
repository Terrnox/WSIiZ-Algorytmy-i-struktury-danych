from zadanie1stos import Stack

def ONP(symbolString):
    stos = Stack()
    operatory = ['+','-','*','/','^']
    for c in symbolString:
        if c in operatory:
            x = stos.pop()
            y = stos.pop()
            if c == '+':
                wynik = x + y
                stos.push(wynik)
            if c == '-':
                wynik = y - x
                stos.push(wynik)
            if c == '*':
                wynik = x * y
                stos.push(wynik)
            if c == '/':
                wynik = y / x
                stos.push(wynik)
            if c == '^':
                wynik = y ** x
                stos.push(wynik)
        elif int(c) >= 0 and int(c) < 10:
            stos.push(int(c))

    wynik_onp = stos.pop()

    return wynik_onp

print("Wynik wyrażenia 7 3 + 5 2 - 2 ^ * wynosi: "+str(ONP("73+52-2^*")))