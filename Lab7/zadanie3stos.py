from zadanie1stos import Stack

def parCheckerMod(symbolString):
    stos = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in ['(','[','{']:
            stos.push(symbol)
        else:
            if stos.empty():
                balanced = False
            current_symbol = stos.pop()
            if current_symbol == '(':
                if symbol != ')':
                    return False
            if current_symbol == '[':
                if symbol != ']':
                    return False
            if current_symbol == '{':
                if symbol != '}':
                    return False
        index += 1

    if balanced and stos.empty():
        return True
    else:
        return False

print(parCheckerMod("{()}[]"))
print(parCheckerMod("{(}}[]"))
print(parCheckerMod("{{()}[]))"))