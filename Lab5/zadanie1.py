def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        F = [0,1]
        i = 2
        while(i<=n):
            F.append(F[i-1]+F[i-2])
            i+=1

        return F[i-1]

n = int(input("Podaj n:"))
if n>=0:
    print(fib(n))
else:
    print("Podano zły argument")