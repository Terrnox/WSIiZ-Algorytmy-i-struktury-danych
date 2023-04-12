#include <iostream>
#include <locale.h>

using namespace std;

int dwumian(int,int);

int minimum(int, int);


int main()
{
    setlocale(LC_CTYPE, "Polish");
    int n;
    int m;
    cout << "Podaj n:" << endl;
    cin >> n;
    cout << endl;
    cout << "Podaj m:" << endl;
    cin >> m;
    cout << endl;
    if (n >= 0 && m >= 0 && n>=m)
    {
        cout << "Wartość dwumianu dla n=" << n << " i m=" << m << " wynosi:" << dwumian(n, m) << endl;
    }
    else
    {
        cout << "Wprowadzono złe dane wejściowe" << endl;
    }
}

int dwumian(int n, int m)
{
    if (n == m || m == 0)
    {
        return 1;
    }
    else 
    {
        int** tab = new int* [n + 1];
        for (int iter = 0; iter <= n; iter++)
        {
            tab[iter] = new int [m + 1];
        }
        for (int i = 0; i < n+1; i++)
        {
            for (int j = 0; j<=minimum(i,m); j++)
            {
                if (i == j || j == 0)
                {
                    tab[i][j] = 1;
                }
                else
                {
                    tab[i][j] = tab[i - 1][j - 1] + tab[i - 1][j];
                }
            }
        }
        int rezultat = tab[n][m];
        return rezultat;
    }
}

int minimum(int a, int b)
{
    if (a < b)
    {
        return a;
    }
    else
    {
        return b;
    }
}
