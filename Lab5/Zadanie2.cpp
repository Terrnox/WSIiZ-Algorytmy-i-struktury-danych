#include <iostream>
#include <iomanip>
#include <locale.h>

using namespace std;

double P(int, int);

int main()
{
    setlocale(LC_CTYPE, "Polish");
    int i;
    int j;
    cout << "Podaj i:" << endl;
    cin >> i;
    cout << endl;
    cout << "Podaj j:" << endl;
    cin >> j;
    cout << endl;
    if ((j >= 0 && i >= 0) && (j!=0 || i!=0))
    {
        cout << setprecision(10) << "P(" << i << "," << j << "): " << P(i, j) << endl;
    }
    else
    {
        cout << "Podano złe dane wejściowe." << endl;
    }

    return 0;
}

double P(int i, int j)
{
    if (i > 0 && j == 0)
    {
        return 0;
    }
    else if (i == 0 && j > 0)
    {
        return 1;
    }
    else
    {
        double** tab = new double* [i + 1];
        for (int iter = 0; iter < i + 1; iter++)
        {
            tab[iter] = new double[j + 1];
        }

        for (int w = 0; w < i + 1; w++)
        {
            for (int k = 0; k < j + 1; k++)
            {
                if (w == 0 && k == 0)
                {
                    continue;
                }
                else if (w > 0 && k == 0)
                {
                    tab[w][k] = 0;
                }
                else if (w == 0 && k > 0)
                {
                    tab[w][k] = 1;
                }
                else
                {
                    tab[w][k] = (tab[w - 1][k] + tab[w][k - 1]) / 2.0;
                }
            }
        }

        double rezultat = tab[i][j];

        for (int iter = 0; iter < i + 1; iter++)
        {
            delete[] tab[iter];
        }

        delete[] tab;

        return rezultat;
    }
    
}

