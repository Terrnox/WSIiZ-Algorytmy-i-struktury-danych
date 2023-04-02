#include <iostream>
using namespace std;

int suma(int [], int);

int main()
{
    int T[9] = {1,2,3,8,6,7,4,21,99};
    int n = size(T);
   

    cout << "Suma wynosi: " << suma(T, n) << endl;
}

int suma(int T[], int n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return T[0];
    }
    else
    {
        int srodek = n / 2;
        int prawy = n - srodek;
        int lewa_suma = suma(T, srodek);
        int prawa_suma = suma(T + srodek, prawy);
        return lewa_suma + prawa_suma;
    }
   
}
