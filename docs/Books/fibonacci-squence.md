## What to prove

If $\phi = (1 + \sqrt{5}) / 2$ then $F_n \leq \phi^{n - 1}$

and

$F_n = F_{n - 1} + F_{n - 2}$

## Steps using induction

If n = 1 (base case), $F_1 = 1 = \phi^{0} = \phi^{1-1}$ which is true.

If $P(1), P(2) ... P(n)$ are true and $n > 1$, we know in particular that $P(n - 1)$ and $P(n)$ are true; so $F_{n - 1} \leq \phi^{n - 2}$ and $F_n \leq \phi^{n - 1}$. Adding these inequalities:

\[ F_{n + 1} = F_{n - 1} + F_n \leq \phi^{n - 2} + \phi^{n - 1} = \phi^{n - 2} (1 + \phi)\]


The important property of the number $\phi$ is that:

\[ 1 + \phi = \phi^2 \]

Plugging this into the preious equation gives $F_{n + 1} \leq \phi^n$, so we prove the inductive step where if $F_n$ is true then $F_{n + 1}$ is true.

## Relationship between $F_m$ and $F_n$

\[F_{n + 3} = F_{n + 2} + F_{n + 1} = F_{n + 1} + F_n + F_{n + 1} = 2F_{n + 1} + F_n \]

Similarly, we can derive $F_{n + 4}$

\[F_{n + 4} = 3F_{n + 1} + 2F_n\]

In general:

\[F_{n + m} = F_m F_{n + 1} + F_{m - 1} F_n \tag{1} \]

Assume $m = (k - 1) n$, or m be a multiple of n in equation (1), we find inductively that:

$F_{m + n} = F_{nk}$ is multiple of $F_n$, thus every third number is even, every fourth number is a multiple of 3, every fifth is a multiple of 5...

**Relative Prime**

if two numbers are relative prime, then the gcd is 1:

\[ gcd(F_n, F_{n + 1}) = 1 \]

## Theorem A

\[gcd(F_m, F_n) = F_{gcd(m, n)} \tag{2} \]