# 0045. Jump Game II

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:

- `0 <= j <= nums[i]` and
- `i + j < n`

Return *the minimum number of jumps to reach* `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

 

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [2,3,0,1,4]
Output: 2
```

 

**Constraints:**

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- It's guaranteed that you can reach `nums[n - 1]`.

## Analysis

This is a greedy, BFS-like "level expansion" approach. Think of `currentEnd` as the farthest index reachable using the jumps we've committed to so far (the boundary of the current "level"), and `farthest` as the farthest index reachable using one more jump from anywhere within the current level.

As we scan `i` from `0` to `n - 2`, we keep updating `farthest = max(farthest, i + nums[i])`. Once `i` reaches `currentEnd`, it means we've exhausted every position in the current level, so we must take another jump: increment `jumps` and extend the boundary to `currentEnd = farthest`.

* Time: $O(n)$
* Space: $O(1)$

## Code

```c++
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int jumps = 0, currentEnd = 0, farthest = 0;
        for (int i = 0; i < n - 1; ++i) {
            farthest = max(farthest, i + nums[i]);
            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest;
            }
        }
        return jumps;
    }
};
```
