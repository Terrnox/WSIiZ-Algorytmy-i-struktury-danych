def S(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    ST = [1,1]
    i = 2
    while(i<=n):
        ST.append(2*ST[i-1]-ST[i-2])
        i+=1
    return ST[n]

n = int(input("Podaj n:"))
print(f"Wartość wyrazu dla {n} wynosi {S(n)}")