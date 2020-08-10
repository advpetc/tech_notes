There are two players playing alternatively, and there is a deck of cards.
Each player can pick 1~3 cards from the **top** of the deck. Find the maximum card value that player one get.

e.g. [8,1,1,1,1] -> p1 pick 1, p2 picks 1,1,1. finally p1 pick 8 which is the highest point it can get.

```c
DP[i] = max(sum(0, i) - DP[i-1],
            sum(0, i) - DP[i-2],
            sum(0, i) - DP[i-3])
      = sum(0, i) - min(DP[i-1], DP[i-2], DP[i-3])
```