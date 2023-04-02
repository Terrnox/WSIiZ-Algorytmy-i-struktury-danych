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