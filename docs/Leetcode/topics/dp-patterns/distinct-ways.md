# Distinct Ways

**Statement**

Given a target find a number of distinct ways to reach the target.

**Approach**

Sum all possible ways to reach the current state.

`routes[i] = routes[i-1] + routes[i-2], ... , + routes[i-k]`

Generate sum for all values in the target and return the value for the target.

**Top-Down**

```c++
for (int j = 0; j < ways.size(); ++j) {
    result += topDown(target - ways[j]);
}
return memo[/*state parameters*/] = result;
```

**Bottom-Up**
```c++
for (int i = 1; i <= target; ++i) {
   for (int j = 0; j < ways.size(); ++j) {
       if (ways[j] <= i) {
           dp[i] += dp[i - ways[j]];
       }
   }
}
 
return dp[target];
```

## 0070. Climbing Stairs

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

```

**Example 2:**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

```

**Constraints:**

-   `1 <= n <= 45`

`dp[i]`: number of ways to reach `i` th starcase. So `dp[i] = dp[i - 1] + dp[i - 2]`

Since we are only using two variables: `dp[i - 1]` and `dp[i - 2]`, we can reduce them to two variables:
```c++
class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) return 1;
        else if (n == 2) return 2;
        int one = 1, two = 2;
        int res = 0;
        for (int i = 3; i <= n; ++i) {
            res = one + two;
            one = two;
            two = res;
        }
        return res;
    }
};
```