## Fast way to find nCr (n choose r)

Def of C(n,r): (N * N - 1 * N - 2 * ... * N - R + 1) / (1 * 2 * ... * R), so to calculate C(n,r), we do N/1 * N-1/2 ... *  N-R+1/R

**Special Property**
C(n,r)=C(n,n-r)

### Code

```c
// https://stackoverflow.com/a/42285958
int NCR(int n, int r)
{
    if (r == 0) return 1;

    /*
     Extra computation saving for large R,
     using property:
     N choose R = N choose (N-R)
    */
    if (r > n / 2) return NCR(n, n - r); 

    long res = 1; 

    for (int k = 1; k <= r; ++k)
    {
        res *= n - k + 1;
        res /= k;
    }

    return res;
}
```