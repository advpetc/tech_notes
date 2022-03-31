# Binomial Coefficient

## Definition

The combinations of the five objects {a,b,c,d,e} taken three at a time are:

```
abc, abd, abe, acd, ace, ade, bcd, bce, bde, cde
```

Therefore, the number of combinations, which we denote by ${n \choose k}$, is

\[ {n \choose k} = \frac{n(n - 1)...(n - k + 1)}{k(k - 1)...(1)} = \frac{n!}{k!(n-k)!}\]

In particular, we have:

${r \choose 0} = 1$, ${r \choose 1} = r$, ${r \choose 2} = \frac{r(r - 1)}{2}$

## Basic Techniques

\[{n \choose k} = {n \choose n - k}, n \geq 0 \tag{1}\]

\[{r \choose k} = \frac{r}{k}{r - 1 \choose k - 1}, k \neq 0 \tag{2}\]

\[{r \choose k} = {r - 1 \choose k} + {r - 1 \choose k - 1} \tag{3}\]

\[\sum_{k = 0}^n {k \choose m} = {0 \choose m} + {1 \choose m} + ... + {n \choose m} = {n + 1 \choose m + 1}, m \geq 0, n \geq 0 \tag{4} \]

## Summation Formulas

Given equation (4), by letting m = 1, we can derive:

\[{0 \choose 1} + {1 \choose 1} ... + {n \choose 1} = 0 + 1 + ... + n = {n + 1 \choose 2} = \frac{(n + 1)n}{2} \tag{5}\]

Rearrange:

\[ 2{n + 1 \choose 2} = n^2 + n \implies n^2 = 2{n + 1 \choose 2} - n = 2{n \choose 2} + {n \choose 1} \tag{6} \]

Applying equation (6) to:

\[ \sum_{k = 0}^{n} k^2  = \sum_{k = 0}{n} (2{k \choose 2} + {k \choose 1}) = 2{n + 1 \choose 3} + {n + 1 \choose 2} \tag{7}\]

By expanding equation (7):

\[1^2 + 2^2 + ... + n^2 = 2\frac{(n + 1)n(n - 1)}{6} + \frac{(n + 1)n}{2} = \frac{1}{3}n(n + \frac{1}{2})(n + 1) \tag{8}\]

## Sum of Products

One important equation:

\[ \sum_k{r \choose k}{s \choose n - k} = {r + s \choose n} \tag{9} \]

Which can be interpret the right-hand side as the number of ways to select n people from among r men and s women; each term on the left is the number of ways to choose k of the men and n - k of women.