## Fibonacci Sequence

Clarification
Assumption
Result
Test

Time Complexity: total nodes of the recursion tree
Space Complexity: call stack (typically equals to the height of the recursion tree)

### Naive Approach

```c
int fib(int n) {
    if (n == 0 || n == 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```

Time: $2^0+2^1+2^2...+2^n \approx 2^n$
Space: n

## pow(a, b)

don't care the case for a == 0 or b < 0 for now

### Naive Approach

```c
int pow(int a, int b) {
    if (b == 0) return 1;
    return pow(a, b - 1) * a;
}
```

### analysis

recursion tree:
2^999
|
2^998
|
2^997
|
2^996
...
there are b nodes and the longest path is b
Time: O(b)
Space: O(b)

### Optimize Space

```c
int pow(int a, int b) {
    if (b == 0) return 1;
    return pow(a, b / 2)  * pow(a, b - b / 2); // why not using b/2? because 3/2 = 1.5 = 1
}
```

2^999
 | |
 2^500 2^499
 | | | |
 250 250 250 249
 ...
 there are 1 + 2 + 4 + ... 2^log(b) = b =\> time: O(b)

Space: O(log(b))



 