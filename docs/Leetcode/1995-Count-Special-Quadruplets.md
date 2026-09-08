# 1995. Count Special Quadruplets

Given a **0-indexed** integer array `nums`, return *the number of **distinct** quadruplets* `(a, b, c, d)` *such that:*

- `nums[a] + nums[b] + nums[c] == nums[d]`, and
- `a < b < c < d`

**Example 1:**

```
Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
```

**Example 2:**

```
Input: nums = [3,3,6,4,5]
Output: 0
Explanation: There are no such quadruplets in [3,3,6,4,5].
```

**Example 3:**

```
Input: nums = [1,1,1,3,5]
Output: 4
Explanation: The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5
```

 

**Constraints:**

- `4 <= nums.length <= 50`
- `1 <= nums[i] <= 100`

### Analysis

This question is similar to Two Sum: 

1. break `nums[a] + nums[b] + nums[c] == nums[d]` into `nums[a] + nums[b] = nums[d] - nums[c]`
2. it turns out we need to find how many sums there are for `nums[d] - nums[c]`

We break the array into two parts: the left side `nums[0:i]` and the right side `nums[i:end]`. We choose any arbitrary numbers from the left side to add to the current value `nums[i]`, and find how many pairs (each pair represents `nums[d] - nums[c]`) of numbers from `nums[i+1:end]` equal the current value. To accomplish it, we need to use a map or a counter to store all the pair sums that can be formed from the right side, and it has to be done **after** we set the pivot `i` so that we can first calculate the possible sums for `nums[a] + nums[b]`.

* Time: $O(n^2)$
* Space: $O(n)$ storing all the possible sums, could only have n possible sums

### Code

```python
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # a + b(i) = d - c(i)
        l = len(nums)
        res = 0
        count = Counter()
        for i in range(l - 1, -1, -1):         
            for a in range(i - 1, -1, -1):
              # if we see the same sum again, the previous configurations should also work, since our i is going from right to left, every previous d and c is greater than the current d and c
                res += count[nums[a] + nums[i]] 
            for d in range(l - 1, i, -1):
                count[nums[d] - nums[i]] += 1
        return res
```

