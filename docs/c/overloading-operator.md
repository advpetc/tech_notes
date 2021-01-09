# Overloading Operator

## Sort Operator on Struct

```c
struct Edge
{
    int a, b, w;
    bool operator< (const Edge &t) const
    {
        return w < t.w; // will sort from small to big, aka, increasing order
    }
}e[M];

sort(e, e + m);
```