# 1340. Jump Game V

Given an array of integers `arr` and an integer `d`. In one step you can jump from index `i` to index:

- `i + x` where: `i + x < arr.length` and `0 < x <= d`.
- `i - x` where: `i - x >= 0` and `0 < x <= d`.

In addition, you can only jump from index `i` to index `j` if `arr[i] > arr[j]` and `arr[i] > arr[k]` for all indices `k` between `i` and `j` (More formally `min(i, j) < k < max(i, j)`).

You can choose any index of the array and start jumping. Return *the maximum number of indices* you can visit.

Notice that you can not jump outside of the array at any time.

 

**Example 1:**

```
Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.
```

**Example 2:**

```
Input: arr = [3,3,3,3,3], d = 3
Output: 1
Explanation: You can start at any index. You always cannot jump to any index.
```

**Example 3:**

```
Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indices.
```

 

**Constraints:**

- `1 <= arr.length <= 1000`
- `1 <= arr[i] <= 10^5`
- `1 <= d <= arr.length`

## Analysis

Because a jump only ever goes from a taller position to a strictly shorter one, this graph of possible jumps has no cycles — it's a DAG. That means the answer for each starting index is simply `1 + the best result among everything it can jump to`, which we can compute with top-down DP (DFS + memoization).

For a given index `i`, we look up to `d` steps to the right and up to `d` steps to the left, but we stop scanning in a direction as soon as we hit an index whose height is `>= arr[i]`, since that blocks any further jump in that direction (per the problem's "no taller index in between" rule) and also means it isn't reachable in one hop anyway.

`dfs(i)` returns the length of the longest visitable chain starting at `i`. The final answer is the maximum of `dfs(i)` over every index, since we're allowed to start anywhere.

* Time: $O(n \cdot d)$, since each of the $n$ indices scans at most `d` positions in each direction, and each state is memoized so it's computed only once.
* Space: $O(n)$ for the memoization array and recursion stack.

## Code

```c++
class Solution {
public:
    vector<int> arr;
    vector<int> memo;
    int d;

    int dfs(int i) {
        if (memo[i] != -1) return memo[i];
        int best = 1;
        for (int j = i + 1; j <= min((int)arr.size() - 1, i + d) && arr[j] < arr[i]; ++j)
            best = max(best, 1 + dfs(j));
        for (int j = i - 1; j >= max(0, i - d) && arr[j] < arr[i]; --j)
            best = max(best, 1 + dfs(j));
        return memo[i] = best;
    }

    int maxJumps(vector<int>& arr, int d) {
        this->arr = arr;
        this->d = d;
        int n = arr.size();
        memo.assign(n, -1);
        int res = 0;
        for (int i = 0; i < n; ++i)
            res = max(res, dfs(i));
        return res;
    }
};
```
