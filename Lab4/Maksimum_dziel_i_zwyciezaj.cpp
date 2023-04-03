#include <iostream>

using namespace std;

int maks(int T[], int lewy, int prawy, int maksimum)
{
    if (lewy == prawy)
    {
        return T[lewy];
    }
    else if ((lewy + 1) == prawy)
    {
        if (T[lewy] > T[prawy])
        {
            return T[lewy];
        }
        else
        {
            return T[prawy];
        }
    }
    else
    {
        int srodek = (lewy + prawy) / 2;
        int maksimum1 = maks(T, lewy, srodek, maksimum);
        int maksimum2 = maks(T, srodek + 1, prawy, maksimum);
        if (maksimum1 > maksimum2)
        {
            return maksimum1;
        }
        else
        {
            return maksimum2;
        }
    }
}


int main()
{
    int T[8] = {9, 0, 6, 7, 17, 26, 8, 19}; //Przykładowy wektor
    int l = 0;   //lewy indeks
    int p = size(T); //prawy indeks
    int maksi = T[0]; //pierwsze maksimum
    cout<<"Maksymalny element wektora wynosi: " << maks(T, l, p, maksi)<<endl;
}

