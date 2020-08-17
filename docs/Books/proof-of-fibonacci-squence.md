## What to prove

$F_n \leq \psi^{n - 1}$ where $\psi = (1 + \sqrt{5}) / 2$ 

and

$F_n = F_{n - 1} + F_{n - 2}$

## Steps using induction

If n = 1 (base case), $F_1 = 1 = \psi^{0} = \psi^{1-1}$ which is true.

If $P(1), P(2) ... P(n)$ are true and $n > 1$, we know in particular that $P(n - 1)$ and $P(n)$ are true; so $F_{n - 1} \leq \psi^{n - 2}$ and $F_n \leq \psi^{n - 1}$. Adding these inequalities:

\[ F_{n + 1} = F_{n - 1} + F_n \leq \psi^{n - 2} + \psi^{n - 1} = \psi^{n - 2} (1 + \psi)\]


The important property of the number $\Psi$ is that:

\[ 1 + \psi = \psi^2 \]

Plugging this into the preious equation gives $F_{n + 1} \leq \psi^n$, so we prove the inductive step where if $F_n$ is true then $F_{n + 1}$ is true.