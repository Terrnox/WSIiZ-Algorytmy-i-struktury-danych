#include <iostream>
#include <locale.h>

using namespace std;



int main()
{
	setlocale(LC_ALL,"Polish");
	int a;
	int maks = 0;
	do
	{
		cout << "Podaj a" << endl;
		cin >> a;
		if (a > maks)
		{
			maks = a;
		}
	} while (a != 0);
	if (maks == 0)
	{
		cout << "Podano 0 na początku" << endl;
	}
	else
	{
		cout << "Maksymalna wartość wynosi:" << maks << endl;
	}
}

