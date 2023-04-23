#include <iostream>
#include <cstdlib>
#include <locale.h>

using namespace std;

int main()
{
    setlocale(LC_ALL, "Polish");
    int n;
    int l = 0;
    int a;
    int wag = 0;
    int waga;
    double sr;
    cout << "Podaj liczbę elementów" << endl;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cout << "Podaj a" << endl;
        cin >> a;
        waga = rand()%4+1;
        cout << "Waga:" << waga << endl;
        l = l = a*waga;
        wag = wag + waga;
    }
    sr = 1.0 * l / wag;
    cout <<"Średnia ważona wynosi " << sr<<endl;
}

