#include <iostream>
using namespace std;

void Merge(int, int, int, int A[], int B[]);
void MergeSort(int, int, int A[], int B[]);

int main(int argc, char** argv) {
	int A[]{ 1,35,42,65,68,25,55,59,70,79 };
	int B[size(A)];
	MergeSort(0, 9, A, B);
	for (int i = 0; i < size(A); i++)
	{
		cout << A[i] << ' ';
	}
	return 0;
}



void Merge(int l, int m, int r, int A[], int B[])
{
    int i = l;
    int j = m;
    int k = l;

    while (i < m && j <= r) 
    {
        if (A[i] <= A[j]) 
        {
            B[k] = A[i];
            i++;
        }
        else 
        {
            B[k] = A[j];
            j++;
        }
        k++;
    }

    while (i < m) 
    {
        B[k] = A[i];
        i++;
        k++;
    }

    while (j <= r) 
    {
        B[k] = A[j];
        j++;
        k++;
    }

    for (int x = l; x <= r; x++) 
    {
        A[x] = B[x];
    }
}


void MergeSort(int l, int r, int A[], int B[])
{
	int m;
	if (r - l < 1) return;
	m = (l + r + 1) / 2;
	MergeSort(l,m-1,A,B);
	MergeSort(m,r,A,B);
	Merge(l,m,r,A,B);
	return;
}