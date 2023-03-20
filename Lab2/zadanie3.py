T = [1, 2, 3, 11, 21, 111, 231] #Przykładowe dane
n = len(T)
j = n-1
while j >= 0:
    i = 0
    while i<j:
        lancuch_liczba1 = str(T[i])
        lancuch_liczba2 = str(T[i+1])
        dl1 = len(lancuch_liczba1)
        dl2 = len(lancuch_liczba2)
        dl_min = min(dl1, dl2)
        for k in range(dl_min):
            if int(lancuch_liczba1[k]) < int(lancuch_liczba2[k]):
                break
            elif int(lancuch_liczba1[k]) > int(lancuch_liczba2[k]):
                tmp = T[i]
                T[i] = T[i+1]
                T[i+1] = tmp
                break
        i+=1
    j-=1

print(T)
