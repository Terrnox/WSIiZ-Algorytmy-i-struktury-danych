from zadanie1stos import Stack
def parChecker(symbolString):
    stos = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            stos.push(symbol)
        else:
            if stos.empty():
                balanced = False
            else:
                stos.pop()
        index += 1

    if balanced and stos.empty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('((())))'))
print(parChecker('(((()))'))
print(parChecker('((()))))'))
print(parChecker('(()(())())'))