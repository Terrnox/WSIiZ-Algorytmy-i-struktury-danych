#include <iostream>
#include <locale.h>

using namespace std;

int S(int);

int main()
{
    setlocale(LC_CTYPE, "Polish");
    int n;
    cout << "Podaj n:" << endl;
    cin >> n;
    if (n >= 0)
    {
        cout << "Wartość wyrazu ciągu S dla n=" << n << " wynosi:" << S(n) << endl;
    }
    else
    {
        cout << "Podano złą wartość dla n." << endl;
    }
}

int S(int n)
{
    if (n == 0)
    {
        return 1;
    }
    else if(n == 1)
    {
        return 1;
    }
    else
    {
        int* T = new int[n + 1];
        T[0] = 1;
        T[1] = 1;
        for (int i = 2; i <= n; i++)
        {
            T[i] = 2 * T[i - 1] - T[i-2];
        }
        int rezultat = T[n];
        return rezultat;
    }
}
