#include <iostream>
#include <locale.h>

using namespace std;

unsigned int fib(int);

int main()
{
    setlocale(LC_CTYPE, "Polish");
    int n;
    cout << "Podaj n:" << endl;
    cin >> n;
    cout <<"Wartość wyrazu ciągu Fibbonaciego dla n="<<n<< " wynosi:" << fib(n) << endl;
}

unsigned int fib(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }
    else
    {
        unsigned int* T = new unsigned int[n+1];
        T[0] = 0;
        T[1] = 1;
        for (int i = 2; i <= n; i++)
        {
            T[i] = T[i - 1] + T[i - 2];
        }
        unsigned int rezultat = T[n];
        return rezultat;
    }
}
