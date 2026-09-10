# 0055. Jump Game

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` *if you can reach the last index, or* `false` *otherwise*.

 

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

 

**Constraints:**

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Analysis

We greedily track the farthest index we could reach so far as we scan left to right. At each index `i`, if `i` is already beyond our farthest reachable index, we can never get there, so we return `false` immediately. Otherwise, we update `farthest = max(farthest, i + nums[i])`. If we finish the scan without ever getting stuck, the last index must be reachable.

**Why greedy works:**

The key fact that makes greedy valid (rather than needing to try all jump-length choices) is that the set of indices reachable from any single index `i` is the contiguous range `[i, i + nums[i]]` — there's no benefit to ever jumping *less* than the maximum, since landing farther can only ever unlock everything a shorter jump could reach, plus more. So the only thing worth remembering about "everything reachable so far" is its rightmost edge, `farthest`; we never need to track the full reachable set.

**Claim:** After the loop body finishes processing index `i` (without having returned `false`), `farthest` equals exactly the maximum index reachable from index `0` using only intermediate landing spots in `[0, i]`.

**Proof (by induction on `i`):**

- *Base case* (`i = 0`): `farthest` is updated to `max(0, 0 + nums[0]) = nums[0]`, which is precisely the farthest index reachable in one jump from the start. The claim holds.
- *Inductive step:* assume the claim holds after processing index `i - 1`, i.e. `farthest` correctly equals the farthest index reachable using landing spots in `[0, i-1]`.
  - If `i > farthest`, then by the inductive hypothesis index `i` is not reachable at all, so no jump can ever originate from it — the algorithm correctly declares failure and stops.
  - If `i <= farthest`, then index `i` *is* reachable, so it's legal to jump from there, extending the reachable frontier to `i + nums[i]`. Since no index beyond the old `farthest` was reachable before (by the inductive hypothesis) except possibly through `i`, `max(farthest, i + nums[i])` is exactly the new farthest reachable index using landing spots in `[0, i]`. This re-establishes the claim.

By induction, the claim holds for every `i` the loop reaches. If the loop runs to completion, it never triggered `i > farthest` for `i = n - 1` either — meaning `n - 1 <= farthest` at that point, i.e. the last index was reachable. Conversely, if the last index is reachable, no `i` in `[0, n-1]` can ever exceed `farthest`, since `farthest` never permanently falls short of a truly reachable index (the induction guarantees it only grows to match the real frontier). So the loop returning `true` is both sound and complete. $\blacksquare$

* Time: $O(n)$
* Space: $O(1)$

## Code

```c++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size(), farthest = 0;
        for (int i = 0; i < n; ++i) {
            if (i > farthest) return false;
            farthest = max(farthest, i + nums[i]);
        }
        return true;
    }
};
```
